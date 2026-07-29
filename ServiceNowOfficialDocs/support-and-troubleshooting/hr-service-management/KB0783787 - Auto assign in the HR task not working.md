---
title: "Auto assign in the HR task not working"
aliases:
  - KB0783787
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783787
kb_number: KB0783787
last_modified: 2025-10-15
---

## Auto assign in the HR task not working

  

### Issue

How to make the HR tasks unassigned when an HR LifeCycle is created.

### Release

New York Patch 1 Hot Fix 1a

### Cause

The instance has configured Assignment Groups in his HR task templates which are used in Activities. When Assignment group is populated and assigned\_to is empty the HR Matching Rules will assign the tasks. If this functionality is not required then inactivate the Matching rules of HR tasks, This can be found under HR Administration -> Assignment Rules -> HR Matching Rules. 

### Resolution

There are 2 matching rules on HR Task, Agents by skills and country and HR Task, Agents by skills, if these two are disabled then the tasks won't be auto-assigned.

The matching rules will be triggered form the Business Rule on HR Task called Auto Assign. DIsabling this BR also will prevent the auto-assign.
