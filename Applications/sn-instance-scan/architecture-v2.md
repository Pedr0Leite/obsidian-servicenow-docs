---
aliases: [sn-instance-scan v2 Architecture, Instance Scanner LLM Context + Comments Field Architecture]
area: application-spec
tags: [scoped-app, application-development, cmdb, acls, ai-agents, spec, architecture, journal-fields]
---

# sn-instance-scan — Architecture v2 (delta)

Scope: `x_snis_iscan` (unchanged from v1)
This note covers ONLY the delta for [[sn-instance-scan/prompt-v2-improvements|the v2 improvements spec]]. For everything not mentioned here (table schema, script includes, ACLs not listed below), v1 behavior in [[sn-instance-scan/architecture|architecture.md]] stands unchanged. Both improvements are additive — no v1 field renamed, retyped, or removed.

---

## Story 8: LLM context export (Improvement 1)

### Components
- Tables: `x_snis_iscan_result` — new field `llm_context` (see schema delta below)
- Business Rules: none
- Client Scripts: none (UI action handles clipboard client-side)
- Script Includes:
  - `IscanSummaryGenerator.buildPrompt(facts)` — REFACTORED (not new) to emit the full self-contained document instead of a terse internal prompt. Same method name, same caller (`generate()`), different (bigger) output.
  - `IscanTableScanner.getOwnedTables()` / `profileTable()` — return-shape addition, name lists already implicit in existing per-table objects (no change needed here — table names/fields already named, not just counted)
  - `IscanAppFilesScanner.scanApp()` — return-shape addition: `business_rule_names[]`, `script_include_names[]`, `flow_names[]`, `acl_names[]`, `ui_action_names[]` alongside existing counts
  - `IscanScanOrchestrator.runScan()` — wiring change only: pass the fuller facts object (now containing name lists) to `buildPrompt()`, persist its output to `x_snis_iscan_result.llm_context`
- Flows: none
- UI: UI Action "Copy LLM Context" on `x_snis_iscan_result` form — client script, clipboard API, copies `llm_context` field value. Classic UI Action (matches v1's existing "Run Scan" UI action pattern on the sibling table — no UIB/portal component introduced for this app in v1, so v2 stays consistent rather than mixing frameworks for one button).
- ACLs: none new — `llm_context` inherits the existing read ACL on `x_snis_iscan_result` (`x_snis_iscan.scanner`, read); write is system-only via Script Include, same as `summary_text`
- Integrations: none (explicitly a non-goal — llm_context is exported for the user to paste elsewhere, app makes no outbound LLM call)

### Scope
- App scope: x_snis_iscan
- Update set: "sn-instance-scan v2 - LLM Context Export"

### Dependencies
- v1 Story 4 (`IscanAppFilesScanner`) and Story 3 (`IscanTableScanner`) — return-shape changes are additive to their existing objects, existing consumers (orchestrator writing `*_count` fields) keep working unchanged
- v1 Story 5 (`IscanSummaryGenerator`) — `buildPrompt()` refactor is the core of this story
- v1 Story 6 (`x_snis_iscan_result` table) — hosts the new field

### Risks / Flags
- `llm_context` on a large full-access scan (many tables, many fields) can get long. Use the same field type precedent as `summary_text` (full text/HTML String) — no length cap enforced in v1 for that field either, so don't introduce one here without a stated reason. If instances hit practical limits later, that's a v3 concern, not a v2 blocker.
- `buildPrompt()` behavior change is a breaking change to its OWN output shape (not its signature) — the in-instance GenAI call (`generate()`) now receives a longer, structured document instead of a terse prompt. Verify this doesn't blow past the target instance's GenAI Controller input token/char limit — if it does, `generate()` should have its own truncation/summarization step before invocation, `llm_context` (the persisted field) stays full-length regardless. Flag as a build-time check, not a design blocker (degrade gracefully per v1's existing GenAI-unavailable path if the call itself fails).
- Fallback mode (`app_files_fallback`) must OMIT the data-model section from `llm_context` entirely, not zero-fill it — a receiving LLM seeing `table_count: 0` would wrongly conclude the app has no tables, rather than "we didn't have access to check." This is a content-correctness risk, not a schema risk — flag to Developer explicitly in the per-component instructions below.

---

## Story 9: Activity stream comments field (Improvement 2)

### Components
- Tables: `x_snis_iscan_run` — new field `comments` (Journal, see schema delta below). Existing `activities` (String, 8000) field is UNCHANGED — do not touch its type or remove it.
- Business Rules: none
- Script Includes:
  - `IscanScanOrchestrator._appendActivity(run, message)` — MODIFIED (not replaced). Keeps its existing String-field prepend + `run.update()` behavior for `activities`, additionally sets `run.comments = message` (journal-append semantics — assigning a string to a Journal field element appends a new journal entry, it does not overwrite prior entries) before the same `run.update()` call. One call site, two fields written, no new method needed.
- Flows: none
- UI: Activity formatter added to the `x_snis_iscan_run` form view — Form Layout configuration only, not code. Renders `comments` journal entries in the standard OOB Activity stream.
- ACLs: `x_snis_iscan_run.comments` — inherits table-level read/write already granted to `x_snis_iscan.scanner` (v1 ACL table, unchanged); no new ACL row needed since Journal fields on a table the role can already write to don't require a separate field-level ACL unless one is later added to restrict it. Flag this as a verify-at-build-time item (see Risks below) rather than asserting it needs zero configuration.

### Scope
- App scope: x_snis_iscan
- Update set: "sn-instance-scan v2 - Activity Stream Comments"

### Dependencies
- v1 Story 1 (`x_snis_iscan_run` table) — hosts the new field
- v1's `_appendActivity()` helper (Implementation Decisions, 2026-07-15) — this story modifies it in place

### Risks / Flags
- Journal fields carry ACL semantics distinct from plain String fields (this is exactly why v1 chose String for `activities` in the first place — see v1 architecture's Implementation Decisions section). Verify at build time that `x_snis_iscan.scanner` can write `comments` without needing an explicit journal-field ACL — OOB Comments/Work notes fields on task-derived tables get their ACL behavior partly from being on `task`; `x_snis_iscan_run` does NOT extend `task` (per v1 schema, it's a standalone table), so this app's `comments` field may need an explicit write ACL where OOB `task.comments` would not. Do not assume parity with `task.comments` ACL behavior — test it.
- `run.comments = message` triggers ServiceNow's journal-entry-per-assignment behavior — confirm the exact API during build (`setJournalEntry()` is the more explicit/reliable path also called out in the v2 prompt as an alternative). Use whichever the target instance version handles predictably; don't assume both are interchangeable without a build-time check.
- `_appendActivity()` now does two field writes per call inside the same `run.update()` — no performance concern (same GlideRecord update, two field values set before it), but note it in code comments so a future maintainer doesn't "clean up" one of the two writes thinking it's redundant.

---

# Table Schema — v2 delta

## x_snis_iscan_result (ADD field)
| Field | Type | Notes |
|---|---|---|
| llm_context | String (full text/HTML) | NEW. Full self-contained architecture document per the buildPrompt() structure below. Superset of what generate()'s internal GenAI prompt uses. Not journal — same "queryable, no journal ACL complications" rationale as v1's `activities`. |

All other `x_snis_iscan_result` fields unchanged from v1 (see [[sn-instance-scan/architecture|architecture.md]]).

## x_snis_iscan_run (ADD field)
| Field | Type | Notes |
|---|---|---|
| comments | Journal | NEW. Standard 'Comments' journal field, same type as OOB task.comments. Additive alongside existing `activities` (String, 8000, unchanged) — NOT a replacement. Feeds the native Activity formatter. |

All other `x_snis_iscan_run` fields unchanged from v1.

## x_snis_iscan_table — unchanged (no v2 delta)

---

# Dev Instructions — v2 delta

## Build Order (append after v1's 12 steps — do not redo v1 steps)
1. Add field `x_snis_iscan_result.llm_context` (String, full text/HTML).
2. Add field `x_snis_iscan_run.comments` (Journal).
3. Update `IscanTableScanner` / `IscanAppFilesScanner` return shapes to include name-list arrays alongside existing counts (additive object properties — existing `*_count` fields on `x_snis_iscan_result` keep being populated from the same underlying data, no change to what's written there).
4. Refactor `IscanSummaryGenerator.buildPrompt(facts)` per the section structure below. Build and unit-verify this BEFORE touching `generate()`, since `generate()`'s only change is consuming the new `buildPrompt()` output.
5. Update `IscanSummaryGenerator.generate(facts)` — no signature change, just consumes the refactored `buildPrompt()` output as its GenAI Controller input. Verify against target instance's input length limits (see Risks, Story 8).
6. Update `IscanScanOrchestrator.runScan()` — persist `buildPrompt()`'s output to `x_snis_iscan_result.llm_context` when writing each result row (this happens regardless of GenAI availability — llm_context does not depend on the GenAI Controller being active, only `summary_text` does).
7. Update `IscanScanOrchestrator._appendActivity()` — add the `comments` journal write alongside the existing `activities` String write. Confirm journal-append API choice at build time (see Risks, Story 9).
8. Create UI Action "Copy LLM Context" on `x_snis_iscan_result` (client-side clipboard copy of `llm_context`).
9. Add Activity formatter to `x_snis_iscan_run` form view (Form Layout config, no code).
10. Verify/add write ACL for `x_snis_iscan.scanner` on `x_snis_iscan_run.comments` if the build-time ACL check (Story 9 risk) shows it's needed.
11. Update ATF tests (see test-plan delta below).

## Per Component

#### IscanSummaryGenerator.buildPrompt(facts) — REFACTORED
- Type: Script Include method (existing include, existing method name)
- Table: none directly — pure string assembly from the `facts` object passed in
- Output sections, in this order:
  1. **App identity** — name, scope, vendor/source, scan date, `scan_mode_used` stated explicitly (e.g. "Scan mode: full_access — table and field data below is complete" vs "Scan mode: app_files_fallback — no table/field access; only automation metadata below").
  2. **Data model** — full table list with `extends_table` and `well_known_base`, per-table field list (name + type), `reference_field_list` relationship graph (table -> target table). OMIT this entire section (not zero-filled) when `scan_mode_used = app_files_fallback`; replace with one line stating why it's absent.
  3. **Automation surface** — counts AND name lists for business rules, script includes, flows, ACLs, UI actions (pulls from the new `*_names[]` arrays in facts, per Story 8 return-shape change).
  4. **Integration points** — REST messages / web services referencing the scope, name + endpoint where available.
  5. **Instruction footer** — fixed closing paragraph (same text every time, not templated per-app) asking the receiving LLM to produce a well-documented architecture summary from the above.
- Scope: x_snis_iscan
- Dependencies: facts object must carry the new name-list arrays from `IscanTableScanner`/`IscanAppFilesScanner` before this refactor is meaningful — build order step 3 before step 4.

#### IscanTableScanner / IscanAppFilesScanner — return-shape addition
- `IscanAppFilesScanner.scanApp()` return object gains: `business_rule_names[]`, `script_include_names[]`, `flow_names[]`, `acl_names[]`, `ui_action_names[]` — same single `sys_metadata` query already used for the counts (v1), just also collect `sys_name`/`name` into arrays during the same in-memory bucketing pass. No new query.
- `IscanTableScanner` — table/field names are already present in its existing per-table objects (`getOwnedTables()`/`profileTable()` never returned counts-only for tables); no structural change needed there, only confirm `buildPrompt()` reads from the existing shape correctly.
- Scope: x_snis_iscan
- Dependencies: none beyond v1

#### UI Action "Copy LLM Context"
- Table: x_snis_iscan_result
- Type: form button, client=true, reads `llm_context` field value and writes to clipboard via standard browser clipboard API (`navigator.clipboard.writeText`) — mirrors how `summary_text` is already displayed on the form, no GlideAjax round-trip needed since the field value is already on the loaded form
- Scope: x_snis_iscan

#### IscanScanOrchestrator._appendActivity() — MODIFIED
- Existing behavior (String `activities` prepend + `run.update()`) unchanged.
- Add: `run.comments = message;` (or `run.comments.setJournalEntry(message)` — confirm which the target instance version handles predictably) before the same `run.update()` call.
- Scope: x_snis_iscan
- Dependencies: `x_snis_iscan_run.comments` field must exist (build order step 2 before step 7)

## ACLs — v2 delta
| Table | Op | Role | Condition |
|---|---|---|---|
| x_snis_iscan_result.llm_context | read | x_snis_iscan.scanner | inherited from existing table-level read ACL, no new row expected |
| x_snis_iscan_run.comments | write | x_snis_iscan.scanner | verify at build time — see Story 9 risk; add explicit field ACL only if the build-time check shows the table-level ACL doesn't cover the new journal field |

No other ACL changes. Both improvements respect v1's rule: "no ACL in this app should grant broader table access than the user already has."

---

## Related
- [[sn-instance-scan]]
- [[sn-instance-scan/prompt|sn-instance-scan v1 Build Prompt]]
- [[sn-instance-scan/architecture|sn-instance-scan Architecture (v1)]]
- [[sn-instance-scan/prompt-v2-improvements|sn-instance-scan v2 Improvements Build Prompt]]
- [[sn-instance-scan/test-plan|sn-instance-scan Test Plan (v1)]]
- [[scoped-apps]]
- [[acls]]
- [[gliderecord-patterns]]
- [[ai-agents]]
- [[wiki/index|Wiki Index]]
