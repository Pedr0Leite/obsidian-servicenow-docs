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
