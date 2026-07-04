---
title: "\"Save\" Button Disabled When Editing Journey Task in Portal"
aliases:
  - KB2631063
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2631063
kb_number: KB2631063
last_modified: 2026-01-03
---

## "Save" Button Disabled When Editing Journey Task in Portal

  

### Issue

When editing a Journey task in the portal, the Save button remains disabled and the date field is shown as mandatory, even after entering all required details.  
This issue occurs in both draft and published states and was also observed in the out-of-the-box (OOB) instance.  
Users are unable to save changes to tasks, impacting workflow in Journey Designer.

### Release

Any Release

### Cause

The issue is related to the Journey Designer plugin version. Older versions of the plugin do not properly validate date fields, causing the Save button to remain disabled even when all required fields are filled.

### Resolution

**Check Plugin Version**

-   Navigate to System Definition → Plugins.
-   Search for Journey Designer.
-   Verify the installed version.

**Upgrade or Repair Plugin**

-   If the version is older than 5.0.2, upgrade the plugin to 5.0.2 or the latest available version.
-   If the plugin is already on the latest version but still causing issues, click Repair to reload missing components.

**Validate After Upgrade**

-   Open the portal and edit a Journey task.
-   Select a future date in the mandatory date field.
-   Confirm that the Save button becomes active and changes can be saved.

**Optional Checks**

-   Clear browser cache and refresh the portal.
-   Test in both draft and published states to ensure consistency.
