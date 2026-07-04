---
title: "Workflow \"Wait for condition\" based on Due date is not moving forward at the expected date"
aliases:
  - KB0869560
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869560
kb_number: KB0869560
last_modified: 2023-12-09
---

## Workflow "Wait for condition" based on Due date is not moving forward at the expected date

  

### Issue

The issue with workflow's "Wait for condition" activity not transitioning forward at the expected time.

### Cause

Due date, which the "Wait for condition" workflow activity was looking at in order to know when/how to transition forward, was changed after the "Wait for condition" workflow activity had already started executing (with a different Due date value - which was set on the insert of the record).

### Resolution

  
The issue was that when the parent record (which the workflow was associated with) was inserted, the Due date value was 2020-12-04 21:42:03 (value 'A').  
  
A user has the ability to change the Due date field value up until the workflow executes the Wait for condition activity. If it is changed after the fact (say, to value 'B'). The workflow will use the value it had on the execution of the Wait for condition activity (value 'A'). Even if the value is changed after the workflow activity starts executing, it won't matter - the new value (value 'B') will not be taken. The workflow will already be executing on the value present when the workflow activity started execution (value 'A').  
  
This is Out of Box (OOB), expected behavior. To rectify this, all the user would need to do is wait until the original due date, and then the workflow would progress: 2020-12-04 21:42:03.
