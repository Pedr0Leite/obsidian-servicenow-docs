---
title: "Flow stage field not being updated in List view (cancellation)"
aliases:
  - KB0786139
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786139
kb_number: KB0786139
last_modified: 2024-04-08
---

## Flow stage field not being updated in List view (cancellation)

  

### Issue

Flow stage field not being updated in List view (cancellation)

Steps to Reproduce:

1.  Submit a request for item: eg  Samsung Galaxy S7 Edge  
    2\. Approved the requested item  
    3\. check stage in list view and form view, it will show correct.  
    4\. Now cancel the parent request, which will cancel the ritm also  
    5\. in form view stage will show as "Request cancelled"  
    6\. List view it will not reflect

### Cause

When a flow designer flow is used for a service catalog item then the sc\_req\_item list view uses the stage of the flow, while the sc\_req\_item form view uses the stage off the sc\_req\_item record.   
  
  

### Resolution

To Resolve

 1. Alter the stages on the custom flow "Service Catalog Item Request" to account for cancellation.

2\. In flow "Service Catalog Item Request" defines a new stage "Cancelled".

Apply the new flow stage by moving the mouse to the far right hand side and choose "add stage" and select "Request Cancelled"  
  

  

### Related Links

[https://docs.servicenow.com/csh?topicname=flow-designer-stages.html&version=latest](https://docs.servicenow.com/csh?topicname=flow-designer-stages.html&version=latest)
