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
| `_computeVariables(...)` | Derives `PROBLEM_LINKED`, `IS_FIRST_LINKAGE`, `RESOLUTION_CODE`, `PROBLEM_STATE`, `WI_REQUIRED` (FIP/Resolved), `CURRENT_WORKAROUND_VALUE`, `WORKAROUND_PREVIOUSLY_SHARED`, `WORKAROUND_PENDING`. |
| `_buildTemplates(...)` | Returns the [[Template Registry]] `7.1`–`7.10.2` with deterministic placeholders pre-filled (`greeting`, `sign_off`, case/product/problem numbers). |
| `_incrementAutoUpdateCount(caseNumber, resetToZero)` | `reset` → count 0 + clear stamp; else count+1 and stamp `u_auto_update_threshold_reached = now` when `count >= threshold`. |
| `_addCaseComment(caseNumber, commentText)` | Writes to `comments` (customer-visible) with appended `\n\n[Note: AI-assisted message reviewed by consultant]`. |

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
4. **Gate 3 — WI required, none linked** → `STOP` with review message.

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

---

## 8. Template Registry

Built by `_buildTemplates()`. `reset_count` drives [[Counter and Cooloff]] behaviour on post.

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

### From prior notes (unverified here)
- **Stuck execution / silent exclusion** — if an execution hangs, is the case ever re-picked? No self-healing documented.
- **NAP shows internal variable** — consultants occasionally saw `{ "NEW_PROBLEM_WORKNOTE_AVAILABLE": true }` instead of the draft; likely approval-step content mapping, not draft generation. Confirm which output variable is bound to the NAP confirmation.
- **Large-context / token limits** — long case histories may exceed model/exec limits; consider summarising older worknotes.
- **Assigned-user eligibility** — locked/inactive user or missing Now Assist CSM group membership → execution error. Needs daily monitoring.

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

## Related Notes

- [[Monitor Work Item AI Agent]] — sibling agent, `u_work_item` → Problem worknote, Global scope
- [[Problem Update Path]]
- [[Stale Case Path]]
- [[AIPF_Flag Cases on Problem State or Work]]
- [[caseUpdateAgentUtil]]
- [[Resolve routing decision and template selection]]
- [[Stale Case Scheduled Job]]
- [[Template Registry]]
- [[Counter and Cooloff]]
- [[Now Assist Panel]]
- [[Now Assist]]
- [[Problem Management]]
- [[Work Item]]
- [[Human in the Loop]]

#servicenow #ai-agent #now-assist #csm #problem-management #architecture #unit4
