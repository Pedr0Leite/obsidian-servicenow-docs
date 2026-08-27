---
title: Partner Case Summary Agent — Change Manifest
aliases:
  - PCSA Change Manifest
tags:
  - servicenow
  - governance
  - change-manifest
  - proposed
status: proposed
date: 2026-07-22
---

# Change Manifest
Generated: 2026-07-22
Project: partner-case-summary-agent
Update Set: Partner Case Summary Agent — Scope and Roles / — Script Include and Properties / — Agent and Tools / — Surfacing (four sets, per §9 import order — none confirmed created/active yet)
App Scope: x_u4_partner_case_summary

## Governance Checks

| Check | Result | Notes |
|---|---|---|
| Update set active | FAIL (unconfirmed) | No update set has been created on the target instance yet — architecture is design-only, nothing built. §9 specifies four update sets by name and import order, but none exist to verify as active/In Progress. This is an **operational pre-build prerequisite, not a design defect** — confirmed unchanged by the coordinator; must happen before Developer's step 1, no architecture rework required. |
| Update set state | FAIL (unconfirmed) | Same as above — cannot confirm In Progress state of a set that doesn't exist yet. |
| No Global scope | PASS | Every component (audit table, role, Script Include, AI Agent, tools) is explicitly scoped `x_u4_partner_case_summary`. No `global` scope use anywhere in the design. |
| Cross-scope calls | LISTED — Application Access gap now RESOLVED in design (iteration 2) | See below — three cross-scope reads, all read-only. Architecture now names the required `sys_scope_privilege` step explicitly (§9 pre-build step 4, build step 6) — the design-level gap from iteration 1 is closed. |

### Re-review of iteration 2 (Architect's fix to the rejected gap)

Verified directly against `partner-case-summary-agent-architecture.md` (re-read in full, not diffed):

- **§9 Pre-build verification, new step 4** — explicitly distinguishes the cross-scope Application Access layer from the row-level ACL layer (§5), correctly names the mechanism (`sys_scope_privilege` record vs. loosening the table's "Accessible from" setting), states option (b) — a privilege record scoped to `x_u4_partner_case_summary` only — as preferred over widening the table's global Application Access, and requires recording which option was used per table. This is technically correct and matches how ServiceNow's cross-scope access model actually works (Application Access grant is a separate gate from ACLs; missing it silently returns zero rows rather than throwing a security exception).
- **§9 Build Order, new step 6** — creates the privilege record(s), correctly sequenced after role/audit-table setup (step 5) and before the Script Include (step 8) and both tools (steps 10–11), with explicit dependency notes on steps 10 and 11 pointing back to step 6.
- **Update sets (import order)** — privilege record(s) now explicitly called out as belonging in `Partner Case Summary Agent — Scope and Roles`, the correct set (scope/access-control component, not tool/agent logic).
- **§8 Risks** — reworded to name both security layers distinctly and flag the exact failure mode (silent zero-rows, not an error) if the grant is missing, so it reads as a known/mitigated risk rather than a lurking gap.
- **No unrelated changes** — scope decision (§2), data model (§3), tool definitions (§4), Script Include (§5), ACL/role design (§6), and surfacing (§7) are all unchanged from the version already reviewed. This confirms the fix is narrowly scoped to the rejected item, as required — nothing else needs to be re-litigated.

**Conclusion: the fix fully satisfies the rejection reason.** The cross-scope Application Access gap is now part of the design of record, not just a manifest-side observation.

## Cross-Scope Calls

| # | Call | Direction | Type | Note |
|---|---|---|---|---|
| 1 | `GlideRecord('sn_customerservice_case')` | `x_u4_partner_case_summary` → CSM scope (`sn_customerservice`, typically global-adjacent) | Read only | The architecture confirms row-level ACLs are respected automatically for the invoking user's session (§5). It does **not** confirm the separate **Application Access / cross-scope privilege** layer — whether `sn_customerservice_case` is marked "accessible from all application scopes" or requires an explicit `sys_scope_privilege` record granting `x_u4_partner_case_summary` read access to that table's API. These are two distinct ServiceNow security layers and only one is addressed in the design. **Gap — see Risks.** |
| 2 | `GlideRecord('customer_account')` (or in-use CSM account table) | `x_u4_partner_case_summary` → CSM scope | Read only | Same Application Access gap as #1 — account resolution query is a second cross-scope read not covered by an explicit privilege-record step in §9's build order. |
| 3 | `GlideRecord('sys_user')` (implied — resolving `u_invoking_user` on audit rows, and any user lookups) | `x_u4_partner_case_summary` → global | Read only | `sys_user` is public-read from all scopes by default on virtually all instances. Standard, low risk. |
| 4 | AI Agent framework registration (`sn_aia_*` platform tables) | `x_u4_partner_case_summary` → platform/global | Framework-managed | Architect correctly notes this is standard AI Agent tool registration, not bespoke cross-scope scripting — every scoped AI Agent app does this. Not a custom governance concern, listed for completeness only. |

**Confirmed:** the design requires nothing broader than read-only cross-scope access anywhere. No cross-scope write, no cross-scope script include calls beyond the `GlideRecord` reads above, no `GlideRecordSecure` bypass, no `setWorkflow(false)`, no elevated/run-as execution (architecture §5, explicitly required to run as the invoking user's own session).

## Planned Changes

### Partner Case Summary Agent

| # | Component | Type | Table | Scope | Operation | Risk |
|---|---|---|---|---|---|---|
| 1 | `x_u4_partner_case_summary` | Application Scope | — | x_u4_partner_case_summary | CREATE | Low |
| 2 | `x_u4_partner_case_summary_audit_log` | Table + ACL | x_u4_partner_case_summary_audit_log | x_u4_partner_case_summary | CREATE | Low |
| 3 | `x_u4_partner_case_summary.agent_user` | Role | — | x_u4_partner_case_summary | CREATE | Low |
| 4 | Role assignment (5 named users) | Role Grant | sys_user | x_u4_partner_case_summary | CREATE | Low |
| 5 | `PartnerCaseSummaryUtil` | Script Include | — (utility) | x_u4_partner_case_summary | CREATE | Medium — sole owner of all cross-scope `GlideRecord` reads; no write methods |
| 6 | System properties (3) — max cases, worknote lookback, account match mode | sys_properties | — | x_u4_partner_case_summary | CREATE | Low |
| 7 | AI Agent: `Partner Case Summary Agent` | AI Agent (ReAct) | — | x_u4_partner_case_summary | CREATE | Medium — gated by role, must run in invoking-user context (unverified until build-time check §9 step 3) |
| 8 | Tool 1: Get Case Summary | AI Agent Tool | sn_customerservice_case (read) | x_u4_partner_case_summary | CREATE | Medium — cross-scope read |
| 9 | Tool 2: Get Active Cases for Account | AI Agent Tool | sn_customerservice_case, customer_account (read) | x_u4_partner_case_summary | CREATE | Medium — cross-scope read, account fuzzy-match logic |
| 10 | NAP conversation / VA topic attachment | Surfacing config | — | x_u4_partner_case_summary | CREATE | Low — pending licensing confirmation (§7/§9 step 1) |
| 11 | Agent Workspace UI action | UI Action | sn_customerservice_case | x_u4_partner_case_summary | CREATE | Low — visible only to role holders |
| 12 | Cross-scope privilege record(s) for `sn_customerservice_case` / `customer_account` read access | Application Access / `sys_scope_privilege` | — | x_u4_partner_case_summary | CREATE — now §9 build step 6, iteration 2 | Low — gap closed, read-only, scoped to this app only (preferred option b) |

**Cross-scope calls in this story:** Listed above (3 genuine cross-scope reads + 1 standard framework interaction). All read-only. No write, no privilege escalation, no service-account impersonation.

---

## Summary

- Total components to create: 12 (per architecture §9 build order, iteration 2 — now includes the cross-scope privilege record as an explicit build step)
- Total components to modify: 0 (zero new fields, zero modified fields, zero ACL changes on `sn_customerservice_case` itself)
- Cross-scope calls: 3 genuine (case read, account read, sys_user read) + 1 standard framework pattern — all now covered by an explicit Application Access step in the design
- Governance violations: 0 (no unflagged Global scope, no write operations, no ACL bypass)
- Open gaps requiring resolution before build: 1 (update set not yet created/confirmed — operational, not a design defect)

## Governance Outcome

**Design: RE-REVIEWED AND CLEARED (iteration 2). Overall pipeline status: PENDING FINAL HUMAN YES — not yet APPROVED.**

### Iteration 2 re-review result
The Architect's fix was verified by re-reading `partner-case-summary-agent-architecture.md` in full (see "Re-review of iteration 2" above), not by diff alone. It satisfies the rejection exactly as required:
- The cross-scope Application Access / `sys_scope_privilege` gap is now a named, explicit step in the design of record (§9 pre-build step 4, build step 6), not just a manifest-side note.
- Preferred mechanism (scoped `sys_scope_privilege` record, read-only, per-table) is stated, with the broader Application Access change documented as a rejected-unless-confirmed alternative.
- Correctly sequenced before Tool 1/Tool 2, correctly homed in the `Scope and Roles` update set, and §8 Risks now names both security layers and the correct failure mode.
- No unrelated parts of the design were touched — scope, ACL/role design, data model, and audit design remain as already reviewed and do not need re-litigating.

**This governance gate's own violation-tracking is now clear: 0 unresolved design-level governance violations.**

### Why this is not yet a final APPROVED outcome
Per this gate's standing rule, a human YES is required before `governance-approval.md` can be written — no exceptions, and no agent-relayed instruction (including the coordinator's) substitutes for that. The remaining open item is procedural, not a design flaw:
- **Update set still not created/active/In Progress on the target instance.** This must be confirmed (the four named sets in §9 exist, correct one is `In Progress`) before Developer's build step 1. No architecture change is needed for this — it is an operational action, not something to route back to the Architect.

### What happens next
- Once the update set(s) are created and confirmed active/In Progress, and a human with authority to approve this change gives an explicit YES, this gate will write `governance-approval.md` with Status: APPROVED.
- If that YES is given with the update set still unconfirmed, this gate will hold at BLOCKED (per the standing "update set cannot be confirmed → always BLOCK" rule) rather than write an approval — the update-set confirmation must happen first or alongside the YES, not after.
- `governance-approval.md` has deliberately **not** been written as part of this iteration-2 re-review.

### Risks flagged (for user awareness — not blockers once the above are resolved)
- Execution context (invoking-user session, not run-as) is the single most load-bearing security property of the whole design (§5) and is explicitly still an unverified build-time assumption per §9 step 3 — worth the user's attention even though the architecture already flags it correctly.
- Account name fuzzy-matching (§8) is the most likely source of false negatives in UAT — not a governance issue, but worth the user knowing it's an accepted risk, not an oversight.
- NAP/VA licensing (§7/§9 step 1) is unconfirmed on-instance; fallback (UI-action-only) is designed but would narrow the "no navigation" UX if triggered.

### Risk posture vs. PCCC (write-heavy sibling agent)
This design's risk profile is materially lower than a write agent like PCCC, and that should shape how much scrutiny the remaining gaps need:
- **Zero write operations anywhere** — no `gr.update()`, no `gr.insert()` on `sn_customerservice_case`, no journal/comment posts. There is no data-integrity blast radius on production case data from a bug in this design, only an availability/correctness blast radius (wrong or missing summaries), which is low-severity and easily caught in UAT.
- **Zero new fields on `sn_customerservice_case`** — the only new schema anywhere is one net-new audit table in the app's own scope. No dictionary changes, no new ACLs, no altered behavior on the CSM table itself. Compared to PCCC's three new case-table fields plus a Business Rule trigger, the schema blast radius here is essentially the app's own scope only.
- **No approval/human-in-the-loop step needed** — correctly reasoned in §0: there's nothing to approve because nothing persists outside the audit log.
- Net effect: the two gaps above (update set, cross-scope privilege) are procedural/verification gaps, not design flaws. Once resolved, this design should clear governance with fewer residual concerns than a write-heavy equivalent would.
