---
title: "HRM Todos Summary widget is refreshing when comments are added to task"
aliases:
  - KB2708184
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2708184
kb_number: KB2708184
last_modified: 2026-01-07
---

## HRM Todos Summary widget is refreshing when comments are added to task

  

### Issue

HRM Todos Summary widget is refreshing/reloading list when comments are added to task

### Release

Any

### Cause

We have record watchers set up in the 'hrm-todos-summary' widget for all approvals and tasks shown on the My Task page, so any record changes other than comments and worknotes are immediately reflected by refreshing the widget.  
  
Widget Link:  
https://"INSTANCE".service-now.com/nav\_to.do?uri=sp\_widget.do?sys\_id=bdc676957317130030f331d7caf6a74d  
  
  
  

### Resolution

Verify whether adding comments to a task in the HRM Todos Summary widget also results in updates to other fields on the task record and make changes as needed.
