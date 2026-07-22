---
aliases: [sn-instance-scan v3 Assessment Report Prompt]
area: application-spec
tags: [scoped-app, application-development, spec, prompt, reporting]
---

# sn-instance-scan v3 — Assessment Report Build Prompt

**STATUS (2026-07-22): Fully implemented.** Decomposed into 4 sub-specs
(Modes → Counting → Cross-refs → Report) — see the `sn-instance-scan`
repo's `CLAUDE.md` ("Instance-assessment extension" section),
`docs/superpowers/INSTANCE_ASSESSMENT_STATUS.md`, and
`docs/superpowers/specs/`/`plans/` for the actual implementation record,
which diverged from/refined this prompt in a few places worth knowing
about if this prompt is ever reused as a template:
- "Full" scan initially shipped scoped to `sys_app` only (Studio/App
  Manager registry), narrower than this prompt's "every application/scope
  on the instance." Corrected 2026-07-22 to iterate `sys_scope`, with an
  OOB-scope table-only fallback (no coherent "app" to tally against) —
  `global` itself is deliberately excluded from that fallback (it owns the
  entire base table set).
- Roles/groups/system properties were initially excluded from the count
  list as a judgment call during brainstorming (recorded, then reversed,
  in the repo's `docs/future-schema-ideas.md`) — added 2026-07-22 per this
  prompt's explicit ask. `group_count` needed a field-existence guard:
  `sys_user_group` has no `sys_scope` column on stock ServiceNow.
- The "Now Assist Readiness Evaluation" reference was a *style* target
  (status-flagged counts + PDF export UX), not a literal separate feature
  to clone — that's what the Report sub-spec built.

This is a historical build prompt, not a live status tracker — the repo
is authoritative for current build state. Copy the block below into a new
Claude Code session (works after `/goal`) only if starting a NEW,
unrelated extension — don't re-run this one, it's done.

## Related
- [[sn-instance-scan/architecture|v1 Architecture]]
- [[sn-instance-scan/prompt-v2-improvements|v2 Improvements]]
- [[sn-instance-scan]]

---

```
GOAL: Extend the existing sn-instance-scan scoped app into an instance-assessment
tool that produces an extractable, descriptive report — quantifying EVERY config
artifact and data volume in scope, and mapping cross-table / cross-app references.
Model the output on two ServiceNow examples: the "Now Assist Readiness Evaluation"
report (status-flagged Q&A with counts) and a full-instance assessment document
(sectioned narrative: platform, licensing, custom tables, processes, CMDB, catalog,
SLA, integrations, conclusions + recommendations). Both are quantified end to end.

BUILD ON THE EXISTING APP — do not rebuild. Current state:
- Scoped app x_snis_iscan (real prefix x_335329_iscan).
- Tables: x_snis_iscan_run (header), x_snis_iscan_result (per-app),
  x_snis_iscan_table (per-table profile: table_name, extends, well_known_base,
  row_count, field_count, reference_field_list).
- Script Includes: IscanAppSelector, IscanTableScanner (has canAccessMetadata()
  gate), IscanAppFilesScanner (sys_metadata fallback), IscanSummaryGenerator
  (GenAI, optional), IscanScanOrchestrator (entry point).
- UI Action "Run Scan" on x_snis_iscan_run → GlideAjax async.
- Three scan modes already exist. Reuse these script includes; add counters + a
  report generator, not a new framework.

CHANGES

1) Rename / redefine the modes (three existing + one new = four):
   - "Custom" → "Custom Apps Only": scans only custom applications (scope prefix +
     non-store source), instance-wide across all custom apps.
   - "Full" → true full-instance scan: EVERY application/scope on the instance, not
     just the current app. If today's full mode is scoped to one app, widen it.
   - "Manual" → user picks ONE entire application via a reference field to sys_app
     (Applications), with a reference qualifier. Scan covers that whole app.
   - NEW "Single Table" → user picks ONE table via a reference field to
     sys_db_object (Tables), with a reference qualifier. Scan targets just that
     table: its fields, reference fields + targets, and record count.

2) Count EVERYTHING (extend the current counts). Per scope, tally every artifact
   type AND data volume — not just tables/BR/SI/flow/ACL/UI action/integration.
   Include: client scripts, UI policies, UI actions, business rules, script
   includes, scheduled jobs, events, notifications, REST/SOAP messages, scripted
   REST APIs, transform maps / import sets, catalog items + variables, workflows,
   Flow Designer flows/subflows/actions, ATF tests, reports, dashboards, PA
   indicators, roles, groups, system properties, fix scripts, processors, inbound
   email actions, service portals/widgets, dictionary overrides, choices, data
   policies — and any other sys_metadata-tracked artifact type. PLUS per owned
   table: record count via GlideAggregate (never getRowCount). Report the count of
   each, the way the assessment example tallies incidents / categories / SLAs /
   CMDB-class records.

3) Field & reference discovery: for each table in scope, read sys_dictionary,
   capture every field, flag reference fields and their target table, and build a
   cross-reference map (which tables/apps reference which). Persist it so the report
   can describe inter-app / inter-table dependencies.

4) Descriptive output scaled to mode: full = instance-level narrative; custom-apps
   = the custom footprint; manual = single-app deep description.

5) Extractable report: generate an exportable document (HTML → PDF) combining both
   example styles:
   - Status-flagged findings (pass / warning / fail + the count) like the Now
     Assist Readiness Evaluation.
   - A sectioned narrative assessment with counts throughout, and recommendations
     flagged wherever config diverges from OOB / best practice.

CONSTRAINTS
- Read-only, runs under the caller's own access; keep the ACL-denial fallback path.
- gs.getProperty() for all config; no hardcoded sys_ids.
- GlideAggregate for counts. GenAI summary stays optional and degrades gracefully.
- Don't over-build: extend existing script includes; add counters + report
  generator only.

ACCEPTANCE
- All four modes run (Custom Apps Only / full instance / manual whole app /
  single table).
- A run yields: per-artifact-type counts, per-table field + reference map with
  cross-app dependencies, and an exportable report matching the two example styles.
- Every finding in the report carries a number.
```
