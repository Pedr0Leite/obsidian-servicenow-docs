---
title: "Is it possible, upon performing a Repair on a SLA, to have the original task_sla remain but be marked as \"canceled\" instead of deleting the original task_sla?"
aliases:
  - KB0784435
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784435
kb_number: KB0784435
last_modified: 2024-04-07
---

## Is it possible, upon performing a Repair on a SLA, to have the original task\_sla remain but be marked as "canceled" instead of deleting the original task\_sla?

  

### Issue

The user wanted to know if it was possible, upon repairing a task\_sla, that it would remain and show as "canceled" instead of having the task\_sla delete per the normal repair process.

### Resolution

Unfortunately, this is not possible.  
  
As is covered in the [documentation](https://docs.servicenow.com/csh?topicname=c_RepairSLAs.html&version=latest "documentation"), the repair function removes the task\_sla record, then recreates and recalculates it from the start (including recreating the workflow).
