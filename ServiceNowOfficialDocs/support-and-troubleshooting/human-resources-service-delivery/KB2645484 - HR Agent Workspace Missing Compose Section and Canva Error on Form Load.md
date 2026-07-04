---
title: "HR Agent Workspace Missing \"Compose\" Section and Canva Error on Form Load"
aliases:
  - KB2645484
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2645484
kb_number: KB2645484
last_modified: 2026-01-03
---

## HR Agent Workspace Missing "Compose" Section and Canva Error on Form Load

  

### Issue

The HR Agent Workspace does not display the Compose section on form load, causing a Canva Error. The section appears only after manual navigation reload.

### Release

Any

### Cause

The system property `glide.activity.api_version` was set to 0 in the affected instance. This property controls the activity stream API version and should be set to 1 by default starting from the Tokyo release.

### Resolution

If the Compose section is missing and a Canva Error occurs in HR Agent Workspace:

1.  Verify the system property  
    Navigate to System Properties and check the value of `glide.activity.api_version`.
2.  Update the property

2.  -   If the value is set to 0, change it to 1.
    -   This property should be set to 1 by default starting from the Tokyo release.

3.  Clear cache and reload  
    After updating the property, clear the instance cache and reload the HR Agent Workspace to confirm the Compose section appears.
4.  Validate across workspaces  
    Check both HR Agent Workspace and CSM Workspace to ensure the issue is resolved.
5.  Monitor after change  
    Confirm that no further Canva errors occur after the update.
6.  Investigate root cause if needed  
    If the property was incorrectly set to 0, review instance history
