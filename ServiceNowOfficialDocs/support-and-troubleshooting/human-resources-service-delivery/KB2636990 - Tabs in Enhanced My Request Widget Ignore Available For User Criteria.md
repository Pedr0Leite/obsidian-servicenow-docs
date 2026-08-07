---
title: "Tabs in Enhanced My Request Widget Ignore \"Available For\" User Criteria"
aliases:
  - KB2636990
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636990
kb_number: KB2636990
last_modified: 2026-01-01
---

## Tabs in Enhanced My Request Widget Ignore "Available For" User Criteria

  

### Issue

Tabs configured with "Available For" user criteria in the Enhanced My Request widget are visible to all users, regardless of criteria.  
Expected behavior: Tabs should be hidden unless the user meets the specified criteria.  
Observed behavior: Tabs remain visible for all users, even with custom or out-of-box filter configurations.

### Release

Any Release

### Cause

-   Root cause identified as a typo in the script include `sn_ex_sp.RequestUtilSNC`:
    -   Field misspelled as `avaiilable_for` instead of `available_for`.
-   This impacted user criteria evaluation for "Available For", while "Not Available For" worked correctly.

### Resolution

·  The typo was corrected and will be included in the Employee Center Bundle October Patch Release (scheduled for October 16, 2025).

·  Recommended solution:

-   Upgrade to the October Patch Release to resolve the issue automatically.
-   Test the fix in a development environment before applying to production.

·  A Problem Record (PRB1648487) was logged for tracking this defect and its resolution.

·  Additional troubleshooting steps attempted:

-   Verified user criteria diagnostics.
-   Checked role elevation and XML import/export.
-   Confirmed direct code modification was blocked due to read-only protection.
