---
title: "Activity set progress bar showing incorrect number of completed tasks"
aliases:
  - KB0959872
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0959872
kb_number: KB0959872
last_modified: 2025-09-03
---

## Activity set progress bar showing incorrect number of completed tasks

  

### Issue

Activity of type HR Task is getting set to completed in Activity set Execution even if HR task is still in Ready state

### Resolution

Fulfiller Acrtivity Configuration for HR Task Template that has for closure condition Optional = True  
  
Fulfiller Acrtivity Configuration - https://<Service Now Instance>.service-now.com/sn\_hr\_le\_fulfiller\_activity\_config\_list.do?sysparm\_query=fulfiller\_activity%3DHR%20Task&sysparm\_view=

HR Task Template associated to Affected HR Task set Optional = True which cause this Activity Status to set to Complete  
  
Please update HR Task Template and set Optional = false to resolve this Issue.
