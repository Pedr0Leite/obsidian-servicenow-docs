---
title: "Custom flow on task_sla table is not triggered when repairing a paused SLA"
aliases:
  - KB0869968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869968
kb_number: KB0869968
last_modified: 2024-02-26
---

## Custom flow on task\_sla table is not triggered when repairing a paused SLA

  

### Issue

Custom flow on task\_sla table is not triggered when repairing a paused SLA

  

### Steps to produce:

1.  Create test SLA called :Test SLA Breached  
    -   Setup on table Incident
    -   trigger condition on priority 3, and pause condition on Resolved  
        
2.  Create flow called : SLA breach test flow  
    -   Trigger on table task\_sla
    -   Trigger condition: create/update
    -   Condition: Has Breached =true
    -   SLA name=Test SLA Breached
    -   Add action to sla related incident short description to Hello.
3.  Create Inicident on priority as 3 , save and see the SLA :Test SLA Breached attached in progress state
4.  Click Repair SLA and see the short description is changed to Hello.  
    
5.  Check flow context, there is  context created for flow: SLA breach test flow.
6.  Change short description to other values and save.
7.  Change state to Resolved and save.
8.  The SLA is in paused state.
9.  Run Repair SLA, notice the short description is unchanged.
10.  Check flow context, there is no context created for flow: SLA breach test flow.

  

### Cause

When repairing an SLA, workflow/flow is turned off.   
  
It was done specifically to ensure that nothing messes with the records that are being used to repair the SLA.

For the SLA current is in paused/cancelled/completed, then related flow will not be triggered.  

For other state of SLA, it will resume the workflow/flow as designed.

### Resolution

This is the expected behaviour. 

When repairing an SLA, workflow/flow is turned off.

It was done specifically to ensure that nothing messes with the records that are being used to repair the SLA.

Checking the script includes: RepairTaskSLA  
  
There are some scripts like below:  
  
var taskSLAFlow = new TaskSLAFlow(this.taskSLAgr, this.slaDefGR);  
taskSLAFlow.setRepairMode(true);  
taskSLAFlow.start();  
  
var taskSLAState = this.getCurrentState();  
switch(taskSLAState) {  
case TaskSLA.STATE\_PAUSED:  
taskSLAFlow.pause();  
break;  
case TaskSLA.STATE\_CANCELLED:  
case TaskSLA.STATE\_COMPLETED:  
taskSLAFlow.cancel();  
break;  
}  
}

For the SLA current is paused/canceled/completed, the related flow will not be triggered.
