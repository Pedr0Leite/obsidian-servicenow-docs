---
title: "Sample script to start a new Flow Designer Context for a Requested Item and cancel prior hung/error flow"
aliases:
  - KB0868549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868549
kb_number: KB0868549
last_modified: 2025-05-15
---

## Issue

When a flow designer flow is errored or hung due to an exception, there is no optional feature to restart the flow. To overcome this drawback, a new flow must be started, associated with Requested Item (RITM) and old flow context must be cancelled.

The JS Script below can be  adjusted to be run as Business Rule, UI Action, or Script Include. As is, it is an example and can run in Script Background.  
  

//RITM Flow Errors out. There is no an option to continue after fixing the exception.  
//Write script to start a new flow context and associate this with RITM. Then cancel the  
old flow context  
// Query the Flow Context of RITM  
//Remove the next 4 lines if running this as a business rule or UI Action and replace  
ritm in the following code to current.  
var ritm = new GlideRecord('sc\_req\_item');  
//Enter the RITM Number below  
ritm.addQuery('number','RITM0010001');  
ritm.query();  
while(ritm.next()){  
gs.log("RITM number = "+ ritm.number);  
gs.log("RITM sys id = "+ ritm.sys\_id);  
gs.log("Sys Flow Context sys id = "+ ritm.flow\_context);  
var hungContext = ritm.flow\_context.toString();  
//Start new flow  
//sn\_flow\_trigger.FlowTriggerAPI.fireCatalogTrigger('global.ENTER CORRECT FLOW NAME  
HERE',ritm);  
sn\_flow\_trigger.FlowTriggerAPI.fireCatalogTrigger('global.service\_catalog\_item\_request',ritm);  
//Find New Flow  
var newFlow = new GlideRecord("sys\_flow\_context");  
newFlow.addQuery('source\_record',ritm.sys\_id);  
newFlow.orderByDesc('sys\_created\_on');  
newFlow.setLimit(1);  
newFlow.query();  
while (newFlow.next()){  
gs.log("source record = "+ newFlow.source\_record);  
gs.log("Flow Context sys id = "+ newFlow.sys\_id);  
gs.log("Sys Created on = "+ newFlow.sys\_created\_on);  
//Associate new flow context with RITM  
ritm.flow\_context = newFlow.sys\_id;  
ritm.update();  
gs.log("Updated the flow context sys id");

} //newFlow Loop

//After Successful Association, cancel old flow.  
sn\_fd.FlowAPI.cancel(hungContext,'Flow cancelled.');  
}//ritm loop. Remove this if it run as Business Rule or UI Action  
//Verify the association is correct  
gs.log("After Updating the flow context");  
var ritms = new GlideRecord('sc\_req\_item');  
//Enter the RITM Number below  
ritms.addQuery('number','RITM0010001');  
ritms.query();  
while(ritms.next()){  
gs.log("RITM number = "+ ritms.number);  
gs.log("RITM sys id = "+ ritms.sys\_id);  
gs.log("Sys Flow Context sys id = "+ ritms.flow\_context);  
}

## Resolution

Review the attached example script and adjust it based on your needs.

## Additional Information

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0859955](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859955)
