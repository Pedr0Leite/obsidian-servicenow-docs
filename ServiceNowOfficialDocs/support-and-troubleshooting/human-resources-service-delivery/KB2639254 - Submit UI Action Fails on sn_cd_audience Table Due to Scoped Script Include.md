---
title: "Submit UI Action Fails on sn_cd_audience Table Due to Scoped Script Include"
aliases:
  - KB2639254
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639254
kb_number: KB2639254
last_modified: 2026-01-01
---

## Submit UI Action Fails on sn\_cd\_audience Table Due to Scoped Script Include

  

### Issue

The Submit UI Action on the `sn_cd_audience` table fails to insert new records and displays an error. The issue occurs because the ScanAjaxProcessor Script Include is scoped incorrectly, causing execution failures.

### Release

Any Release

### Cause

The Script Include `ScanAjaxProcessor` is scoped to a specific application instead of Global, which prevents the UI Action from executing as expected.

### Resolution

To resolve this issue:

1.  Verify Plugin Version

1.  -   Navigate to System Definition > Plugins.
    -   Search for Content Publishing and confirm the version.

2.  Remove Temporary Workarounds

2.  -   If any custom workaround was applied to the UI Action, revert those changes to restore the original configuration.

3.  Upgrade Content Publishing Plugin

3.  -   Go to System Definition > Plugins.
    -   Select Content Publishing and click Upgrade.
    -   Upgrade to version 34.0.5 or later, which includes the fix for PRB1725045.

4.  Validate the Fix

4.  -   After the upgrade, navigate to the `sn_cd_audience` table.
    -   Test the Submit UI Action by creating a new record.
    -   Confirm that the record is inserted successfully without errors.

5.  Reference Documentation

5.  -   Review PRB1725045 for details on the fix.
