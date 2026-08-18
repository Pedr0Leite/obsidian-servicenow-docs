---
aliases: [Applications Index]
area: applications-index
tags: [index, routing, custom-app]
---

# Applications INDEX — in-house builds

Everything we designed or built ourselves. **This is the layer that answers "has
this been solved before?"** — architecture, data models, decisions, known debt.

Convention: `Applications/<app>/<app>.md` is the overview note; supporting notes
(backlog, test plan, architecture variants) sit beside it. `wiki/entities/<app>.md`
is a thin pointer back here, never a copy.

## Applications

### [[capacity-planner]] — Capacity Management Overview
**Status: built and deployed.** Scoped app `x_u4bsh_capmgmt`, Now SDK (Fluent),
`@servicenow/sdk` 4.8.0. Plans projects/BAU against team capacity in FTE across
the year. Vanilla-JS SPA at `x_u4bsh_capmgmt_planner.do` + Scripted REST API.

| Note | What it covers |
|---|---|
| `capacity-planner.md` | Overview, data model (5 tables), business logic, REST surface, frontend, deployment, **§12 known issues / architectural debt** |
| `capacity-planner-backlog-2026-07.md` | Open backlog as of 2026-07 |
| `capacity-planner-future-analysis.md` | Open business questions needing sign-off |
| `capacity-planner-set-start-and-end-date-to-plan-items.md` | Date derivation behaviour |
| `generate-capacity-plan-items.md` | Plan item generation |

**Read §12 before building anything new in ServiceNow.** It is the best record of
what goes wrong here: N+1 GlideRecord patterns, an inactive business rule that
silently stopped propagating, the SDK skipping `sys_properties` rows with
placeholder sys_ids, and `.list` URLs failing in the Next Experience shell.

### [[erp-crm-360|erp-crm-360]] — ERP/CRM 360
**Status: brainstorm / brief only. Not built.** Custom scoped app (proposed
`x_u4bsh_erpcrm`) to surface Unit4 ERP financial context inside CSM/ITSM records,
plus an ERP integration control tower. React UI via Fluent `UiPage`.

| Note | What it covers |
|---|---|
| `erp-crm-360-brief.md` | Full build brief: licensing map, five-layer architecture, remote-tables design, data model, React UI, Comp AI conversion, agent assignments, phase gates, **Appendix A (now-sdk setup)** |

Key decisions recorded there: no Source-to-Pay entitlement so the Store ERP
Integration Framework is rebuilt; IntegrationHub **is** available (23 ERP flows
already run on `unit4dev1`); Zero Copy Connector for ERP may replace two layers
and must be evaluated first. Pairs with `other-applications/unit4-erp/`.

### [[partner-case-summary-agent]] — Partner Case Summary Agent
**Status: proposed, not built.** Now Assist AI Agent for Partner Managers to
summarize `sn_customerservice_case` records from natural language, without list
navigation.

| Note | What it covers |
|---|---|
| `partner-case-summary-agent.md` | Story and acceptance criteria |
| `partner-case-summary-agent-architecture.md` | Technical design |
| `partner-case-summary-agent-test-plan.md` | Test plan traced to ACs |
| `change-manifest.md` | Governance change manifest |

### [[sn-instance-scan]] — ServiceNow Instance Scan
**Status: deployed 2026-07-22**, v3 instance-assessment extension implemented.
Scoped app that walks `sys_db_object` with an ACL fallback to inventory an
instance. Useful for enumerating flows, transform maps and Scripted REST APIs
rather than reading them by hand.

| Note | What it covers |
|---|---|
| `architecture.md` / `architecture-v2.md` | Design, v1 and v2 |
| `test-plan.md` | Test plan |
| `reusable-prompt-to-process-scan-results.md` | Prompt for processing scan output |
| `ServiceNow-Instance-Architecture-Assessment-example.md` | Worked example output |

## Related

- Custom solutions built inside the vendor docs tree live at
  `ServiceNowOfficialDocs/custom-solutions/` — notably
  `proactive-customer-case-communicator/` (PCCC), a live Now Assist AI Agent with
  ATF suites and a runbook.
- Generated code graphs: `graphify/capacity-planner/`, `graphify/sn-instance-scan/`
- Agent definitions that build these: `ClaudeAgents/README.md`
