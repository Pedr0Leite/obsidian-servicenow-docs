---
title: Partner Case Summary Agent — Test Plan
aliases:
  - PCSA Test Plan
tags:
  - servicenow
  - now-assist
  - ai-agent
  - csm
  - test-plan
  - proposed
status: proposed
date: 2026-07-22
---

# Partner Case Summary Agent — Test Plan

> [!info]
> Traces to acceptance criteria in [[partner-case-summary-agent]]. Test user throughout: `andreea.ionescu@unit4.com` (per story AC "Test user validates both flows end-to-end in sub-prod or scoped prod").

## Related
- [[partner-case-summary-agent]]
- [[partner-case-summary-agent-architecture]]
- [[partner-case-summary-agent-prompt-package]] — v3 tool design; §11 of that note maps Tests 3/4/5/6/7/12 to the new tool split and two new required tests (bulk-summarization partial failure, serialized-list round trip). Tests 3 and 12 below are additionally **blocked** by defect D4 (scoped-app `GlideRecord` doesn't inherit caller ACLs) until that fix lands.

---

## Story: Partner Case Summary Agent

### Test 1: Single-case summary — happy path
- Precondition: `andreea.ionescu@unit4.com` holds role `x_u4_partner_case_summary.agent_user`; a known case (e.g. `CS0001234`) exists with non-empty `short_description` and at least one work note/comment; the user already has ACL read access to this case under existing `sn_customerservice_case` ACLs.
- Steps:
  1. Log in as `andreea.ionescu@unit4.com`.
  2. Open the primary surface (NAP or VA topic, per build outcome) and ask: "Summarize case CS0001234."
  3. Observe the response.
- Expected result: Agent returns a 2-3 line summary covering current status, next steps, and blockers, grounded in the case's actual `short_description`/state/work notes — no fabricated content. Response arrives without requiring any list/filter navigation.
- Validates: AC1 ("Given a case number... returns a 2-3 line summary"), AC4 (no fabrication), AC5 (no navigation required).

### Test 2: Single-case summary — nonexistent case number
- Precondition: Same user; case number that does not exist, e.g. `CS9999999`.
- Steps:
  1. Ask the agent: "Summarize case CS9999999."
- Expected result: Agent responds that the case could not be found — no error stack trace or raw exception surfaced.
- Validates: AC1 (robustness), general implementation quality (not a named AC but required for a usable conversational flow).

### Test 3: Single-case summary — case exists but user lacks ACL read access
- Precondition: A real case exists that `andreea.ionescu@unit4.com` is **not** authorized to view under current `sn_customerservice_case` ACLs (e.g. belongs to an account/assignment group she has no visibility into). Requires test data setup or a second known restricted case.
- Steps:
  1. Ask the agent to summarize that case number.
- Expected result: Agent responds with a "not found" style message — **identical wording** to Test 2's nonexistent-case response (no distinct "access denied" message that would leak the case's existence). No case data of any kind is returned.
- Validates: AC6 ("only see cases they're already authorized to view under existing case ACLs... no privilege escalation").

### Test 4: Account active-case summary — happy path
- Precondition: Test user holds the role; a known account (e.g. "Acme Corp") has 2+ active cases (mix of states, none closed/cancelled/resolved) that the user is authorized to view.
- Steps:
  1. Ask the agent: "Show me open cases for Acme Corp."
  2. Observe the response.
- Expected result: Agent returns one consolidated list with a 2-3 line summary per active case (status/next steps/blockers each), covering all active cases for that account that the user can see. No closed/cancelled/resolved cases appear in the list.
- Validates: AC2 ("Given a client/account name... returns a 2-3 line summary for each, presented as one consolidated list"), AC3 ("Active" = standard active field, excluding closed/cancelled/resolved), AC5 (natural-language ask, no navigation).

### Test 5: Account active-case summary — excludes inactive states
- Precondition: Same account as Test 4, but confirm it also has at least one closed, one cancelled, and one resolved case.
- Steps:
  1. Re-run the same ask as Test 4.
  2. Cross-check the returned case list against a direct list-view query (`account=X AND active=true`) as ground truth.
- Expected result: Agent's returned case set matches the ground-truth active-only query exactly — no closed/cancelled/resolved case numbers appear.
- Validates: AC3 explicitly.

### Test 6: Account active-case summary — ACL filtering applied per case
- Precondition: Account has active cases, some of which the test user is authorized to see and at least one which she is not (e.g. different assignment group with a restrictive ACL).
- Steps:
  1. Ask the agent for that account's open cases.
- Expected result: The consolidated list includes only the cases the user is authorized to view; the case she lacks access to is silently omitted (not listed as "restricted," just absent) — the returned `case_count` reflects only the visible subset, not the account's true total.
- Validates: AC6, and architecture §5/§6's ACL-transparency design decision.

### Test 7: Account name ambiguity / no match
- Precondition: Account name that doesn't exactly match any `customer_account.name` value, or one that fuzzy-matches multiple accounts.
- Steps:
  1. Ask the agent: "Show me open cases for [ambiguous or misspelled name]."
- Expected result: Agent does not silently guess or return an empty result framed as "no cases" — it either asks for clarification/confirmation or clearly states it could not resolve the account name.
- Validates: Architecture §8 risk mitigation (not a named story AC, but required for a trustworthy conversational UX matching AC5's spirit).

### Test 8: Role-gated access — non-authorized user cannot invoke the agent
- Precondition: A ServiceNow user who is **not** one of the 5 named Partner Managers and does not hold `x_u4_partner_case_summary.agent_user`.
- Steps:
  1. Log in as that user.
  2. Attempt to locate/open the agent via NAP/VA and via the Agent Workspace UI action (if visible).
- Expected result: Agent is not available to invoke (not listed in NAP/VA for this user; UI action not visible on the case form/list for this user).
- Validates: AC6 ("Only the 5 named users (or their assigned role) can invoke the agent").

### Test 9: No Copilot Studio / external connector artifacts present
- Precondition: Build complete.
- Steps:
  1. Review the scoped app `x_u4_partner_case_summary` and any related config for Microsoft Copilot Studio connector references, OAuth client ID/secret fields, or external connector setup.
- Expected result: None found — entirely ServiceNow-native (AI Agent, tools, Script Include, role, NAP/VA/UI action), no external Microsoft-side dependency or credentials to manage.
- Validates: AC7 ("No Microsoft Copilot Studio connector... created or exposed").

### Test 10: Audit logging
- Precondition: Test user available; audit table `x_u4_partner_case_summary_audit_log` deployed.
- Steps:
  1. Run Test 1 (single case) and Test 4 (account) as the test user.
  2. Query `x_u4_partner_case_summary_audit_log` for rows tied to that session.
- Expected result: One audit row for the single-case invocation (`u_request_type = single_case`, `u_case` populated, `u_invoking_user = andreea.ionescu@unit4.com`); one audit row per case actually returned for the account invocation (`u_request_type = account_active_cases`, `u_account` populated, `u_case_count_returned` matching the visible count from Test 4).
- Validates: Story's security requirement ("Log/audit AI Agent tool invocations... for traceability").

### Test 11: End-to-end sign-off (test user, both flows, sub-prod or scoped prod)
- Precondition: All prior tests pass; test user is `andreea.ionescu@unit4.com` in sub-prod or scoped prod per the story's explicit requirement.
- Steps:
  1. Run Test 1 and Test 4 as a combined session end to end, unassisted (no dev/architect guiding the interaction).
  2. Confirm the Partner Manager persona could complete both asks using natural language alone, with no list/filter navigation at any point.
- Expected result: Both flows succeed, summaries are accurate against the underlying case data, no navigation required, no unauthorized data exposed.
- Validates: AC8 ("Test user validates both flows end-to-end in sub-prod or scoped prod") — the closing acceptance criterion, gating go-live.

### Test 12: Execution context / no service-account impersonation (build-integrity check)
- Precondition: Access to inspect the AI Agent tool execution configuration (architect/developer level, not an end-user test).
- Steps:
  1. Confirm the AI Agent tools execute in the invoking user's own session context, not a fixed run-as/service account.
  2. Re-run Test 3 and Test 6 while monitoring executed `GlideRecord` query context to confirm ACLs were evaluated against the real invoking user, not an elevated identity.
- Expected result: Confirmed — no elevated execution context anywhere in the tool chain.
- Validates: Architecture §5's core security assumption; underpins AC6 for both Test 3 and Test 6 above.
