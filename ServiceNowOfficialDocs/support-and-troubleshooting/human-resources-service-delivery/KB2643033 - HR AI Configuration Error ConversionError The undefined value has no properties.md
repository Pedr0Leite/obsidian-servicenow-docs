---
title: "HR AI Configuration Error: \"ConversionError: The undefined value has no properties\""
aliases:
  - KB2643033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2643033
kb_number: KB2643033
last_modified: 2025-12-16
---

## HR AI Configuration Error: "ConversionError: The undefined value has no properties"

  

### Issue

The error originates from an out-of-the-box script include (`HR_MLPortalUtilsSNC`) and related widgets. Despite successful ML solution training, the error continued across multiple plugin versions and instances.

### Release

Any

### Cause

-   The script include attempted to access properties of an undefined value during HR AI configuration processing.
-   The issue was confirmed as an OOTB defect, not related to customer customization.
-   Plugin upgrades and widget reversion did not eliminate the error.

### Resolution

If this error occurs:

-   Check error source: Review logs to confirm the error originates from `HR_MLPortalUtilsSNC` and related portal widgets.
-   Validate ML training: Ensure the ML solution training completes successfully (though this may not resolve the error).
-   Apply temporary fix: Add error handling in the script include to prevent undefined value access. This can stop the error from flooding logs.
-   Revert widgets if modified: Confirm widgets are at store/OOTB versions to rule out customization issues.
-   Upgrade plugins: Ensure the Employee Center and HR plugins are at the latest version.
