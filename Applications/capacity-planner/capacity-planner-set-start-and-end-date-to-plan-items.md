---
title: Backfill Plan Item Start/End Dates (Fix Script)
tags:
  - servicenow
  - capacity-planning
  - internal-tool
  - scoped-app
  - fix-script
  - business-rules
  - data-remediation
  - access-control
aliases:
  - capmgmt-date-backfill
  - backfillPlanItemDates
date: 2026-07-02
---

# Backfill Plan Item Start/End Dates

## Context

[[capacity-planner|Capacity Management Overview (x_u4bsh_capmgmt)]] derives each Plan Item's (`x_u4bsh_capmgmt_initiative`) `u_start`/`u_end` fields via the **derive-initiative-dates** Business Rule, which fires *after insert/update/delete* on `x_u4bsh_capmgmt_allocation` and recomputes the min/max of the linked Periods' start/end dates.

That BR only fires on allocation changes going forward — it never runs retroactively. Any initiative whose allocations were created before the BR existed, or loaded via direct import/data load, can end up with `u_start`/`u_end` blank or stale, with no allocation-side trigger to fix it.

This note documents a one-time Fix Script (`backfillPlanItemDates`) that replicates the BR's derivation logic across **every existing initiative**, for exactly that situation.

## Summary of what the script does

1. Iterates every `x_u4bsh_capmgmt_initiative` record.
2. For each one, queries its `x_u4bsh_capmgmt_allocation` rows where `u_period` is not empty, ordered by `u_period.u_start_date` (chronological — the legacy `u_month` field has no year and can't produce a real date, so allocations without `u_period` are skipped, matching existing BR behavior).
3. Tracks the earliest linked Period's `u_start_date` and the latest linked Period's `u_end_date`.
4. Writes those back to the initiative as `u_start`/`u_end` in `YYYY-MM` format — but only if the computed value actually differs from what's currently stored.
5. Logs a dry-run preview by default (`DRY_RUN = true`) before any writes happen.

## Key gotchas (why this isn't a trivial script)

- **ACL bypass is intentional, not a workaround.** `u_start`/`u_end` carry a hard deny-all-writes field ACL (`answer = true`, `adminOverrides: false` — see [[capacity-planner#4. Roles & Permissions|Roles & Permissions]]). That ACL is enforced for `GlideRecordSecure`, Scripted REST APIs, GlideAjax, and UI/form submissions — **not** for plain server-side `GlideRecord`, which is what Business Rules and Fix Scripts use. This is exactly how `derive-initiative-dates` is able to write these fields in production, and why this script can too. Never port this logic behind `GlideRecordSecure` or a Scripted REST endpoint — it will be silently blocked there.
- **Must run in-scope.** These are scoped-app tables (`x_u4bsh_capmgmt_*`). Create the Fix Script with its **Application** field set to *Capacity Management Overview*, not Global — otherwise it will hit cross-scope access restrictions unless the tables are explicitly marked "Accessible from: All application scopes."
- **Ordering by `u_period`, not `u_month`.** `u_period` is the year-aware field (see [[capacity-planner#10. Known Issues / Architectural Debt|Known Issues]] — the multi-year migration is incomplete); ordering/deriving dates from the bare `u_month` choice field would be wrong since it carries no year.

## The script

```javascript
// ============================================================================
// Fix Script: Backfill x_u4bsh_capmgmt_initiative.u_start / u_end
// App: Capacity Management Overview (x_u4bsh_capmgmt)
// ============================================================================
// WHY THIS EXISTS
// derive-initiative-dates (Business Rule, after insert/update/delete on
// x_u4bsh_capmgmt_allocation) only fires when an allocation changes. It does
// NOT run retroactively, so any initiative whose allocations were created
// before that BR existed (or via a direct data load / import) can have
// u_start/u_end blank or stale. This is a one-time backfill that replicates
// the BR's derivation logic across every existing initiative.
//
// ACL NOTE
// u_start/u_end carry a hard deny-all-writes field ACL
// (script: `answer = true`, adminOverrides: false). That ACL is enforced for
// GlideRecordSecure, Scripted REST APIs, GlideAjax, and UI/form submissions -
// it is NOT enforced for plain server-side GlideRecord, which is what
// Business Rules and Fix Scripts use. That's exactly how derive-initiative-dates
// is able to write these fields today, and it's why this script can too.
// Do not port this logic behind GlideRecordSecure or a Scripted REST endpoint -
// it will be silently blocked there.
//
// SCOPE NOTE
// x_u4bsh_capmgmt_initiative/allocation/period are scoped-app tables. Unless
// this app's tables are marked "Accessible from: All application scopes" (or
// a Cross Scope Privilege exists for Global), a Fix Script created in Global
// scope will fail to read/write them. Create this Fix Script WITH THE
// APPLICATION FIELD SET TO "Capacity Management Overview" (or run it from a
// Background Script with that scope selected in Studio) so it executes
// in-scope and cross-scope restrictions don't apply.
//
// ORDERING
// Allocations are ordered by u_period so the earliest/latest linked period
// drives u_start/u_end. u_period.u_start_date / u_end_date are real dates,
// so ordering by u_period.u_start_date gives a correct chronological
// sequence (unlike the legacy u_month field, which has no year and can't be
// used to derive real dates - allocations with u_period empty are skipped,
// matching what the existing BR already does).
// ============================================================================

(function backfillPlanItemDates() {

    var DRY_RUN = true; // set to false only after reviewing the dry-run log output
    var updatedCount = 0;
    var unchangedCount = 0;
    var skippedNoPeriodCount = 0;

    var initGr = new GlideRecord('x_u4bsh_capmgmt_initiative');
    initGr.query();

    while (initGr.next()) {
        var minStart = null; // 'YYYY-MM-DD' string, lexicographically comparable
        var maxEnd = null;

        var allocGr = new GlideRecord('x_u4bsh_capmgmt_allocation');
        allocGr.addQuery('u_initiative', initGr.getUniqueValue());
        allocGr.addNotNullQuery('u_period');
        allocGr.orderBy('u_period.u_start_date'); // chronological, as requested
        allocGr.query();

        while (allocGr.next()) {
            var periodStartVal = allocGr.u_period.u_start_date.getValue();
            var periodEndVal = allocGr.u_period.u_end_date.getValue();

            if (periodStartVal && (minStart === null || periodStartVal < minStart)) {
                minStart = periodStartVal;
            }
            if (periodEndVal && (maxEnd === null || periodEndVal > maxEnd)) {
                maxEnd = periodEndVal;
            }
        }

        if (minStart === null || maxEnd === null) {
            // No allocations linked to a Period record - nothing to derive from.
            // (Allocations still on the legacy u_month-only field can't produce
            // a real date; this matches current BR behavior.)
            skippedNoPeriodCount++;
            continue;
        }

        var newStart = minStart.substring(0, 7); // 'YYYY-MM'
        var newEnd = maxEnd.substring(0, 7);

        if (initGr.getValue('u_start') === newStart && initGr.getValue('u_end') === newEnd) {
            unchangedCount++;
            continue;
        }

        gs.info('[backfillPlanItemDates] ' + initGr.getValue('u_name') +
            ' (' + initGr.getUniqueValue() + '): u_start ' +
            initGr.getValue('u_start') + ' -> ' + newStart + ', u_end ' +
            initGr.getValue('u_end') + ' -> ' + newEnd);

        if (!DRY_RUN) {
            initGr.setValue('u_start', newStart);
            initGr.setValue('u_end', newEnd);
            initGr.setWorkflow(false); // this is a mechanical backfill, not a user edit
            initGr.autoSysFields(false); // don't touch sys_updated_on/by for a backfill
            initGr.update();
        }

        updatedCount++;
    }

    gs.info('[backfillPlanItemDates] DRY_RUN=' + DRY_RUN +
        ' | updated=' + updatedCount +
        ' | unchanged=' + unchangedCount +
        ' | skipped (no linked period)=' + skippedNoPeriodCount);

})();

// ============================================================================
// VERIFICATION (run after the real pass, DRY_RUN = false)
// ============================================================================
// 1. Re-run this script with DRY_RUN left true - it should now report
//    updated=0 (nothing left to change) and the same skipped count as before.
// 2. Spot check a few records directly:
//
//    var g = new GlideRecord('x_u4bsh_capmgmt_initiative');
//    g.addNotNullQuery('u_start');
//    g.setLimit(10);
//    g.query();
//    while (g.next()) {
//        gs.print(g.u_name + ': ' + g.u_start + ' -> ' + g.u_end);
//    }
//
// 3. Cross-check one record's derived dates by hand against its allocations'
//    linked periods (x_u4bsh_capmgmt_allocation.u_period.u_start_date/u_end_date)
//    to confirm the min/max logic matches derive-initiative-dates.
// ============================================================================
```

## Related documentation

- [[capacity-planner]] — full app overview, data model, roles/ACLs, Business Rules
- [[generate-capacity-plan-items]] — companion bulk-creation script; Plan Items it generates are exactly the ones this backfill later fixes dates for once allocations exist
- [[access-control-rules]] — general ACL rule model, relevant to why this bypass works
- [[acl-function-fields]] — field-level ACL mechanics for `u_start`/`u_end`
- [[business-rule-api-now-ts]] — Fluent API backing `derive-initiative-dates`
