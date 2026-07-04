---
title: " Unable to View Model Categories While Configuring CMDB Success Advisor from CMDB Workspace"
aliases:
  - KB2757655
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2757655
kb_number: KB2757655
last_modified: 2026-02-10
---

## Unable to View Model Categories While Configuring CMDB Success Advisor from CMDB Workspace

  

### Issue

When configuring CMDB Success Advisor from the CMDB Workspace, model categories do not appear for selection, and the UI displays “Available resource and model categories \[0\]”. This behavior occurs when all Hardware Asset Management (HAM) resource categories are in an opt-out state.

### Symptoms

While setting up CMDB Success Advisor from CMDB Workspace, no model categories are available for selection.

The configuration page shows:

-   Available resource and model categories \[0\]

-   CMDB Success Advisor setup cannot proceed due to missing model categories.

![](/sys_attachment.do?sys_id=79cc41ea97fa76d0539e35d11153afdd)

### Release

ALL

### Cause

If Hardware Asset Management (HAM) is installed, at least one HAM resource category must be opted in.

In some instances, all HAM resource categories are set to Opt-in = false (opted out). When this happens:

-   CMDB Success Advisor cannot retrieve model categories
-   The UI displays zero available categories

This behavior is expected and by design.

![](/sys_attachment.do?sys_id=80adc5ea973e76d0539e35d11153afc7)

### Resolution

Opt in at least one Hardware Asset Management (HAM) resource category.

Once a resource category is opted in, CMDB Success Advisor will successfully display model categories during setup.

1.  Navigate to the following table:

-   -   sn\_hamp\_resource\_category.list

1.  Open any Hardware Asset Management (HAM) Resource Category record.
2.  Set Opt in = true for at least one resource category.
3.  Save the record.
4.  Return to CMDB Workspace.
5.  Re-run or refresh the CMDB Success Advisor setup.

Model categories should now be visible and available for selection.
