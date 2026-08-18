---
aliases: [Wiki Index]
area: wiki-index
tags: [wiki, index]
---
Catalog of the LLM-maintained wiki layer. Read this first when answering a query; drill into linked pages next.

See `wiki/backlinks-log.md` for backlink health-check history.

## Entities (apps, integrations, custom builds)
- [[capacity-planner]] — in-house capacity planning app. Source: `Applications/capacity-planner/`.
- [[sn-instance-scan]] — scoped app that scans a ServiceNow instance (sys_db_object walk + ACL fallback). Deployed 2026-07-22; v3 instance-assessment extension fully implemented — check the repo, not this vault, for current build status.
- [[erp-crm-360]] — proposed scoped app surfacing Unit4 ERP financial context inside CSM/ITSM, plus an ERP integration control tower. Status: brief only, not built. Source: `Applications/erp-crm-360/`.
- [[partner-case-summary-agent]] — proposed Now Assist AI Agent for Partner Managers to summarize `sn_customerservice_case` cases. Status: proposed, not yet built. Source: `Applications/partner-case-summary-agent/`.

## Concepts (core ServiceNow dev topics, synthesized across sources)
- [[acls]] — access control rules, scoped-app ACL patterns.
- [[gliderecord-patterns]] — GlideRecord query/perf idioms.
- [[flow-designer]] — flows, subflows, actions.
- [[scoped-apps]] — scoped app structure, namespacing, packaging.
- [[ai-agents]] — Now Assist AI Agents, ReAct loop, sn_aia_* tables.
- [[ai-search]] — AI Search (AIS), vector/semantic search tuning.
- [[cis]] — CIS (Data Foundations) certification notes.
- [[cta]] — Certified Technical Architect track (weekly notes + capstone).
- [[ciwf]] — domain separation use cases.
- [[cmdb]] — CSDM v5, Process Mining.
- [[integrations]] — REST/SOAP, DevOps, SCCM, Sharepoint, Teams.
- [[integrations-diagrams]] — integration/structure reference diagrams.
- [[email]] — SMTP/IMAP config, Outlook Actionable Messages.
- [[event-management]] — Event Management reference.
- [[frameworks-libraries]] — AngularJS/ReactJS in ServiceNow, EfficientGlideRecord.
- [[install-stuff]] — Engagement Messenger, LDAP, multi-provider SSO.
- [[itom]] — IT Operations Management reference.
- [[knowledge-base-articles]] — personal KB drafts by topic.
- [[logics-and-creations]] — confidential attachments, backup, SSO, upgrades.
- [[mid-server]] — ECC Queue, MID install/commands.
- [[migrations]] — cross-instance/company data migration.
- [[platform-analytics]] — Performance Analytics / metrics.
- [[random-scripts]] — misc script snippets.
- [[roles-per-module]] — role reference by module.
- [[server-client-scripts]] — server/client scripting snippets.
- [[service-catalog]] — Service Catalog reference.
- [[service-portal]] — widgets, portal methods/events.
- [[service-portfolio-management]] — SPM reference.
- [[system-properties]] — Next Experience theme applicability.
- [[tips-and-tricks]] — useful UI Actions.
- [[workspace]] — Workspace UI Actions, App Shell UX, custom app forms.

## Syntheses (cross-cutting write-ups, evolving theses)
- [[genai-prompt-vs-ai-agent]] — when to use a flat GenAI prompt vs a ReAct AI Agent loop.

## Queries (answers filed back from conversations)
- [[catalog-item-prefill-and-modal]] — prefill catalog item variables via URL (`sysparm_variable_values`) vs. opening a catalog item in a Service Portal modal (`spModal.open`) with prefilled data.

## Raw source map
Not wiki pages — where curated/raw material already lives in this vault. The LLM reads from these, never edits them as part of wiki maintenance.

| Location | What |
|---|---|
| `ServiceNowOfficialDocs/` | ~46,000 official ServiceNow docs. Own index: `ServiceNowOfficialDocs/INDEX.md`. |
| `ServiceNowOfficialDocs/now-assist-ai/` | Custom curated Now Assist notes. Own index: `llms.txt`. |
| `Notion/ServiceNow/` | Personal notes, 30 topic folders (AI & VA, CMDB, Flow Designer, Security & ACL, Scripts, CTA, Integrations, etc.) — see `Notion/INDEX.md`. |
| `Applications/` | Notes on in-house custom ServiceNow apps. |
| `chats/code/` | Imported Claude Code session exports. |
| `logs/` | Session logs (`/save` output). |
| `raw/inbox/` | Landing zone for new sources not yet ingested into the wiki. |

All 30 `Notion/ServiceNow/` topic folders are now promoted to concept pages above, except `Notion/ServiceNow/Applications/` (Anonymize Data, Update Set Mover, Update Sets - Full Applications) which is covered under [[scoped-apps]] rather than duplicated, and `Notion/ServiceNow/AI & VA/` and `Scripts/` and `Security & ACL/` which are covered under [[ai-agents]]/[[ai-search]], [[gliderecord-patterns]], and [[acls]] respectively.

New Notion topic folders created after this pass: promote to a concept page (`wiki/concepts/<name>.md`) the first time a query needs to synthesize across it plus another source — don't pre-build stubs for folders nobody has asked about yet.
