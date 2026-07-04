---
title: "Unable to edit HR Template"
aliases:
  - KB0784338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784338
kb_number: KB0784338
last_modified: 2024-04-07
---

## Unable to edit HR Template

  

### Issue

It's not possible to edit HR templates even with Admin Access.

### Cause

Script HRServiceCreatorUtilAjax which verifies if user is having access to update the HR template is trying to call function hr\_utils.checkUserHasRole which doesn't exist in the instance.

https://xx.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=f65370019f22120047a2d126c42e7000

### Resolution

Suggestion to update hr\_Utils script include merging OOB functions/changes with custom code or revert it to OOTB to resolve the issue
