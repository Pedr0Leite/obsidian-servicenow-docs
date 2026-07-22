---
aliases: [sn-instance-scan Test Plan]
area: application-spec
tags: [scoped-app, application-development, atf, spec, test-plan]
---

# sn-instance-scan — Test Plan

## Story: Custom-only scope filter

#### Test 1: Custom-only excludes store apps
- Precondition: instance has at least one x_-scoped store-installed app and one x_-scoped internally-developed app
- Steps:
  1. Run scan with mode = custom_only
  2. Inspect x_snis_iscan_result records created
- Expected result: result set includes the internal x_ app, excludes the store-installed x_ app
- Validates: SCOPE SELECTION #2 (source/vendor filter, not string prefix only)

## Story: Table & field discovery (full access)

#### Test 2: Full scan happy path
- Precondition: run as user with read access to sys_db_object/sys_dictionary and a target custom app's tables
- Steps:
  1. Run scan with mode = full and select the target custom app
  2. Open the resulting x_snis_iscan_result record
- Expected result: scan_mode_used = 'full_access'; table_count > 0; related x_snis_iscan_table rows exist with row_count, field list, and reference_field_list populated; any table extending task/cmdb_ci is flagged well_known_base accordingly
- Validates: ALGORITHM steps 2-3

#### Test 3: Row count uses GlideAggregate, not getRowCount
- Precondition: same as Test 2, target table has a known row count
- Steps:
  1. Run scan
  2. Compare x_snis_iscan_table.row_count to actual table count
- Expected result: value matches actual count; validated via code inspection that IscanTableScanner.profileTable uses GlideAggregate COUNT (not GlideRecord.getRowCount())
- Validates: ALGORITHM step 3 constraint

## Story: ACL-denial fallback

#### Test 4: ACL-denied app falls back cleanly
- Precondition: ATF test user with no read access to sys_db_object and sys_dictionary rows for the target scope
- Steps:
  1. Impersonate ATF test user
  2. Run scan against the target custom app
  3. Check for thrown errors / script log errors
  4. Open resulting x_snis_iscan_result record
- Expected result: no exception thrown; scan_mode_used = 'app_files_fallback'; script_include_count, business_rule_count, acl_count, ui_action_count, flow_count are populated from sys_metadata; x_snis_iscan_table has zero rows (no table access) and result record notes fallback mode
- Validates: ALGORITHM step 4, CONSTRAINT "never assume security_admin", ATF negative case

#### Test 5: canAccessMetadata gate is deterministic, not exception-based
- Precondition: code inspection + Test 4 result
- Steps:
  1. Review IscanTableScanner.canAccessMetadata() implementation
- Expected result: uses GlideRecord.canRead() checks before querying; fallback path in orchestrator is chosen by this boolean, not triggered from a catch block
- Validates: ALGORITHM step 4 explicit requirement

## Story: Architecture summary generation

#### Test 6: Summary generated via single GenAI call
- Precondition: Now Assist / Generative AI Controller active on instance, x_snis_iscan.genai_enabled = true
- Steps:
  1. Run scan (full or fallback mode) against one app
  2. Inspect x_snis_iscan_result.summary_text
- Expected result: summary_text populated, references app's actual tables/automation counts (plausibility check, not exact match); confirm via code inspection that generation is a single GenAI Controller call, not an AI Agent/ReAct execution (no sn_aia_execution_plan records created by this app)
- Validates: OUTPUT "generated summary text", CONSTRAINT "not a multi-step reasoning agent"

#### Test 7: GenAI unavailable degrades gracefully
- Precondition: x_snis_iscan.genai_enabled = false (or GenAI Controller API absent)
- Steps:
  1. Run scan
- Expected result: result record created with all structured fields populated, summary_text is null/empty, no error thrown
- Validates: Risk flag — GenAI optionality per spec ("Optionally hand...")

## Story: Results table, form, list view

#### Test 8: List and form views render expected fields
- Precondition: at least one completed scan run
- Steps:
  1. Open x_snis_iscan_result list view
  2. Open one record's form view
- Expected result: list shows app, scan date, scan mode, table count, automation count columns; form shows all result fields plus related list of x_snis_iscan_table child records
- Validates: OUTPUT "form/list view to browse results per app"

## Story: Read-only / no destructive operations

#### Test 9: Scan performs no writes to scanned application data
- Precondition: full scan run against a custom app with known data
- Steps:
  1. Snapshot record counts / data on scanned app's tables before scan
  2. Run scan
  3. Compare snapshot after scan
- Expected result: zero writes to any scanned table; only x_snis_iscan_* tables are modified
- Validates: CONSTRAINT "Read-only app, no destructive operations"

## Story: Manual scan mode

#### Test 10: Manual mode scans only selected apps
- Precondition: instance has 3+ eligible apps
- Steps:
  1. Run scan with mode = manual, select 2 specific apps
  2. Check x_snis_iscan_run.app_count and resulting x_snis_iscan_result records
- Expected result: exactly 2 result records created, matching the selected apps, no others
- Validates: SCOPE SELECTION #3

---

# Test Plan Delta — v2 improvements

See [[sn-instance-scan/architecture-v2|architecture-v2]] for design. Delta only — v1 tests above are unchanged and still apply.

## Story: LLM context export

#### Test 11: llm_context populated on full-access scan with all required sections
- Precondition: run as user with full read access, target a custom app with tables, business rules, and script includes
- Steps:
  1. Run scan with mode = full or custom_only against the target app
  2. Open resulting x_snis_iscan_result record, inspect llm_context
- Expected result: llm_context contains, in order: app identity section (incl. explicit "scan mode: full_access" statement), data model section (table list, extends_table, well_known_base, field lists, reference_field_list graph), automation surface section with NAMES (not just counts) of business rules/script includes/flows/ACLs/UI actions, integration points section, fixed instruction footer paragraph
- Validates: Improvement 1, CHANGES #1-2

#### Test 12: llm_context omits data model section on fallback mode
- Precondition: ATF test user with no read access to sys_db_object/sys_dictionary (same setup as v1 Test 4)
- Steps:
  1. Run scan against the target app (triggers app_files_fallback)
  2. Inspect llm_context
- Expected result: data model section is ABSENT (not present with zero/empty values) and replaced with a single line explaining no table/field access was available; automation surface section still populated from sys_metadata names
- Validates: Improvement 1, CHANGES #2 ("Omit entirely... not just zero-filled")

#### Test 13: summary_text and llm_context stay in sync (single fact assembly)
- Precondition: GenAI Controller active, x_snis_iscan.genai_enabled = true
- Steps:
  1. Run scan
  2. Compare summary_text and llm_context for the same result record
- Expected result: summary_text's claims (table counts, automation counts) are consistent with what llm_context states — no contradiction between the two, confirming both were built from the same buildPrompt() output
- Validates: Design note "one fact assembly, two consumers"

#### Test 14: Copy LLM Context UI action copies field value
- Precondition: a completed scan result record with non-empty llm_context
- Steps:
  1. Open x_snis_iscan_result form
  2. Click "Copy LLM Context" UI action
  3. Paste clipboard contents elsewhere
- Expected result: pasted text exactly matches llm_context field value, no truncation
- Validates: Improvement 1, CHANGES #4

#### Test 15: Scanner return-shape addition doesn't break existing count fields
- Precondition: any completed scan run (full or fallback)
- Steps:
  1. Inspect x_snis_iscan_result business_rule_count, script_include_count, flow_count, acl_count, ui_action_count
- Expected result: all *_count fields populated exactly as in v1 (regression check — name-list addition must not change existing count values)
- Validates: Improvement 1, CHANGES #5 ("Existing *_count fields... unchanged")

## Story: Activity stream comments field

#### Test 16: comments journal field receives progressive entries
- Precondition: none
- Steps:
  1. Start a scan run (any mode)
  2. While running (or after completion), open x_snis_iscan_run form, check the Activity formatter
- Expected result: Activity stream shows the same progressive milestone messages that appear in the activities String field, each as a separate journal entry (not one giant blob)
- Validates: Improvement 2, CHANGES #1-2

#### Test 17: activities field unchanged and still queryable
- Precondition: same run as Test 16
- Steps:
  1. Inspect x_snis_iscan_run.activities (String field, not the Activity formatter)
- Expected result: activities field still contains the full prepended log exactly as in v1 behavior — confirms comments is additive, not a replacement
- Validates: Improvement 2, CONSTRAINT ("Do not swap activities to Journal type")

#### Test 18: scanner role can write comments without elevated privilege
- Precondition: user with x_snis_iscan.scanner role only (no admin, no security_admin)
- Steps:
  1. Run a scan as this user
  2. Confirm no ACL-denied error on the comments field write, and Activity stream populates
- Expected result: no exception; comments journal entries appear — validates the build-time ACL check flagged in architecture-v2 resolved correctly (either table-level ACL covers it, or the added field ACL does)
- Validates: Improvement 2 build-time risk (journal field ACL parity with non-task table)
