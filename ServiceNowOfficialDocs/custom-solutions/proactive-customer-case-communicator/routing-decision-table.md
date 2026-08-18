---
aliases:
  - "Routing Decision Table"
  - "PCCC Routing Decision Table"
area: "custom-solutions/proactive-customer-case-communicator"
tags:
  - servicenow
  - ai-agent
  - now-assist
  - csm
  - problem-management
  - unit4
---

# Resolve Routing Decision and Template Selection — Decision Table

Companion reference for [[Proactive Customer Case Communicator]] §7 (Deterministic Routing) — the same gate order and template-selection logic there, expressed as exhaustive equivalence classes instead of prose. Cross-reference the two: prose for *why*, this table for *every combination*.

**Scope of this document.** §1–§5 cover `caseRoutingPCCCUtil.resolve()` — what template a given input set produces. §6–§8 cover everything *around* it: how a case reaches the agent at all, what happens to the message afterwards, and which combinations can never occur. Read §6 first if the question is "why did nothing happen", and §1–§5 if the question is "why did it pick *that* template".

> [!important] Verify the **tool**, not just the Script Include
> `resolve()` being correct does not mean it runs. The AI Agent Tool "Resolve routing decision and template selection" holds its own script field, and on 2026-08-07 it was still executing a stale pre-refactor inline copy while the Script Include sat unused. The tool script must read:
> ```javascript
> (function(inputs) {
>     return new caseRoutingPCCCUtil().resolve(inputs);
> })(inputs);
> ```
> Symptom of the stale copy: an unlinked case returning `Template could not be determined for problem_state: , resolution_code: , routing_decision: 6B`. See [[Proactive Customer Case Communicator#17. Changelog|§17]].

---

## 1. Input normalisation — `_boolish()`

Every input arrives as an upstream-populated **string**. Four normalised states:

| Raw value (any case, any padding) | `_boolish` |
|---|---|
| `true`, `'true'`, `'yes'`, `'y'`, `'1'` | `'true'` |
| `false`, `'false'`, `'no'`, `'n'`, `'0'` | `'false'` |
| missing, `null`, `undefined`, `''`, `'null'`, `'undefined'` | `'empty'` |
| anything else (a Problem number, an unresolved `{token}`) | `'unknown'` |

**All six boolean-ish inputs are normalised** as of 2026-08-07 (evening): `problem_linked`, `wi_required`, `has_work_item`, `is_first_linkage`, `workaround_pending`, `new_worknote_available`. Every downstream comparison is a plain boolean; no bare-literal comparisons remain in the tool.

The three content flags (`is_first_linkage`, `workaround_pending`, `new_worknote_available`) collapse to a simple boolean at the top of `resolve()`, where `'empty'` correctly reads as false — an absent workaround means no workaround. Only the gates below distinguish `'empty'` from `'unknown'`.

Before this change, a `workaround_pending` of `'True'` failed twice in one pass: `6C` skipped the `7.4` branch **and** `append_workaround` stayed `false`, so the workaround was dropped in both directions at once.

> `_boolish` is a shield, not a cure. The underlying defect is the agent emitting literal `"null"` strings and mixed-case booleans into tool inputs. Fix that in the agent prompt's Step 5 and this whole defect class disappears at source.

`_boolish` returns strings, not boolean-or-null, so "absent" and "uninterpretable" stay distinguishable at the call site. Collapsing them is what let a blank value read as a legitimate answer in the original defect.

---

## 2. Gate-level outcomes (checked before routing/template logic runs)

Evaluated strictly in this order. First match wins.

| # | Gate | Key conditions | Outcome | Message? |
|---|---|---|---|---|
| 1 | Gate 1 | `problem_linked` → `'unknown'` | `STOP` + named reason | ❌ |
| 2 | Gate 1 | `problem_linked` → `'false'`/`'empty'`, `case_state` contains `"Awaiting"` | `STOP_GATE1` → **7.2** | ✅ |
| 3 | Gate 1 | `problem_linked` → `'false'`/`'empty'`, otherwise | `STOP_GATE1` → **7.1** | ✅ |
| 4 | Resolution guard | `resolution_code` = `Risk Accepted` or `Duplicate` | `STOP` | ❌ |
| 5 | Gate 2b | `problem_state = "Closed"` **and** `resolution_code = "Canceled"` | `6B` → **7.8** | ✅ |
| 6 | Gate 3 | `wi_required` → `'unknown'` | `STOP` + named reason | ❌ |
| 7 | Gate 3 | `wi_required` = `'true'`, `has_work_item` = `'false'` | `STOP` "No Work Item linked" | ❌ |
| 8 | Gate 3 | `wi_required` = `'true'`, `has_work_item` = `'empty'`/`'unknown'` | `STOP` "could not be confirmed" | ❌ |
| 9 | Gate 3 | `wi_required` = `'true'`, `has_work_item` = `'true'` | proceed | — |
| 10 | Gate 3 | `wi_required` = `'false'`/`'empty'` | proceed (gate does not apply) | — |

Notes on individual gates:

- **Row 1** exists so an uninterpretable value never becomes a guess. Telling a customer no Problem is linked when one may be is worse than sending nothing.
- **Row 3** is the default no-Problem path, and since 2026-08-07 its body is skill-generated (see §7).
- **Row 4** is the only case-insensitive comparison in the whole gate chain.
- **Rows 6–8** fail **closed** by design. `wi_required` absent deliberately means "not required": per the Business Rule in §3 of the parent doc, a Work Item is only demanded for Problem states `104` (Fix in Progress) and `106` (Resolved), and every New/Assess/RCA path omits the input entirely. Treating blank as "required" would silence those.

> [!bug] Removed gate — workaround-only-change override
> A gate once sat between rows 8 and 10: `workaround_only_latest_change = true` **and** `workaround_pending = true` → `6C` / **7.4** with `fill_workaround_token = true`, bypassing the 6A/6B/6C classification entirely. Added 2026-07-24, dropped from `resolve()` in the 2026-08-07 Script Include refactor, and confirmed gone from the live tool once the tool was repointed at the Script Include that evening. `caseUpdateAgentUtil` still computes `WORKAROUND_ONLY_LATEST_CHANGE` and the agent prompt's Step 5 still passes `workaround_only_latest_change` into the tool call — `resolve()` ignores it. **The only live path to `7.4` is row 23 below.** Open decision: restore the gate, or retire the dead input and variable.

---

## 3. Routing decision (after all gates pass)

| Condition | `routing_decision` |
|---|---|
| `is_first_linkage` truthy | `6A` |
| `implied_state` empty or the string `'null'` | `6B` |
| `problem_state === implied_state` | `6C` |
| otherwise (state changed) | `6B` |

---

## 4. Template selection by route

### `6A` — first linkage

| # | `problem_state` | `resolution_code` | Template |
|---|---|---|---|
| 11 | `New` or `Assess` | any | **7.3** |
| 12 | `Root Cause Analysis` | any | **7.6** |
| 13 | `Fix in Progress` | any | **7.7** |
| 14 | `Resolved` or `Closed` | `Fix Applied` | **7.5** |
| 15 | anything else (`Resolved` without `Fix Applied`, unrecognised state) | — | `STOP` fallback |

### `6B` — not first linkage, and state changed or `implied_state` absent

| # | `problem_state` | `resolution_code` | Template |
|---|---|---|---|
| 16 | `New` or **`Assess`** | any | **7.3** |
| 17 | `Root Cause Analysis` | any | **7.6** |
| 18 | `Fix in Progress` | any | **7.7** |
| 19 | `Resolved` or `Closed` | `Fix Applied` | **7.5** |
| 20 | `Resolved` | `Canceled` | **7.8** |
| 21 | **blank / empty** | — | `6B_DEGRADED` → **7.10.2** + `gs.warn` |
| 22 | present but unrecognised | — | `STOP` fallback |

> [!success] Resolved 2026-08-07 — the 6B/`Assess` gap (row 16)
> `6A` had an explicit `New || Assess` branch; `6B` had neither an `Assess` branch nor a generic fallback, so a Problem sitting at `Assess` that routed through `6B` hit the safety-fallback `STOP` and **no customer message was sent**. Open since 2026-07-16. `6B` now mirrors `6A`. ⚠️ The T2 ATF case asserting a `STOP` here now fails by design — update the assertion to `7.3`.

> [!info] Row 21 — `6B_DEGRADED`, added 2026-08-07
> Past Gate 1, `problem_linked` is confirmed `'true'`. A blank `problem_state` at that point is a **data-population fault**, not a Problem state — every previously observed instance was the Gate 1 defect leaking unlinked cases into this classification, and that path is now closed.
>
> Rather than send nothing, these route to `7.10.2` under a distinct `routing_decision` label with a `gs.warn` naming the original route. Safe content-wise: `7.10.2`'s body is skill-generated from case comments and work notes, so it asserts nothing about the Problem's state.
>
> Row 22 keeps its `STOP` deliberately. A state that is *present but unrecognised* is a new or unmapped Problem state and must surface, not quietly receive "no significant change". `6A` likewise keeps a plain `STOP` for a blank state — first linkage with no state is a much stronger signal of upstream breakage.
>
> **A rising `6B_DEGRADED` count is an input-pipeline alarm, not a routing outcome to accept.**

### `6C` — not first linkage, `implied_state` set, `problem_state === implied_state`

Evaluated in order; first match wins.

| # | `workaround_pending` | `new_worknote_available` | `implied_state` / `resolution_code` | Template |
|---|---|---|---|---|
| 23 | `true` | — | — | **7.4** |
| 24 | `false` | `true` | — | **7.9** |
| 25 | `false` | `false` | `implied_state = "Resolved"` **and** `resolution_code` ∈ {`Canceled`, `Fix Applied`} | **7.10.1** |
| 26 | `false` | `false` | anything else | **7.10.2** |

Row 26 is the catch-all — `6C` never reaches the safety fallback. `7.10.2` is reachable from exactly two places: here, and the `6B_DEGRADED` path (row 21). Both require a linked Problem, which is why `7.10.2` remains unreachable for any case without one — Gate 1 fires first.

---

## 5. Post-template flags

Apply to every 6A/6B/6C row:

```text
append_workaround     = workaround_pending && template ≠ '7.4'
append_worknote       = new_worknote_available && template ≠ '7.9'
fill_workaround_token = (template === '7.4')
fill_worknote_token   = (template === '7.9')
```

All gate rows (`STOP_GATE1`, `STOP`) and `6B_DEGRADED` return every flag `false`.

`append_*` lets a state template also carry a workaround or worknote in one combined message (state body + `[WORKAROUND]`), while `7.4` / `7.9` own their token directly.

Since 2026-08-07 both content flags are `_boolish`-normalised, so `'True'`, `' true '`, `'Yes'` and `'1'` are all read correctly. Before that they silently read as *not set*, skipping rows 23–24 **and** leaving the matching `append_*` flag `false` — dropping the workaround or worknote in both directions at once.

---

## 6. How a case reaches the agent — the two entry paths

Routing never runs unless something invokes the agent. Two independent triggers.

### 6.1 Problem Update Path (event-driven)

Business Rule `AIPF_Flag Cases on Problem State or Work` sets `u_problem_updated = true` on associated cases. Exempt from the active-execution dedup check — always fires.

| # | Condition on the Problem | Result |
|---|---|---|
| 27 | insert, or `state` / `workaround` (non-empty) / `work_notes` changed | proceed |
| 28 | `resolution_code` = `duplicate` or `risk_accepted` | exit, no flag |
| 29 | `state = 107` (Closed) **and** `resolution_code = fix_applied` | exit — already communicated at Resolved |
| 30 | state-only change landing on `state = 102` (Assess) | exit |
| 31 | `state ∈ {104, 106}`, `resolution_code ≠ canceled`, no `u_work_item` child | exit |
| 32 | all guards passed | flag cases where `problem = current`, `active = true`, `category ∈ {0,1}`, `state ≠ 6` |

Problem state codes in code: `102` Assess · `104` Fix in Progress · `106` Resolved · `107` Closed. `New` and `Root Cause Analysis` are handled by display name in the routing tool.

### 6.2 Stale Case Path (time-driven)

Shared base filter, ANDed onto every rule:

```text
active=true ^ assigned_toISNOTEMPTY ^ categoryIN0,1 ^ stateNOT IN3,6,18
[^ accountIN<case.filter.accounts>]        (optional)
[^ numberIN<case.test.cases>]              (optional)
^ (u_auto_update_count<threshold OR u_auto_update_threshold_reached<=now-cooloffDays)
```

| # | Rule | Priority | Problem linked | Problem state | Stale window |
|---|---|---|---|---|---|
| 33 | 1 | P1/P2 | no | — | Monday/Thursday cycle **only** |
| 34 | 2 | P1/P2 | yes | `104` Fix in Progress | 14 days |
| 35 | 3 | P1/P2 | yes | any other | 7 days |
| 36 | 4 | P3/P4 | no | — | 10 days |
| 37 | 5 | P3/P4 | yes | any | 28 days |

Rule 1 alone is day-of-week gated (`gdt.getDayOfWeekLocalTime()`, 1 = Monday, 4 = Thursday). Rules 2–5 run every firing.

Per-case skip logic inside the job (duplicated from the BR and the routing tool — three authorities, patch one and miss two):

| # | Skip condition |
|---|---|
| 38 | linked Problem `resolution_code` = `risk_accepted` or `duplicate` |
| 39 | linked Problem `state ∈ {104, 106}` and no `u_work_item` via `parent` |
| 40 | an `sn_aia_execution_plan` for the agent already exists with `objective CONTAINS <case number>` and `state ∈ {ready, in_progress}` |

> [!warning] `state NOT IN 3,6,18` excludes Awaiting Customer Info
> The base filter drops state `18`, so the Stale Case Path can never surface a case whose state contains "Awaiting". **Template `7.2` is therefore unreachable from the stale path** — it can only be selected when the Problem Update Path invokes the agent on such a case. Verify the `18` mapping on your instance before relying on this.

---

## 7. Counter and cooloff — what happens after the message

`reset_count` travels with the selected template and drives Tool 3.

| `reset_count` | Templates | Effect |
|---|---|---|
| `true` | 7.3 – 7.9 | count → 0, threshold stamp cleared (meaningful update) |
| `false` | 7.10.1, 7.10.2 | count + 1; stamp `u_auto_update_threshold_reached` when count ≥ threshold |
| `skip` | 7.1, 7.2 | counter untouched — case surfaces every run |

Defaults: threshold 3, cooloff 7 days, stale 2 days.

```text
no-change #1 → count 1
no-change #2 → count 2
no-change #3 → count 3 → stamp → 7-day cooloff begins
… case excluded from the job for 7 days …
cooloff expires → picked up → next no-change RE-STAMPS → new 7-day cooloff
meaningful Problem update (Problem Update Path) → FULL reset to 0
```

Only a meaningful Problem update resets to zero. Cooloff expiry does not.

> [!important] Why `7.10.2` cannot simply be reused for no-Problem cases
> `7.10.2` is `reset_count = false`, and full reset happens **exclusively** through `_getCaseProblemDetails()` clearing `u_problem_updated`, or Tool 3 with `reset_count = true` — both of which require the Problem Update Path. A case with no Problem linked can never reach either. Routing `7.10.2` to unlinked cases would therefore let the counter climb permanently and lock the case into an endless cooloff-restamp cycle. This is why "Option A" reuses `7.1` (`skip`) with a skill-generated body instead. Any future attempt at Option B must add a reset path first — e.g. reset on a new customer comment, or on `u_last_comment_from_customer` changing.

---

## 8. Template bodies — static vs skill-generated

| Template | Body source |
|---|---|
| `7.1` | **Stale Case Summarization skill** via `_getStaleCaseSum()` (since 2026-08-07 evening) |
| `7.2` – `7.9` | static text in `_buildTemplates()`, plus agent-filled tokens |
| `7.10.1` | static |
| `7.10.2` | **Stale Case Summarization skill** via `_getStaleCaseSum()` |

`_getStaleCaseSum()` returns the skill's `response` string **as-is**. It must not be `JSON.stringify`-ed — doing so wrapped every generated body in literal double quotes in the posted customer comment (fixed 2026-08-07). Returns `''` on failure, logged, no throw.

Tokens still LLM/agent-filled: `[MEANINGFUL_TITLE]`, `[RELEASE_VERSION]`, `[WORKAROUND]`, `[WORKNOTE]`.

---

## 9. Worked scenarios

Concrete end-to-end traces. Each row is a full path from trigger to customer outcome.

| Scenario | Entry | Key inputs | Route | Template | Counter |
|---|---|---|---|---|---|
| P3 case, no Problem, In Progress, 31 days stale (`CS0991191`) | Stale rule 4 | `problem_linked = 'false'`, `case_state = "In Progress"` | `STOP_GATE1` | **7.1** (skill body) | untouched |
| Same case, but state contains "Awaiting" | — | — | — | — | never picked up — base filter excludes state 18 |
| P1 case, no Problem, Awaiting Customer Info | Problem Update Path only | `problem_linked = 'empty'`, `case_state` contains "Awaiting" | `STOP_GATE1` | **7.2** | untouched |
| Problem just linked, state `New` | Problem Update Path | `is_first_linkage = 'true'`, `problem_state = 'New'` | `6A` | **7.3** | reset to 0 |
| Problem just linked, state `Assess` | Problem Update Path | `is_first_linkage = 'true'`, `problem_state = 'Assess'` | `6A` | **7.3** | reset to 0 |
| Problem moved to `Assess`, not first linkage | Problem Update Path | `implied_state = 'New'`, `problem_state = 'Assess'` | `6B` | **7.3** (was STOP before 2026-08-07) | reset to 0 |
| Linked Problem, `problem_state` blank | either | `problem_linked = 'true'`, `problem_state = ''` | `6B_DEGRADED` | **7.10.2** + `gs.warn` | count + 1 |
| Linked Problem, unmapped new state | either | `problem_state = 'Awaiting Vendor'` | `6B` | **none — STOP** (by design) | unchanged |
| Problem moved to `Fix in Progress`, Work Item exists | Problem Update Path | `wi_required = 'true'`, `has_work_item = 'true'` | `6B` | **7.7** | reset to 0 |
| Same, Work Item missing | Problem Update Path | `wi_required = 'true'`, `has_work_item = 'false'` | gate row 7 | **none — STOP** | unchanged |
| Same, `has_work_item` blank | Problem Update Path | `wi_required = 'true'`, `has_work_item = 'empty'` | gate row 8 | **none — STOP** | unchanged |
| Workaround added, state unchanged | Problem Update Path | `workaround_pending = 'true'`, `problem_state === implied_state` | `6C` | **7.4** | reset to 0 |
| Workaround added, value arrives as `'True'` | Problem Update Path | `_boolish` → `'true'` | `6C` | **7.4** (silently dropped before 2026-08-07) | reset to 0 |
| New worknote, state unchanged | Problem Update Path | `new_worknote_available = 'true'` | `6C` | **7.9** | reset to 0 |
| P1 + linked Problem in FIP, 14 days quiet, nothing new | Stale rule 2 | `workaround_pending = 'false'`, `new_worknote_available = 'false'` | `6C` | **7.10.2** | count + 1 |
| Same, after 3 no-change messages | Stale rule 2 | threshold reached | — | — | 7-day cooloff, case excluded |
| Problem resolved `Fix Applied`, follow-up cycle | Stale rule 2/5 | `implied_state = 'Resolved'`, `resolution_code = 'Fix Applied'` | `6C` | **7.10.1** | count + 1 |
| Problem `Resolved` + `Canceled` | Problem Update Path | state changed | `6B` | **7.8** | reset to 0 |
| Problem `Closed` + `Canceled` | Problem Update Path | gate row 5 | `6B` | **7.8** | reset to 0 |
| Problem `Risk Accepted` | either | resolution guard | `STOP` | none | unchanged |
| `problem_linked` = a Problem number instead of a boolean | either | `_boolish` → `'unknown'` | `STOP` | none — named reason in NAP | unchanged |
| Agent already running for this case | Stale path | skip row 40 | — | not invoked | unchanged |

---

## 10. Structurally unreachable combinations

Useful when a test or report expects something that cannot happen.

| Expectation | Why it cannot occur |
|---|---|
| `7.10.2` on a case with no linked Problem | reachable only from `6C` (row 26) and `6B_DEGRADED` (row 21); both sit past Gate 1, which fires first on unlinked cases |
| `7.10.1` on a case with no linked Problem | same — `6C` only |
| `7.2` from the Stale Case Path | base filter excludes case state `18` |
| `7.4` via the workaround-only-change override | override removed in the 2026-08-07 refactor; only §4 row 23 remains |
| `6C` on a first linkage | `is_first_linkage` truthy routes to `6A` before the `implied_state` comparison |
| Counter reset to 0 on a no-Problem case | reset requires the Problem Update Path, which needs a linked Problem |
| A message on a `Fix in Progress` Problem with no Work Item | Gate 3 fails closed (post-2026-08-07) |
| A `STOP` on `6B` + `Assess` | fixed 2026-08-07 — now `7.3`, §4 row 16 |
| `6B_DEGRADED` on a case with no linked Problem | Gate 1 returns first; the degraded path exists only past a confirmed `problem_linked = 'true'` |
| `6A` + blank `problem_state` producing a message | `6A` keeps a plain `STOP`; the degraded fallback is `6B`-only, deliberately |

---

## 11. ATF coverage for the 2026-08-07 changes

Two existing T2 assertions move **by design** — update them, do not revert the code:

| Test | Was | Now |
|---|---|---|
| `6B` + `Assess` | `STOP` | **7.3** |
| `wi_required = true`, `has_work_item` blank | message released | `STOP` (fail-closed) |

New cases to add:

| Input | Expected |
|---|---|
| `6B` + blank `problem_state` | `6B_DEGRADED` / **7.10.2**, `gs.warn` emitted |
| `6B` + present-but-unrecognised `problem_state` | `STOP` |
| `6A` + blank `problem_state` | `STOP` (asymmetry is intentional) |
| `workaround_pending: 'True'` | **7.4**, `fill_workaround_token = true` |
| `new_worknote_available: 'Yes'` | **7.9**, `fill_worknote_token = true` |
| `is_first_linkage: '1'` | route `6A` |
| `problem_linked: ' FALSE '` | `STOP_GATE1` / **7.1** |
| `problem_linked: 'PRB0052356'` | `STOP`, named reason |

The last four are regression guards for `_boolish`. Without them the normalisation can be reverted silently.

---

## Related

- [[Proactive Customer Case Communicator]] — parent architecture doc; §7 for the prose version of §1–§5, §4 for the Stale Case Path, §9 for counter/cooloff, §13 for open risks, §17 for the change history
- [[caseRoutingPCCCUtil]]
- [[Resolve routing decision and template selection]]
- [[Template Registry]]
- [[stale-case-summarization-skill-notes|Stale Case Summarization]]
- [[Stale Case Scheduled Job]]
- [[Counter and Cooloff]]
