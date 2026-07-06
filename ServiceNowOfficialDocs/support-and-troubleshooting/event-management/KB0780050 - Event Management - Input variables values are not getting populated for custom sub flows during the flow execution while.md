---
title: "Event Management - Input variables values are not getting populated for custom sub flows during the flow execution while creating incidents/tasks."
aliases:
  - KB0780050
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780050
kb_number: KB0780050
last_modified: 2024-04-08
---

## Event Management - Input variables values are not getting populated for custom sub flows during the flow execution while creating incidents/tasks.

  

### Issue

When we check the flow execution that is responsible for creation of tasks/incidents from the alert management rule, we will notice that Input variables values are not getting populated, they will be empty and so the action section in the Subflow will fail to create any incidents for the corresponding alerts.

### Release

Any

### Cause

Input variables are defined in the wrong format.

### Resolution

1\. The Subflow variable values are checked in the script include: EvtMgmtAlertManagementProcess

2\. All the Subflow inputs variables are hardcoded and passed to the function: "callActivateSubflowAPI"  
  
3\. Below is the script text where the input variables are hardcoded. And we have been using the same input variables in all the script includes where we are supposed to create the incidents & alerts.  

callActivateSubflowAPI:function(actionFullName,ruleName,ruleSysId,alertGR,manuallyRun,numOfExecutions,executionsLimit,actionId,actionName){  
  
var executionGR = this.createExectionRec();  
var inputs = {"ah\_alertrulename": ruleName, "ah\_alertruleid": ruleSysId, "ah\_alertgr" : alertGR, "ah\_executionid" : executionGR.getUniqueValue(), "ah\_username" : gs.getUserName(), "ah\_userdisplayname" : gs.getUserDisplayName()};  
try {  
var contextId= SNC.AlertManager.executeSubflow(actionFullName,this.evtMgmtCommons.getRecordDomain(alertGR), inputs);  
var logMessage ="";  
if (GlideStringUtil.nil(contextId)) {  
logMessage = this.getFailureExecutingLogMessage(manuallyRun, numOfExecutions, executionsLimit, gs.getMessage("Subflow '{0}' couldn't be started.",\[actionName\]));  
}   
else {  
logMessage = this.getSuccessExecutingLogMessage(manuallyRun, numOfExecutions, executionsLimit);  
}  
  
this.addExecutionRunForRecord(executionGR, alertGR.sys\_id, ruleSysId, manuallyRun, contextId, actionName, "",this.SUBFLOW\_LINK, logMessage,actionId);  
return contextId;  
}

Therefore, all the input variables should be defined in a format as "**ah\_xxxxx**", only then they will be considered as valid and data will be populated.

4.For reference check the OOB of Subflow and make sure we are creating the input variables in the same format.
