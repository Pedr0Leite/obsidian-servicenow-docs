---
title: "To-dos page on portal displays errors after upgrade"
aliases:
  - KB0869772
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869772
kb_number: KB0869772
last_modified: 2025-05-28
---

## To-dos page on portal displays errors after upgrade

  

### Issue

When impersonating a certain user and navigating to the user's HR Portal, selecting the "To-dos" page icon (top right of HR Portal) displayed the following errors: 

Server JavaScript error Cannot find function getRecordShortDescription in object \[object Object\].

Line number 550 (sys\_script\_include.fb5a924473b7130030f331d7caf6a764.script)

Script source code logged to browser console

Failing widget: 'HRM Todos Summary' (bdc676957317130030f331d7caf6a74d)

### Cause

The user had customized the **hr\_PortalUtil** Script Include (sys\_id=3c764fda534032003585c3c606dc34e9).

### Resolution

Revert the Script Include **hr\_PortalUtil** to its out of the box (OOB) state.
