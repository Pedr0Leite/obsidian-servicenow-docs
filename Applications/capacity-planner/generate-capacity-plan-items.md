---
title: Generate Plan Items from Active Initiatives (Background Script)
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - business-rules
  - data-remediation
  - access-control
aliases:
  - GeneratePlanItems
  - generate-capacity-plan-items
date: 2026-07-03
---

# Generate Plan Items from Active Initiatives

## Context

[[capacity-planner|Capacity Management Overview (x_u4bsh_capmgmt)]] normally creates a Plan Item (`x_u4bsh_capmgmt_initiative`) linked to an Initiative one at a time, through the `/api/x_u4bsh_capmgmt/capacity/add` endpoint (`addInitiative` handler). This note documents a one-time bulk generation script that creates a Plan Item for every **active** `x_u4bsh_initiati_0_initiative` record that doesn't already have one, ahead of the separate [[capacity-planner-set-start-and-end-date-to-plan-items|date backfill]] and the status bulk-import work.

`u_plan_status` is deliberately left empty by this script - it's populated afterward by a separate Import Set/Transform Map sourced from a status migration spreadsheet, not by this script.

## Field mapping rules

| Plan Item field | Source | Rule |
|---|---|---|
| `u_name` | `short_description` | Direct copy. |
| `u_initiative` | (link) | The source Initiative's `sys_id`. |
| `u_snow_ref` | `number` | Direct copy. |
| `u_type` | `initiative_type` | `enhancement` -> `Enhancement`. Anything else (`new_feature`, `new_application`, blank) -> `Project`. Confirmed against the actual `initiative_type` choice list (3 values) on `x_u4bsh_initiati_0_initiative`. |
| `u_area` | `business_area_function`, resolved via lookup table `x_u4bsh_initiati_0_business_area_function` | **Not** a direct copy. `business_area_function` (36 raw choice values on the Initiative) is looked up against `x_u4bsh_initiati_0_business_area_function`, and that record's `business_area` field is used as the actual `u_area` value (10 target choices). This is how the many-to-one rollup (36 source values -> 10 target values) gets resolved correctly instead of guessed. |
| `u_tshirt_size` | `high_level_sizing` | Clean 1:1 ordinal map: X-Small<1mo -> XS, Small 1mo -> S, Medium 2-3mo -> M, Large 3-5mo -> L, X-Large>5mo -> XL. |
| `u_priority` | `priority` | **Confirmed 2026-08-10.** Identity - the source rank is already the target value (source 1 -> P1, 2 -> P2, and so on). No map, the raw value is copied straight through. P0 (BAU) is a category, not a rank, and is never produced by this script. |
| `u_snow_status` | `state` | **Confirmed 2026-08-10.** Source is `state`, not `status`. Direct label map over the 7 `state` values - the Plan Item's stored status value *is* the Initiative state's label, e.g. Approved (2) -> `Approved`. Full map: Pending (-5), New (1), Screening (-3), Qualifying (-4), Approved (2), Completed (3), Canceled (7). |
| `u_plan_status` | - | Left empty on purpose. |
| `u_start`, `u_end` | - | Never touched - system-derived by `derive-initiative-dates`, ACL-locked. |

## Key gotchas

- **Business rules are disabled for the insert** (`newGR.setWorkflow(false)`). The `sync-initiative-fields` Business Rule normally copies several of these same fields directly from the linked Initiative when `u_initiative` is set - but its copy logic doesn't know about the `x_u4bsh_initiati_0_business_area_function` lookup rollup for `u_area`, so if it ran it could silently overwrite this script's correctly-resolved value with a naive direct copy. Disabling workflow means this script is fully responsible for every field it sets - nothing is left for the BR to fill in.
- **`u_priority` and `u_snow_status` mappings are confirmed as of 2026-08-10** and no longer guesses. Priority is an identity copy (no map at all - `PRIORITY_MAP` was deleted). `SNOW_STATUS_MAP` now reads the source `state` field, not `status`, and maps its 7 values directly to their labels; the old 43-value `status` rollup is gone. A `state` value outside the 7 is still left blank and logged (`UnmappedStatus`), never defaulted.
- **Lookup field name on `x_u4bsh_initiati_0_business_area_function` is assumed to be `name`** - verify this against the real table before running for real; the script queries `addQuery('name', businessAreaFunctionValue)`.
- **`addActiveQuery()` assumes a standard `active` field** on `x_u4bsh_initiati_0_initiative`. Verify this table actually has one; if not, the active-record filter needs to be replaced with whatever field actually represents "active" on this table.
- **Idempotent** - re-running skips any Initiative that already has a linked Plan Item (`u_initiative` treated as a unique key), so it's safe to run multiple times as mappings get corrected.

## The script

```javascript
// ============================================================
// Generate Plan Items - Bulk create x_u4bsh_capmgmt_initiative
// for every ACTIVE x_u4bsh_initiati_0_initiative that does not
// yet have a linked Plan Item (u_initiative as unique key).
//
// INSTRUCTIONS:
//   1. Open Background Scripts in scope x_u4bsh_capmgmt
//   2. Set DRY_RUN = true, run, review the log output
//   3. Set DRY_RUN = false, run again to perform real inserts
//
// FIELD MAPPING RULES (see accompanying .md note for full context)
//   u_name          <- source.short_description
//   u_initiative    <- source sys_id (the link itself)
//   u_snow_ref      <- source.number
//   u_type          <- source.initiative_type: 'enhancement' -> 'Enhancement',
//                       anything else (new_feature / new_application / blank) -> 'Project'
//   u_area          <- resolved via lookup table x_u4bsh_initiati_0_business_area_function,
//                       matched on source.business_area_function, using that record's
//                       business_area field. NOT a direct copy of business_area_function.
//   u_tshirt_size   <- ordinal map from source.high_level_sizing
//   u_priority      <- source.priority, copied as-is (source rank N = target PN)
//   u_snow_status   <- direct label map from source.state (7 values)
//   u_plan_status   <- left empty on purpose (populated later by the status import set)
//   u_start/u_end   <- never touched (system-derived, ACL-locked)
//
// business rules are disabled for this insert (setWorkflow(false)) so the
// sync-initiative-fields BR does not overwrite the field values this script
// computes explicitly (in particular u_area, which needs the lookup-table
// rollup below rather than the BR's naive direct copy).
// ============================================================

var DRY_RUN = true; // <-- set to false to execute real inserts

// ---- Choice mapping tables ------------------------------------------------

// high_level_sizing (source) -> u_tshirt_size (target). Clean 1:1 ordinal map.
var TSHIRT_MAP = {
    '5': 'XS', // X-Small < 1 month
    '4': 'S',  // Small 1 month
    '3': 'M',  // Medium 2-3 months
    '2': 'L',  // Large 3-5 months
    '1': 'XL'  // X-Large > 5 months
};

// priority (source) -> u_priority (target). Identity: source rank N -> PN.
// No map needed - the stored values match, so the raw value is copied through.

// state (source, 7 values) -> u_snow_status (target). Direct: the target's
// stored value IS the source's label, e.g. Approved (2) -> 'Approved'.
var SNOW_STATUS_MAP = {
    '-5': 'Pending',
    '1':  'New',
    '-3': 'Screening',
    '-4': 'Qualifying',
    '2':  'Approved',
    '3':  'Completed',
    '7':  'Canceled'
};

// initiative_type (source) -> u_type (target)
function mapType(initiativeType) {
    if (initiativeType === 'enhancement') {
        return 'Enhancement';
    }
    return 'Project'; // new_feature, new_application, or blank all default to Project
}

// Resolve u_area via the lookup table, per the business's mapping rule.
// VERIFY: confirm the actual matching field name on
// x_u4bsh_initiati_0_business_area_function (assumed 'name' below) before a real run.
function resolveArea(businessAreaFunctionValue) {
    if (!businessAreaFunctionValue) {
        return '';
    }
    var lookupGR = new GlideRecord('x_u4bsh_initiati_0_business_area_function');
    lookupGR.addQuery('name', businessAreaFunctionValue); // VERIFY field name
    lookupGR.setLimit(1);
    lookupGR.query();
    if (lookupGR.next()) {
        return lookupGR.getValue('business_area') || '';
    }
    return '';
}

// ---- Counters ---------------------------------------------------------
var skipped = 0;
var inserted = 0;
var unmappedArea = 0;
var unmappedStatus = 0;
var errors = 0;

gs.info('[GeneratePlanItems] Start. DRY_RUN=' + DRY_RUN);

// ---- Process every active source initiative ----------------------------
var sourceGR = new GlideRecord('x_u4bsh_initiati_0_initiative');
sourceGR.addActiveQuery(); // VERIFY: assumes this table has a standard 'active' field;
                            // if not, replace with the correct active-state filter.
sourceGR.query();

while (sourceGR.next()) {
    var sourceSysId = sourceGR.getUniqueValue();
    var sourceNumber = sourceGR.getValue('number') || sourceSysId;
    var sourceShortDesc = sourceGR.getValue('short_description') || '';
    var sourceInitiativeType = sourceGR.getValue('initiative_type') || '';
    var sourceBusinessAreaFunction = sourceGR.getValue('business_area_function') || '';
    var sourceHighLevelSizing = sourceGR.getValue('high_level_sizing') || '';
    var sourcePriority = sourceGR.getValue('priority') || '';
    var sourceState = sourceGR.getValue('state') || '';

    // Idempotency check - skip if a Plan Item already references this initiative
    var existingGR = new GlideRecord('x_u4bsh_capmgmt_initiative');
    existingGR.addQuery('u_initiative', sourceSysId);
    existingGR.setLimit(1);
    existingGR.query();
    if (existingGR.next()) {
        gs.info('[GeneratePlanItems] Skip (already exists): ' + sourceNumber + ' -> ' + existingGR.getUniqueValue());
        skipped++;
        continue;
    }

    // Resolve mapped field values
    var resolvedType = mapType(sourceInitiativeType);
    var resolvedArea = resolveArea(sourceBusinessAreaFunction);
    var resolvedTshirt = TSHIRT_MAP[sourceHighLevelSizing] || '';
    var resolvedPriority = sourcePriority; // identity - source rank is already the target value
    var resolvedSnowStatus = SNOW_STATUS_MAP[sourceState] || '';

    if (!resolvedArea) {
        gs.warn('[GeneratePlanItems] No area mapping found for ' + sourceNumber +
            ' (business_area_function="' + sourceBusinessAreaFunction + '") - u_area will be left blank.');
        unmappedArea++;
    }
    if (!resolvedSnowStatus) {
        gs.warn('[GeneratePlanItems] No snow_status mapping found for ' + sourceNumber +
            ' (state="' + sourceState + '") - u_snow_status will be left blank.');
        unmappedStatus++;
    }

    if (DRY_RUN) {
        gs.info('[GeneratePlanItems] [DRY RUN] Would insert: ' + sourceNumber +
            ' | name=' + sourceShortDesc +
            ' | type=' + resolvedType +
            ' | area=' + resolvedArea +
            ' | tshirt=' + resolvedTshirt +
            ' | priority=' + resolvedPriority +
            ' | snow_status=' + resolvedSnowStatus);
        inserted++;
        continue;
    }

    try {
        var newGR = new GlideRecord('x_u4bsh_capmgmt_initiative');
        newGR.initialize();
        newGR.setWorkflow(false); // prevent sync-initiative-fields BR from overwriting the values set below

        newGR.setValue('u_name', sourceShortDesc);
        newGR.setValue('u_initiative', sourceSysId);
        newGR.setValue('u_snow_ref', sourceNumber);
        newGR.setValue('u_type', resolvedType);
        newGR.setValue('u_area', resolvedArea);
        newGR.setValue('u_tshirt_size', resolvedTshirt);
        newGR.setValue('u_priority', resolvedPriority);
        newGR.setValue('u_snow_status', resolvedSnowStatus);
        newGR.setValue('u_plan_status', ''); // explicitly empty - populated later by the status import set

        var newSysId = newGR.insert();
        gs.info('[GeneratePlanItems] Inserted: ' + sourceNumber + ' -> ' + newSysId);
        inserted++;
    } catch (ex) {
        gs.error('[GeneratePlanItems] Error inserting ' + sourceNumber + ': ' + ex.message);
        errors++;
    }
}

// ---- Final summary -------------------------------------------------------
var prefix = DRY_RUN ? '[DRY RUN] ' : '';
gs.info(
    '[GeneratePlanItems] ' + prefix + 'Complete. ' +
    'Skipped=' + skipped + ' ' +
    'Inserted=' + inserted + ' ' +
    'UnmappedArea=' + unmappedArea + ' ' +
    'UnmappedStatus=' + unmappedStatus + ' ' +
    'Errors=' + errors
);

// ============================================================
// VERIFICATION (after a real run, DRY_RUN = false)
// ============================================================
// 1. Re-run with DRY_RUN = true - should report inserted=0 (everything now
//    skipped as already-existing).
// 2. Spot check a few records:
//
//    var g = new GlideRecord('x_u4bsh_capmgmt_initiative');
//    g.addNotNullQuery('u_initiative');
//    g.setLimit(10);
//    g.query();
//    while (g.next()) {
//        gs.print(g.u_name + ' | area=' + g.u_area + ' | type=' + g.u_type +
//            ' | tshirt=' + g.u_tshirt_size + ' | priority=' + g.u_priority +
//            ' | snow_status=' + g.u_snow_status + ' | plan_status="' + g.u_plan_status + '"');
//    }
//
// 3. Confirm UnmappedArea/UnmappedStatus counts from the log. UnmappedStatus
//    should now be 0 - SNOW_STATUS_MAP covers all 7 source 'state' values, so
//    any hit means an unexpected state value worth investigating. UnmappedArea
//    still reflects the business_area_function lookup, which is unchanged.
// ============================================================
```

## Related documentation

- [[capacity-planner]] - full app overview, data model, roles/ACLs, Business Rules
- [[capacity-planner-set-start-and-end-date-to-plan-items]] - companion backfill note for `u_start`/`u_end`, same ACL-bypass reasoning (plain server-side `GlideRecord` doesn't enforce field ACLs)
- [[capacity-planner-backlog-2026-07]] — July 2026 backlog: CAPMGMT-02 (allocation import validation) converges the idempotency check pattern this script uses; CAPMGMT-03 hardens the allocation import path that follows this script's Plan Item generation
- [[access-control-rules]] - general ACL rule model
- [[business-rule-api-now-ts]] - Fluent API backing `sync-initiative-fields`, which this script intentionally bypasses via `setWorkflow(false)`
