---
title: "Why are Incidents automatically set to resolved, but Alert remain open from Netcool integration?"
aliases:
  - KB0749203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749203
kb_number: KB0749203
last_modified: 2024-04-07
---

## Why are Incidents automatically set to resolved, but Alert remain open from Netcool integration?

  

### Issue

# Overview

Netcool and other monitoring tools sends event to mid server connector.  Depending on the attributes of the incoming events, event rule, and alert action/ alert management rules will convert these event to Alerts and incidents.

# \[How Alerts and Incident state changes\]

1.  First an event comes in with Critical.   
    A. An alert gets created with the severity of critical   
    B. An incident get's created with the state of "in progress"   
      
    2.Second an event comes in with Severity info   
    A. A new alert gets created if the message key is different, or the same Alert gets updated if the message key is the same   
    B. If the Message key is the same the Alert Severity will be changed to info, but the state will remain open. We do no close Alerts with the severity of info   
    C. The incident that's associate with the alert will be switched to resolved   
      
    3\. Third if the second event comes with Clear   
    A. The alert severity will be set to Clear   
    B. The Alert state is set to closed.   
    C. Since the Alert is set to closed. The incident will also be set to close 

# Example

  
1\. The EvtMgmtAlertActions is script include which close only Alerts if the incident are in state 6 or 7 only, and if the stat is not info "5"   
  
  
EvtMgmtAlertActions   
var alert = new GlideRecord('em\_alert');   
// Get alerts with delay, this makes sure all BR on create/update alerts completed before the job is running   
alert.addQuery('sys\_updated\_on', '<=', inProgress);   
alert.addQuery('state', '!=', 'Closed');   
alert.addQuery('severity', '!=', '5');   
alert.addNotNullQuery('incident');   
var gr = alert.addJoinQuery('incident', 'incident', 'sys\_id');   
gr.addCondition('state', 'IN', '6,7'); // 6 - Resolved or 7 - Closed   
  
alert.query();   
while (alert.next()) {   
// create a mapping from alert to service   
alert.setValue('state', 'Closed');   
var alertManager = new SNC.AlertManager();   
alertManager.updateWorkNotesOnAlert(alert, 'Closing alert because the related incident is already Resolved or Closed');   
  
2\. The business rule Close associated closes the incident.   
  
Close associated incident   
  
condition for the business rule to run   
((previous.state != 'Closed' && current.state == 'Closed')||(previous.severity != '5' && current.severity == '5') ||(previous.severity != '0' && current.severity == '0')) && current.incident !='NULL' && current.incident !='' && current.incident !=null   
  
\--where you can change the closure notes   
task.close\_code = "Solved Remotely (Permanently)";   
task.close\_notes = "Closed the task associated with alert: " + current.number;
