---
title: PCCC — Manual Test Scenarios (Actor-Based)
aliases:
  - PCCC Manual Test Scenarios
  - PCCC Test Cases
tags:
  - servicenow
  - ai-agent
  - now-assist
  - csm
  - testing
  - proactive-customer-case-communicator
  - custom-solutions
scope: sn_csm_ai_agents
status: draft
created: 2026-07-22
---

# PCCC — Manual Test Scenarios (Actor-Based)

> [!abstract] One-liner
> Runnable manual test cases for [[Proactive Customer Case Communicator]], written as actor scripts (who does what, what the other person should see) instead of an abstract edge matrix. Companion to [[PCCC - Testing - ATF Build & Manual Runbook]] — that note maps edges to concerns, this one is the actual step-by-step script to execute them.

> [!warning] Environment
> Run all of these in **sub-prod only** (`unit4dev3` or equivalent). Never point at real customer cases — use `sn_csm_ai_agents.case.test.cases` to scope the agent/job to specific test case numbers, per [[Proactive Customer Case Communicator - ATF Test Suite]] prerequisites.

## Actors used throughout

| Actor | Role | Notes |
|---|---|---|
| **User1** | Consultant, `assigned_to` on the test Case | Must be active, unlocked, in `sn_customerservice.now_assist_users` role + Now Assist CSM group — agent runs **as this user** |
| **User2** | Problem/Work Item owner (could be same person as User1 in real life, but keep separate for test clarity — e.g. a Problem Manager) | Makes the Problem/Work Item changes that should trigger the agent |
| **Consultant** | = User1, when acting in the NAP (Approve/Modify/Reject) | |

---

## 1. Problem Update Path — trigger scenarios

### T-1.1 — User2 raises a new Problem and links it to User1's Case (first linkage)

**Preconditions:** Test Case (assigned to User1) exists, `category` = Issue/Question, `active` = true, no Problem linked yet.

**Steps:**
1. User2 creates a Problem, sets `state` = New.
2. User2 links the Problem to the Case (`problem` field on `sn_customerservice_case` = new Problem).

**Expected result:**
- `AIPF_Flag Cases on Problem State or Work` fires on the Problem, sets `u_problem_updated = true` on the Case.
- Agent triggers, runs Steps 1–6 ([[PCCC - Testing - ATF Build & Manual Runbook#Part A — How the agent works, step by step]]).
- `IS_FIRST_LINKAGE = true` → routing `6A`, template `7.3` (New/Assess).
- **User1 sees a new draft appear in the NAP** — not blank, not raw JSON — proposing an "identified problem" message.

---

### T-1.2 — User2 changes Problem state to Fix in Progress, with a Work Item already linked

**Preconditions:** Case already linked to a Problem (post T-1.1), Problem has a `u_work_item` child.

**Steps:**
1. User2 updates Problem `state` → Fix in Progress (104).

**Expected result:**
- BR gate 5 (WI required for 104/106) passes since WI exists.
- Case flagged, agent fires.
- `IS_FIRST_LINKAGE = false`, `implied_state` (last sent) ≠ `problem_state` → `6B`, template `7.7`.
- **User1 sees a new "fix in progress" draft in NAP.**

---

### T-1.3 — User2 changes Problem state to Fix in Progress, with NO Work Item linked

**Steps:**
1. User2 updates Problem `state` → Fix in Progress, no `u_work_item` child exists.

**Expected result:**
- BR gate 5 exits — case is **not** flagged (verifiable via T3 in ATF: `u_problem_updated` stays false).
- No agent trigger, no NAP message at all. This is correct behavior, not a bug — confirms the WI gate works.

---

### T-1.4 — User2 writes a Problem work note (no state/workaround change)

**Preconditions:** Case linked to Problem, Problem `state` unchanged since last communication.

**Steps:**
1. User2 adds a Problem work note with new technical detail (not a greeting-only or internal-routing note).

**Expected result:**
- BR trigger gate fires (work_notes changed).
- Case flagged, agent runs.
- Routing lands on `6C` (state unchanged) since `implied_state == problem_state`.
- Step 4 resolves `NEW_PROBLEM_WORKNOTE_AVAILABLE = true` (new content, not previously sent).
- Template `7.9` selected.
- **User1 sees a new "worknote update" draft in NAP**, with noise stripped out (see T-1.4b).

### T-1.4b — Same as above, but the work note contains internal-only content

**Steps:**
1. User2's work note reads: *"Hi, PS consultant confirmed root cause not reproducible. @jane.doe can you check the logs? Please reassign to Tier 2."*

**Expected result:**
- Draft in NAP should read something like *"Not reproducible"* only — greeting, role reference, mention, and reassignment request all stripped per Step 2 cleaning rules ([[PCCC - Testing - ATF Build & Manual Runbook#Part A]]).
- **Fail condition:** any of the raw internal phrasing (mentions, "please reassign", role names) appears in the customer-facing draft.

---

### T-1.4c — User2 changes ONLY the workaround field (workaround-only-change override)

**Added 2026-07-24**, confirmed working end-to-end on a live test the same day — see [[Proactive Customer Case Communicator#17. Changelog]].

**Preconditions:** Case linked to Problem, Problem `state` unchanged since last communication, workaround field currently empty or containing an already-shared value.

**Steps:**
1. User2 edits **only** the Problem's `workaround` field, setting a genuinely new (not previously shared) value — no other field changes in the same edit.

**Expected result:**
- Agent fires via the same real-time chain as always: BR → `u_problem_updated` flag → Flow Designer trigger (`u_problem_updated CHANGESTO true`) → agent.
- Routing tool's `WORKAROUND_ONLY_LATEST_CHANGE` variable evaluates true (derived from `sys_audit`/`sys_journal_field` history showing the workaround field as the only thing that changed) → **template `7.4` fires directly**, bypassing the normal `6A`/`6B`/`6C` state-based decision entirely.
- **User1 sees a new "workaround shared" draft in NAP** (`[WORKAROUND]` token filled with the new value).
- **Fail condition:** no draft appears, or a different template (e.g. `7.10.2` "nothing new") fires instead — this was the original bug this fix addresses.

### T-1.4d — Same as T-1.4c, but the "new" workaround is placeholder/junk text

**Steps:**
1. User2 sets the workaround field to junk/placeholder text (e.g. "N/A", "TBD", or obvious test filler).

**Expected result:**
- `[WORKAROUND]` token does **not** get filled with the junk text — this is the CLEAN AND FILTER CONTENT semantic filter correctly rejecting placeholder content, by design (confirmed working-as-designed 2026-07-24, not a bug). Confirm the draft either omits the workaround section gracefully or the message doesn't send, rather than leaking "N/A"/"TBD" to the customer.

---

### T-1.5 — User2 repeats the same work note content (no new information)

**Preconditions:** T-1.4 already ran and was approved (message sent to customer).

**Steps:**
1. User2 re-saves the Problem with the same work note text (or a trivial re-save with no new content).

**Expected result:**
- Agent fires (BR sees work_notes changed).
- Step 4 dedup check: this content already appears in `worknote_history` → `NEW_PROBLEM_WORKNOTE_AVAILABLE = false`.
- **User1 should NOT see a duplicate draft** — either no NAP message, or a "6C nothing new" (`7.10.2`) message, never a repeat of the already-sent worknote.

---

### T-1.6 — User2 sets Problem resolution to Risk Accepted / Duplicate

**Steps:**
1. User2 sets Problem `resolution_code` = Risk Accepted (or Duplicate).

**Expected result:**
- Routing hits the resolution guard → `STOP`.
- **User1 sees `stop_reason` displayed in NAP** ("No communication required — Problem resolution code is Risk Accepted..."), no draft, no send option.

---

### T-1.7 — User2 sets Problem to Resolved/Closed + Fix Applied (final closure message)

**Steps:**
1. User2 updates Problem `state` → Resolved, `resolution_code` = Fix Applied (with WI linked).

**Expected result:**
- Routing `6A` or `6B` depending on prior history → template `7.5` ("Hi" greeting, not "Dear" — verify greeting word specifically).
- **User1 sees the fix/release draft in NAP.**
- Per Template Registry, `reset_count = true` — confirm the case's `u_auto_update_count` goes back to 0 after this is approved (cross-check against [[PCCC - Testing - ATF Build & Manual Runbook#B3. Manual edges — volume / stale job]]).

---

## 2. NAP Approval Flow — User1 actions

### T-2.1 — User1 approves a draft as-is

**Preconditions:** Any of the above scenarios produced a pending draft.

**Steps:**
1. User1 opens NAP, clicks **Approve**.

**Expected result:**
- Text posted verbatim to Case `comments` (customer-visible Additional Comments).
- Disclaimer `[Note: AI-assisted message reviewed by consultant]` appended.
- Counter/flag updated per the template's `reset_count` contract.

### T-2.2 — User1 modifies the draft before approving

**Steps:**
1. User1 edits the draft text in NAP (e.g. adds a personal note).
2. User1 clicks **Approve**.

**Expected result:**
- The **modified** text is what's posted to `comments`, not the original AI draft.
- Disclaimer still appended.
- **Fail condition:** original unmodified draft gets posted instead of the edit.

### T-2.3 — User1 rejects the draft

**Steps:**
1. User1 clicks **Reject**.

**Expected result:**
- Nothing posted to `comments`.
- Case state (counter, `u_problem_updated`, etc.) should reflect "no update sent" — confirm it doesn't silently behave as if approved (check counter didn't increment/reset incorrectly).
- Confirm whether the same content is offered again on the next trigger, or considered "handled" and lost (open question — log actual behavior).

---

## 3. Bug-report-driven scenarios (reproduce the reported issues)

### T-3.1 — Reproduce: blank NAP panel

**Steps:**
1. Run T-1.1 or T-1.2 (a normal trigger that should produce a draft).
2. Watch the NAP immediately as the agent executes.

**Expected result:** Draft renders.
**What to capture if it fails:** Does the panel ever populate on refresh/reopen? Is there an error in the agent execution log (`sn_aia_execution_plan` / `sn_aia_execution_task`)? Does it correlate with a specific step (fetch failing, routing STOP with no message bound, etc.)?

### T-3.2 — Reproduce: internal JSON leaking into NAP (`{"NEW_PROBLEM_WORKNOTE_AVAILABLE": true}`)

**Steps:**
1. Run T-1.4 (worknote-only update) several times in a row — this is the path most likely to hit Step 4's JSON-producing instruction, and the issue is intermittent.
2. Also try T-1.2/T-1.7 to see if Step 5's larger JSON block (`ROUTING_DECISION`, `SELECTED_TEMPLATE`, etc.) leaks the same way.

**Expected result:** Draft message only, never raw JSON.
**Root cause already confirmed** (see [[PCCC - Testing - ATF Build & Manual Runbook#Known issue — internal JSON leaking into NAP]]): the agent's Instructions ask the LLM to "produce" these JSON blocks as output with only a "do not display to end-user" prose guardrail — no structural separation from the chat turn. Use this test to **confirm reproduction rate** (how often it leaks) before/after any instruction fix — this is what "validated in non-production" in the bug's Acceptance Criteria should mean concretely.

### T-3.3 — Reproduce: missing proactive trigger after work item note

**Steps:**
1. User2 adds a note directly to the **Work Item** (`u_work_item`), not the Problem itself.

**Expected result / question to resolve:** The BR (`AIPF_Flag Cases on Problem State or Work`) fires on `problem` insert/update — **does a Work Item note alone trigger anything?** Per the architecture note, the trigger is Problem-centric. If the bug report expects a Work Item note to proactively notify User1, and the BR only watches the Problem table, that's a real gap — confirm whether Work Item notes are expected to bubble up to a Problem work note automatically (integration point) or whether this is a **feature gap, not a bug** (Case UWID0067437 / Problem PRB0065509 referenced in the original bug report are a good pair to test this directly against).

### T-3.4 — Reproduce: consultant can't tell why nothing happened (silent STOP without visibility)

**Steps:**
1. Trigger a `STOP_GATE1` or `STOP` scenario (T-1.3, T-1.6) where no Problem is linked or a guard blocks it.

**Expected result:** Confirm the consultant actually sees *something* (stop reason) rather than the NAP just staying blank/silent — cross-check against T-3.1, since "blank NAP" and "silent STOP" may be the same underlying symptom reported by different users.

---

## 4. Eligibility & platform edges

### T-4.1 — User1 (assigned_to) is inactive/locked

**Steps:**
1. Deactivate or lock User1's account.
2. Run T-1.1.

**Expected result:** Execution should fail cleanly (agent runs as Case Assigned To). Capture: does this fail silently (no NAP, no log) or with a visible error? This is flagged as unmonitored in the architecture doc — use this test to establish current behavior as a baseline.

### T-4.2 — User1 missing Now Assist CSM role/group

**Steps:**
1. Remove `sn_customerservice.now_assist_users` role (or CSM group membership) from User1.
2. Run T-1.1.

**Expected result:** Same as T-4.1 — document actual failure behavior.

---

## 5. Stale Case Path (time-driven) scenarios

### T-5.1 — Case goes quiet, no Problem change, scheduled job picks it up

**Preconditions:** Case's `u_last_comment_from_unit4` older than `stale.threshold.days` (default 2), `u_auto_update_count` below threshold.

**Steps:**
1. Let the Stale Case Scheduled Job run (or run it manually in sub-prod).

**Expected result:** Subflow fires for the case, agent runs as User1, produces a "6C nothing new" (`7.10.2`) or appropriate no-change message. User1 sees it in NAP.

### T-5.2 — Repeat T-5.1 until threshold reached

**Steps:**
1. Let the job pick up the same case for 3 consecutive stale cycles with nothing new (default threshold = 3).

**Expected result:** On the 3rd no-change pass, `u_auto_update_threshold_reached` gets stamped, case excluded from the job for the cooloff window (default 7 days).

### T-5.3 — Cooloff expiry

**Steps:**
1. Advance past the cooloff window (or lower `case.auto.update.cooloff.days` in a test config).
2. Let the job run again with still nothing new.

**Expected result:** Case picked up again; counter **re-stamps** threshold and restarts cooloff (does not reset to 0) — confirm against [[PCCC - Testing - ATF Build & Manual Runbook#B3. Manual edges — volume / stale job]].

### T-5.4 — Meaningful Problem update resets everything

**Steps:**
1. From a case with `u_auto_update_count > 0` (post T-5.1/5.2), User2 makes a real Problem update (state/workaround/worknote change per gate 1).

**Expected result:** Counter fully resets to 0 via `_getCaseProblemDetails()` — confirm this happens even mid-cooloff.

---

## 6. Session fixes (2026-07-24) — regression tests

New/hardened behavior confirmed live on 2026-07-24 — see [[Proactive Customer Case Communicator#17. Changelog]] for full detail. These guard against the specific fixes regressing.

### T-6.1 — `[RELEASE_VERSION]` placeholder does not leak into the draft

**Preconditions:** Trigger template `7.5` (Resolved/Closed + Fix Applied) per T-1.7, but with `fix_notes` left as placeholder/filler text (e.g. blank, "TBD") rather than a real release version.

**Expected result:** The `[RELEASE_VERSION]` token is deleted and the sentence referencing it is rewritten, not left as a literal `[RELEASE_VERSION]` string in the customer-facing draft. **Fail condition:** the literal token or a placeholder value appears in the draft User1 sees in NAP.

### T-6.2 — Token-leak check catches `[WORKAROUND]`/`[WORKNOTE]` too, not just `[RELEASE_VERSION]`

**Steps:** Trigger any combination of T-1.4c (workaround) and T-1.4 (worknote) in the same draft cycle (e.g. via `append_workaround`/`append_worknote` combined-message flags), with a scenario likely to leave an unfilled token.

**Expected result:** No literal `[WORKAROUND]`, `[WORKNOTE]`, or `[RELEASE_VERSION]` token ever appears in a NAP draft — the token check now runs mandatorily on every draft, not just after the `[RELEASE_VERSION]`-specific fix path.

### T-6.3 — Template 7.8 prompts User1 to choose a closing, not inferred by the AI

**Preconditions:** Trigger template `7.8` (Problem Resolved+Canceled or Closed+Canceled per T-1.6/T-1.7 variants).

**Steps:** Observe the drafting flow in NAP before the draft is presented.

**Expected result:** User1 is explicitly prompted to pick **1 of 3 closings** before the draft is generated — the AI does not infer the closing wording from Problem cause notes on its own. **Fail condition:** a draft appears directly with no closing choice presented.

### T-6.4 — Approve/Modify/Reject renders as clickable NAP buttons

**Preconditions:** Any scenario producing a pending draft (e.g. T-1.1, T-1.2).

**Expected result:** The Approve/Modify/Reject options render as clickable buttons in NAP (numbered-list format under the hood), the same rendering mechanism already used for the `7.8` closing-choice options in T-6.3 — not as plain text User1 has to type a response to.

### T-6.5 — Tool-call inputs pass through unmodified (no LLM mistranscription)

**Preconditions:** Any scenario where `WORKAROUND_PENDING` (or another Tool 1-fetched variable) is passed into Tool 2's routing call — e.g. T-1.4c.

**Expected result:** The value routed into Tool 2 matches exactly what Tool 1 fetched — spot-check by comparing the actual Problem/Case field value against what the routing decision acted on. **Fail condition:** routing behaves as if a fetched variable had a different value than what's actually on the record (the original bug this fix addresses was a silent mistranscription of `WORKAROUND_PENDING` specifically).

---

## Coverage cross-reference

| Scenario group | Maps to runbook section |
|---|---|
| §1 Problem Update Path | Part A steps 1–6, [[PCCC - Testing - ATF Build & Manual Runbook#B1. Manual edges — LLM drafting & content quality]] |
| §2 NAP Approval | [[PCCC - Testing - ATF Build & Manual Runbook#B2. Manual edges — NAP approval flow]] |
| §6 Session fixes (2026-07-24) | [[Proactive Customer Case Communicator#17. Changelog]] |
| §3 Bug repro | Same section, bug-specific rows |
| §4 Eligibility | Same section, eligibility row |
| §5 Stale Path | [[PCCC - Testing - ATF Build & Manual Runbook#B3. Manual edges — volume / stale job]] |

Deterministic logic underlying all of these (routing branches, template contract, BR gates, counter math) is already regression-tested by ATF — see [[Proactive Customer Case Communicator - ATF Test Suite]]. These scenarios exist to catch what ATF structurally cannot: LLM output quality and the live NAP conversation.

---

## Related Notes

- [[PCCC - Testing - ATF Build & Manual Runbook]]
- [[Proactive Customer Case Communicator]]
- [[Proactive Customer Case Communicator - ATF Test Suite]]
- [[Now Assist Panel]]
- [[Human in the Loop]]

#servicenow #ai-agent #now-assist #csm #testing #custom-solutions
