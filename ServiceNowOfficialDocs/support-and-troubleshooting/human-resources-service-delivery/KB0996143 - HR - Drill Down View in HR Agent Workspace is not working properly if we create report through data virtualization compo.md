---
title: "HR - Drill Down View in HR Agent Workspace is not working properly if we create report through data virtualization component"
aliases:
  - KB0996143
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996143
kb_number: KB0996143
last_modified: 2024-08-16
---

## HR - Drill Down View in HR Agent Workspace is not working properly if we create report through data virtualization component

  

### Issue

Drill Down View in HR Agent Workspace is not working properly if we create report through data virtualization component

### Cause

1.  Navigate to "sys\_ui\_list.list" from platform and filter by Table: "=sn\_hr\_core\_case", View: "=Default view", Parent: "=NULL" and User: "=NULL"
2.  Observed that there are three list records for the same Default view
3.  This is causing the list to get overlapped with the views and showing one column.

### Resolution

1.  Login as admin
2.  Navigate to "sys\_ui\_list.list" from platform and filter by Table: "=sn\_hr\_core\_case", View: "=Default view", Parent: "=NULL" and User: "=NULL"
3.  Delete the unnecessary list views (Default views) except one Default view
4.  Navigate to HR Case Management --> All HR Cases --> All
5.  Make a right click on any of the column header and navigate to "Configure --> List Layout"
6.  Configure the necessary columns displayed to the Default view and save.
