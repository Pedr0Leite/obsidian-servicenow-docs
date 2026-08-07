---
title: "How to set show completed to-dos as true by default on New Hire Onboarding - new hire reminder?"
aliases:
  - KB1112425
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1112425
kb_number: KB1112425
last_modified: 2025-09-03
---

## How to set show completed to-dos as true by default on New Hire Onboarding - new hire reminder?

  

### Issue

How to set show completed to-dos as true by default on New Hire Onboarding - new hire reminder?

### Resolution

  
The default behaviour of the ticket page to show completed todos when parent case is complete. If you wish different behaviour it can be modified from the widget.  
HRM Task List(hrm-task-list) - /nav\_to.do?uri=sp\_widget.do?sys\_id=40e783993bdb13004d3b695593efc488  
  
  
In server script see lines  
+++++  
var caseUtil = new sn\_hr\_sp.hr\_PortalUtil(grCase);  
data.caseInfo = caseUtil.\_getRelevantInfoForRecord(grCase);  
var caseOptions = caseUtil.getHeaderOptions({onTicketPage: data.onTicketPage, recordInfo: data.caseInfo});  
if(!caseOptions.showFilter)  
data.showCompletedToDos = true;  
} else  
data.showCompletedToDos = true;  
}  
++++++  
  
You can modify them accordingly or create a new widget altogether  
Please allow any RCA if invalidated by changing widget)  
However this might impact a closed case ticket page.(please test thoroughly)
