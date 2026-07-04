---
title: "SAMP: Duplicate SAM Value Builder Task Numbers on samp_sp_vb_task Table"
aliases:
  - KB3024338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3024338
kb_number: KB3024338
last_modified: 2026-05-17
---

## SAMP: Duplicate SAM Value Builder Task Numbers on samp\_sp\_vb\_task Table

  

### Issue

 

Duplicate Number values exist on the SAM Value Builder Task (`samp_sp_vb_task`) table, causing records to be flagged during ServiceNow Health Scans.

### Symptoms

 

-   Two or more SAM Value Builder Task records share the same Number field value (e.g., `SVB0001014`, `SVB0001015`).
-   ServiceNow Health Scan results flag duplicate record numbers on the `samp_sp_vb_task` table.
-   The duplicate records have different Sys IDs but identical Number and Name values.

### Facts

 

The original (non-duplicate) records are installed via plugin XML with hardcoded Number values and Sys IDs. These records are consistent across all instances:

| Number | Name | Sys ID |
| --- | --- | --- |
| `SVB0001014` | Complete Microsoft SQL Server License Management Guided Setup | `82114d270f4d3110ebd9579ac4767ef7` |
| `SVB0001015` | Complete Microsoft Windows Server License Management Guided Setup | `fb744de70f4d3110ebd9579ac4767e77` |

The duplicate records are created by an update script during a plugin install or upgrade. These records share the same Number and Name across instances but have different Sys IDs per instance:

| Number | Name | Sys ID |
| --- | --- | --- |
| `SVB0001014` | Cisco Webex Meetings | _Instance-specific_ |
| `SVB0001015` | Roadmunk | _Instance-specific_ |

The duplicates do not impact the creation or numbering of new SAM Value Builder Tasks. UI Actions on `samp_usage_under_management`, `samp_sp_apps_and_plugins`, and `samp_sp_publisher_pack_utilization` correctly assign the next sequential Number when creating new tasks.

### Release

All Releases

### Cause

 

During a SAM plugin install or upgrade, an update script creates additional SAM Value Builder Task records (for Cisco Webex Meetings and Roadmunk) using hardcoded Number values that conflict with existing records already installed via the plugin XML. Because the original records have their Numbers baked into the XML rather than assigned by the `sys_number_counter` sequencer, the update script inadvertently reuses the same Number values, resulting in duplicates.

### Resolution

 

Run the background script below to renumber the duplicate records and update the `sys_number_counter` sequencer so that future records continue in the correct sequence.

### Before You Begin

-   The script includes a dry-run mode enabled by default (`dryRun = true`). Run it in dry-run mode first to review the planned changes in the system logs before committing.
-   Validate the output in the system logs to confirm the correct records are identified for renumbering.
-   Once satisfied, set `dryRun = false` and run the script again to apply the changes.

### Steps

1.  Navigate to **System Definition > Scripts - Background**.
2.  Paste the script below into the editor.
3.  Run the script with `dryRun = true` (default) and review the output in the system logs.
4.  Confirm the correct duplicate records are identified and the proposed new Numbers are appropriate.
5.  Set `dryRun = false` and run the script again to apply the changes.
6.  Verify the duplicates have been renumbered by checking the `samp_sp_vb_task` table.
7.  Re-run the Health Scan to confirm the duplicate number findings are resolved.

### Background Script

// =========================================================================== // Fix Duplicate Numbers on samp\_sp\_vb\_task // =========================================================================== // PURPOSE: Finds duplicate Number values, renumbers the newer duplicates // with the next available numbers, and updates the sys\_number\_counter // sequencer so future records continue in sequence. // // TABLE: samp\_sp\_vb\_task (SAM Value Builder Tasks) // PREFIX: SBV // // ⚠️ DRY RUN MODE: Set dryRun = false to commit changes. // =========================================================================== var dryRun = true; // Set to false to apply changes var duplicateMap = {}; var ga = new GlideAggregate('samp\_sp\_vb\_task'); ga.addAggregate('COUNT', 'number'); ga.addHaving('COUNT', 'number', '>', 1); ga.query(); while (ga.next()) { var dupNumber = ga.getValue('number'); var records = \[\]; var gr = new GlideRecord('samp\_sp\_vb\_task'); gr.addQuery('number', dupNumber); gr.orderBy('sys\_created\_on'); gr.query(); while (gr.next()) { records.push({ sys\_id: gr.getUniqueValue(), number: gr.getValue('number'), created\_on: gr.getValue('sys\_created\_on') }); } duplicateMap\[dupNumber\] = records; } var toRenumber = \[\]; for (var num in duplicateMap) { var set = duplicateMap\[num\]; gs.info('Duplicate Number: ' + num + ' — ' + set.length + ' records found'); gs.info(' Keeping oldest: sys\_id=' + set\[0\].sys\_id + ', created\_on=' + set\[0\].created\_on); for (var i = 1; i < set.length; i++) { gs.info(' Will renumber: sys\_id=' + set\[i\].sys\_id + ', created\_on=' + set\[i\].created\_on); toRenumber.push(set\[i\].sys\_id); } } if (toRenumber.length === 0) { gs.info('No duplicate Numbers found. No changes needed.'); } else { gs.info('Total records to renumber: ' + toRenumber.length); var grMax = new GlideRecord('samp\_sp\_vb\_task'); grMax.orderByDesc('number'); grMax.setLimit(1); grMax.query(); var highestNumber = 0; if (grMax.next()) { var currentMax = grMax.getValue('number'); highestNumber = parseInt(currentMax.replace(/\[^0-9\]/g, ''), 10); gs.info('Current highest Number on table: ' + currentMax + ' (numeric: ' + highestNumber + ')'); } var sampleNumber = grMax.getValue('number'); var numericPart = sampleNumber.replace(/^\[A-Za-z\]+/, ''); var padLength = numericPart.length; var nextNumber = highestNumber; for (var j = 0; j < toRenumber.length; j++) { nextNumber++; var paddedNum = String(nextNumber); while (paddedNum.length < padLength) { paddedNum = '0' + paddedNum; } var newNumber = 'SBV' + paddedNum; var grUpdate = new GlideRecord('samp\_sp\_vb\_task'); if (grUpdate.get(toRenumber\[j\])) { var oldNumber = grUpdate.getValue('number'); if (dryRun) { gs.info('\[DRY RUN\] Would update sys\_id=' + toRenumber\[j\] + ': ' + oldNumber + ' → ' + newNumber); } else { grUpdate.setValue('number', newNumber); grUpdate.setWorkflow(false); grUpdate.autoSysFields(false); grUpdate.update(); gs.info('Updated sys\_id=' + toRenumber\[j\] + ': ' + oldNumber + ' → ' + newNumber); } } } var grSeq = new GlideRecord('sys\_number\_counter'); grSeq.addQuery('table', 'samp\_sp\_vb\_task'); grSeq.query(); if (grSeq.next()) { var oldSeqNumber = grSeq.getValue('number'); if (dryRun) { gs.info('\[DRY RUN\] Would update sys\_number\_counter sequencer from ' + oldSeqNumber + ' → ' + nextNumber); } else { grSeq.setValue('number', nextNumber); grSeq.update(); gs.info('Updated sys\_number\_counter sequencer: ' + oldSeqNumber + ' → ' + nextNumber); } } else { gs.warn('Could not find sys\_number\_counter record for samp\_sp\_vb\_task. Check the category value manually.'); } gs.info('============================================================'); if (dryRun) { gs.info('DRY RUN COMPLETE. Set dryRun = false to apply changes.'); } else { gs.info('COMPLETE. ' + toRenumber.length + ' records renumbered. Sequencer updated to ' + nextNumber + '.'); } }   

### Script Behavior Summary

1.  **Identifies duplicates** — Queries the `samp_sp_vb_task` table using `GlideAggregate` to find Number values with more than one record.
2.  **Preserves the oldest record** — For each duplicate set, the record with the earliest `sys_created_on` timestamp retains its original Number.
3.  **Renumbers newer duplicates** — Assigns the next available sequential Number (based on the current highest Number on the table) to each duplicate.
4.  **Updates the sequencer** — Modifies the `sys_number_counter` record for `samp_sp_vb_task` so future records continue from the correct value.
5.  **Respects system fields** — Uses `setWorkflow(false)` and `autoSysFields(false)` to prevent business rules from firing and to preserve the original `sys_updated_on` and `sys_updated_by` values.

This is a cosmetic issue only. The duplicate Numbers do not affect SAM Value Builder Task functionality or the creation of new tasks. The resolution is recommended to clear Health Scan findings.

### Related Links

 

-   [SAM Value Builder](https://docs.servicenow.com/bundle/latest/page/product/software-asset-management2/concept/sam-value-builder.html)
-   [Auto-numbering](https://docs.servicenow.com/bundle/latest/page/administer/auto-numbering/concept/c_AutoNumbering.html)
