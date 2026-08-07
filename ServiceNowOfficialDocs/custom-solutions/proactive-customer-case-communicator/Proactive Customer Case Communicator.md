---
title: Proactive Customer Case Communicator — Architecture Analysis
aliases:
  - PCCC
  - Proactive Case Communication
  - Proactive Customer Case Communicator AI Agent
tags:
  - servicenow
  - ai-agent
  - now-assist
  - csm
  - problem-management
  - architecture
  - unit4
scope: sn_csm_ai_agents
platform: now-assist-panel
status: pilot
created: 2026-07-16
last_updated: 2026-08-07
---

# Proactive Customer Case Communicator

> [!abstract] One-liner
> A human-in-the-loop [[Now Assist]] AI Agent in the `sn_csm_ai_agents` scope that **drafts** customer-facing case updates and presents them to the assigned consultant for **Approve / Modify / Reject** in the [[Now Assist Panel]] (NAP). Nothing is ever posted to a customer without human sign-off. Routing and template selection are **deterministic** (script), the LLM only writes prose.

Solves the "silent case" problem: cases stay open while work happens in [[Problem Management]] / [[Work Item]] land, but the customer hears nothing. This agent surfaces controlled updates and paces them so consultants aren't flooded and customers aren't spammed.

Related agent shipped in the same programme: [[Monitor Work Item AI Agent]].

---

## 1. System Context

| Attribute | Value |
|---|---|
| App scope | `sn_csm_ai_agents` |
| Primary table | `sn_customerservice_case` |
| Related tables | `problem`, `u_work_item`, `sys_journal_field` |
| Surface | [[Now Assist Panel]] (NAP) — consultant review |
| Runs as | Case **Assigned To** user |
| Human control | Mandatory approval on every draft |
| AI role | Prose drafting only — **no** process decisions |
| Deterministic role | [[AIPF_Flag Cases on Problem State or Work]], [[Resolve routing decision and template selection]], [[caseUpdateAgentUtil]] |

Two entry points converge on one shared agent evaluation → draft → review → post loop:

- [[Problem Update Path]] — event-driven (Business Rule flags cases)
- [[Stale Case Path]] — time-driven ([[Stale Case Scheduled Job]])

---

## 2. Component Inventory

| Component | Type | Note |
|---|---|---|
| [[AIPF_Flag Cases on Problem State or Work]] | Business Rule (`problem`) | Flags associated cases on relevant Problem activity |
| [[caseUpdateAgentUtil]] | Script Include | All data fetch, variable compute, template registry, comment post, counter |
| Fetch Case and Problem Details | Agent Tool 1 (read) | Calls `_getCaseProblemDetails()` |
| [[Resolve routing decision and template selection]] | Agent Tool 2 (script/routing) | Deterministic gates + template pick |
| Add response to additional comments | Agent Tool 3 (write) | `_addCaseComment()` + `_incrementAutoUpdateCount()` |
| Proactive Customer Case Communicator | AI Agent | Worknote synthesis, semantic vars, draft, approval flow |
| [[Stale Case Scheduled Job]] | Scheduled Job | Queries stale cases, fires agent via subflow |
| Proactive Case Outreach – Agent Invocation | Subflow | `sn_csm_ai_agents.proactive_case_outreach__agent_invocation` |

> [!note] Architecture evolved 2-tool → 3-tool
> Earlier design had **Tool 1 (fetch) + Tool 2 (post)** with routing done inside agent instructions. Current design inserts a dedicated **deterministic routing Tool 2** and pushes the writer to **Tool 3**, giving clean read → decide → write separation and removing routing from LLM reasoning. See [[#8. Template Registry]] and [[#7. Deterministic Routing]].

---

## 3. Problem Update Path

Event-driven. See [[Problem Update Path]].

```text
Problem state / workaround / worknote change  (or first Problem→Case linkage)
        │
[[AIPF_Flag Cases on Problem State or Work]]   → sets u_problem_updated = true
        │
Agent trigger: u_problem_updated → true  OR  problem field populated on case
        │
Tool 1  _getCaseProblemDetails()   (also clears flag + resets counter if flagged)
        │
Agent resolves LAST_TEMPLATE_STYLE / IMPLIED_STATE / NEW_WORKNOTE_AVAILABLE
        │
Tool 2  routing → routing_decision + selected_template
        │
Agent drafts ONE combined message (state body + workaround/worknote if applicable)
        │
NAP: Approve / Modify / Reject
        │
Tool 3  post to Additional Comments + AI disclaimer + counter update
```

### Business Rule logic — `AIPF_Flag Cases on Problem State or Work`

Fires on `problem` insert/update. Exit conditions and gates (grounded in the committed script):

1. **Trigger gate** — proceed only if insert, or `state` / `workaround` (non-empty) / `work_notes` changed.
2. **Resolution-code guard** — exit if `resolution_code` is `duplicate` or `risk_accepted`.
3. **Closed + Fix Applied guard** — exit if `state == 107` and `resolution_code == fix_applied` (already communicated at Resolved).
4. **Assess guard** — exit if a **state-only** change lands on `state == 102` (Assess).
5. **Work Item gate** — for `state IN (104 Fix in Progress, 106 Resolved)` and `resolution_code != canceled`, a `u_work_item` (child via `parent`) **must** exist or exit.
6. **Flag cases** — `u_problem_updated = true` on all `sn_customerservice_case` where `problem = current`, `active = true`, `category IN (0,1)` (Issue/Question), `state != 6` (not Solution Provided), optionally filtered by `sn_csm_ai_agents.case.filter.accounts`.

> [!info] Problem state codes seen in code
> `102` Assess · `104` Fix in Progress · `106` Resolved · `107` Closed. `New` and `Root Cause Analysis` are handled by display-name in the routing tool.

---

## 4. Stale Case Path

Time-driven safety net. See [[Stale Case Path]] and [[Stale Case Scheduled Job]].

The job query (committed script) selects cases that are:

- `active = true`, `assigned_to` NOT NULL, `category IN (0,1)`, `state != 6`
- `u_last_comment_from_unit4 <= now - staleDays` (gone quiet)
- **AND** (`u_auto_update_count < threshold` **OR** `u_auto_update_threshold_reached <= now - cooloffDays`) → i.e. under the no-change cap, or past cooloff
- optionally scoped by `case.filter.accounts` and `case.test.cases`

For each hit it calls `sn_fd.FlowAPI.startSubflowQuick(subflow, {case_number, run_as_user: assigned_to, trigger_timestamp})`.

> [!warning] Volume / batching is an open post-pilot item
> Pilot ≈ 30–40 qualifying cases per run across 2 accounts. No batching/pacing/cap exists — a large simultaneous qualifying set could spike platform load and flood a consultant's NAP. See [[#13. Risks & Open Questions]].

---

## 5. `caseUpdateAgentUtil` (Script Include)

Central utility in `sn_csm_ai_agents`. Methods:

| Method | Responsibility |
|---|---|
| `_getCaseProblemDetails(caseNumber)` | Fetch case + problem, compute vars, build templates, return everything. **Side effect:** clears `u_problem_updated`; if it was set, also resets `u_auto_update_count = 0` and clears `u_auto_update_threshold_reached`. |
| `_computeVariables(...)` | Derives `PROBLEM_LINKED`, `IS_FIRST_LINKAGE`, `RESOLUTION_CODE`, `PROBLEM_STATE`, `WI_REQUIRED` (FIP/Resolved), `CURRENT_WORKAROUND_VALUE`, `WORKAROUND_PREVIOUSLY_SHARED`, `WORKAROUND_PENDING`. As of 2026-07-24, also derives **`WORKAROUND_ONLY_LATEST_CHANGE`** — see [[#17. Changelog]]. |
| `_buildTemplates(...)` | Returns the [[Template Registry]] `7.1`–`7.10.2` with deterministic placeholders pre-filled (`greeting`, `sign_off`, case/product/problem numbers). As of 2026-07-24, greeting/sign-off use **first-name only** via new `cnFirst`/`caFirst` helpers (contact-name-first, case-assignee-first) — see [[#17. Changelog]]. |
| `_incrementAutoUpdateCount(caseNumber, resetToZero)` | `reset` → count 0 + clear stamp; else count+1 and stamp `u_auto_update_threshold_reached = now` when `count >= threshold`. |
| `_addCaseComment(caseNumber, commentText)` | Writes to `comments` (customer-visible) with appended `\n\n[Note: AI-assisted message reviewed by consultant]`. |

### Tool 1 wrapper script (literal, as configured on the AI Agent Tool)

```javascript
(function(inputs) {
    var caseNumber = inputs.case_number;
    if (!caseNumber) {
        return {
            success: false,
            error: 'Missing case_number input'
        };
    }

    var util = new sn_csm_ai_agents.caseUpdateAgentUtil();
    var data = util._getCaseProblemDetails(caseNumber);

    return {
        success: data.success,
        error: data.error || null,
        case_details: data.case_details,
        problem_details: data.problem_details,
        variables: data.variables,
        templates: data.templates,
        problem_url: data.problem_url || null
    };
})(inputs);
```

Shape worth reusing elsewhere: thin `inputs → util call → shaped return` wrapper on the AI Agent Tool itself, all real logic (ACL checks, side effects, field derivation) lives in the Script Include.

### Tool 3 wrapper script (literal, as configured on the AI Agent Tool)

Writer tool — posts the approved message, then updates the [[Counter and Cooloff]] state via `_incrementAutoUpdateCount`. Counter update only runs if the comment post itself succeeded, and only when `reset_count` isn't `'skip'`.

```javascript
(function(inputs) {
    // only string inputs are allowed 
    // return outputs object where the keys in it are understandable by LLM
    var caseNumber = inputs.case_number;
    var comment = inputs.customer_facing_update;
    var resetCount = inputs.reset_count;

    if (!caseNumber || !comment) {
        return {
            success: false,
            error: 'Missing required inputs: case_number and customer_facing_update'
        };
    }

    var util = new sn_csm_ai_agents.caseUpdateAgentUtil();
    var result = util._addCaseComment(caseNumber, comment);
    if (!result.success) {
        return {
            success: false,
            error: result.message
        };
    }



    // Update the auto update count only if comment posted successfully apart from No problem WIP/Awaiting info follow-up
  
    var validResetValues = ['true', 'false', 'skip'];
    if (validResetValues.indexOf(resetCount) === -1) {
        return {
            success: false,
            error: 'Invalid reset_count value: ' + resetCount + '. Must be true, false, or skip.'
        };
    }
    if (resetCount !== 'skip') {
        util._incrementAutoUpdateCount(caseNumber, resetCount === 'true');
    }
    return {
        success: true,
        message: result.message
    };

})(inputs);
```

### First-linkage detection (the clever bit)

`IS_FIRST_LINKAGE` is **not** guessed by the LLM — it's derived from `sys_journal_field`:

1. **Anchor** = oldest case work-note containing the Problem number + `"has been associated with the Case"`.
2. **Fallback anchor** = state-change work-note `"has been updated to state - <state>"`.
3. First-linkage is `true` **iff no AI comment** (matched by the disclaimer string) exists with `sys_created_on >= anchor`.

`comments_history` (last state-template style sent) and `worknote_history` (last 5 AI comments, for worknote dedup) are pulled the same way, with `[code]…[/code]` and `⚠` lines stripped. `WORKAROUND_PREVIOUSLY_SHARED` scans the last 10 AI comments for the plain-text workaround substring.

> [!tip] Why journal-mining instead of a flag
> There's no dedicated "last template sent" field — state history is reconstructed from the customer-visible journal, keyed off the AI disclaimer marker. Fragile if the disclaimer string or worknote wording changes; see maintainability risk.

---

## 6. Draft Posting & AI Disclaimer

Every approved message is written to **Additional Comments** with:

```text
<customer-facing body>

[Note: AI-assisted message reviewed by consultant]
```

That disclaimer string is load-bearing — it's the marker every history query above depends on.

---

## 7. Deterministic Routing

Tool 2 = [[Resolve routing decision and template selection]]. Pure script, **no LLM**. Inputs are the resolved variables; output is `{routing_decision, selected_template, append_workaround, append_worknote, fill_workaround_token, fill_worknote_token}`.

### Gate order

1. **Gate 1 — no problem linked** → `STOP_GATE1`; template `7.2` if case state contains "Awaiting", else `7.1`.
2. **Resolution guard** → `Risk Accepted` / `Duplicate` → `STOP` (no template, stop_reason surfaced in NAP).
3. **Closed + Canceled** → `6B` / `7.8`.
4. **Gate 3 — WI required** → proceeds only on positive confirmation that a Work Item exists; `STOP` if none is linked, or if `has_work_item` cannot be confirmed (hardened 2026-08-07).
5. **Workaround-only-change override (added 2026-07-24)** — if `WORKAROUND_ONLY_LATEST_CHANGE` is true (the latest Problem edit touched *only* the workaround field, and the value is genuinely new/not previously shared), template `7.4` fires **directly**, bypassing the 6A/6B/6C decision below entirely — regardless of what state-based bookkeeping (`IS_FIRST_LINKAGE`/`implied_state`) would otherwise compute. See [[#17. Changelog]] for why this was needed and how the variable is derived.

### Decision after gates

| Condition | `routing_decision` |
|---|---|
| `IS_FIRST_LINKAGE = true` | `6A` |
| no `implied_state` | `6B` |
| `problem_state == implied_state` | `6C` (state unchanged) |
| otherwise | `6B` (state changed) |

### Template selection matrix

| Route | Problem state / condition | Template |
|---|---|---|
| 6A first linkage | New / Assess | `7.3` |
| 6A | Root Cause Analysis | `7.6` |
| 6A | Fix in Progress | `7.7` |
| 6A | Resolved/Closed + Fix Applied | `7.5` |
| 6B state changed | New | `7.3` |
| 6B | Root Cause Analysis | `7.6` |
| 6B | Fix in Progress | `7.7` |
| 6B | Resolved + Fix Applied / Closed + Fix Applied | `7.5` |
| 6B | Resolved + Canceled | `7.8` |
| 6C state unchanged | workaround pending | `7.4` |
| 6C | new worknote available | `7.9` |
| 6C | prior was Resolved (Canceled/Fix Applied) | `7.10.1` (follow-up) |
| 6C | nothing new | `7.10.2` (no significant change) |
| any | undetermined | `STOP` (safety fallback) |

`append_*` flags let a state template also carry a workaround/worknote in one combined message (e.g. state body + `[WORKAROUND]`), while `7.4`/`7.9` own their token directly.

> [!bug] Open bug — 6B missing an 'Assess' check that 6A has (confirmed still open 2026-07-24)
> `6A` has an explicit `New || Assess` branch → template `7.3`. **`6B` has no equivalent `Assess` branch and no generic fallback** — a Problem sitting at `Assess` that routes through `6B` (i.e. not first-linkage, state changed) currently falls through to the safety-fallback `STOP`, with **no customer message sent at all**. This is the same gap already documented as a "known asymmetry" in [[Proactive Customer Case Communicator - ATF Test Suite]]'s T2 section (written 2026-07-16, mirrors the live tool's actual behavior rather than silently "fixing" the test) — not a newly discovered issue, just re-confirmed live and flagged here as still unresolved as of 2026-07-24.

### Tool 2 — `caseRoutingPCCCUtil` (Script Include)

Refactored 2026-08-07 from an inline AI Agent Tool wrapper into a Script Include, so it is unit-testable and version-controlled. Still a pure function — no reads, no writes, no LLM call inside it — matching the "deterministic first" design principle. The AI Agent Tool now calls `new caseRoutingPCCCUtil().resolve(inputs)` and returns its output unchanged.

The 6B bug above is still visible directly in this code: the `routingDecision === '6B'` branch has no `New || Assess` case, unlike `6A`'s explicit one.

> [!warning] Every input arrives as a **string**, and it is populated upstream
> The tool's input variables are filled before `resolve()` runs — they are not read straight off the record. A value can therefore arrive as `'false'`, `'False'`, `' false '`, `'No'`, `'null'`, or blank, and the same execution can contain an unresolved placeholder token where a value should be. **Any comparison here that tests `===` against a single literal is a latent bug.** Gate 1 was hardened for exactly this on 2026-08-07 — see [[#17. Changelog]]. The remaining boolean inputs (`wi_required`, `has_work_item`, `workaround_pending`, `new_worknote_available`, `is_first_linkage`) still use bare-literal comparisons and carry the same exposure; logged in [[#13. Risks & Open Questions]].

```javascript
var caseRoutingPCCCUtil = Class.create();
caseRoutingPCCCUtil.prototype = {
    initialize: function() {},

    /**
     * Deterministic routing + template selection for the Proactive Customer
     * Case Communicator. Pure function: no reads, no writes — decision only.
     *
     * @param {Object} inputs
     *   problem_linked, case_state, is_first_linkage, implied_state,
     *   problem_state, resolution_code, workaround_pending,
     *   new_worknote_available, wi_required, has_work_item, last_template_style
     * @return {Object} { success, routing_decision, selected_template,
     *   append_workaround, append_worknote, fill_worknote_token,
     *   fill_workaround_token, [stop_reason] }
     */
    resolve: function(inputs) {
        inputs = inputs || {};

        var isFirstLinkage = inputs.is_first_linkage;
        var impliedState = inputs.implied_state || null;
        var problemState = inputs.problem_state || '';
        var resolutionCode = inputs.resolution_code || '';
        var workaroundPending = inputs.workaround_pending;
        var newWorknoteAvailable = inputs.new_worknote_available;
        var lastTemplateStyle = inputs.last_template_style || null; // reserved

        // Gate 1 — No problem linked.
        //
        // Inputs arrive as upstream-populated strings, so this value shows up as
        // 'false', 'False', ' false ', 'No', 'null' or blank depending on who
        // filled it. The previous test (=== false || === 'false') matched only
        // two of those; every other shape fell through into the 6A/6B/6C
        // classification below, which assumes a Problem exists — producing a
        // 'Template could not be determined ... routing_decision: 6B' stop and
        // NO customer message, on a case that should have received 7.1 or 7.2.
        // Normalise first, then branch on all three outcomes explicitly.
        var problemLinked = this._boolish(inputs.problem_linked);

        if (problemLinked === 'unknown') {
            // Present but uninterpretable. Do not guess: guessing 'not linked'
            // would tell a customer no Problem is linked when one may well be.
            return this._stop('problem_linked could not be interpreted as a boolean ' +
                '(received: ' + JSON.stringify(inputs.problem_linked) + '). ' +
                'No message sent — fix the input before retrying.');
        }

        if (problemLinked === 'false' || problemLinked === 'empty') {
            var caseState = inputs.case_state || '';
            if (caseState.indexOf('Awaiting') !== -1) {
                return this._out('STOP_GATE1', '7.2');
            }
            return this._out('STOP_GATE1', '7.1');
        }

        // Resolution guard — Risk Accepted / Duplicate
        if (resolutionCode === 'Risk Accepted' || resolutionCode === 'Duplicate' ||
            resolutionCode.toLowerCase() === 'risk accepted' ||
            resolutionCode.toLowerCase() === 'duplicate') {
            return this._stop('No communication required — Problem resolution code is ' +
                resolutionCode + '. Case update skipped.');
        }

        // Gate 2b — Closed + Canceled (before WI gate)
        if (problemState === 'Closed' && resolutionCode === 'Canceled') {
            return this._out('6B', '7.8');
        }

        // Gate 3 — Work Item required but not linked.
        //
        // This gate protects a customer message, so it must fail CLOSED. The
        // previous test (=== true / === 'false' on raw inputs) failed open in
        // both directions: wi_required 'True' read as not-required and skipped
        // the gate entirely, and has_work_item 'False' read as not-false, which
        // also skipped it — either one releasing a message on a Problem with no
        // Work Item linked. Normalise, then require positive confirmation.
        //
        // An ABSENT wi_required stays "not required" on purpose: per the Business
        // Rule in §3, a Work Item is only demanded for states 104 (Fix in
        // Progress) and 106 (Resolved), and every New/Assess/RCA path omits the
        // input entirely. Treating blank as "required" would silence those.
        var wiRequired = this._boolish(inputs.wi_required);
        var hasWorkItem = this._boolish(inputs.has_work_item);

        if (wiRequired === 'unknown') {
            return this._stop('wi_required could not be interpreted as a boolean ' +
                '(received: ' + JSON.stringify(inputs.wi_required) + '). ' +
                'No message sent — fix the input before retrying.');
        }

        if (wiRequired === 'true') {
            if (hasWorkItem === 'false') {
                return this._stop('No Work Item linked to Problem. Communication cannot be ' +
                    'sent until a Work Item is linked. Please review.');
            }
            if (hasWorkItem !== 'true') {
                // 'empty' or 'unknown'. A required Work Item that cannot be
                // confirmed is not a confirmed Work Item — do not release a
                // customer message on the strength of an unverified gate.
                return this._stop('A Work Item is required for this Problem state but ' +
                    'has_work_item could not be confirmed (received: ' +
                    JSON.stringify(inputs.has_work_item) + '). ' +
                    'No message sent — fix the input before retrying.');
            }
        }

        // Routing decision
        var routingDecision;
        if (isFirstLinkage === true || isFirstLinkage === 'true') {
            routingDecision = '6A';
        } else if (!impliedState || impliedState === 'null') {
            routingDecision = '6B';
        } else if (problemState === impliedState) {
            routingDecision = '6C';
        } else {
            routingDecision = '6B';
        }

        // Template selection
        var selectedTemplate;

        if (routingDecision === '6A') {
            if (problemState === 'New' || problemState === 'Assess') {
                selectedTemplate = '7.3';
            } else if (problemState === 'Root Cause Analysis') {
                selectedTemplate = '7.6';
            } else if (problemState === 'Fix in Progress') {
                selectedTemplate = '7.7';
            } else if ((problemState === 'Resolved' || problemState === 'Closed') &&
                resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            }
        } else if (routingDecision === '6B') {
            if (problemState === 'New') {
                selectedTemplate = '7.3';
            } else if (problemState === 'Root Cause Analysis') {
                selectedTemplate = '7.6';
            } else if (problemState === 'Fix in Progress') {
                selectedTemplate = '7.7';
            } else if (problemState === 'Resolved' && resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            } else if (problemState === 'Resolved' && resolutionCode === 'Canceled') {
                selectedTemplate = '7.8';
            } else if (problemState === 'Closed' && resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            }
        } else if (routingDecision === '6C') {
            if (workaroundPending === true || workaroundPending === 'true') {
                selectedTemplate = '7.4';
            } else if (newWorknoteAvailable === true || newWorknoteAvailable === 'true') {
                selectedTemplate = '7.9';
            } else if (impliedState === 'Resolved' &&
                (resolutionCode === 'Canceled' || resolutionCode === 'Fix Applied')) {
                selectedTemplate = '7.10.1';
            } else {
                selectedTemplate = '7.10.2';
            }
        }

        // Safety fallback — never return undefined template
        if (!selectedTemplate) {
            return this._stop('Template could not be determined for problem_state: ' +
                problemState + ', resolution_code: ' + resolutionCode +
                ', routing_decision: ' + routingDecision);
        }

        var appendWorkaround = (workaroundPending === true || workaroundPending === 'true') &&
            selectedTemplate !== '7.4';
        var appendWorknote = (newWorknoteAvailable === true || newWorknoteAvailable === 'true') &&
            selectedTemplate !== '7.9';

        return {
            success: true,
            routing_decision: routingDecision,
            selected_template: selectedTemplate,
            append_workaround: appendWorkaround,
            append_worknote: appendWorknote,
            fill_worknote_token: selectedTemplate === '7.9',
            fill_workaround_token: selectedTemplate === '7.4'
        };
    },

    // ---- helpers (keep return shape identical to the original tool) ----

    /**
     * Normalise an upstream-populated tool input to one of four explicit
     * states: 'true' | 'false' | 'empty' | 'unknown'.
     *
     * Deliberately returns strings, not a boolean-or-null, so that "absent"
     * and "not a boolean" stay distinguishable at the call site. Collapsing
     * them is what let a blank value be read as a legitimate answer.
     */
    _boolish: function(v) {
        if (v === true) return 'true';
        if (v === false) return 'false';
        if (v === null || v === undefined) return 'empty';

        var s = String(v).trim().toLowerCase();
        if (s === '' || s === 'null' || s === 'undefined') return 'empty';
        if (s === 'true' || s === 'yes' || s === 'y' || s === '1') return 'true';
        if (s === 'false' || s === 'no' || s === 'n' || s === '0') return 'false';
        return 'unknown';
    },

    _out: function(decision, template) {
        return {
            success: true,
            routing_decision: decision,
            selected_template: template,
            append_workaround: false,
            append_worknote: false,
            fill_worknote_token: false,
            fill_workaround_token: false
        };
    },

    _stop: function(reason) {
        return {
            success: true,
            routing_decision: 'STOP',
            selected_template: null,
            stop_reason: reason,
            append_workaround: false,
            append_worknote: false,
            fill_worknote_token: false,
            fill_workaround_token: false
        };
    },

    type: 'caseRoutingPCCCUtil'
};
```

---

## 8. Template Registry

Built by `_buildTemplates()`. `reset_count` drives [[Counter and Cooloff]] behaviour on post.

> [!info] Rewritten 2026-07-24 — first-name greeting/sign-off + 7 bodies rewritten verbatim
> Greeting and sign-off across templates `7.3`–`7.8` and `7.10.2` now use **first name only** (via new `cnFirst`/`caFirst` helper functions — contact-name-first / case-assignee-first), not the full name. The bodies of `7.3`, `7.4`, `7.5`, `7.6`, `7.7`, `7.8`, and `7.10.2` were rewritten **verbatim per a canonical template sheet** (source: `Prompt_16_07_after requested improvements.txt`, tracked as a reference memory outside this vault). `7.1`, `7.2`, `7.9`, and `7.10.1` were **left untouched** — they still use `cs`/`pn`/`[MEANINGFUL_TITLE]` placeholders as before, but now automatically inherit the first-name greeting/sign-off since that logic lives in the shared helper, not per-template. See [[#17. Changelog]].

| ID | reset_count | Use | Greeting |
|---|---|---|---|
| `7.1` | skip | No problem linked, case In Progress — "actively reviewing" | Dear |
| `7.2` | skip | No problem linked, Awaiting Customer Info — follow-up | Dear |
| `7.3` | true | Problem identified (New/Assess) | Dear |
| `7.4` | true | Workaround shared `[WORKAROUND]` | Dear |
| `7.5` | true | Fix in upcoming release `[RELEASE_VERSION]` → Solution Provided | Hi |
| `7.6` | true | Root Cause Analysis / technical assessment | Dear |
| `7.7` | true | Work Item In Progress (fix being built) | Dear |
| `7.8` | true | Working-as-designed / closed, no fix | Dear |
| `7.9` | true | Worknote update `[WORKNOTE]` | Dear |
| `7.10.1` | false | Follow-up after fix applied | Dear |
| `7.10.2` | false | No significant change | Dear |

Placeholders still LLM/agent-filled: `[MEANINGFUL_TITLE]`, `[RELEASE_VERSION]`, and the synthesised `[WORKAROUND]` / `[WORKNOTE]` bodies.

---

## 9. Counter and Cooloff

See [[Counter and Cooloff]]. Prevents low-value "no change" spam on the stale path.

```text
reset_count=true  → count 0, threshold stamp cleared  (meaningful update)
reset_count=false → count +1; stamp when count >= threshold  (no-change / follow-up, problem linked)
reset_count=skip  → counter untouched  (no problem linked; surfaces every run)
```

Lifecycle (defaults: threshold 3, cooloff 7d, stale 2d):

```text
no-change #1 → count 1
no-change #2 → count 2
no-change #3 → count 3  → u_auto_update_threshold_reached = now  → cooloff starts
… case excluded from job for 7 days …
cooloff expires → picked up → next no-change RE-STAMPS threshold → new 7-day cooloff
meaningful Problem update (via Problem Update Path) → FULL reset to 0
```

> [!important] Only a meaningful Problem update resets to 0
> Cooloff expiry does **not** reset the counter — the first post-cooloff no-change message re-stamps and restarts cooloff. Full reset happens exclusively through `_getCaseProblemDetails()` clearing the flag, or Tool 3 with `reset_count=true`.

---

## 10. Data Model

Custom fields on `sn_customerservice_case`:

| Field | Type | Purpose |
|---|---|---|
| `u_problem_updated` | Boolean | Set true by BR to trigger agent; cleared when Tool 1 picks the case |
| `u_auto_update_count` | Integer | No-change message count (stale path, problem linked) |
| `u_auto_update_threshold_reached` | DateTime | Stamped at threshold; drives cooloff exclusion |
| `u_last_comment_from_unit4` | (journal-derived) | Last agent/Unit4 comment timestamp — staleness measure |

---

## 11. System Properties

| Property | Default | Purpose |
|---|---|---|
| `sn_csm_ai_agents.u4.case.update.stale.threshold.days` | 2 | Days quiet before pickup |
| `sn_csm_ai_agents.u4.case.auto.update.threshold` | 3 | Max no-change messages before cooloff |
| `sn_csm_ai_agents.case.auto.update.cooloff.days` | 7 | Cooloff window after threshold |
| `sn_csm_ai_agents.case.filter.accounts` | — | Restrict to accounts (optional; empty = all) |
| `sn_csm_ai_agents.case.test.cases` | — | Restrict to specific case numbers (testing) |

---

## 12. Security & Access

- Role added to agent data-access / user-access config: `sn_customerservice.now_assist_users`.
- Agent runs **as the Case Assigned To user** → that user must be active, unlocked, and a Now Assist CSM user, or the execution fails.
- ACL committed in the Case update set for the custom fields.

---

## 13. Risks & Open Questions

> [!caution] These are carried from prior design/operational analysis, not all verifiable from the update-set scripts. Flagged as such.

### Verified from code
- **Journal-string coupling** — every history/first-linkage query depends on the exact disclaimer string `[Note: AI-assisted message reviewed by consultant]` and worknote phrasing (`"has been associated with the Case"`, `"has been updated to state -"`). Change the wording anywhere and detection silently breaks.
- **WI check duplicated** — Work-Item existence is enforced in both [[AIPF_Flag Cases on Problem State or Work]] (state `104/106`) and [[Resolve routing decision and template selection]] (`WI_REQUIRED`). Two authorities → patch one, miss the other.
- **No batching in [[Stale Case Scheduled Job]]** — every qualifying case fires a subflow in one `while` loop. No cap, pacing, or backpressure.
- **Bare-literal boolean comparisons remain on the content flags** (found 2026-08-07, partially fixed) — Gates 1 and 3 now normalise through `_boolish()`, but `workaround_pending`, `new_worknote_available` and `is_first_linkage` still test `=== true || === 'true'`. Each silently treats `'True'`, `' true '`, `'Yes'` and `'1'` as *not* set. These fail in the **quiet** direction rather than the dangerous one — a workaround or worknote is simply not communicated, and `is_first_linkage` misreads route 6A as 6B — so no wrong statement reaches a customer. Lower priority than the gates, but the same one-line change each.
- **Tool inputs are not trustworthy as delivered** (found 2026-08-07) — a live execution carried `new_worknote_available: "{organize_general_knowledge}.4"`, an unresolved placeholder token, alongside blanks in every other Problem field. Inputs are populated upstream and arrive as strings; the router cannot assume they are well-formed. There is no validation step between population and `resolve()`.

### From prior notes (unverified here)
- **Stuck execution / silent exclusion** — if an execution hangs, is the case ever re-picked? No self-healing documented.
- **NAP shows internal variable** — consultants occasionally saw `{ "NEW_PROBLEM_WORKNOTE_AVAILABLE": true }` instead of the draft; likely approval-step content mapping, not draft generation. Confirm which output variable is bound to the NAP confirmation. **Still open as of 2026-07-24** — not addressed by this session's fixes (those targeted `[RELEASE_VERSION]`/`[WORKAROUND]`/`[WORKNOTE]` token leakage specifically, a related but distinct symptom — see [[#17. Changelog]]).
- **Large-context / token limits** — long case histories may exceed model/exec limits; consider summarising older worknotes.
- **Assigned-user eligibility** — locked/inactive user or missing Now Assist CSM group membership → execution error. Needs daily monitoring.
- **6B missing an Assess-state branch** (found 2026-07-24) — see the bug callout in [[#7. Deterministic Routing]]. Not yet fixed.

### Resolved 2026-08-07 — see [[#17. Changelog]]
- ~~Gate 1 missed every `problem_linked` value except boolean `false` and the exact string `'false'`~~ — fixed via `_boolish()` normalisation; blank, missing, `'False'`, `' false '`, `'No'`, `'0'` and `'null'` now all trip the gate.
- ~~Gate 3 failed **open** on `wi_required` / `has_work_item`~~ — fixed; the gate now requires positive confirmation that a Work Item exists before letting a message through, instead of only stopping on two exact literals.

### Resolved this session (2026-07-24) — see [[#17. Changelog]] for full detail
- ~~`[RELEASE_VERSION]` placeholder/filler leaking into drafts~~ — fixed; placeholder/filler `fix_notes` now treated as empty, token deleted and sentence rewritten instead of leaking through.
- ~~Token-leak check only ran once~~ — Step 6.4's token scan is now mandatory/always-run (even after the 6.1 fix runs) and also scans for `[WORKAROUND]`/`[WORKNOTE]`, not just `[RELEASE_VERSION]`.
- ~~Workaround-only Problem edits not reliably firing template 7.4~~ — fixed via the new `WORKAROUND_ONLY_LATEST_CHANGE` variable + routing override gate (see [[#7. Deterministic Routing]]). Confirmed working end-to-end on live test.
- ~~`[WORKAROUND]` token not filling on some test cases~~ — investigated, **not a bug**: confirmed this is the CLEAN AND FILTER CONTENT semantic filter correctly rejecting placeholder/junk test text, the same rule that blocks "N/A"/"TBD" workarounds from ever reaching a customer. Working as designed.

### Open questions
- Max cases per run / cap / batching strategy before broad rollout?
- Timeout + owner for stuck executions?
- Exact NAP-bound output variable, and is the draft stored separately from routing vars?
- Automated maintenance of Now Assist CSM group membership?
- Business vs technical ownership; UAT sign-off gate before Production job activation?

---

## 14. Deployment (Update Sets)

Import order matters (fields/scope first, agent config last). Key sets:

- `Proactive case communication – Case` — custom fields on `sn_customerservice_case`
- `Proactive Case communication - monitor case` — base agent config (post-clone)
- `AIPF_Proactive case_trigger flow and notification` (Global)
- `AIPF_proactive_case_communication_2` — instructions, tools, BR, Script Include, properties
- `AIPF_proactive_case_communication_2_agent_user_role` — role grant
- `…_refinement`, `…_refinement 2`, `…_refinement 4` (ignore refinement 3 — folded into 4)
- `…_script_include`, `…_script_include 2`, `…_scriptinclude_stale` — journal/history + routing tool
- `AIPF_NAP conversation idle timeout` — 24h → 72h (Global, per Unit4 request)

Post-deploy: agent active, 3 tools attached, trigger active, Script Include in scope, BR active on `problem`, 5 properties present, custom fields present, **Scheduled Job present but INACTIVE** until UAT sign-off.

---

## 15. Design Principles

1. [[Human in the Loop]] — draft only; consultant Approve/Modify/Reject; no autonomous sends.
2. **Deterministic first, AI second** — BR + routing tool + Script Include own every branch; LLM writes prose.
3. **Communication hygiene** — Risk Accepted / Duplicate suppressed, WI-gated states, workaround/worknote dedup.
4. **Pacing** — [[Counter and Cooloff]] caps no-change noise.
5. **Read/write separation** — Tool 1 read, Tool 2 decide, Tool 3 write.

---

## 16. Scorecard

| Area | Assessment | Score |
|---|---|---:|
| Business value | Real trust/escalation problem | 9/10 |
| Governance | Strong human-in-the-loop | 10/10 |
| AI safety | AI drafts, deterministic decides | 9/10 |
| Maintainability | Journal-string coupling + duplicated WI checks | 6/10 |
| Scalability | No batching/cap on stale job | 6/10 |
| Operational monitoring | No stuck-execution/failure monitoring | 5/10 |
| CX impact | High if stable | 9/10 |

> [!summary] Verdict
> Architecturally sound and business-relevant. Strongest choice: separating deterministic process logic from AI language. Main gap is **operational reliability** — batching, stuck-execution monitoring, NAP content mapping, user/group eligibility, and decoupling detection from magic strings — before broad production rollout.

---

## 17. Changelog

Session-by-session record of live changes to the deployed PCCC components. Source: VS Code Claude Code session working directly against the ServiceNow instance (Agent API), not this vault — captured here after the fact so the architecture doc stays current.

### 2026-08-07 — Routing tool moved to a Script Include; Gate 1 hardened

**Refactor — `caseRoutingPCCCUtil` (Script Include)**
- The inline Tool 2 wrapper (`(function(inputs){...})(inputs)`) became a Script Include exposing `resolve(inputs)`, with `_out()`/`_stop()` helpers. Return shape is byte-identical to the previous tool, so nothing downstream changes. The AI Agent Tool now calls `new caseRoutingPCCCUtil().resolve(inputs)`.
- Motivation: the inline script was not unit-testable, which is how the Gate 1 defect below survived a full ATF suite.

**Bug — Gate 1 fell through for almost every representation of "no problem linked"**

Reported live: a case with no Problem linked produced

```
Stop reason : Template could not be determined for problem_state: , resolution_code: , routing_decision: 6B
```

Diagnosis. Gate 1 tested `problemLinked === false || problemLinked === 'false'` — two literals. Inputs are populated upstream and arrive as **strings**, so the value also appears as `'False'`, `' false '`, `'No'`, `'0'`, `'null'`, or blank. Any of those skipped the gate and fell into the 6A/6B/6C classification, which assumes a Problem exists. With no `implied_state`, the decision table sends that straight to `6B`; the `6B` branch has no case for an empty `problem_state`, so it hit the safety fallback and stopped. **The customer received nothing, where the design specifies template `7.1` (or `7.2` when the case state contains "Awaiting").**

The `STOP` message named `6B`, which made this look like the open 6B/Assess bug. It is unrelated — 6B was only ever the fall-through destination, never a decision about the Problem.

Fix. Added `_boolish(v)`, returning one of four explicit states — `'true'`, `'false'`, `'empty'`, `'unknown'` — after trimming and lowercasing. Gate 1 now branches on all of them:

| `problem_linked` | outcome |
|---|---|
| `true`, `'true'`, `'yes'`, `'y'`, `'1'` | proceed to the resolution guard |
| `false`, `'false'`, `'no'`, `'n'`, `'0'` (any case, any padding) | `STOP_GATE1` → `7.1` / `7.2` |
| missing, `null`, `''`, `'null'`, `'undefined'` | `STOP_GATE1` → `7.1` / `7.2` |
| anything else (e.g. a Problem number) | `STOP` with a named `stop_reason`, no message |

`'empty'` deliberately routes to Gate 1 rather than to `STOP`: a case whose Problem fields are *all* blank is a case with no Problem. The `'unknown'` branch exists so an uninterpretable value never becomes a guess — telling a customer no Problem is linked when one may be is worse than sending nothing.

`_boolish` returns strings rather than a boolean-or-null so that "absent" and "not a boolean" stay distinguishable at the call site. Collapsing them is what let a blank value read as a legitimate answer in the first place.

Verified. The full T2 matrix plus 17 new Gate 1 cases — 34 checks, 0 failures — and the reported input replayed verbatim now yields `STOP_GATE1` / `7.1`. Note the reported payload rendered as `problem_linked: false`, which the *old* code handles correctly; replaying it against the old script confirms the runtime value must have been one of the other shapes above, since every one of those reproduces the reported stop exactly.

**Bug — Gate 3 failed open on `wi_required` / `has_work_item`**

Same root cause as Gate 1, found while fixing it, and worse in effect. The gate read:

```javascript
if ((wiRequired === true || wiRequired === 'true') &&
    (hasWorkItem === false || hasWorkItem === 'false')) {
```

Both halves had to match exact literals for the gate to fire, so it failed **open** in two independent ways: `wi_required: 'True'` read as not-required and skipped the gate entirely, and `has_work_item: 'False'` read as not-`'false'` and also skipped it. Either one released a customer message on a Problem with **no Work Item linked** — the precise thing the gate exists to prevent, and unlike the Gate 1 defect this one sends a message rather than withholding one.

Fix. Both inputs go through `_boolish()`, and the gate now demands *positive confirmation* rather than only stopping on a recognised negative:

| `wi_required` | `has_work_item` | outcome |
|---|---|---|
| false / absent / blank | anything | gate does not apply — proceed |
| true | true | proceed |
| true | false | `STOP` — "No Work Item linked to Problem" (unchanged wording) |
| true | blank, missing, or unrecognised | `STOP` — presence could not be confirmed |
| unrecognised | anything | `STOP` — `wi_required` uninterpretable |

An **absent** `wi_required` deliberately stays "not required": per the Business Rule in [[#3. Problem Update Path]] a Work Item is only demanded for states `104` (Fix in Progress) and `106` (Resolved), and every New/Assess/RCA path omits the input. Treating blank as required would silence those. This is the opposite default to Gate 1, and for the opposite reason — there, blank Problem fields *are* the evidence of no Problem.

Verified. 13 new T2 rows, 50 checks total, 0 failures. Reverting only the gate body and re-running fails 9 of them — each returning `6B` / `7.7`, i.e. a live "Fix in Progress" update sent on a Problem with no confirmed Work Item. The tests were confirmed capable of failing before being trusted.

> [!note] Gate 3 is one of two authorities
> [[AIPF_Flag Cases on Problem State or Work]] enforces the same Work-Item rule before the agent ever fires ([[#13. Risks & Open Questions]], "WI check duplicated"). This change hardens the router's copy only. The Business Rule's own check was not reviewed for the same class of defect.

**Found, not fixed (flagged so it isn't lost)**
- `workaround_pending`, `new_worknote_available` and `is_first_linkage` still use bare-literal comparisons. They fail quietly rather than dangerously — content is omitted, not misstated — so they were left for a separate change. See [[#13. Risks & Open Questions]].
- The same execution carried `new_worknote_available: "{organize_general_knowledge}.4"` — an unresolved placeholder token. Benign in the router (it is not `'true'`), but it means input population itself is producing malformed values and nothing validates them before `resolve()` runs. Root cause not investigated.
- `6B` still has no `Assess` branch (open since 2026-07-24, untouched here).

### 2026-07-24 — Template rewrite, prompt hardening, workaround-only-change fix

**Phase 1 — Template rewrite (`caseUpdateAgentUtil.script.js`, live in ServiceNow)**
- Added first-name greeting/sign-off helpers (`cnFirst`/`caFirst`) — templates now greet/sign with first name only, not full name.
- Rewrote the 7 "Z-column" bodies verbatim per a canonical template sheet: `7.3`, `7.4`, `7.5`, `7.6`, `7.7`, `7.8`, `7.10.2`.
- Left `7.1`, `7.2`, `7.9`, `7.10.1` untouched (still `cs`/`pn`/`[MEANINGFUL_TITLE]`-based) — they now inherit first-name greeting/sign-off automatically since that logic moved into the shared helper.

**PCCC agent prompt** (canonical source: `Prompt_16_07_after requested improvements.txt`, saved as a reference memory outside this vault — not itself a vault file)
- **Step 6.1 fix** — `[RELEASE_VERSION]` handling: placeholder/filler `fix_notes` now treated as empty; the token is deleted and the sentence rewritten, instead of the literal placeholder leaking into the customer-facing draft.
- **Step 6.4 hardened** — the token-leak check is now mandatory/always-run (even after 6.1 runs), and scans for `[WORKAROUND]`/`[WORKNOTE]` too, not just `[RELEASE_VERSION]`.
- **New Step 5.5** — for template `7.8` (Problem Resolved+Canceled / Closed+Canceled), the consultant is now explicitly prompted to pick 1 of 3 closings before drafting — the AI no longer infers the closing from cause notes.
- **Steps 7.1/7.3 (Approve/Modify/Reject)** changed to numbered-list format — NAP renders these as clickable buttons, confirmed working, same rendering mechanism already used for the `7.8` closing-choice options (see Step 5.5 above).
- **Step 5 tool-call inputs rewritten** as an explicit named list ("copy verbatim, don't re-derive") — fixes an LLM reliability bug where a fetched variable (`WORKAROUND_PENDING`) was being silently mistranscribed before being passed on.

> [!note] Step numbering has shifted since this doc's original walkthrough
> The architecture note's [[#3. Problem Update Path]] flow diagram and the Part A walkthrough in [[PCCC - Testing - ATF Build & Manual Runbook]] describe an earlier Step 1–6 structure (fetch → clean → title → worknote-availability JSON → routing JSON → draft). The live prompt now has sub-steps (5.5, 6.1, 6.4, 7.1, 7.3) layered into that structure per the fixes above. The high-level flow (fetch → clean → route → draft → NAP approval → post) is unchanged; only the fine-grained step numbering inside "resolve variables" and "draft/approve" has grown more granular. Treat the original Step 1–6 summary as the conceptual model, and this changelog as the current implementation detail.

**Workaround-only-change scenario** (previously not firing reliably)
- Diagnosed the real-time trigger chain end-to-end: BR → `u_problem_updated` flag → Flow Designer trigger (`u_problem_updated CHANGESTO true`) → agent. Confirmed this pipeline does work as designed.
- Added **`WORKAROUND_ONLY_LATEST_CHANGE`** — a new deterministic variable in `caseUpdateAgentUtil.script.js`, derived from existing `sys_audit`/`sys_journal_field` history. Deliberately **no new schema field** was added (explicit call made to avoid one).
- Added an override gate in [[Resolve routing decision and template selection]] (see [[#7. Deterministic Routing]]): when the latest Problem edit touched only the workaround field and it's genuinely new/unshared, template `7.4` fires directly, regardless of state-based `6A`/`6B`/`6C` bookkeeping drift.
- Fixed a sync gap where local Script Include edits weren't reaching the live instance — pushed directly via the Agent API, confirmed live.
- **Rolled back** an earlier BR-based direct-invocation experiment — [[AIPF_Flag Cases on Problem State or Work]] (`AIPF_FlagCasesonProblemStateorWork.script.js`) is back to its original, untouched state.
- **Confirmed working end-to-end**: template `7.4` fired correctly on the next real test.

**Investigated, no code change (working as designed)**
- `[WORKAROUND]` token not filling on some test cases — confirmed this is the CLEAN AND FILTER CONTENT semantic filter correctly rejecting placeholder/junk test text, by design (same rule blocking "N/A"/"TBD" workarounds from reaching customers).

**Found, not yet fixed (flagged so it isn't lost)**
- The routing tool's `6B` branch is missing an `Assess`-state check that `6A` has — a Problem sitting at `Assess` routed through `6B` currently falls through to the safety-fallback `STOP` with no message sent. See the bug callout in [[#7. Deterministic Routing]].

---

## Related Notes

- [[Monitor Work Item AI Agent]] — sibling agent, `u_work_item` → Problem worknote, Global scope
- [[Problem Update Path]]
- [[Stale Case Path]]
- [[AIPF_Flag Cases on Problem State or Work]]
- [[caseUpdateAgentUtil]]
- [[Resolve routing decision and template selection]]
- [[caseRoutingPCCCUtil]] — extracted Script Include version of the routing logic, see [[Proactive Customer Case Communicator - ATF Test Suite]]
- [[Stale Case Scheduled Job]]
- [[Template Registry]]
- [[Counter and Cooloff]]
- [[Now Assist Panel]]
- [[Now Assist]]
- [[PCCC - Testing - ATF Build & Manual Runbook]] — agent walkthrough + full testing matrix
- [[PCCC - Manual Test Scenarios]] — actor-based runnable test scripts
- [[Problem Management]]
- [[Work Item]]
- [[Human in the Loop]]

#servicenow #ai-agent #now-assist #csm #problem-management #architecture #unit4
