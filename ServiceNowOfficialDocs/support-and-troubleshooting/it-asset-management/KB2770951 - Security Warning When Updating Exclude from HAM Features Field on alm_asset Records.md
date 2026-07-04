---
title: "Security Warning When Updating \"Exclude from HAM Features\" Field on alm_asset Records"
aliases:
  - KB2770951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2770951
kb_number: KB2770951
last_modified: 2026-05-12
---

## Security Warning When Updating "Exclude from HAM Features" Field on alm\_asset Records

  

# Security Warning When Updating "Exclude from HAM Features" Field on alm\_asset Records

## Issue

Records in the `alm_asset` table have the Exclude from HAM features (`exclude_from_ham`) field set to an incorrect `true`/`false` value. Attempting to update the field through the UI returns a Security warning, preventing the correction.

## Symptoms

-   Manually editing the `exclude_from_ham` field on an `alm_asset` record produces a "Security warning" message and the update is blocked.
-   Bulk list-edit or update-set attempts against the field fail with the same security warning.
-   The incorrect field values may have been set by a HAM reconciliation or normalization job.

## Facts

-   Table: `alm_asset`
-   Field: `exclude_from_ham` (Exclude from HAM features)
-   Relevant plugins: Hardware Asset Management (HAM)
-   The "Security warning" message is the platform's standard indicator of an ACL denial on a write operation.

## Cause

One or more of the following platform protections is blocking the update:

1.  ACL restriction — A write or update ACL exists on `alm_asset.exclude_from_ham` (or the parent `alm_asset.*`) that the current user's roles do not satisfy. The "Security warning" message confirms an ACL denial.
2.  Data Policy — A server-side data policy on the `alm_asset` table may be enforcing the field as read-only under certain conditions.
3.  Business Rule validation — An out-of-box Business Rule from the HAM plugin may be validating or reverting changes to the field based on asset class, model category, or license entitlement conditions.

## Solution

### Step 1: Diagnose the blocking mechanism

1.  Enable Security Debug Navigate to System Diagnostics > Session Debug > Debug Security, then attempt the update again. The debug output identifies exactly which ACL is denying the write.
    
2.  Review ACLs Navigate to System Security > Access Control (ACL) and filter on `alm_asset.exclude_from_ham`. Examine any write/update ACL rules and verify whether your roles satisfy the conditions.
    
3.  Review Data Policies Navigate to System Policy > Data Policies and filter to the `alm_asset` table. Look for any policy targeting the `exclude_from_ham` field.
    
4.  Review Business Rules Navigate to System Definition > Business Rules and filter to the `alm_asset` table. Search for rules that reference `exclude_from_ham`, particularly `before` insert/update rules.
    

### Step 2: Resolve the restriction

-   If the cause is an ACL, ensure the updating user holds the required role (commonly `asset` or `ham_admin`). Alternatively, elevate to `security_admin` to review and adjust the ACL.
-   If a Data Policy is enforcing read-only status, evaluate whether the policy condition should be adjusted or an exception added.
-   If a Business Rule is reverting the change, determine whether the rule logic is functioning as intended for your use case.

### Step 3: Bulk-correct records with a background script

When multiple records require correction, use the following background script. The script includes a dry-run mode, logging, and safety filters.

> Important considerations before running:
> 
> -   Run the dry-run first. The script defaults to `DRY_RUN = true` and only lists what it would update. Review the system log output before setting the flag to `false`.
> -   `setWorkflow(false)` bypasses Business Rules, which should circumvent the security warning. If you are still blocked, run the script under an account with the `security_admin` elevated privilege.
> -   `autoSysFields(false)` preserves the original `sys_updated_on` and `sys_updated_by` values so the update does not appear as a mass record touch.
> -   Safety filter — The script automatically skips records that already have the correct value.
> -   Post-update risk — Because `setWorkflow(false)` skips Business Rules, it also skips any HAM normalization logic that would re-evaluate the field. If a reconciliation job runs after this update, it may revert your changes. Confirm the root cause of the incorrect values (e.g., model category mappings, asset class) to prevent recurrence.

```
/**
 * Background Script: Update "Exclude from HAM features" on alm_asset
 *
 * PRODUCTION SAFE — Includes dry-run mode, logging, and batch control.
 *
 * Instructions:
 *   1. Set DRY_RUN = true and run first to validate record counts and targets.
 *   2. Replace the encoded queries below with your actual filters.
 *   3. Review the output log carefully.
 *   4. Set DRY_RUN = false and run again to commit changes.
 */

// ============================================================
// CONFIGURATION
// ============================================================
var DRY_RUN = true; // <-- Set to false to commit changes

// Records that should be set to TRUE (currently incorrectly false)
var QUERY_SET_TRUE = 'YOUR_ENCODED_QUERY_HERE'; // e.g. 'sys_idINsys_id1,sys_id2,sys_id3'

// Records that should be set to FALSE (currently incorrectly true)
var QUERY_SET_FALSE = 'YOUR_ENCODED_QUERY_HERE'; // e.g. 'sys_idINsys_id1,sys_id2,sys_id3'

// ============================================================
// SCRIPT — Do not modify below unless needed
// ============================================================

var totalUpdated = 0;
var errors = [];

function updateRecords(encodedQuery, newValue) {
    if (!encodedQuery || encodedQuery === 'YOUR_ENCODED_QUERY_HERE') {
        gs.info('>>> Skipping — no query provided for exclude_from_ham = ' + newValue);
        return;
    }

    var gr = new GlideRecord('alm_asset');
    gr.addEncodedQuery(encodedQuery);

    // Safety: only target records that actually need changing
    gr.addQuery('exclude_from_ham', !newValue);
    gr.query();

    var count = gr.getRowCount();
    gs.info('>>> Found ' + count + ' record(s) to set exclude_from_ham = ' + newValue);

    if (DRY_RUN) {
        gs.info('>>> DRY RUN — Listing records that would be updated:');
        while (gr.next()) {
            gs.info('    [DRY RUN] ' + gr.getDisplayValue() +
                ' | sys_id: ' + gr.getUniqueValue() +
                ' | Current value: ' + gr.getValue('exclude_from_ham') +
                ' | Asset tag: ' + gr.getValue('asset_tag') +
                ' | Model: ' + gr.getDisplayValue('model'));
        }
        return;
    }

    // Live run
    while (gr.next()) {
        try {
            gr.setValue('exclude_from_ham', newValue);
            gr.setWorkflow(false);    // Skip business rules
            gr.autoSysFields(false);  // Preserve sys_updated_on/by
            var result = gr.update();

            if (result) {
                totalUpdated++;
                gs.info('    [UPDATED] ' + gr.getDisplayValue() +
                    ' | sys_id: ' + result +
                    ' | exclude_from_ham → ' + newValue);
            } else {
                var errMsg = 'Failed to update sys_id: ' + gr.getUniqueValue() +
                    ' | ' + gr.getDisplayValue();
                errors.push(errMsg);
                gs.error('    [ERROR] ' + errMsg);
            }
        } catch (e) {
            var catchMsg = 'Exception on sys_id: ' + gr.getUniqueValue() + ' | ' + e.message;
            errors.push(catchMsg);
            gs.error('    [EXCEPTION] ' + catchMsg);
        }
    }
}

gs.info('==========================================================');
gs.info('Update Exclude from HAM Features — ' + (DRY_RUN ? 'DRY RUN' : 'LIVE RUN'));
gs.info('==========================================================');

// Process both sets
updateRecords(QUERY_SET_TRUE, true);
updateRecords(QUERY_SET_FALSE, false);

gs.info('==========================================================');
if (DRY_RUN) {
    gs.info('DRY RUN complete — Review output above. Set DRY_RUN = false to commit.');
} else {
    gs.info('LIVE RUN complete — Total updated: ' + totalUpdated);
    if (errors.length > 0) {
        gs.info('Errors encountered: ' + errors.length);
        errors.forEach(function(err) { gs.error('  ' + err); });
    }
}
gs.info('==========================================================');
```

### Step 4: Prevent recurrence

If the incorrect values were set by a HAM reconciliation or normalization job, address the root cause rather than relying on manual field overrides. Review and correct the following as applicable:

-   Model category mappings
-   Asset class assignments
-   License entitlement configurations

Correcting these upstream inputs ensures the normalization job sets the `exclude_from_ham` field to the intended value on subsequent runs.
