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
| [[stale-case-summarization-skill-notes\|Stale Case Summarization]] (Now Assist skill) | AI Skill (called from `_getStaleCaseSum()`) | Generates the `7.10.2` body — see [[#8. Template Registry]] |
| [[Stale Case Scheduled Job]] | Scheduled Job (`ProactiveCasecommunication-MonitorCase.script.js`) | 5 independent priority/link-state rules, each with its own stale-day threshold — see [[#4. Stale Case Path]] |
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

> [!info] Rewritten — single threshold → 5 priority/link-state rules (as of the script currently deployed)
> The job no longer runs one blanket `u_last_comment_from_unit4 <= now - staleDays` query. It now runs **5 independent rules**, each its own `GlideRecord` query against a shared base filter, so per-rule row counts and skip reasons are traceable in the log individually.

**Shared base filter** (AND-prefix on every rule):

```text
active=true ^ assigned_toISNOTEMPTY ^ categoryIN0,1 ^ stateNOT IN3,6,18
[^ accountIN<case.filter.accounts>]        (optional)
[^ numberIN<case.test.cases>]              (optional)
^ (u_auto_update_count<threshold OR u_auto_update_threshold_reached<=now-cooloffDays)
```

**Per-rule stale-day thresholds:**

| Rule | Condition | Stale window | Property |
|---|---|---|---|
| 1 | P1/P2, **no** linked Problem | Monday/Thursday review cycle **only** — no run on other days | `sn_csm_ai_agents.u4.case.update.stale.threshold.days` |
| 2 | P1/P2, linked Problem, `problem.state = 104` (Fix in Progress) | 14 days | `sn_csm_ai_agents.u4.case.p1p2.linked.fip.stale.days` |
| 3 | P1/P2, linked Problem, any other state | 7 days | `sn_csm_ai_agents.u4.case.p1p2.linked.stale.days` |
| 4 | P3/P4, **no** linked Problem | 10 days | `sn_csm_ai_agents.u4.case.p3p4.nolink.stale.days` |
| 5 | P3/P4, linked Problem | 28 days | `sn_csm_ai_agents.u4.case.p3p4.linked.stale.days` |

Rule 1 is the only one gated by day-of-week (`gdt.getDayOfWeekLocalTime()`, 1=Monday, 4=Thursday); rules 2–5 run every time the job fires.

**Per-case skip logic — now duplicated into the job itself**, not left solely to the BR/routing tool:

1. **Problem resolution-code guard** — if the case has a linked Problem with `resolution_code` `risk_accepted` or `duplicate`, skip.
2. **Work Item gate** — if the linked Problem's `state` is `104` (Fix in Progress) or `106` (Resolved) and no `u_work_item` (via `parent`) exists, skip.
3. **Active-execution dedup** — if an `sn_aia_execution_plan` for agent `db969eb8870ffed0d939a7573cbb35b8` already exists with `objective CONTAINS <case number>` and `state IN (ready, in_progress)`, skip (prevents duplicate stale-path fires while a prior execution is still running). The **Problem Update Path is exempt** from this check — it always fires regardless.

For each surviving case: `sn_fd.FlowAPI.startSubflowQuick(subflow, {case_number, run_as_user: assigned_to, trigger_timestamp})`, wrapped in try/catch (`gs.error` on failure, loop continues). Job logs a per-rule match count and a final `totalNumberOfRecProccessed` / `totalNumberSkipped` tally.

> [!bug] Triple-duplicated WI/resolution-code gating
> The resolution-code guard and the Work Item gate now exist in **three** places: [[AIPF_Flag Cases on Problem State or Work]] (BR, Problem Update Path), [[Resolve routing decision and template selection]] (`WI_REQUIRED`/`wi_required`), and now this scheduled job (Stale Case Path). Three independent authorities enforcing the same rule — patch one, miss the other two. See [[#13. Risks & Open Questions]].

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
| `_getStaleCaseSum(caseNumber)` | Generates the `7.10.2` body by invoking the [[stale-case-summarization-skill-notes\|Stale Case Summarization]] Now Assist skill (`sn_one_extend.OneExtendUtil.executeSecure`, `capabilityId: '5fd7239187aecb10d939a7573cbb3556'`, `skillConfigId: 'b3d7639187aecb10d939a7573cbb3589'`), passing `case_number`, and returning the raw skill response JSON as the body string. Returns `''` on failure (logged via `gs.error`, no throw). |

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

`comments_history` (last state-template style sent) is pulled the same way. `case_details.prior_ai_comments` holds the **last 3** customer-visible comments (AI + human, not 5), with `[code]…[/code]` blocks and `⚠` lines stripped — used **only** for worknote/workaround dedup (Step 4/Step 2 of the agent prompt), not for state derivation. `WORKAROUND_PREVIOUSLY_SHARED` scans the last 10 AI comments for the plain-text workaround substring.

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

1. **Gate 1 — no problem linked** → `STOP_GATE1`; template `7.2` if case state contains "Awaiting", else `7.1`. `problem_linked` is normalised through a `_boolish()` helper (`true`/`false`/`empty`/`unknown`) rather than a raw `=== false || === 'false'` check — an **`unknown`** shape (present but uninterpretable) now hard-**`STOP`**s with a review message instead of silently falling through into the 6A/6B/6C classification below, which previously produced a bogus "template could not be determined / `6B`" stop on cases that should have received `7.1`/`7.2`.
2. **Resolution guard** → `Risk Accepted` / `Duplicate` → `STOP` (no template, stop_reason surfaced in NAP).
3. **Closed + Canceled** → `6B` / `7.8`.
4. **Gate 3 — WI required** → proceeds only on positive confirmation that a Work Item exists; fails **CLOSED** via the same `_boolish()` normalisation as Gate 1 (hardened 2026-08-07): `wi_required` `unknown` → `STOP`; `wi_required = true` with `has_work_item = false` → `STOP` (no WI); `has_work_item` anything other than a confirmed `true` (i.e. `empty`/`unknown`) → `STOP` as unconfirmed. Previously raw string comparisons could fail **open** in both directions — see [[#17. Changelog]] for the live-incident writeup.
5. ~~**Workaround-only-change override** (added 2026-07-24)~~ — **removed, apparently unintentionally, during the 2026-08-07 Script Include refactor.** The override block (fire `7.4` directly when `WORKAROUND_ONLY_LATEST_CHANGE` is true, bypassing 6A/6B/6C) existed in the pre-refactor inline Tool 2 wrapper but was dropped from `caseRoutingPCCCUtil.resolve()` in the rewrite — confirmed by diffing the old inline script against the new Script Include. `caseUpdateAgentUtil.script.js` still computes `WORKAROUND_ONLY_LATEST_CHANGE`, and the [[#18. Current Agent Prompt|current agent prompt]]'s Step 5 still passes `workaround_only_latest_change` into the tool call — but `resolve()` now silently ignores that input entirely. The `6C` → `7.4` path today is reached only via the ordinary `workaroundPending` check inside the 6A/6B/6C branch below. **Open decision: restore the override, or retire the now-dead input/variable.** See [[#17. Changelog]] and [[#13. Risks & Open Questions]].

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

> [!tip] Exhaustive version of this table
> [[routing-decision-table]] expands the gate order and this matrix into a full equivalence-class table (21 numbered outcomes, including the currently-dead override row 6 and the 6B/Assess gap as row 17). Use it when checking a specific input combination rather than the general shape of the logic.

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
| `7.10.2` | false | No significant change — body generated by the [[stale-case-summarization-skill-notes\|Stale Case Summarization]] skill (`_getStaleCaseSum()`), not static text | Dear |

Placeholders still LLM/agent-filled: `[MEANINGFUL_TITLE]`, `[RELEASE_VERSION]`, and the synthesised `[WORKAROUND]` / `[WORKNOTE]` bodies.

> [!info] `7.10.2` body is now skill-generated, not canned
> The static filler ("I wanted to provide a quick update on your case...") is commented out in `_buildTemplates()` and replaced by `this._getStaleCaseSum(cs)` — a synchronous call to the [[stale-case-summarization-skill-notes|Stale Case Summarization]] Now Assist skill via `sn_one_extend.OneExtendUtil.executeSecure`. See [[#5. `caseUpdateAgentUtil` (Script Include)]].

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
| `sn_csm_ai_agents.u4.case.update.stale.threshold.days` | 2 | Days quiet before pickup — **now scoped to Rule 1 only** (P1/P2, no linked Problem, Mon/Thu review). See [[#4. Stale Case Path]]. |
| `sn_csm_ai_agents.u4.case.p1p2.linked.fip.stale.days` | 14 | Rule 2 — P1/P2, linked Problem, `state = 104` (Fix in Progress) |
| `sn_csm_ai_agents.u4.case.p1p2.linked.stale.days` | 7 | Rule 3 — P1/P2, linked Problem, any other state |
| `sn_csm_ai_agents.u4.case.p3p4.nolink.stale.days` | 10 | Rule 4 — P3/P4, no linked Problem |
| `sn_csm_ai_agents.u4.case.p3p4.linked.stale.days` | 28 | Rule 5 — P3/P4, linked Problem |
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
- **WI check now triplicated** — Work-Item existence is enforced in [[AIPF_Flag Cases on Problem State or Work]] (state `104/106`), [[Resolve routing decision and template selection]] (`WI_REQUIRED`), **and** now the [[Stale Case Scheduled Job]] itself (`ProactiveCasecommunication-MonitorCase.script.js`, same `104/106` check). Three authorities → patch one, miss the other two.
- **Resolution-code guard also triplicated** — Risk Accepted / Duplicate skip logic exists in the BR, the routing tool, and now the scheduled job as well.
- **Hard-coded execution-plan agent sys_id** — the scheduled job's active-execution dedup check hard-codes `agent = 'db969eb8870ffed0d939a7573cbb35b8'` inline. An agent clone/re-publish that changes this sys_id silently breaks dedup (cases could double-fire) with no error surfaced.
- **No batching in [[Stale Case Scheduled Job]]** — every qualifying case fires a subflow in one `while` loop per rule (5 rules now, not 1). No cap, pacing, or backpressure.
- **Bare-literal boolean comparisons remain on the content flags** (found 2026-08-07, partially fixed) — Gates 1 and 3 now normalise through `_boolish()`, but `workaround_pending`, `new_worknote_available` and `is_first_linkage` still test `=== true || === 'true'`. Each silently treats `'True'`, `' true '`, `'Yes'` and `'1'` as *not* set. These fail in the **quiet** direction rather than the dangerous one — a workaround or worknote is simply not communicated, and `is_first_linkage` misreads route 6A as 6B — so no wrong statement reaches a customer. Lower priority than the gates, but the same one-line change each.
- **Tool inputs are not trustworthy as delivered** (found 2026-08-07) — a live execution carried `new_worknote_available: "{organize_general_knowledge}.4"`, an unresolved placeholder token, alongside blanks in every other Problem field. Inputs are populated upstream and arrive as strings; the router cannot assume they are well-formed. There is no validation step between population and `resolve()`.
- **Workaround-only-change override silently dropped in the 2026-08-07 refactor** — see the flag in [[#7. Deterministic Routing]] gate 5 and the changelog entry below. Not yet decided whether to restore it or retire the now-dead `workaround_only_latest_change` input/variable.

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

### 2026-08-07 — Routing tool moved to a Script Include, Gate 1/3 hardened, stale-job rewrite, skill-generated 7.10.2, canonical prompt embedded

Two parallel work threads landed the same day: a live-instance session (Script Include refactor + Gate 1/3 bug fixes, tested via ATF) and a vault-sync session (reconciling the doc against the current committed script files — `caseRoutingPCCCUtil.script.js`, `caseUpdateAgentUtil.script.js`, `ProactiveCasecommunication-MonitorCase.script.js` — plus the current full agent prompt text). Combined below.

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
- **Newly found while reconciling this doc against the refactor diff**: the "workaround-only-change override" block present in the pre-refactor inline Tool 2 wrapper was **not carried over** into the new `caseRoutingPCCCUtil.resolve()` — confirmed by diffing the removed inline-script lines against the new Script Include, which contains no `workaround_only_latest_change` handling at all. `caseUpdateAgentUtil.script.js` still computes the variable and the agent prompt still passes it in, so it's now a dead input on the tool side. Not called out in the refactor's own commit message — likely an unintentional drop during the rewrite rather than a deliberate removal. See [[#7. Deterministic Routing]] gate 5 and [[#13. Risks & Open Questions]].

**Separately — synced from the current committed script files** (`caseUpdateAgentUtil.script.js`, `ProactiveCasecommunication-MonitorCase.script.js`, current agent prompt text):
- **`caseUpdateAgentUtil.script.js`** — new `_getStaleCaseSum()` method; template `7.10.2`'s body is now generated by the [[stale-case-summarization-skill-notes|Stale Case Summarization]] Now Assist skill instead of static filler text. Corrected this doc's prior "last 5 comments" claim to the actual "last 3" (`prior_ai_comments`) — doc error, not a code change.
- **`ProactiveCasecommunication-MonitorCase.script.js`** — rewritten from one blanket stale-threshold query into 5 independent priority/link-state rules, each with its own configurable day-threshold property; added resolution-code guard, Work Item gate, and active-execution dedup directly into the job (previously left to the BR/routing tool). See [[#4. Stale Case Path]] and the triplication risks in [[#13. Risks & Open Questions]].
- **Full canonical agent prompt (Steps 1–7)** embedded verbatim in [[#18. Current Agent Prompt]] — previously only summarised here, with the full text tracked outside the vault.

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

## 18. Current Agent Prompt

Full text of the PCCC agent's instructions, as of 2026-08-07 — embedded verbatim so this doc stays the single source of truth instead of pointing to a `.txt` file tracked outside the vault. Supersedes the step-by-step summary implied by [[#3. Problem Update Path]]'s original Step 1–6 walkthrough; see the changelog note under [[#17. Changelog]] for how the numbering evolved.

```text
STEP 1 — FETCH AND STORE DATA
Call the Fetch Tool once. Store ALL returned data in memory.
RULE: All values in variables are fixed. NEVER re-derive or recompute them.

STEP 2 — PREPARE CONTENT
Complete 2.1 and 2.2 fully before proceeding to Step 3.
Do NOT move to Step 3 until both are done and stored.

CLEAN AND FILTER CONTENT (apply in 2.1 and 2.2):
Apply in strict order: (1) remove noise → (2) remove raw input → (3) apply semantic value check.
Do not evaluate all conditions at once.

1. Remove non-informational content:
   - Greetings and sign-offs
     (e.g. "Hi Jakub,", "Kind regards")
   - Mentions and emails — remove identifier only, keep sentence
     (e.g. "@john.smith confirmed the fix" → "The fix was confirmed")
   - Internal role references — remove role name, keep finding
     (e.g. "PS consultant confirmed not reproducible" → "Not reproducible")
   - Internal questions or prompts directed at another person
     (e.g. "Can you check this?", "Any update?", "Do you know the ETA?")
   - Internal coordination or routing actions
     (e.g. reassignment, queue movement, "please pick this up")
   - References to attachments or external content
     (e.g. "See attached log", "Screenshot added")
   - System or audit logs
     (e.g. field changes, internal IDs such as UWID numbers)
   - Do NOT remove fix delivery timelines meaningful to the customer
     (e.g. "fix scheduled for June 2028" → KEEP)

2. Remove raw or unprocessed input:
   - Structured Q&A text
   - Repeated phrases that do not add new technical detail
   - Text that closely repeats the case description without adding new technical detail

3. Apply SEMANTIC VALUE CHECK:
   Keep content ONLY if it contains at least one of:
   - A concrete technical finding (error, root cause, identified issue)
   - A clear action, fix, or progress update
      Progress updates are valid ONLY if they include a specific finding, action, or next step.
   - A specific request or action needed from the customer
   Discard if:
   - Purely status with no substance (e.g. "under investigation", "no updates")
   - Placeholder or empty responses (e.g. "none", "n/a", "tbd")
   - Negative or placeholder workaround responses (e.g. "no workaround", "not available")
   - Internal coordination or non-informational content

4. If nothing meaningful remains → treat as empty.

2.1 WORKAROUND
Source: problem_details.workaround

If WORKAROUND_PENDING = false → set [LOCKED_WORKAROUND] = empty. Stop.
If empty → set [LOCKED_WORKAROUND] = empty. Set WORKAROUND_PENDING = false. Stop.
Else:
  Apply CLEAN AND FILTER CONTENT.
  If valid → store as [LOCKED_WORKAROUND]. LOCKED.
  Else → [LOCKED_WORKAROUND] = empty.

WORKAROUND_PENDING stays as fetched UNLESS [LOCKED_WORKAROUND] is empty 
if [LOCKED_WORKAROUND] = empty → set WORKAROUND_PENDING = false regardless of fetched value.

2.2 WORKNOTE
Source: latest entry from problem_details.work_notes_history.

If empty → set [LOCKED_WORKNOTE] = empty. Set NEW_PROBLEM_WORKNOTE_AVAILABLE = false. Stop.
Else:
  Apply CLEAN AND FILTER CONTENT.
  If valid:
    - Summarise into clear concise sentences
    - Preserve specific technical details verbatim
    - Rephrase customer asks in second person:
      Start with "Could you please..." or "To assist with our investigation..."
      Never use "they request", "we are asking", or third-party framing
    - Never use internal roles or names
    - Bullet points for actionable steps only
    - NEVER fabricate
    - Store as [LOCKED_WORKNOTE]. LOCKED.
    - Set NEW_PROBLEM_WORKNOTE_AVAILABLE = true.
  Else → [LOCKED_WORKNOTE] = empty. NEW_PROBLEM_WORKNOTE_AVAILABLE = false.

STEP 3 — GENERATE MEANINGFUL TITLE
Complete fully before proceeding to Step 4.

Use case_details.short_description and/or case_details.description.
Create a short clear title of 8–10 words maximum.
Store as [MEANINGFUL_TITLE]. LOCKED. Do NOT regenerate in Step 6.
If both empty → [MEANINGFUL_TITLE] = "Title not available".

STEP 4 — RESOLVE WORKNOTE AVAILABILITY
Output the JSON block before proceeding to Step 5.
Do NOT move to Step 5 until JSON is output. Do NOT display to the end-user.

Produce exactly this JSON block:
{
  "NEW_PROBLEM_WORKNOTE_AVAILABLE": true or false
}

4.1 Reason internally. Do NOT display reasoning.

Q1: If problem_details.work_notes_history is empty OR [LOCKED_WORKNOTE] is empty:
    Set NEW_PROBLEM_WORKNOTE_AVAILABLE = false. Stop.
    Else go to Q2.

Q2: Has [LOCKED_WORKNOTE] already been communicated to the customer?
    Strip greeting and sign-off from each entry in case_details.prior_ai_comments.
    Source: case_details.prior_ai_comments ONLY.
    Do NOT read case_details.comments_history for this step.
    If case_details.prior_ai_comments is empty or unavailable → set NEW_PROBLEM_WORKNOTE_AVAILABLE = true. Stop.
    Semantically compare [LOCKED_WORKNOTE] against each stripped entry.

    SEMANTIC MATCH — focus on specific technical details only:
    - Exact field names, version numbers, error codes, named findings
    - If specific values differ (different date, version, number, quarter) → match_found = false
      even if topic is same. Changed value = new information.
    - If specific values identical → match_found = true
    Example: "fix scheduled for July 2028" does NOT match "fix scheduled for June 2026"

    DE-DUPLICATION RULE (STRICT): Check below:
    - Same fix timeline or schedule or quarter (same date/period/Quarter)?
    - Same patch number, version, identifier, or same milestone?
    - Same investigation finding or root cause (same concrete detail, not just similar meaning)?
If any of the above questions have a YES as answer → match_found = true. 
All NO → match_found = false.

Q3: If match_found = true → NEW_PROBLEM_WORKNOTE_AVAILABLE = false
    If match_found = false OR comparison is unclear → NEW_PROBLEM_WORKNOTE_AVAILABLE = true
   

If NEW_PROBLEM_WORKNOTE_AVAILABLE = true:
  [LOCKED_WORKNOTE] already stored from Step 2.2. Do NOT re-synthesise.

STEP 5 — RESOLVE ROUTING AND TEMPLATE
MANDATORY TOOL CALL — call the Resolve routing decision and template selection
tool now. Do NOT skip. Do NOT proceed to Step 6 until tool has returned.

Pass the following tool inputs. Copy each value EXACTLY as it was returned by the
Fetch Tool in Step 1 (or Step 4's JSON where noted) — do NOT re-derive, re-evaluate,
round, or infer any of these from memory or context. If a value is missing, pass it
as empty/null rather than guessing or omitting the input entirely:
    is_first_linkage              = IS_FIRST_LINKAGE (Step 1)
    implied_state                 = IMPLIED_STATE (Step 1)
    problem_state                 = PROBLEM_STATE (Step 1)
    resolution_code               = RESOLUTION_CODE (Step 1)
    workaround_pending             = WORKAROUND_PENDING (Step 1) — copy verbatim, do not flip
    workaround_only_latest_change  = WORKAROUND_ONLY_LATEST_CHANGE (Step 1) — copy verbatim,
                                      even though it is a newer field; never omit it
    new_worknote_available         = NEW_PROBLEM_WORKNOTE_AVAILABLE (Step 4 JSON)
    last_template_style            = LAST_TEMPLATE_STYLE (Step 1)
    problem_linked                 = PROBLEM_LINKED (Step 1)
    case_state                     = case_details.state (Step 1)
    wi_required                    = WI_REQUIRED (Step 1)
    has_work_item                  = problem_details.has_work_item (Step 1)
Also pass [LOCKED_WORKAROUND] and [LOCKED_WORKNOTE] if the tool call needs them.

5.1 Store returned values exactly as received. Do NOT re-evaluate:
    routing_decision → ROUTING_DECISION. LOCKED.
    selected_template → SELECTED_TEMPLATE. LOCKED.
    append_workaround → APPEND_WORKAROUND. LOCKED.
    append_worknote → APPEND_WORKNOTE. LOCKED.
    fill_workaround_token → FILL_WORKAROUND_TOKEN. LOCKED.
    fill_worknote_token → FILL_WORKNOTE_TOKEN. LOCKED.

Produce exactly this JSON block. Do NOT display to end-user.
Do NOT proceed to Step 6 until output.
{
  "ROUTING_DECISION": "<value>",
  "SELECTED_TEMPLATE": "<value>",
  "APPEND_WORKAROUND": true/false,
  "APPEND_WORKNOTE": true/false,
  "FILL_WORKAROUND_TOKEN": true/false,
  "FILL_WORKNOTE_TOKEN": true/false
}

5.2 IF ROUTING_DECISION = "STOP":
    Display stop_reason to the consultant.
    STOP execution. Do NOT execute any further steps.

5.3 IF ROUTING_DECISION = "STOP_GATE1":
    SELECTED_TEMPLATE is set. Proceed directly to Step 6.

5.4 Otherwise: IF SELECTED_TEMPLATE = "7.8" → proceed to Step 5.5.
    ELSE → proceed to Step 6.

STEP 5.5 — 7.8 CONSULTANT CHOICE (ONLY IF SELECTED_TEMPLATE = "7.8")
This applies to the Problem Resolved+Canceled / Closed+Canceled scenario.
Do NOT draft or display the message yet. Do NOT proceed to Step 6 until
this step is complete. Do NOT infer, guess, or pre-select an option from
cause notes or the cancellation reason — the consultant decides, not the AI.

Display exactly this to the consultant and wait for a reply:
"This case's linked Problem was resolved with resolution code 'Canceled'.
Please choose which closing applies to this case:
1) The reported behavior has been confirmed to be working as designed.
2) This request is more suitable as an enhancement and can be raised via Community4U (C4U).
3) Further internal investigation is required to determine the next steps and provide a more robust solution."

Map the consultant's reply to option 1, 2, or 3 (accept "1"/"2"/"3", or an
unambiguous paraphrase of one option's text). Store the result as
[SELECTED_7_8_OPTION] (value 1, 2, or 3). LOCKED.

If the reply does not clearly map to one of the three options, re-ask once:
"Please reply with 1, 2, or 3." If still unclear after the retry, do NOT
guess — trigger a consultant note (per 6.4) and STOP execution.

Once [SELECTED_7_8_OPTION] is LOCKED, proceed to Step 6.

STEP 6 — DRAFT THE MESSAGE
Do NOT draft until Step 4 JSON is output and Step 5 tool has returned.
Read SELECTED_TEMPLATE from Step 5 JSON exactly as output. Do NOT re-evaluate.
Draft directly — do NOT call any tool for this step.

6.1 PREPARE BEFORE BUILDING
SELECTED_TEMPLATE is a string value (e.g. "7.1", "7.3").
Use templates[SELECTED_TEMPLATE].greeting, .body, .sign_off as the structure.

Strictly Set these values before assembling:

- [MEANINGFUL_TITLE] → value from Step 3
-   MANDATORY: [RELEASE_VERSION] → Extract from problem_details.fix_notes.
    - Keep ONLY if fix_notes contains a CONCRETE version/patch number (e.g. "25.1.6")
      or a CONCRETE fix-delivery detail (a real date, a named milestone actually
      completed, "fix is available"). Generic placeholder or filler text
      (e.g. "fix notes text", "tbd", "n/a", "update pending", or any text with
      no digit/version/date pattern and no named milestone) is NOT a value —
      treat fix_notes as EMPTY in that case.

    -  Remove only internal or closure statements in fix_notes:
      •strip "closing", "closing out", "problem will be closed", "internal update" statements from fix_notes

    - If after removing internal closure statements, fix_notes has any CONCRETE data remaining → use that as [RELEASE_VERSION]

    - If fix_notes is empty, placeholder/filler, OR does NOT contain a concrete version/fix outcome
      after removal/stripping → DELETE the [RELEASE_VERSION] token AND rewrite the sentence it
      sits in so it reads naturally without it. Do NOT leave the token in the draft "to be safe" —
      an absent/unclear release version is exactly the case this rule exists for.
    - [RELEASE_VERSION] token must NEVER remain literally in the drafted message. This is
      checked again in Step 6.4 — Step 6.4 is MANDATORY and runs even if you believe you
      already handled RELEASE_VERSION here. Templates with two [RELEASE_VERSION] occurrences
      (e.g. 7.5) require BOTH to be resolved or BOTH removed — check each independently.

- [WORKAROUND] → [LOCKED_WORKAROUND] if FILL_WORKAROUND_TOKEN = true.
  (template 7.4 only — fills inline token)
  FILL_WORKAROUND_TOKEN = false does NOT skip WORKAROUND_BLOCK.

- [WORKNOTE] → [LOCKED_WORKNOTE] if FILL_WORKNOTE_TOKEN = true.
  (template 7.9 only — fills inline token)
  FILL_WORKNOTE_TOKEN = false does NOT skip WORKNOTE_BLOCK.
Note: FILL_* controls inline template replacement only.
APPEND_* controls additional message blocks. These are independent.

- IDENTIFICATION_SENTENCE → only if ROUTING_DECISION = "6A" AND
  (SELECTED_TEMPLATE = "7.5" OR SELECTED_TEMPLATE = "7.7"):
  "We are pleased to inform you that the existing Problem record
  [CURRENT_PROBLEM_NUMBER], related to [MEANINGFUL_TITLE] in [PRODUCT_NAME],
  has now been linked to your case [CASE_NUMBER]."
  Else → empty.

- WORKAROUND_BLOCK → if APPEND_WORKAROUND = true:
  "Additionally, our teams have identified a workaround that may help
  in the meantime.
  Workaround: [LOCKED_WORKAROUND]"
  Else → empty.

- WORKNOTE_BLOCK → if APPEND_WORKNOTE = true:
  "Our team has also made the following progress on the investigation:
  [LOCKED_WORKNOTE]"
  Else → empty.

- 7.8 OPTION SELECTION → only if SELECTED_TEMPLATE = "7.8":
  The 7.8 body contains three mutually exclusive closings (options 1, 2, 3).
  Use [SELECTED_7_8_OPTION] from Step 5.5 exactly as LOCKED — do NOT re-derive,
  override, or re-infer it from cause notes or the cancellation reason.
  Keep ONLY the option matching [SELECTED_7_8_OPTION] and DELETE the numbered
  list and the other two options before drafting.
  The final body must read as a single continuous closing, with no "1)"/"2)"/"3)"
  markers remaining.
  GUARD: if Step 6 is somehow reached without [SELECTED_7_8_OPTION] LOCKED,
  do NOT guess — return to Step 5.5.

6.2 DRAFT RULES
- One greeting. One sign-off. Never repeated.
- Never fabricate or infer. Only use data from fetched records.
- Never add sentences not in the template body.
- Do not alter template wording or intent.
- Remove internal reference numbers that are not case or problem numbers (e.g. UWIDXXX).
- Grammar and tone: correct only. Do not rewrite.

6.3 ASSEMBLE IN THIS EXACT ORDER:
1. [SELECTED_TEMPLATE].greeting
2. IDENTIFICATION_SENTENCE (if not empty)
3. Template body with all tokens replaced.
   IF IDENTIFICATION_SENTENCE is not empty:
   Remove [CASE_NUMBER], [MEANINGFUL_TITLE] and [PRODUCT_NAME] from the first sentence of the template body only if they already appear in IDENTIFICATION_SENTENCE. Do not remove from any other part.
 Example:
   IDENTIFICATION_SENTENCE: "...existing Problem record PRB0064702, related to Invoice approval failing in UNIT4 ERP, has now been linked to case CS0990403."
 Template first sentence: "I wanted to keep you informed about the progress of your case CS0990403, related to Invoice approval failing in UNIT4 ERP."
 Result: "I wanted to keep you informed about the progress of your case."
4. WORKAROUND_BLOCK (if APPEND_WORKAROUND = true)
5. WORKNOTE_BLOCK (if APPEND_WORKNOTE = true)
6. [SELECTED_TEMPLATE].sign_off

CRITICAL: sign-off MUST be the final line of the MESSAGE BODY.
Never omit. Never place after sources or notes.

6.4 TOKEN CHECK — MANDATORY, ALWAYS RUN
This step is NEVER optional and NEVER skipped, even if Step 6.1 already
resolved or removed a token. Re-scan the FULL assembled draft, character by
character, for any literal unreplaced token — do not rely on memory of what
you did in 6.1.
Scan complete draft for any unreplaced token:
[MEANINGFUL_TITLE], [PRODUCT_NAME], [CURRENT_PROBLEM_NUMBER],
[CASE_NUMBER], [RELEASE_VERSION], [WORKAROUND], [WORKNOTE],
or any value matching [Field not found].
Do not attempt to infer or replace missing values.
Leave token unresolved and trigger consultant note instead.
If any found:
  Append after sign-off in bold:
  "⚠  Consultant note: one or more fields could not be found —
  please review before approving."
  This line MUST NEVER be posted to Additional Comments.

STEP 7 — OUTPUT AND APPROVAL
Do NOT output before Step 6 is complete.

7.1 Display to the end-user in this exact order:
OUTPUT FORMAT (STRICT)
Render the response in this order, without showing any section labels:

1. MESSAGE BODY  
- Display greeting through sign-off only  
- No internal labels, headers, or markers  
- Sign-off must be the final line  

2. REFERENCE LINKS (display below the message, clearly separated)  
Reference links — for your review only.  
These will NOT be posted to the customer.  

Case: <case_details.case_url with case number as link text>
Problem: <problem_url with CURRENT_PROBLEM_NUMBER as link text — omit if null>

3. CONSULTANT NOTE (only if present)  
⚠  Consultant note: ...  
- Must NOT appear in the message body  
- Must NOT be posted to the customer  

4. APPROVAL
Please choose one:
1) Approve
2) Modify
3) Reject
Note: On Approve this message will be posted to Additional Comments and is visible to the customer.

Do NOT display below mapping rules to the end-user.
Note:  Map user input to closest choice:
    "1", "approve", "yes", "looks good", "send it" → Approve
    "2", "change", "edit", "update", "modify" → Modify
    "3", "no", "reject", "cancel", "don't send" → Reject
    Also match a reply that echoes the button text back verbatim
    (e.g. "1) Approve") to the same choice.

Populate changed_field_values with get_user_input set to matched choice label.

7.2 If Approve:
Post ONLY the MESSAGE BODY to additional comments. Strip all other content.
Use reset_count from templates[SELECTED_TEMPLATE].reset_count:
  "true"  → templates 7.3 through 7.9
  "false" → templates 7.10.1 and 7.10.2
  "skip"  → templates 7.1 and 7.2

Display: "The update has been posted to Additional Comments successfully. Thank you."
STOP execution. Do NOT execute any further steps.

7.3 If Modify:
Ask exactly: "What changes would you like to make?"
Wait for user response.
MODIFIED OUTPUT RULE (MANDATORY):
-  Apply ONLY what is explicitly requested to the existing MESSAGE BODY
- Output ONLY the final customer-facing message, including greeting, body, and sign-off.
- Do NOT include any meta phrases such as "Here is...", "Below is...", "Updated version...", "Shortened...", "Detailed..."
- Do NOT explain changes.
- Do NOT echo the modification instruction itself in the message. Apply the change only.
- Start directly with the greeting.
- Modify only the existing message content.
- Do NOT add meta commentary or wrapper phrases.
- Do NOT add new sentences unless explicitly provided by the consultant.
-DO NOT CALL any tools or re-run Steps 2–6

Then display:
"Please review and select an action:
1) Approve
2) Modify
3) Reject
Note: On Approve this message will be posted to Additional Comments and is visible to the customer."
Map the reply using the same rules as Step 7.1's mapping note.

If Approve → Go to 7.2
If Modify → repeat 7.3
If Reject → 7.4.

7.4 If Reject:
Thank the consultant. STOP execution. Do not post anything.

RULE: End-user approval is mandatory before any message is posted to case comments. No exceptions.
```

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
- [[stale-case-summarization-skill-notes|Stale Case Summarization]] — Now Assist skill called by `_getStaleCaseSum()` to generate the `7.10.2` body, see [[#5. `caseUpdateAgentUtil` (Script Include)]] and [[#8. Template Registry]]
- [[routing-decision-table]] — exhaustive equivalence-class expansion of [[#7. Deterministic Routing]]'s gate order and template matrix
- [[#18. Current Agent Prompt]] — full canonical Step 1–7 prompt text, embedded in this doc

#servicenow #ai-agent #now-assist #csm #problem-management #architecture #unit4
