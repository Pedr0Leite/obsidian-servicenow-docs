---
aliases: [sn-instance-scan Architecture]
area: application-spec
tags: [scoped-app, application-development, cmdb, acls, ai-agents, spec, architecture]
---

# sn-instance-scan — Architecture

Scope: `x_snis_iscan` (vendor token `snis`, adjust to actual vendor prefix at install)
App name: sn-instance-scan

## Story 1: Scan configuration & scope selection

### Components
- Tables: `x_snis_iscan_run` (scan run header — mode, filters, status)
- Business Rules: none (scan is on-demand, not data-triggered)
- Client Scripts: none required (UI action + Script Include does the work; onClick just calls GlideAjax or triggers async record)
- Script Includes:
  - `IscanAppSelector` — resolves the app list for the 3 scan modes
- Flows: none
- UI: UI Action "Run Scan" on `x_snis_iscan_run` form; list view of `sys_app` filtered when mode = Manual (use a related list / slushbucket variable, not custom UI)
- ACLs: `x_snis_iscan_run` — read/write role `x_snis_iscan.user` (or `admin` only in v1 — flag as decision below)
- Integrations: none

### Scope
- App scope: x_snis_iscan
- Update set: "sn-instance-scan v1 - Scan Engine"

### Dependencies
- None (foundation story)

### Risks / Flags
- DECISION NEEDED: who can run scans? Recommend a dedicated role `x_snis_iscan.scanner` rather than defaulting to admin, so the ACL-fallback path (constraint: "never assume security_admin") actually gets exercised in normal use, not just as a theoretical negative test.
- `sys_app` list for Manual mode can be large on instances with many store apps — use a reference qualifier, not a full unfiltered slushbucket.

---

## Story 2: Custom-only scope filter (source/vendor aware)

### Components
- Tables: reads `sys_app` (OOB)
- Script Includes: `IscanAppSelector.getCustomApps()` — filters `sys_app` where scope starts with configurable prefix AND `vendor`/`source` indicates internal/private (not `store`), per spec requirement to avoid store-installed x_ apps leaking into "custom"
- ACLs: read-only on `sys_app` (OOB, already readable to most roles)

### Scope
- App scope: x_snis_iscan

### Dependencies
- Story 1 (scan run record must exist to hold the resolved app list)

### Risks / Flags
- `sys_app.source` values vary by release (Vancouver+ has cleaner vendor tracking). Verify actual field/value on target instance before hardcoding a condition — build the query with `gs.getProperty()`-driven prefix but keep the source/vendor check as a documented, single-place filter so it's easy to adjust per-instance without code changes elsewhere.

---

## Story 3: Table & field discovery per app (primary path)

### Components
- Tables owned by scanned app — discovered dynamically, not stored as a list; results persisted to `x_snis_iscan_table` (child of `x_snis_iscan_run`)
- Script Includes:
  - `IscanTableScanner.scanApp(appSysId)` — orchestrates steps 2-3 of the algorithm
  - `IscanTableScanner.getOwnedTables(scopeSysId)` — GlideRecord on `sys_db_object` where `sys_scope=scopeSysId`
  - `IscanTableScanner.profileTable(tableName)` — row count (GlideAggregate), field list (sys_dictionary, app-added fields only), reference fields
- ACLs: relies on OOB read ACLs on `sys_db_object`, `sys_dictionary`, and each scanned table — no new ACLs granted by this app (read-only, respects existing access)

### Scope
- App scope: x_snis_iscan

### Dependencies
- Story 1, Story 2

### Risks / Flags
- GlideAggregate COUNT on very large tables (task, cmdb_ci) is cheap but still a full index scan — cap scan to owned custom tables only in practice; OOB base tables are never "owned" by an x_ scope so this is naturally bounded.
- `sys_dictionary` "fields added by this app" = filter `sys_dictionary.sys_scope = app scope` (dictionary entries themselves carry scope for extended fields) — inherited OOB fields don't have rows with that scope, so no extra logic needed to exclude them.

---

## Story 4: ACL-denial fallback via Application Files

### Components
- Script Includes:
  - `IscanTableScanner.canAccessMetadata()` — explicit `new GlideRecord('sys_db_object').canRead()` / `new GlideRecord('sys_dictionary').canRead()` check, called BEFORE attempting primary path (per spec: deterministic check, not caught error)
  - `IscanAppFilesScanner.scanApp(appSysId)` — queries `sys_metadata` where `sys_scope = app` to enumerate script includes, business rules, ACLs, UI actions, flows
- Tables: results still land in `x_snis_iscan_run` / `x_snis_iscan_table`, with `x_snis_iscan_run.scan_mode_used = 'app_files_fallback'`

### Scope
- App scope: x_snis_iscan

### Dependencies
- Story 3 (shares the profile/result tables)

### Risks / Flags
- `sys_metadata` is a big polymorphic table; filtering by `sys_scope` and reading `sys_class_name` to bucket into (script include / business rule / ACL / UI action / flow) is metadata-only, aligns with non-goal "not a static code analyzer."
- This path yields no row counts / field lists (no table access) — write-up must say so explicitly, not silently omit.

---

## Story 5: Architecture summary generation (GenAI)

### Components
- Script Includes:
  - `IscanSummaryGenerator.buildPrompt(runFacts)` — assembles the gathered facts (table names, extends, field types, business rule labels, integration hits) into one prompt
  - `IscanSummaryGenerator.generate(runFacts)` — single call to Generative AI Controller (`sn_one_extend.GenerativeAIInvocationAPI` or equivalent scripted API per instance's Now Assist plugin version), one-shot summarization — explicitly NOT an AI Agent/ReAct loop per spec
- Tables: `x_snis_iscan_run.summary_text` (or child `x_snis_iscan_result` — see Story 6, summary lives there)
- Integrations: Generative AI Controller (internal platform API, not an external REST call)

### Scope
- App scope: x_snis_iscan

### Dependencies
- Story 3 or Story 4 (needs gathered facts first)

### Risks / Flags
- Generative AI Controller availability depends on Now Assist plugin being active on target instance — must degrade gracefully (skip summary, keep structured facts) if the API is absent. Check plugin/table existence, don't hard-fail the whole scan over a missing GenAI capability.
- Keep this optional per spec ("Optionally hand...") — build the structured result table so it's useful with or without the GenAI text.

---

## Story 6: Results table, form, and list view

### Components
- Tables: `x_snis_iscan_result` — one record per scanned app (see schema below)
- UI: list view (app, scan date, scan mode, table count, automation count) and form view (adds summary text, related list to `x_snis_iscan_table`)
- ACLs: `x_snis_iscan_result` read for `x_snis_iscan.user`, write reserved to the Script Include (system-generated)

### Scope
- App scope: x_snis_iscan

### Dependencies
- Stories 3, 4, 5 (this is where their output lands)

### Risks / Flags
- None beyond standard list/form config.

---

## Story 7: ATF coverage

### Components
- ATF test: "Full scan happy path" — custom scope, table access, tables found, result record created, scan_mode_used = 'full_access'
- ATF test: "ACL-denied fallback" — simulate a user without sys_db_object/sys_dictionary read, confirm scan_mode_used = 'app_files_fallback', no exception thrown, result record still created

### Scope
- App scope: x_snis_iscan

### Dependencies
- All prior stories

### Risks / Flags
- ATF "impersonate user" step needs a test user role deliberately excluded from sys_db_object/sys_dictionary read — provision this as ATF test data, not a production role.

---

# Table Schema

## x_snis_iscan_run (scan run header)
| Field | Type | Notes |
|---|---|---|
| scan_mode | Choice | full / custom_only / manual |
| status | Choice | pending / running / complete / error |
| requested_by | Reference (sys_user) | default: current user |
| started | Glide Date/Time | |
| completed | Glide Date/Time | |
| app_count | Integer | apps in scope for this run |
| activities | String (8000) | Progressive milestone log; appended by `_appendActivity()` helper, updated immediately after each append for live form visibility. String (not Journal) — queryable, avoids ACL complications of journal fields. |

## x_snis_iscan_result (one row per scanned app — the primary output table from spec)
| Field | Type | Notes |
|---|---|---|
| run | Reference (x_snis_iscan_run) | |
| app | Reference (sys_app) | |
| scan_date | Glide Date/Time | |
| scan_mode_used | Choice | full_access / app_files_fallback |
| table_count | Integer | |
| business_rule_count | Integer | |
| script_include_count | Integer | |
| flow_count | Integer | |
| acl_count | Integer | |
| ui_action_count | Integer | |
| integration_count | Integer | REST messages / web services referencing this scope |
| table_list | String (4000) or related list | see x_snis_iscan_table for structured version |
| summary_text | String (full text/HTML) | GenAI-generated, optional |

## x_snis_iscan_table (child — table profile, only populated on full-access path)
| Field | Type | Notes |
|---|---|---|
| result | Reference (x_snis_iscan_result) | |
| table_name | String | sys_db_object.name |
| extends_table | String | sys_db_object.super_class.name |
| well_known_base | Choice | task / cmdb_ci / other / none — flagged per spec step 2 |
| row_count | Integer | via GlideAggregate |
| field_count | Integer | app-added fields only |
| reference_field_list | String | comma list of ref fields, for relationship graph |

---

# Dev Instructions

## Build Order
1. Create scoped app `x_snis_iscan` (do not deviate from prefix without explicit sign-off).
2. Create tables in this order (FK dependencies): `x_snis_iscan_run` → `x_snis_iscan_result` → `x_snis_iscan_table`.
3. Create system properties (see Properties list below) before any script references them.
4. Create Script Include `IscanAppSelector` (Story 1/2).
5. Create Script Include `IscanTableScanner` (Story 3/4) — includes the `canAccessMetadata()` gate.
6. Create Script Include `IscanAppFilesScanner` (Story 4).
7. Create Script Include `IscanSummaryGenerator` (Story 5) — build last since it depends on facts shaped by steps 5-6.
8. Create Script Include `IscanScanOrchestrator` — top-level entry point the UI Action calls; wires 4-7 together per app, writes `x_snis_iscan_result`/`x_snis_iscan_table`.
9. Create UI Action "Run Scan" on `x_snis_iscan_run` (calls orchestrator via GlideAjax, async — do not run scan synchronously in UI Action for full/custom scans, only reasonable for a single manual app to avoid browser timeout on large instances).
10. Create list/form views for all three tables.
11. Create ACLs (read on result/table for scanner role; no write ACLs beyond system).
12. Write ATF tests.

## System Properties (use gs.getProperty(), never hardcode)
- `x_snis_iscan.custom_scope_prefix` — default `x_`
- `x_snis_iscan.row_count_timeout_ms` — GlideAggregate safety threshold, default 5000
- `x_snis_iscan.genai_enabled` — true/false, default true (auto-disables gracefully if API absent regardless)

## Per Component

#### IscanAppSelector
- Type: Script Include (client callable: false)
- Table: reads sys_app
- Methods:
  - `getFullScanApps()` — GlideRecord sys_app, no filter, return array of sys_ids
  - `getCustomApps()` — GlideRecord sys_app where `scope STARTSWITH gs.getProperty('x_snis_iscan.custom_scope_prefix')` AND `source` (or `vendor`) indicates internal — check actual field name/values on target instance during build (Vancouver+: `sys_app.source`; older: may need `sys_store_app` absence check as the internal/private signal instead — verify, don't assume)
  - `getManualApps(sysIdArray)` — validate each sys_id is a real sys_app record (isValidRecord pattern) before returning
- Scope: x_snis_iscan
- Dependencies: x_snis_iscan_run table must exist

#### IscanTableScanner
- Type: Script Include
- Table: sys_db_object, sys_dictionary, target scanned tables (dynamic)
- Methods:
  - `canAccessMetadata()` → boolean. Logic: `new GlideRecord('sys_db_object').canRead() && new GlideRecord('sys_dictionary').canRead()`. Called by orchestrator BEFORE any query — this is the deterministic gate from the spec, not a try/catch.
  - `getOwnedTables(appScopeSysId)` → array of {name, extends, well_known_base}. GlideRecord sys_db_object where sys_scope = appScopeSysId. For well_known_base: walk super_class chain (or check `sys_db_object.super_class.name` directly, single level is enough per "flag tables that extend task/cmdb_ci/other well-known bases" — don't build a full inheritance walker unless a table extends an intermediate custom table that itself extends task; handle that by following super_class up to 3 levels max, stop early).
  - `profileTable(tableName)` → {row_count, fields[], reference_fields[]}. row_count via `new GlideAggregate(tableName); ga.addAggregate('COUNT'); ga.query();` — never `GlideRecord.getRowCount()` per spec. fields via GlideRecord sys_dictionary where name=tableName AND sys_scope = app scope (this naturally excludes inherited OOB fields, no extra filtering logic needed). reference_fields = subset of fields where internal_type = 'reference', capture `reference` (target table) for the relationship graph.
- Scope: x_snis_iscan
- Dependencies: none beyond OOB tables (read-only, uses caller's own access — no elevated privilege)

#### IscanAppFilesScanner
- Type: Script Include
- Table: sys_metadata
- Methods:
  - `scanApp(appScopeSysId)` → {script_includes[], business_rules[], acls[], ui_actions[], flows[]}. Single GlideRecord query on sys_metadata where sys_scope = appScopeSysId, bucket by `sys_class_name` (sys_script_include, sys_script, sys_security_acl, sys_ui_action, sys_hub_flow). One query + in-memory bucketing, not 5 separate queries — sys_metadata is the shared base table so a single pass works.
- Scope: x_snis_iscan
- Dependencies: none

#### IscanSummaryGenerator
- Type: Script Include
- Methods:
  - `buildPrompt(facts)` → string. Plain string template: app name, table list w/ extends, business rule/flow/script include counts, integration hits. Keep it a single flat prompt — this is a summarization task per spec, no chaining.
  - `generate(facts)` → string or null. Checks GenAI Controller availability first (e.g. does the invocation API/table exist — instance-version dependent, verify exact API name against target instance's Now Assist plugin during build); if unavailable or `x_snis_iscan.genai_enabled` is false, return null and let orchestrator store facts without summary_text.
- Scope: x_snis_iscan
- Dependencies: IscanTableScanner and/or IscanAppFilesScanner output (facts must be assembled first)

#### IscanScanOrchestrator
- Type: Script Include (client callable: true, this is what the UI Action's GlideAjax calls)
- Methods:
  - `runScan(scanMode, manualAppList)` — creates x_snis_iscan_run, resolves app list via IscanAppSelector, loops apps: canAccessMetadata() → true: IscanTableScanner path, writes x_snis_iscan_table rows, scan_mode_used='full_access'; false: IscanAppFilesScanner path, scan_mode_used='app_files_fallback'. Either way, assembles facts, calls IscanSummaryGenerator.generate(), writes one x_snis_iscan_result row per app. Updates run.status/completed at the end.
- Scope: x_snis_iscan
- Dependencies: all above Script Includes

#### UI Action "Run Scan"
- Table: x_snis_iscan_run
- Type: form button, client=true, uses GlideAjax to call IscanScanOrchestrator.runScan() async (show a "scan running" message, don't block the UI thread on large instances)
- Scope: x_snis_iscan

## ACLs
| Table | Op | Role | Condition |
|---|---|---|---|
| x_snis_iscan_run | read/create | x_snis_iscan.scanner | none |
| x_snis_iscan_result | read | x_snis_iscan.scanner | none |
| x_snis_iscan_result | write | none (system only via script) | script sets via Script Include running as the requesting user, not elevated |
| x_snis_iscan_table | read | x_snis_iscan.scanner | none |
| sys_db_object, sys_dictionary, scanned tables | read | (unchanged, OOB) | app relies on requesting user's existing access, grants nothing new |

Note: no ACL in this app should grant broader table access than the user already has — the whole design is "scan under caller's access, fall back cleanly when denied," so the app's own ACLs only gate the *result* tables, never the scanned tables.

## Implementation Decisions (2026-07-15)

### Client-side GlideAjax fix
`RunScan.client.js` originally used `new global.GlideAjax(...)` — `global` is undefined client-side (Rhino doesn't expose it), causing a silent ReferenceError and the "Run Scan" button doing nothing. Fixed to `new GlideAjax('IscanScanOrchestrator')`.

### Progressive activity logging (`scan_findings` field)
`_appendActivity(run, message)` helper in `IscanScanOrchestrator`:
- Prepends `gs.now()` timestamp + message + newline
- Calls `run.update()` immediately after each append for live form visibility without waiting for scan completion

**Field rename (2026-07-22):** `activities` renamed to `scan_findings` across the entire codebase — original name was misleading. Both `scan_findings` (plain String, queryable, ACL-free) and `comments` (Journal) are kept populated; they serve different purposes.

**Journal field bug (found and fixed 2026-07-22):** The `comments` Journal field was silently dropping all appends after the first because the same `GlideRecord` instance was reused across all `_appendActivity()` calls. Fix: re-query a fresh record per journal write. See [[gliderecord-patterns]] for the general pattern.

### Verbose logging additions
Added `gs.info/warn/error` calls across all six script includes:
- `IscanAppSelector` — app count resolution and which mode resolved how many apps
- `IscanTableScanner` — per-app scan mode selection, table profile counts
- `IscanAppFilesScanner` — file count per type (script includes, BRs, ACLs, flows, UI actions)
- `IscanSummaryGenerator` — GenAI availability check, prompt size, output length
- `IscanScanOrchestrator` — scan start/end, per-app timing, error paths
- `IscanReportGenerator` — PDF generation steps

Build (`now-sdk build`) passes cleanly with all additions — confirmed 2026-07-15. Not yet deployed to any instance; next step is deploying and verifying button fix + activity field live.

Source: [[raw/sessions/2026-07-15#Session 16:58 — sn-instance-scan]]

## Debugging Notes (2026-07-20)

### Execute ACL on `IscanScanOrchestrator` blocking GlideAjax

**Symptom:** "Run Scan" button returned "No response from the scan service" with zero server-side logs — not even the first `gs.info` at the top of `IscanScanOrchestrator.runScanAjax` fired.

**Root cause:** Zero logs at the method entry point means the Script Include body never ran — this is the fingerprint of an execute ACL denial, not a code error. The execute ACL for `IscanScanOrchestrator` grants only to `x_335329_iscan.scanner`; the user was `admin` but not a member of that role.

**Update (session 21:33):** User confirmed calling user is `admin`. Since admin bypasses ACL evaluation entirely, the execute ACL hypothesis is eliminated. With admin producing zero server logs, the request likely never left the browser — the problem is client-side.

**Next diagnostic step (pending):** Open browser DevTools on the form, click "Run Scan", and check:
1. **Console** — any JS error before/during the click handler (e.g. `runScanAsync is not defined`).
2. **Network** (filter: `xmlhttp.do`) — confirm whether a POST with `sysparm_processor=x_335329_iscan.IscanScanOrchestrator` and `sysparm_name=runScanAjax` is actually sent; inspect response body if so.

**Status (2026-07-20):** Unresolved — awaiting DevTools results.

Sources: [[raw/sessions/2026-07-20#Session 21:28 — sn-instance-scan]], [[raw/sessions/2026-07-20#Session 21:33 — sn-instance-scan]]

---

## Known Gap: global-scope customizations on base-system tables (identified 2026-07-22)

The v3 instance-assessment extension counts artifacts scoped to each app. This misses a category of customization that is common in real instances: **customer-owned artifacts that target OOB/base-system tables** — e.g. custom fields with `u_` or `x_*_` prefix added to `incident`, `sc_request`, etc., or customer-scoped Business Rules / ACLs / UI Policies whose `name` (sys_scope) is a customer scope but whose `table_name` is an OOB table.

Counting only by `sys_scope = appScopeSysId` on OOB tables produces a zero count (those tables' scope is `global`), hiding all customizations applied to them.

Proposed extension: a separate "customizations on base-system tables" section that queries:
- `sys_dictionary` where `internal_type` = `string`/etc. AND `element` STARTSWITH `u_` or `x_` AND `name` (table) is an OOB table
- `sys_script` (Business Rules), `sys_security_acl` (ACLs), `sys_ui_policy`, etc. where `sys_scope` = customer scope AND `collection` is an OOB table

Not yet built — identified during report output extension planning. See `sn-instance-scan` repo's `docs/superpowers/` for current build status.

Source: [[raw/sessions/2026-07-22#Session 17:09 — obsidian-servicenow-docs]]

---

## Open design questions (pre-build)
- Dedicate a `x_snis_iscan.scanner` role (rather than requiring admin) so the ACL-fallback path is testable in ATF.
- Verify `sys_app.source` / vendor field values on the live target instance before hardcoding custom-vs-store filter logic.

## Related
- [[sn-instance-scan/test-plan|sn-instance-scan Test Plan]]
- [[sn-instance-scan/architecture-v2|sn-instance-scan Architecture v2]]
- [[scoped-apps]]
- [[acls]]
- [[gliderecord-patterns]]
- [[ai-agents]]
- [[wiki/index|Wiki Index]]
