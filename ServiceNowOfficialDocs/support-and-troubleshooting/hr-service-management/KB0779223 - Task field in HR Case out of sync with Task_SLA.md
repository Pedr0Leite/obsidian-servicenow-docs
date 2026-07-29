---
title: "Task field in HR Case out of sync with Task_SLA"
aliases:
  - KB0779223
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779223
kb_number: KB0779223
last_modified: 2024-04-08
---

## Task field in HR Case out of sync with Task\_SLA

  

### Issue

Task field in HR Case is not  syncing with Task\_SLA record which is attached to the record.

### Release

London, Madrid

### Cause

This issue was reported on PRB1343402.

### Resolution

This issue was reported on PRB1343402.

PRB1343402:The "SLA" field in the HR case record and the "Business elapsed percentage" on the related Task SLA are not in sync.  
  
PRB1343402 is closed on won't fix because the SLA values were never implemented to be in sync.

For example: if a case has multiple sub cases (with tasks) and sub tasks,  Currently we do not have a way to calculate the true top level case percentage complete.

Hence this is considered as an enhancement.
