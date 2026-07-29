---
title: "When worknotes are added to an incident, task_slas are being duplicated"
aliases:
  - KB0814942
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814942
kb_number: KB0814942
last_modified: 2024-04-08
---

## When worknotes are added to an incident, task\_slas are being duplicated

  

### Issue

The user is facing an issue where when they are adding a work note to an incident, the associated task\_slas on that incident are being duplicated. They wanted to know why.

### Resolution

The cause for the behavior is that there are conflicting conditions on the SLA Definition along with the use of the "Simple" Condition type.  
  
The example incident INC0010000 has a state of "Pending" and is still active.  
  
When adding a work note to the incident, the start condition on SLA Definition "INC Response - 15 Min" is met because the incident's state is not Resolved or Closed. Thus, a new Task SLA is attached (because the user has configured their SLA Definition to use the "Simple" condition type, the system does not test if the stop condition matches).  
  
Now, when SLA processing processes the existing Task SLAs it finds the one just created and so tests for pause/stop/cancel. Stop condition matches as this checks for State is Resolved or is not New, thus the Task SLA gets instantly marked as completed.  
  
The simplest fix for this issue is to set the Condition type back to "Default", which is the Out of Box (OOB) value. Once that change was made, task\_slas no longer duplicated.
