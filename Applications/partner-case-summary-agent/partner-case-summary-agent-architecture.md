---
title: Partner Case Summary Agent — Technical Architecture
aliases:
  - Partner Case Summary Agent Architecture
  - PCSA Architecture
tags:
  - servicenow
  - now-assist
  - ai-agent
  - csm
  - architecture
  - proposed
status: proposed
scope: x_u4_partner_case_summary
date: 2026-07-22
---

# Partner Case Summary Agent — Technical Architecture

> [!info] Status
> Design only. Resolves both open questions from [[partner-case-summary-agent|the story]]: role-vs-group access design, and Virtual Agent/NAP licensing with a documented fallback. Nothing built yet.

> [!warning] §4 and §5 superseded by the v4 prompt package
> The prompt/tool design has moved on to **v4** (three tools; per-case summarization runs inside the account-query loop and is returned as `resume`) since this section was first written — see [[partner-case-summary-agent-prompt-package]] for the current agent prompt, full tool contracts, and a script defect register (D1-D6). §4 below is kept for the original two-tool rationale but is no longer the build target; §5's ACL claim is corrected in that package's D2. See §17 Changelog.

## Related
- [[partner-case-summary-agent]] — locked story this design implements
- [[partner-case-summary-agent-prompt-package]] — canonical v3 agent prompt, tool contracts, defect register, open items
- [[Proactive Customer Case Communicator]] — sibling agent on the same table; this design intentionally diverges from its write-heavy pattern where noted

---

## 0. Divergence from PCCC — read this first

PCCC is a **write** agent: draft → human approval → post to a customer-visible field. This agent is **read-only**: it never writes to `sn_customerservice_case`, never posts a comment, never changes state. Consequences:

- **No Approve/Modify/Reject loop.** There is nothing to approve — the output is a transient chat response, not a persisted case update. NAP/Virtual Agent renders the summary and the interaction ends. Building an approval step here would just add friction for zero governance benefit.
- **No custom fields, no counters, no cooloff.** PCCC's `u_problem_updated`, `u_auto_update_count`, etc. exist to pace and dedupe *outbound customer communication*. This agent produces nothing outbound and nothing persisted, so none of that state exists. Zero new fields on `sn_customerservice_case`.
- **No Business Rule trigger.** PCCC is proactive (BR flags cases, scheduled job sweeps stale ones). This agent is reactive-only — a Partner Manager asks, the agent answers. No BR, no scheduled job.
- **No "AI disclaimer" journal marker.** PCCC stamps every post with a marker string because later logic mines the journal for history. This agent never writes to the journal, so there is nothing to mark and nothing to mine.
- **What carries over from PCCC's house style:** a single Script Include owns all data access (mirrors `caseUpdateAgentUtil`), tools stay thin wrappers around Script Include methods, read/write separation as a principle (here it's simply read/read, since there's no write tool at all), system properties for anything configurable (max cases per summary, active-state exclusion list), and the same scoped-app ACL/role pattern for security.
- **Audit is the one PCCC-style control that stays.** The story requires logging which cases were summarized by whom — that governance concern is identical in a read agent, so it's implemented the same way conceptually (a log table / event, not a journal post).

---

## 1. System Context

| Attribute | Value |
|---|---|
| App scope | `x_u4_partner_case_summary` (new scoped app — see §2 scope note) |
| Primary table | `sn_customerservice_case` (read-only access) |
| Related tables | `sys_user`, `customer_account` (or the CSM account table in use), new `x_u4_partner_case_summary_audit_log` |
| Surface | [[Now Assist Panel]] conversational entry (primary) + [[virtual-agent|Virtual Agent]] topic (equivalent primary option) + Agent Workspace UI action (secondary/fallback, documented) |
| Runs as | The invoking Partner Manager's own session/ACL context — **not** an elevated service account (see §5) |
| Human control | None needed — read-only, nothing to approve |
| AI role | Summarization prose only, from real fetched fields — no case-state decisions |
| Deterministic role | Script Include owns the query/filter logic (which cases are "active", which fields feed the summary) |

---

## 2. Scope Decision

The story doesn't lock an app scope (only the table is locked). Recommendation: **new dedicated scoped app**, not reuse of `sn_csm_ai_agents` (PCCC's scope).

Reasoning:
- This agent has a different owner (Partner Manager tooling vs. consultant-facing case communication), different role/audience, and no shared components with PCCC beyond the table.
- Bundling into `sn_csm_ai_agents` would mean the audit log table, role, and tools ship inside a scope whose existing update-set history and naming conventions belong to a different feature. Cleaner lifecycle (enable/disable/rollback independently) with its own scope.
- Cross-scope note: the AI Agent framework tables (`sn_aia_*`) are platform/global tables the agent framework itself uses regardless of app scope — this is normal AI Agent tool registration, not a custom cross-scope call. Flagged for Governance review per house process, but it is the standard AI Agent platform pattern, not bespoke cross-scope scripting.

**App scope:** `x_u4_partner_case_summary`
**Update set naming:** `Partner Case Summary Agent — <component>` (see §9 build order for the per-set breakdown)

> [!flag] Cross-scope dependency to confirm with Governance
> Tool scripts will run `GlideRecord('sn_customerservice_case')` from a custom scope. Confirm the table's scope (CSM plugin, typically global) allows cross-scope read via the standard ACL evaluation path — it does by default for `GlideRecord` respecting ACLs, but Governance should sign off since this is the one genuine cross-scope read in the design.

---

## 3. Data Model — new components on `sn_customerservice_case`

**None.** No custom fields are added to the case table. This is the first explicit divergence to call out: PCCC needed `u_problem_updated`, `u_auto_update_count`, `u_auto_update_threshold_reached` because it paces asynchronous proactive outreach. This agent has no async trigger and no pacing problem — it answers a synchronous ask and returns. Zero schema changes to `sn_customerservice_case`.

### New table: `x_u4_partner_case_summary_audit_log`

Satisfies the story's audit requirement ("log/audit AI Agent tool invocations — which cases were summarized, by whom").

| Field | Type | Purpose |
|---|---|---|
| `u_invoking_user` | Reference (`sys_user`) | Who asked |
| `u_request_type` | Choice: `single_case` / `account_active_cases` | Which tool was invoked |
| `u_case` | Reference (`sn_customerservice_case`) | Populated for `single_case`; also written once per matching case for `account_active_cases` (one row per case summarized, not one row per request) |
| `u_account` | Reference (account table) | Populated for `account_active_cases` |
| `u_case_count_returned` | Integer | How many cases were actually summarized (post-ACL-filter count — see §5) |
| `sys_created_on` | (out of box) | Timestamp — no separate field needed |

Row-per-case (not row-per-request) on the account flow so "which cases were summarized, by whom" is answerable with a single flat query, matching the story's wording exactly.

---

## 4. AI Agent + Tools

**AI Agent name:** `Partner Case Summary Agent`
**Framework:** Now Assist ReAct AI Agent
**Scope:** `x_u4_partner_case_summary`

### Tool 1 — "Get Case Summary"

| | |
|---|---|
| Type | Agent Tool (read) — calls Script Include |
| Input | `case_number` (string, e.g. `CS0001234`) |
| Output | `{ found: boolean, case_number, short_description, state_label, assignment_group, assigned_to, summary_text }` or `{ found: false, reason }` |
| GlideRecord logic | `new GlideRecord('sn_customerservice_case'); gr.addQuery('number', caseNumber); gr.query();` — standard `GlideRecord` respects ACLs automatically for the running user; if `gr.next()` returns false (either the case doesn't exist or the user has no read access — indistinguishable by design, see §5), return `found:false`. Read fields: `short_description`, `state`, `assignment_group`, `assigned_to`, `comments` (or `work_notes` per data-source decision below), `account`. |
| Data source for summary | `short_description` + last N (default 5, via system property) entries from `work_notes`/`comments` journal, filtered to non-empty, most recent first — passed to the LLM instruction as grounding context. No fabrication: instructions explicitly require the 2-3 line summary (status / next steps / blockers) to be derivable only from these fetched fields; if a dimension isn't present in the data (e.g. no blocker mentioned), the agent states "no blocker noted" rather than inventing one. |
| Audit | Script Include writes one `x_u4_partner_case_summary_audit_log` row per invocation (`u_request_type = single_case`) |

### Tool 2 — "Get Active Cases for Account"

| | |
|---|---|
| Type | Agent Tool (read) — calls Script Include, internally re-uses Tool 1's summarization method per case |
| Input | `account_name` (string — free text as spoken/typed by the Partner Manager) |
| Output | `{ found: boolean, account_name, resolved_account_sys_id, case_count, cases: [ { case_number, short_description, summary_text }, ... ] }` |
| GlideRecord logic — account resolution | `new GlideRecord('customer_account'); gr.addQuery('name', 'STARTSWITH', accountName); gr.query();` (exact-match first, `STARTSWITH`/`CONTAINS` fallback if zero hits, per system property `x_u4_partner_case_summary.account_match_mode`). If zero or multiple ambiguous matches, return a disambiguation response rather than guessing (agent instruction: ask the user to confirm which account). |
| GlideRecord logic — case query | `new GlideRecord('sn_customerservice_case'); gr.addQuery('account', resolvedAccountSysId); gr.addActiveQuery(); gr.query();` — `addActiveQuery()` uses the table's standard `active=true` field, which per the story's locked definition already excludes closed/cancelled/resolved states (confirm the CSM plugin's `active` field flag configuration excludes those specific `state` values as a pre-build check — see §9 step 1). Cap result count via `gr.setLimit()` bound to a system property (default 25) to bound token usage / response size; if the cap is hit, output includes `truncated: true` and the true `case_count` so the agent can tell the user more cases exist than shown. |
| Per-case summarization | For each matching `GlideRecord` row, build the same summary input structure as Tool 1 and let the agent produce a 2-3 line summary; tool returns the raw per-case data, **the agent** (not the tool) does the LLM summarization pass per case — this keeps the tool deterministic/data-only and the summarization step where it belongs (LLM), consistent with PCCC's read/decide/write separation principle even though there's no write step here. |
| Audit | One `x_u4_partner_case_summary_audit_log` row per case actually summarized (`u_request_type = account_active_cases`, `u_account` set), plus the `u_case_count_returned` total |

> [!note] Why two tools, not one
> Keeping the tools split mirrors the story's two named capabilities and keeps each tool's GlideRecord query simple and independently testable, matching PCCC's convention of one tool per distinct data operation rather than one do-everything tool.

> [!warning] Superseded — v4 uses three tools, not two
> "Get Active Cases for Account" was split into two tools (Search Account → user selection gate → Get Active Cases from Account), with per-case summarization now happening *inside* Get Active Cases from Account's query loop via `sn_uxc_gen_ai.TaskSummarize`, returned per case as `resume` rather than as a separate bulk step. (An intermediate v3 briefly used a fourth, standalone `GetBulkCasesSummarization` tool — superseded, see the prompt package's changelog.) Full contracts: [[partner-case-summary-agent-prompt-package#8. Tool contracts|prompt package §8]]. The "one tool per data operation" rationale above still holds — it's *why* the split happened, just with a finer grain than originally designed.

---

## 5. Script Include — `PartnerCaseSummaryUtil`

Single Script Include, scoped, owning all data access — mirrors `caseUpdateAgentUtil`'s centralization role in PCCC.

| Method | Responsibility |
|---|---|
| `getCaseSummaryData(caseNumber)` | `GlideRecord` lookup by `number`, ACL-respecting. Returns null/not-found object if no record is returned by the query — **does not distinguish** "case doesn't exist" from "case exists but caller has no read access" in the response (returning that distinction would itself be a privilege-escalation leak — see ACL note below). Called directly by Tool 1, and once per row by Tool 2. |
| `getActiveCasesForAccount(accountName)` | Resolves account (exact/fuzzy per system property), then queries active cases scoped to that account, respecting the same ACL context. Returns the capped, ACL-filtered case list. |
| `logInvocation(invokingUser, requestType, caseSysId, accountSysId, caseCountReturned)` | Single method that writes to `x_u4_partner_case_summary_audit_log`. Called by both tools after every invocation (success or not-found), so denied/empty lookups are auditable too. |

No write methods exist in this Script Include — there is no `_addCaseComment`-equivalent, by design (§0).

### Why ACL enforcement here is "do nothing extra," and why that's the point

> [!bug] Corrected by the prompt package (D2) — plain `GlideRecord` is NOT sufficient here
> The claim below — that `GlideRecord` "automatically" respects the invoking user's ACLs — holds for a Business Rule or Client Script running in the user's own session, but **not** for a scoped-app Script Include: scoped-app `GlideRecord` evaluates against the **application's** access rights, not the caller's record-level ACLs. Both query methods (`getCaseSummaryData`, `getActiveCasesForAccount`) must use `GlideRecordSecure()`, not `GlideRecord()`. Without this fix, Search Account / Get Active Cases from Account can return records the Partner Manager cannot open, and — since the per-case summarization step moved in-loop (v4) — that same unsecured query feeds sys_ids straight into `TaskSummarize`, so the tool generates and returns summary **content** for those cases, a worse leak than existence disclosure. See [[partner-case-summary-agent-prompt-package#9. Script defect register|prompt package §9, D2]] for the full writeup and fix. The paragraph below is kept for historical context; treat "do nothing extra" as false until `GlideRecordSecure()` is in place.

`GlideRecord` queries executed in the context of the invoking user automatically apply `sn_customerservice_case` ACLs — rows the user isn't authorized to read are simply not returned by `gr.query()`/`gr.next()`. The Script Include does not need (and must not add) any bypass such as `setWorkflow(false)`, `autoSysFields(false)`, or an elevated service account impersonation. This is the mechanism that satisfies "respect existing case ACLs, no privilege escalation" — it's automatic as long as:

1. The AI Agent tool executes as the **requesting user's session**, not a fixed run-as account (confirm this is the default AI Agent execution mode at build time — PCCC deliberately runs as `Assigned To` for its own reasons; this agent must **not** copy that pattern and must run as the invoking Partner Manager).
2. No script in the Script Include ever escalates the `GlideRecord` beyond default ACL evaluation.

This is flagged explicitly as a build-time verification step in §9 and a test case in the test plan — it is the single most important security property of the whole design.

---

## 6. ACL / Role Design — resolves Open Question 1

**Recommendation: dedicated custom role, assigned directly to the 5 named users — not a group.**

Rationale:
- 5 named, specific individuals is exactly the case where a role-assignment-to-user is simpler and more auditable than standing up a group for a set this small and this static. A group adds an indirection layer (group membership table, group-to-role mapping) that buys nothing at this scale and is one more place membership can silently drift.
- The story explicitly frames access as "5 named users (or their assigned role)" — a role is the mechanism, direct assignment is the simplest correct implementation of it.
- If this population is expected to grow into a standing "Partner Manager" job function with regular onboarding/offboarding, a group would pay off later — but that's a "when it grows" migration, not a day-one requirement. Design leaves the door open: the ACL is written against the **role**, so migrating from direct role assignment to role-via-group later is a zero-script change (just add group-to-role inheritance).

### Components

| Component | Detail |
|---|---|
| Role | `x_u4_partner_case_summary.agent_user` |
| Assignment | Direct role grant to the 5 named `sys_user` records (andreea.ionescu, andy.christenson, elsa.granzow, eva.beltowska, henric.ceder) |
| AI Agent data-access / user-access config | Agent's "who can invoke" configuration restricted to `x_u4_partner_case_summary.agent_user` (same pattern as PCCC's `sn_customerservice.now_assist_users` gate, just scoped to this agent instead of granted broadly) |
| Table ACL | **No new ACL is added on `sn_customerservice_case` itself.** The role gates *invocation of the agent*, not *read access to cases* — case-level read access continues to be governed entirely by whatever ACLs already exist on `sn_customerservice_case` today, for the invoking user's existing roles/groups. This is the load-bearing design choice that prevents privilege escalation: holding `x_u4_partner_case_summary.agent_user` lets you *ask the agent a question*, it does not grant you read access to any case you couldn't already open in Agent Workspace. |
| Audit log ACL | New table `x_u4_partner_case_summary_audit_log`: read restricted to admin/scoped-app-admin role only (Partner Managers don't need to read the audit log; it's for governance) |

> [!important] The role is an invocation gate, not a data-access grant
> This is the answer to "no privilege escalation via the agent." A Partner Manager with the role who asks about a case they don't have ACL rights to see gets a "not found / no access" response — same as if they'd tried to open that case directly in the platform.

---

## 7. Surfacing — resolves Open Question 2

**Recommendation: Now Assist Panel (NAP) conversational entry point as primary, with an Agent Workspace UI action as the documented secondary/fallback path — exactly as the story's implementation notes already lean.** Virtual Agent topic is an acceptable equivalent primary surface if NAP conversational entry isn't the preferred channel for this persona; the two aren't mutually exclusive, but standardize on **one** as primary to avoid duplicate maintenance of the natural-language entry logic.

### Decision inputs to confirm on the target instance before committing (this is the "resolve, don't leave dangling" part)

1. **Now Assist / AI Agent licensing/plugin state** — check `sn_aia_*` plugin activation (`com.glide.ai.agent` or the Now Assist framework plugin family already active for PCCC, since PCCC runs in this same instance) and whether the **Now Assist Panel** is enabled for the CSM workspace specifically (NAP entitlement can be workspace-scoped). Since PCCC already ships NAP-based interaction on this same instance, licensing is very likely already present — this is largely a confirmation step, not a new procurement question.
2. **Virtual Agent plugin/licensing** — check `com.glide.cs.chatbot` (Virtual Agent) plugin activation and whether a Virtual Agent topic can be scoped to the 5 named users' persona (VA topics are typically broadly available once licensed, so the role-gate needs to sit in the topic's conversation flow, not just the AI Agent tool layer).
3. **Fallback trigger condition:** if neither NAP nor VA licensing is confirmed active for this instance/workspace within the build window, ship the Agent Workspace UI action as the **only** entry point for go-live, and treat NAP/VA surfacing as a fast-follow once licensing is confirmed — this keeps the story's "no list/filter navigation" acceptance criterion at risk only in the fallback case, which should be flagged to the Partner Manager stakeholders explicitly if it's invoked (a plain UI action is still "low navigation" relative to raw list/filter work, just not fully conversational).

### Primary surface: Now Assist Panel

- Entry point: NAP conversational session with the `Partner Case Summary Agent` attached, available to users holding `x_u4_partner_case_summary.agent_user`.
- Natural-language routing: the agent's own instructions (ReAct reasoning) distinguish "summarize case CS0001234" (routes to Tool 1) from "show me open cases for Acme Corp" (routes to Tool 2) — no separate NLU/topic model needed, this is exactly what the ReAct framework's tool-selection reasoning is for.

### Secondary/fallback: Agent Workspace UI action

- A UI action on the `sn_customerservice_case` list/form (visible only to `x_u4_partner_case_summary.agent_user`) that opens the same agent conversation pre-seeded with the current case number — power-user shortcut, not a replacement for the conversational entry point.
- Also serves as the **documented fallback** per open question 2 if NAP/VA licensing isn't available: same agent, same tools, same ACL/role gate, just invoked from a button instead of free text. This is a UI entry point change only — zero change to the tools, Script Include, or ACL design above.

---

## 8. Risks / Flags

- **Cross-scope GlideRecord read** on `sn_customerservice_case` from `x_u4_partner_case_summary` — flagged for Governance sign-off (§2). Two distinct security layers are in play here and must not be conflated: row-level ACL enforcement (§5, automatic per invoking-user session) and the separate cross-scope **Application Access** grant (§9 pre-build step 4 / build step 6) that determines whether the scoped app can query the table's API at all. Missing the latter presents as a silent zero-rows result, not an error — resolved by adding an explicit `sys_scope_privilege` record before Tool 1/Tool 2 are built.
- **Account name resolution is fuzzy by nature** (free-text "Acme Corp" vs. exact `customer_account.name`) — ambiguous/zero matches must produce a disambiguation response, not a guess or an empty silent result. Build this deliberately; it's the most likely source of "agent said no cases" false negatives in UAT.
- **Response size / token limits** on the account-summary flow if an account has many active cases — capped via `setLimit()` + system property (§4), with `truncated` signaling back to the agent/user, same class of risk PCCC flagged for long case histories.
- **NAP/VA licensing unresolved until confirmed on-instance** (§7) — fallback path is designed and ready, but confirm before build to avoid last-minute surface swap.
- **`found:false` ambiguity is intentional**, not a bug — see §5. Do not "fix" this later by adding a distinct "no access" message; that would leak case existence to unauthorized users.
- **No new field/table changes to `sn_customerservice_case` itself** — only a net-new audit table. Low blast radius on the CSM table compared to PCCC.

---

## 9. Dev Instructions — Build Order

### Pre-build verification (do first, blocks everything else)
1. Confirm on target instance: Now Assist / AI Agent plugin active; NAP entitlement for CSM workspace; Virtual Agent plugin state. Record findings against §7 decision inputs — this determines whether NAP, VA, or UI-action-only ships at go-live.
2. Confirm `sn_customerservice_case.active` field's underlying state-value configuration actually excludes closed/cancelled/resolved states per the story's "Active" definition (§3 story's locked AC) — check Dictionary/`active` calculation, don't assume.
3. Confirm AI Agent tools can be configured to execute in the **invoking user's session context** (not a run-as/service account) — this is the load-bearing ACL assumption in §5. If the platform's AI Agent framework defaults to a different execution context, this must be corrected before any tool logic is written.
4. **[REVISED — iteration 2 — Governance rejection, cross-scope Application Access gap]** Confirm or create the cross-scope Application Access privilege granting `x_u4_partner_case_summary` read access to `sn_customerservice_case` and the account table (`customer_account` or the CSM account table in use) before Tool 1/Tool 2 development starts. This is a distinct security layer from row-level ACLs (§5) — ACL correctness is irrelevant if the cross-scope table-access grant isn't in place first; without it, Tool 1/Tool 2 would silently return zero rows regardless of ACL correctness, presenting as a runtime bug rather than a governance gap. Check: open each table's Application Access record (System Definition > Tables, "Accessible from" field) — if set to "This application scope only," either (a) change it to "All application scopes" if that's an acceptable platform-wide change for CSM (confirm with the table's owning team before doing this, since it affects every scoped app on the instance, not just this one), or (b) leave it restricted and instead create a `sys_scope_privilege` record scoped specifically to `x_u4_partner_case_summary` granting read-only access to that table's API. **Option (b) is preferred** — it grants access to this app only, without loosening the target table's access posture for every other scoped app on the instance. Record which option was used and why, for each of the two tables (`sn_customerservice_case`, account table).

### Build Order
1. Create scoped app `x_u4_partner_case_summary`.
2. Create table `x_u4_partner_case_summary_audit_log` with fields per §3.
3. Create role `x_u4_partner_case_summary.agent_user` (no table ACL changes on `sn_customerservice_case` — see §6).
4. Assign the role directly to the 5 named `sys_user` records.
5. Create ACL(s) on `x_u4_partner_case_summary_audit_log`: read restricted to admin/app-admin only.
6. **[REVISED — iteration 2 — Governance rejection, cross-scope Application Access gap]** Create the `sys_scope_privilege` record(s) granting `x_u4_partner_case_summary` read-only access to `sn_customerservice_case` and the account table, per pre-build verification step 4's option (b) — must exist before step 9/10 (Tool 1/Tool 2) or those tools will silently return zero rows.
7. Create system properties (see table below).
8. Create Script Include `PartnerCaseSummaryUtil` with the three methods in §5 (build `getCaseSummaryData` first — it's the dependency for both tools and for account-flow per-case summarization).
9. Create AI Agent `Partner Case Summary Agent` in scope, gated by `x_u4_partner_case_summary.agent_user` for invocation.
10. Create Tool 1 "Get Case Summary" — wraps `getCaseSummaryData`. Depends on step 6's cross-scope privilege being in place.
11. Create Tool 2 "Get Active Cases for Account" — wraps `getActiveCasesForAccount`, reuses Tool 1's per-case data shape. Depends on step 6's cross-scope privilege being in place.
12. Write agent instructions: tool-routing logic (case number pattern → Tool 1; account/company name phrasing → Tool 2), summarization grounding rules (2-3 lines: status/next steps/blockers, derived only from fetched fields, no fabrication), disambiguation behavior for ambiguous account names.
13. Attach primary surface per §7 pre-build verification outcome: NAP conversation (preferred) and/or VA topic.
14. Build the Agent Workspace UI action (secondary path always, primary fallback if NAP/VA unavailable) on `sn_customerservice_case`, visible only to role holders.
15. Wire `logInvocation` calls into both tool paths (success and not-found/denied cases both log).
16. Package update sets per component (see below), test in sub-prod with `andreea.ionescu@unit4.com`.

### Update sets (import order)
- `Partner Case Summary Agent — Scope and Roles` (app scope, role, role assignment, audit table + ACL, **cross-scope `sys_scope_privilege` record(s) — see pre-build step 4 / build step 6**)
- `Partner Case Summary Agent — Script Include and Properties`
- `Partner Case Summary Agent — Agent and Tools`
- `Partner Case Summary Agent — Surfacing` (NAP/VA config and/or UI action, per §7 outcome)

### Per Component

#### Script Include: `PartnerCaseSummaryUtil`
- Type: Script Include
- Table: N/A (utility)
- Scope: `x_u4_partner_case_summary`
- Dependencies: none (build first among app logic)
- Logic: see §5. No write methods. No ACL bypass of any kind.

#### Tool 1: Get Case Summary
- Type: AI Agent Tool
- Dependencies: `PartnerCaseSummaryUtil.getCaseSummaryData`
- Input/Output: see §4

#### Tool 2: Get Active Cases for Account
- Type: AI Agent Tool
- Dependencies: Tool 1's data shape, `PartnerCaseSummaryUtil.getActiveCasesForAccount`
- Input/Output: see §4

#### AI Agent: Partner Case Summary Agent
- Type: Now Assist ReAct AI Agent
- Dependencies: both tools, role `x_u4_partner_case_summary.agent_user`
- Scope: `x_u4_partner_case_summary`

#### Role: `x_u4_partner_case_summary.agent_user`
- Type: Role
- Dependencies: none
- Note: gates agent invocation only, not table-level read (§6)

#### Table: `x_u4_partner_case_summary_audit_log`
- Type: Table + ACL
- Dependencies: none
- Fields: see §3

### System Properties

| Property | Default | Purpose |
|---|---|---|
| `x_u4_partner_case_summary.max_cases_per_account_summary` | 25 | Cap on Tool 2 result set (`setLimit()`) |
| `x_u4_partner_case_summary.worknote_lookback_count` | 5 | How many recent journal entries feed summarization grounding |
| `x_u4_partner_case_summary.account_match_mode` | `exact_then_startswith` | Account name resolution strategy |

---

## 10. Dependencies

- Depends on the Now Assist / AI Agent framework already active on this instance (confirmed likely present, since PCCC runs on it — §9 step 1 verifies rather than assumes).
- Depends on `sn_customerservice_case`'s existing ACL configuration being correct and complete already — this design adds no case-level ACLs and relies entirely on what's already governing case visibility today, **provided §5's `GlideRecordSecure()` fix (D4) is applied** — plain `GlideRecord` in a scoped-app Script Include does not inherit this automatically.
- No dependency on PCCC's components — separate scope, separate Script Include, no shared code. Comparison in this document is for consistency/convention only, not a build dependency.

---

## 17. Changelog

### 2026-08-11 (later same day) — v4 prompt package: back to three tools, summarization moved in-loop
- [[partner-case-summary-agent-prompt-package]] revised to v4: the standalone `GetBulkCasesSummarization` tool introduced in v3 is removed. Per-case `TaskSummarize` calls now happen inside Get Active Cases from Account's own query loop, returned per case as a `resume` field — three tools total, not four.
- Defect register reset against the current script: new D1 (`ReferenceError` on undefined `rec` — leftover from an earlier `forEach` implementation, blocks every account with active cases), D3 (empty table name, Search Account only — Get Active Cases from Account's own table-name defect from v3 is fixed), D4 (unguarded `JSON.parse` — same shape as v3's D5, renumbered), D5/D6 (performance/config, same substance as v3's D6/D7). The v3 ACL defect carries forward unchanged, renumbered **D2** (was D4) — still the single most load-bearing open issue.
- Architecture §4/§5 callouts and this changelog updated to reference D2 (not D4) and three tools (not four) accordingly.

### 2026-08-11 — v3 prompt package landed; tool count 2→4; ACL claim in §5 corrected
- Full canonical agent prompt (name/description/role/instructions), memory-variable table, and four tool contracts landed in a new companion note: [[partner-case-summary-agent-prompt-package]]. §4 above (2-tool design) is superseded — kept for its original rationale, not as the build target.
- **Regression/correction found while reconciling this doc against the prompt package:** §5's core claim that plain `GlideRecord` "automatically" enforces the invoking user's ACLs is **false for scoped-app Script Includes** — confirmed as defect D4 in the prompt package. Both query methods need `GlideRecordSecure()`. This was an unverified assumption in the original design, not a regression from a prior working state (nothing has been built yet), but it is the single most load-bearing security claim in the document and it does not hold as written.
- Account-level summarization moved from "the agent does per-case LLM reasoning over tool-returned data" (original §4 Tool 2 design) to a dedicated `GetBulkCasesSummarization` tool wrapping `sn_uxc_gen_ai.TaskSummarize` — a genuinely different data flow, not just a rename. Six more defects (D1, D2, D3, D5, D6, D7) catalogued in the prompt package, three of them (D1-D3) blocking on the account path.
- Test plan impact and open items (O1-O5) tracked in the prompt package rather than duplicated here — see that note's §10/§11.
