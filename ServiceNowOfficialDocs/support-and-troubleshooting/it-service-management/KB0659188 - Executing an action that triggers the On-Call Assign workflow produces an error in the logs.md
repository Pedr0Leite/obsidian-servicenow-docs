---
title: "Executing an action that triggers the On-Call Assign workflow produces an error in the logs"
aliases:
  - KB0659188
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0659188
kb_number: KB0659188
last_modified: 2025-06-24
---

## Executing an action that triggers the On-Call Assign workflow produces an error in the logs

  

### Issue

Executing an action triggering the On-Call Assign workflow produces the following error in the logs:

Is there any schedule at the time?(be827be2db7103001d80d001cf961926): org.mozilla.javascript.WrappedException: Wrapped ReferenceError: "vars" is not defined. (answer = ifScript();
 
function ifScript() {
var rota = new SNC.OnCallRotation();
var gdt = new GlideDateTime();
var escalationPlan = rota.getEscalationPlan(vars.assignment\_group.sys\_id.toString(), gdt);
 
if (JSUtil.nil(rota) || JSUtil.nil(rota.getCurrentRotaID())) {
return 'no';
}
return 'yes';
}
; line 6) (<refname>; line 51)

### Cause

The On-Call: Assign workflow is designed to be triggered by creating a New Call of type Incident, and clicking Submit. The system then searches the Trigger Rules table and starts the workflow based on conditions.

When you create an Incident directly from the Incidents module, you cannot use the On-Call: Assign workflow. Instead, you need to create a workflow that runs when your condition is matched. 

The Process Trigger Rule Script action is in charge of setting the value of

var vars = {};

                vars.assignment\_group = rule.group;

if this is not set, then the workflow fails when running the line:

var escalationPlan = rota.getEscalationPlan(vars.assignment\_group.sys\_id.toString(), gdt);

The event kicks off only when creating a new incident through the new\_call record, which kicks off automatically if the New Call record is of type Incident.

### Resolution

Navigate to the Process Trigger Rule script action:

https://<instance>/nav\_to.do?uri=sysevent\_script\_action.do?sys\_id=2d7a7000eb301100fcfb858ad106fe42

Use guard code  such that the workflow could be triggered as intended (via trigger rules), with vars passed to workflow and change the **var escalationPlan = rota.getEscalationPlan(vars.assignment\_group.sys\_id.toString(), gdt);** so it acquires the assignment\_group directly from the incident after the trigger rule has made the assignment:

var assignmentGroupSysId = ""  
if (typeof vars !== "undefined" && vars && vars.assignment\_group)
else
    assignmentGroupSysId = current.assignment\_group.sys\_id.toString();
var escalationPlan = rota.getEscalationPlan(assignmentGroupSysId, gdt);
