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

Companion reference for [[Proactive Customer Case Communicator]] §7 (Deterministic Routing) — the same gate order and template-selection logic there, expressed as an exhaustive equivalence-class table instead of prose. Cross-reference the two: prose for *why*, this table for *every combination*.

Full mapping of the routing tool's logic, expressed as equivalence classes (only
the inputs that actually gate each outcome are listed; everything else is "don't care").

## Gate-level outcomes (checked before routing/template logic even runs)

| # | Outcome | Key conditions | Notes |
|---|---|---|---|
| 1 | `STOP_GATE1` → **7.2** | `problem_linked = false` **and** `case_state` contains `"Awaiting"` | Substring match, case-sensitive |
| 2 | `STOP_GATE1` → **7.1** | `problem_linked = false` **and** `case_state` doesn't contain `"Awaiting"` | Default no-problem-linked path |
| 3 | `STOP` → *(no template)* | `problem_linked = true`; `resolution_code` = `Risk Accepted` or `Duplicate` | Case-insensitive on this check only |
| 4 | `6B` → **7.8** | `problem_linked = true`; not RA/Dup; `problem_state = "Closed"` **and** `resolution_code = "Canceled"` | Exact-case match |
| 5 | `STOP` → *(no template)* | Passes 1–4; `wi_required = true` **and** `has_work_item = false` | "WI missing" block |
| 6 | `6C` → **7.4** (override) | Passes 1–5; `workaround_only_latest_change = true` **and** `workaround_pending = true` | `fill_workaround_token=true`, `append_workaround=false` — ⚠️ see note below |

> [!bug] Row 6 is stale as of the 2026-08-07 Script Include refactor
> This override block existed in the pre-refactor inline Tool 2 wrapper but was **not carried over** into `caseRoutingPCCCUtil.resolve()` when the tool was rewritten as a Script Include — confirmed by diffing the removed inline-script lines against the new Script Include, which contains no `workaround_only_latest_change` handling at all. `workaround_only_latest_change` is still computed by `caseUpdateAgentUtil.script.js` and still passed in by the agent prompt's Step 5 tool call, but `resolve()` now silently ignores it. **Row 6 currently does not fire in the live tool** — the only path to `7.4` today is via row 18 in the `6C` table below. See [[Proactive Customer Case Communicator#7. Deterministic Routing|§7]] gate 5 and [[Proactive Customer Case Communicator#17. Changelog|the changelog]] for the full writeup; not yet decided whether to restore this row or delete it.

If none of 1–6 fire, `routing_decision` is computed from `is_first_linkage` /
`implied_state` / `problem_state`, then a template is picked.

## `6A` outcomes — `is_first_linkage = true`

| # | Outcome | `problem_state` | `resolution_code` |
|---|---|---|---|
| 7 | 6A → **7.3** | `New` or `Assess` | any |
| 8 | 6A → **7.6** | `Root Cause Analysis` | any |
| 9 | 6A → **7.7** | `Fix in Progress` | any |
| 10 | 6A → **7.5** | `Resolved` or `Closed` | `Fix Applied` |
| 11 | 6A → `STOP` fallback | anything else (e.g. `Resolved` without `Fix Applied`, unrecognized state) | — |

## `6B` outcomes — `is_first_linkage = false` **and** (`implied_state` empty/null **or** `problem_state ≠ implied_state`)

| # | Outcome | `problem_state` | `resolution_code` |
|---|---|---|---|
| 12 | 6B → **7.3** | `New` | any |
| 13 | 6B → **7.6** | `Root Cause Analysis` | any |
| 14 | 6B → **7.7** | `Fix in Progress` | any |
| 15 | 6B → **7.5** | `Resolved` or `Closed` | `Fix Applied` |
| 16 | 6B → **7.8** | `Resolved` | `Canceled` |
| 17 | 6B → `STOP` fallback | anything else — **including `Assess`** | — |

> ⚠️ Notable asymmetry: `Assess` only maps to 7.3 under **6A** — the 6B block
> never checks for it, so a not-first-linkage case stuck in `Assess` hits the
> fallback STOP, not 7.3.

## `6C` outcomes — `is_first_linkage = false` **and** `implied_state` set **and** `problem_state === implied_state`

| # | Outcome | `workaround_pending` | `new_worknote_available` | `implied_state` / `resolution_code` |
|---|---|---|---|---|
| 18 | 6C → **7.4** | `true` | — | — |
| 19 | 6C → **7.9** | `false` | `true` | — |
| 20 | 6C → **7.10.1** | `false` | `false` | `implied_state = "Resolved"` and `resolution_code` = `Canceled` or `Fix Applied` |
| 21 | 6C → **7.10.2** | `false` | `false` | anything else (e.g. `implied_state ≠ "Resolved"`, or Resolved with a different resolution code) |

Row 18 is the same 7.4 destination as override row 6 — *nominally* reachable two
ways, via the workaround-only-change shortcut or normally through 6C when
`problem_state === implied_state` and a workaround is pending. With row 6 not
currently firing (see the bug callout above), row 18 is the **only** live path
to `7.4` as of 2026-08-07.

## Post-template flags

Apply to every 6A/6B/6C row:

- `append_workaround = workaround_pending && template ≠ '7.4'`
- `append_worknote = new_worknote_available && template ≠ '7.9'`
- `fill_workaround_token = (template === '7.4')`
- `fill_worknote_token = (template === '7.9')`

---

## Related

- [[Proactive Customer Case Communicator]] — parent architecture doc; see §7 (Deterministic Routing) for the prose version of this table, §13 (Risks & Open Questions) for the row-6 discrepancy, and §17 (Changelog) for the 2026-08-07 refactor writeup
- [[caseRoutingPCCCUtil]]
- [[Resolve routing decision and template selection]]
- [[Template Registry]]
- [[stale-case-summarization-skill-notes|Stale Case Summarization]]
