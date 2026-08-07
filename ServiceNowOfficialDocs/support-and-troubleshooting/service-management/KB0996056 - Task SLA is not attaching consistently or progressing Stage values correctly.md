---
title: "Task SLA is not attaching consistently or progressing Stage values correctly"
aliases:
  - KB0996056
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996056
kb_number: KB0996056
last_modified: 2024-08-14
---

## Task SLA is not attaching consistently or progressing Stage values correctly

  

### Issue

The user had two task SLAs which should attach and, upon hitting the correct Cancel conditions, transition Stage value from "In Progress" to "Cancelled".

Intermittently, only one of the task SLAs would attach, and even when both attached, neither would cancel when meeting the Cancel condition(s). The user wanted to know why.

### Cause

The Flow associated with one of the task SLA's SLA Definition (_contract\_sla_ record) was set to inactive (active = false).

In the localhost logs, the below error was the clue that directed attention to the Flow: 

`SEVERE *** ERROR *** The flow named: SLA notification and escalation flow has not been published within application scope: global`  
`com.glide.plan.runners.FlowObjectAPIException: The flow named: SLA notification and escalation flow has not been published within application scope: global`

### Resolution

As a result of the Flow, which was associated with one of the expected task SLA's SLA Definition, being set to a value of active = false, the above two behaviors were experienced. 

Once the Flow was set to active = true, the two behaviors subsided. All expected task SLAs attached immediately on insert of the task record, and they transitioned flawlessly to a Stage of "Cancelled" when their respective Cancel conditions were met.
