---
title: "Excessive White Space and Inconsistent Tab Width in Microsite Tabs"
aliases:
  - KB2636792
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636792
kb_number: KB2636792
last_modified: 2026-01-01
---

## Excessive White Space and Inconsistent Tab Width in Microsite Tabs

  

### Issue

When browsing between tabs in a microsite, excessive white space appears, especially with many tabs or long text.

-   Tab layout changes unpredictably when switching between tabs.
-   Navigation becomes unclear and inconsistent for users.

### Release

Any Release

### Cause

The issue is related to tab layout and spacing in the microsite, specifically with the Rich Content (CD) widget.  
Older versions of the widget contained a CSS selector that caused inconsistent tab width and spacing.  
Although the instance was on version 33.0.3, the problematic content was created using an older widget version.

### Resolution

1.  Verify the widget version:
    -   Navigate to Widget Instances and confirm the version of Rich Content (CD).
    -   If the version is older than 32.0.0, update to the latest version (recommended: 33.0.9).
2.  Recreate the tabs using the current widget version:
    -   Add a new tab element in the microsite.
    -   Manually enter tab titles (avoid copy-paste to prevent formatting issues).
    -   Move the existing tab content into the newly created tabs.
3.  Save and publish the updated microsite.
4.  Test navigation between tabs to confirm consistent tab width and removal of excessive white space.

Additional Info:

-   The issue was resolved in widget version 32.0.0 and later.
-   Updating to the latest version ensures compatibility and fixes layout inconsistencies.
