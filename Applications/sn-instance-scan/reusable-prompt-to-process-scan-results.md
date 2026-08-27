# Reusable prompt — ServiceNow instance architecture from sn-instance-scan reports

Attach the sn-instance-scan PDF(s) and paste everything below the line.

---

Act as a ServiceNow Certified Technical Architect. Attached are one or more
`sn-instance-scan` run reports for a client instance. Reconstruct and document that
instance's architecture, then produce a client-ready assessment.

## 1. Extract before you interpret

Parse every attached PDF programmatically (pdfplumber or equivalent) — do not skim.
Extract, per report:

- Run header: scan mode, status, started/completed, requested_by, apps scanned.
- Scan findings log verbatim.
- For `custom_only` / `full_access` runs, per application:
  scope name, vendor, artifact inventory with counts AND the named artifacts
  (script includes, business rules, flows, ACLs, UI actions, UI policies, client
  scripts, scheduled jobs, scripted REST, notifications, SLA definitions, catalog
  items, ATF tests, fix scripts, processors, portals/widgets, import sets);
  the full data model (each table: extends, well-known base, row count, field list
  with types, dictionary overrides, inbound reference count); the outbound
  reference graph; base-system tables the app customises but does not own; the
  cross-reference table.
- For `modules` runs: the complete `sys_plugins` table — plugin display name, plugin
  ID, active in sys_plugins, confirmed active, status mismatch. Report the row count
  you parsed and reconcile it against the count in the findings log; state the delta
  if any (table rows split across page breaks get dropped).

Persist the parsed data (e.g. JSON) before analysing it.

## 2. Derive the capability footprint from anchor plugins

Do NOT keyword-count. For each suite, decide Active / Foundation-only / Absent by
checking named anchor plugins, and cite the anchors you found:

| Suite | Anchor examples |
|---|---|
| ITSM | `com.snc.problem`, `com.snc.change_management`, `com.snc.best_practice.incident.*`, `com.snc.knowledge_advanced` |
| Request | `com.glideapp.servicecatalog(.platform/.wizard/.rest.api)` |
| SLM | `com.snc.sla.*` |
| ITAM | `com.snc.asset_management`, `com.snc.sam`, `com.snc.fixed_asset`, `com.snc.contract_management` |
| CMDB/CSDM | `com.snc.cmdb.*`, `com.snc.cmdb.ci_lifecycle_manager`, `com.snc.ng_bsm`, `com.snc.best_practice.itsm_csdm.*` |
| ITOM | `com.glideapp.agent` (MID), `com.snc.discovery`, `com.snc.service_mapping`, `com.glideapp.itom.*`, event mgmt, cloud mgmt |
| HRSD / CSM / FSM | `com.sn_hr_core`, `com.sn_customerservice`, `com.snc.work_management` |
| SecOps / IRM | `com.snc.security_incident`, `com.snc.vul`, `com.sn_grc*` |
| SPM/PPM | `com.snc.project*`, `com.snc.demand*`, `com.snc.sdlc*` (read-role stubs alone ≠ installed) |
| AI | `com.now_assist_core`, `com.glide.ais`, `com.glide.cs*` (Virtual Agent), `com.snc.nlu_studio`, plus any Now Assist skill / AI Agent / Agentic Workflow modules |
| Integration | `com.glide.hub.*` (IntegrationHub), spokes, `com.glide.graphql*`, `com.glide.rest*`, `com.glideapp.ecc` |
| Security | `com.glide.high_security`, `com.glide.acl.service`, `com.snc.platform.security.oauth`, MFA/adaptive auth, `com.glide.sm.*` |
| ALM | `com.glide.automated_testing_framework`, `com.glide.source_control`, `com.glide.system_update_set*`, `com.glide.continuousdelivery`, `com.glide.upgrade_center` |

Explicitly list the suites that are **absent** — absence is a finding.

Also flag: domain separation present/absent; deprecated modules still active;
release-indicating plugins (e.g. `*_x_family` → Xanadu family) and mark the release
as **inferred**.

## 3. Produce three UML views

Render with Graphviz (`dot`) to both PNG at ≥150 dpi and SVG. Keep aspect ratio
under about 2.3:1 so the images stay readable on a landscape page. Use invisible
weighted edges to force vertical layering if a diagram spreads too wide, and do NOT
use `splines=ortho` (it silently drops edge labels).

1. **Deployment diagram** — client tier (browser / mobile / VA web client / email),
   ServiceNow cloud (prod app node, database, search, schedulers, ECC queue),
   sub-production instances, customer network / DMZ (MID Server, LDAP, IdP, on-prem
   sources), external systems (3rd-party APIs, CI/CD, NLU provider). Use UML
   stereotypes («device», «node», «execution environment», «component»). Draw the
   MID Server link as outbound-initiated ECC polling. **Mark everything inferred with
   a dashed border and say so in the legend.**
2. **Component diagram** — capability map in layers: Experience, Application,
   Intelligence & Analytics, Platform Core, Integration, Security & Governance,
   Application Lifecycle. Put each custom scope in as a «custom application»
   component. Include a note box listing what is absent.
3. **Class diagram** — for each custom scope: every table as a UML class with real
   field names and types, stereotypes, row/field counts, aggregation (filled diamond)
   for parent-child, dashed dependencies to platform tables (`sys_app`, `sys_user`,
   `sys_db_object`, `task`, `cmdb_ci`), multiplicities, and a separate compartment
   for the automation surface (script includes, business rules, flows, UI actions,
   ACLs). Add a note box with architectural observations.

## 4. Write the assessment (.docx, English)

Structure — cover page, TOC, then:

1. Executive summary — what the instance is, plus a severity-ranked findings table.
2. Scope, method and confidence — what the scans cover, what they cannot tell you
   (topology, release, licensing, adoption, process config, other scopes), and an
   explicit High / Medium / Inferred confidence statement.
3. Platform baseline — module inventory, activation drift, suite footprint table
   with anchor-plugin evidence, governance posture.
4. Deployment architecture — access channels, instance tier, MID Server hop,
   identity, sub-production and promotion.
5. Capability architecture — where value sits, where the gaps are, automation-stack
   split, the AI layer.
6. Custom application architecture — one subsection per scope: purpose, data model
   table, automation surface, integration points, flagged base-system customisations.
7. Integration architecture.
8. Security and access architecture.
9. Application lifecycle and upgrade readiness.
10. Recommendations — numbered table with recommendation, why, priority.
11. Open questions — everything the scan cannot answer.
- Annex A: the three UML figures on **landscape** pages, with captions.
- Annex B: this prompt.

## 5. Rules

- **Never invent.** Every claim traces to a scan value or a named plugin. If it does
  not, label it `⚠️ Inferred` and say what would confirm it.
- If the data model section says it was unavailable (mode was not `full_access`),
  treat the data model as **UNKNOWN** — do not conclude the app has no tables.
- Activation ≠ adoption. Say so wherever it matters.
- Use correct platform terminology and inline code formatting for table names, field
  names, plugin IDs, scopes and API classes.
- Call out release-dependent behaviour and state the release you are assuming.
- Verify at the end: re-read the extracted data and check every number in the
  document against it. Report any figure you could not confirm.

Deliver: the `.docx`, the three PNG + SVG diagrams, and the Graphviz `.dot` sources.
