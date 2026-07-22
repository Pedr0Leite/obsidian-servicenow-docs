---
title: PCCC — Agent Walkthrough & Full Testing Runbook
aliases:
  - PCCC Testing Runbook
  - PCCC - Testing - ATF Build & Manual Runbook
tags:
  - servicenow
  - ai-agent
  - now-assist
  - csm
  - testing
  - atf
  - proactive-customer-case-communicator
  - custom-solutions
scope: sn_csm_ai_agents
status: draft
created: 2026-07-22
---

# PCCC — Agent Walkthrough & Full Testing Runbook

> [!abstract] One-liner
> Fills the dead link left by [[Proactive Customer Case Communicator - ATF Test Suite]] ("Part B" / manual runbook). Part A = step-by-step of how the agent actually runs end-to-end. Part B = every edge worth testing, split into what ATF already covers (deterministic layer) vs. what's manual-only (LLM drafting + NAP approval flow).

Source: [[Proactive Customer Case Communicator]] (architecture) + [[Proactive Customer Case Communicator - ATF Test Suite]] (existing automated suite). No new instance access used to write this — compiled from what's already in the vault.

---

## Part A — How the agent works, step by step

Two triggers converge on the same agent:

1. **Problem Update Path** (event-driven) — [[AIPF_Flag Cases on Problem State or Work]] fires on `problem` insert/update, sets `u_problem_updated = true` on linked active cases.
2. **Stale Case Path** (time-driven) — [[Stale Case Scheduled Job]] queries quiet cases and fires the agent via subflow `proactive_case_outreach__agent_invocation`.

Once triggered, the agent (`sn_aia_agent` "Proactive Customer Case Communicator", ReAct strategy, scope `sn_csm_ai_agents`) runs:

| Step | What happens | Tool / owner |
|---|---|---|
| **1 — Fetch & store** | Calls the fetch tool once, stores all returned case/problem data in memory. Values are fixed — never re-derived. | Tool 1 `_getCaseProblemDetails()` (read-only). Also clears `u_problem_updated` and, if it was set, resets the auto-update counter. |
| **2 — Clean & filter content** | Cleans work notes / prior comments in strict order: strip greetings/sign-offs → strip raw mentions/emails (keep the sentence) → strip internal role references, internal-only questions, coordination/routing chatter, attachment references. | Agent (LLM), deterministic *rules*, not judgment |
| **3 — Title** | Builds `[MEANINGFUL_TITLE]` (8–10 words) from `short_description`/`description`. Locked once set — not regenerated later. | Agent (LLM) |
| **4 — Resolve worknote availability** | Decides `NEW_PROBLEM_WORKNOTE_AVAILABLE` (true/false) from `problem_details.work_notes_history` + `[LOCKED_WORKNOTE]` + prior AI comments, reasoning internally. | Agent (LLM) — **outputs this as a raw JSON block**, see [[#Known issue — internal JSON leaking into NAP]] below |
| **5 — Routing & template selection** | Calls the deterministic routing tool, stores `ROUTING_DECISION` / `SELECTED_TEMPLATE` / `APPEND_WORKAROUND` / `APPEND_WORKNOTE` / `FILL_WORKAROUND_TOKEN` / `FILL_WORKNOTE_TOKEN` verbatim (all LOCKED). Also produces a raw JSON block of these values before continuing. If `ROUTING_DECISION == STOP`, displays `stop_reason` to the consultant and halts. | Tool 2 = [[Resolve routing decision and template selection]] → delegates to [[caseRoutingUtil]] (pure function, see [[#7. Deterministic Routing]] in the architecture note) |
| **6 — Draft the message** | Combines the selected template body with any appended workaround/worknote content, using the locked variables from steps 3–5. Produces ONE customer-facing draft. | Agent (LLM), template text is fixed, only prose/token-filling is generative |
| **7 — Human review (NAP)** | Draft is presented in the [[Now Assist Panel]] for the assigned consultant: **Approve / Modify / Reject**. Nothing is posted without this. | [[Human in the Loop]] |
| **8 — Post** | On approval, writes to `comments` (customer-visible Additional Comments) with the fixed AI disclaimer appended, and updates the auto-update counter per the template's `reset_count` contract. | Tool 3 `_addCaseComment()` + `_incrementAutoUpdateCount()` |

See [[Proactive Customer Case Communicator#5. `caseUpdateAgentUtil` (Script Include)]] and [[Proactive Customer Case Communicator#7. Deterministic Routing]] for the exact method/gate logic behind steps 1, 4–5, 8.

### Known issue — internal JSON leaking into NAP

Confirmed live (see session note below, not yet promoted to the architecture doc): **Steps 4 and 5 both instruct the LLM to "Produce exactly this JSON block... Do NOT display to the end-user."** There is no structural separation between "internal state passed forward" and "what's rendered in NAP chat" — the only guardrail is a prose instruction. When the model's instruction-following slips, that JSON block (e.g. `{"NEW_PROBLEM_WORKNOTE_AVAILABLE": true}`) becomes the visible chat turn instead of staying internal. This is a stronger, more specific explanation than the older "likely approval-step content mapping" guess in [[Proactive Customer Case Communicator#13. Risks & Open Questions]] — it's a prompt-design gap (turn output used as a scratchpad), not a Tool 3 output-variable binding bug. Not yet fixed — needs a governance-approved instruction rewrite (move state-passing off conversational turn output) before it can be closed. See [[#Edge — internal JSON block leaks into NAP]] below for how to test/reproduce it.

---

## Part B — Full testing matrix

### B0. What's already automated (ATF)

[[Proactive Customer Case Communicator - ATF Test Suite]] covers the **deterministic layer only**:

| Test | Covers |
|---|---|
| T1 — Template registry integrity | All 11 templates: no leftover tokens, first-name greeting/sign-off, correct greeting word, `reset_count` contract, no false "actively working" claim on 7.7/7.10.2 |
| T2 (+ T2a) — Routing decision matrix | 22 branch combinations through [[caseRoutingUtil]] (gates 1–3, 6A/6B/6C, append/fill flags, safety fallback) |
| T3 — Business Rule case flagging | `AIPF_Flag Cases on Problem State or Work` flag/exit gates (8 scenarios) |
| T4 — Counter & cooloff mechanics | Increment, threshold stamp, reset |

**Not covered by ATF** (explicitly out of scope per that note): LLM drafting (worknote synthesis, semantic dedup, title generation, 7.8 option pick) and the NAP approval flow. Everything below is where those live — manual only, until/unless someone builds harnessing for them.

### B1. Manual edges — LLM drafting & content quality

| Edge | How to trigger | What to check |
|---|---|---|
| Worknote noise filtering | Problem work note containing a greeting, an @mention, an internal role reference ("PS consultant confirmed..."), a routing instruction ("please pick this up"), an attachment reference | Draft strips all of the above per Step 2 rules, keeps the underlying finding |
| Title generation with both fields empty | Case with empty `short_description` AND `description` | `[MEANINGFUL_TITLE]` = "Title not available", not a hallucinated title |
| Title generation with long/messy description | Very long or bullet-heavy `description` | Title stays 8–10 words, doesn't just truncate mid-sentence |
| Worknote dedup (already communicated) | Same work note content sent in a prior AI comment, then problem work note re-saved unchanged | `NEW_PROBLEM_WORKNOTE_AVAILABLE = false` — no duplicate customer message |
| Workaround dedup | Same workaround text already in one of the last 10 AI comments | `WORKAROUND_PREVIOUSLY_SHARED = true`, not re-sent as new |
| First-linkage detection (anchor found) | Case already has an "has been associated with the Case" journal entry for this problem, followed by an AI comment | `IS_FIRST_LINKAGE = false` |
| First-linkage detection (no anchor, fallback) | No association journal entry, only a "has been updated to state -" entry | Fallback anchor used correctly |
| 7.8 "no fix" option pick | Problem Closed with no fix, working-as-designed scenario | Correct tone/option chosen inside template 7.8 (this is LLM judgment, not deterministic — ATF can't check it) |
| Large context / long history | Case with a long problem history (many worknotes/comments) | Draft doesn't truncate mid-thought or drop required sections — flagged in architecture doc as an open risk, no mitigation confirmed |

### B2. Manual edges — NAP approval flow

| Edge | How to trigger | What to check |
|---|---|---|
| **Blank NAP** | Trigger the agent normally, observe panel immediately after work item update | Panel renders the draft, not blank — reported bug, root cause not yet confirmed here (separate from the JSON-leak issue below) |
| **Missing proactive trigger** | Add a work note to a linked Problem/Work Item | Agent actually fires — check `u_problem_updated` got set (via T3-style assertion) and that the trigger condition on the agent picked it up |
| **Edge — internal JSON block leaks into NAP** | Trigger Step 4 and/or Step 5 repeatedly (e.g. re-run the same case update several times) since this is intermittent | Confirm whether the JSON block (`NEW_PROBLEM_WORKNOTE_AVAILABLE`, or the `ROUTING_DECISION`/`SELECTED_TEMPLATE`/... block) appears as the chat content instead of the draft. If reproduced, this validates the root cause in [[#Known issue — internal JSON leaking into NAP]] |
| Approve | Consultant clicks Approve on a valid draft | Comment posted to `comments` with AI disclaimer `[Note: AI-assisted message reviewed by consultant]` appended; counter updated per template's `reset_count` |
| Modify then approve | Consultant edits the draft text before approving | Modified text (not original draft) is what gets posted; disclaimer still appended |
| Reject | Consultant rejects | Nothing posted to `comments`; confirm counter/flag state is NOT altered incorrectly (should behave as if no update was sent) |
| STOP routes surfaced correctly | Force a `STOP` (e.g. `resolution_code = Risk Accepted`, or `Duplicate`, or WI required but missing) | `stop_reason` is shown to the consultant, no draft/approval options offered, no customer comment possible |
| STOP_GATE1 routes | No problem linked, case state "Awaiting..." vs. any other state | Correct template (`7.2` vs `7.1`) offered, no crash |
| Assigned-user eligibility failure | `assigned_to` user is inactive/locked, or missing the `sn_customerservice.now_assist_users` role / Now Assist CSM group | Execution fails cleanly — check what (if anything) the consultant/case sees; flagged as unmonitored in the architecture doc |
| Stuck execution | Simulate a long-running or hung agent execution | Confirm whether the case is ever re-picked, or silently excluded forever — flagged as undocumented/unverified |
| NAP chat idle timeout | Leave a draft pending past the configured idle window | Confirm the `AIPF_NAP conversation idle timeout` (24h → 72h per Unit4 request) behaves as expected, doesn't silently drop the draft |

### B3. Manual edges — volume / stale job

| Edge | How to trigger | What to check |
|---|---|---|
| No-change message cap | Same stale case picked up repeatedly with nothing new | Counter increments each no-change pass, stamps `u_auto_update_threshold_reached` at the configured threshold (default 3), case excluded from job for the cooloff window (default 7d) |
| Cooloff expiry behavior | Let cooloff window pass, case picked up again with still nothing new | Counter **re-stamps** and restarts cooloff (does NOT reset to 0) — only a meaningful Problem update resets it fully |
| Full reset on meaningful update | Stale case with count > 0, then a real Problem state/workaround/worknote change lands | Counter resets to 0 via `_getCaseProblemDetails()` clearing the flag |
| Large simultaneous batch | Many stale cases (pilot saw ~30–40 across 2 accounts) qualify in one scheduled job run | No batching/pacing exists today — check for platform load spikes or a flooded consultant NAP; flagged as an open risk, no cap currently enforced |
| Account/case scoping | `sn_csm_ai_agents.case.filter.accounts` and `sn_csm_ai_agents.case.test.cases` properties set | Job only picks up in-scope accounts/cases — use `case.test.cases` to safely pilot against specific numbers |

### B4. Data integrity edges

| Edge | How to trigger | What to check |
|---|---|---|
| WI check duplication drift | Change the Work-Item-required logic in only one of the two places it's enforced ([[AIPF_Flag Cases on Problem State or Work]] vs. [[caseRoutingUtil]]) | The two authorities can drift — verify both still agree after any change to either |
| Disclaimer string change | Someone edits the AI disclaimer text or worknote phrasing ("has been associated with the Case", "has been updated to state -") | Every history/first-linkage/dedup query silently breaks since they string-match on these — regression-test after any copy change |

---

## Suite structure recommendation

Keep ATF's `PCCC – Deterministic Regression` suite as-is (T1–T4, [[#B0. What's already automated (ATF)]]). Everything in B1–B4 is a manual test checklist — not currently automatable without either (a) a mocked LLM harness for drafting quality, or (b) UI-level test automation against the NAP itself. Track manual runs against this checklist per release rather than trying to force them into ATF.

---

## Related Notes

- [[PCCC - Manual Test Scenarios]] — runnable actor-based scripts (User1/User2) for every edge in Part B
- [[Proactive Customer Case Communicator]]
- [[Proactive Customer Case Communicator - ATF Test Suite]]
- [[caseUpdateAgentUtil]]
- [[caseRoutingUtil]]
- [[Resolve routing decision and template selection]]
- [[AIPF_Flag Cases on Problem State or Work]]
- [[Stale Case Scheduled Job]]
- [[Template Registry]]
- [[Counter and Cooloff]]
- [[Now Assist Panel]]
- [[Human in the Loop]]

#servicenow #ai-agent #now-assist #csm #testing #atf #custom-solutions
