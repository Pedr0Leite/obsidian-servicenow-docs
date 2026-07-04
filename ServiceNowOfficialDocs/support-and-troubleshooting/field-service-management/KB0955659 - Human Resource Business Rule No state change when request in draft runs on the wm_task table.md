---
title: "Human Resource Business Rule \"No state change when request in draft\" runs on the wm_task table"
aliases:
  - KB0955659
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955659
kb_number: KB0955659
last_modified: 2024-02-23
---

## Human Resource Business Rule "No state change when request in draft" runs on the wm\_task table

  

### Issue

When you update the work order task which is in Cancelled State, the Human Resource Business Rule "No state change when request in draft" runs on the wm\_task table

Steps to Reproduce:

1.  Update the comment in one of the following wm\_task in state cancelled.
2.  You will see the pop up related to the "No state change when a request in draft"  
    
3.  The state will change to draft from original cancelled  
    

### Release

Orlando

### Cause

Expected Behaviour

### Resolution

The Business Rule Executing is "No state change when request in draft" which is on the 'sm\_task' table:  
/nav\_to.do?uri=sys\_script.do?sys\_id=4b153b70c31102004d431a4112d3ae22  
  
This Business Rule has a Message "The task can only be in draft state, because the request is in either draft state or awaiting approval state" > Check in the Actions Tab.  
  
Work Order Task: WOT00####  
sm\_task\_list.do?sysparm\_query=numberSTARTSWITHWOT0074925&sysparm\_view=  
  
The above Business Rule is coming from the 'Service Management Core' Plugin.  
  

### Related Links

Doc Link:  
[Paris Service Management](https://docs.servicenow.com/bundle/paris-service-management-for-the-enterprise/page/product/service-management-core/reference/r_InstallWServMgmtCore.html "Paris Service Management")
