---
title: "Removal/Hiding of the 'Request Approved' stage from displaying on RITM list-view (and in general)"
aliases:
  - KB0656547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656547
kb_number: KB0656547
last_modified: 2026-02-23
---

## Removal/Hiding of the 'Request Approved' stage from displaying on RITM list-view (and in general)

  

### Issue

Request to remove the Request Approved stage from displaying on RITM list-view, and in general, as it seemed to be negatively affecting reporting for one of their teams who use Service Catalog.  
  
  

### Release

### Cause

It is the OOB (Out of Box) behavior for "Request Approved" to appear in the list-view.

### Resolution

It is not recommend to attempt to remove this stage.   
  
A business rule on the table sc\_request: "Cascade Request Approval to Request Item" sets the stage to "request\_approved" for all requested items with stage="waiting\_for\_approval" (the default value). Altering this could cause other workflows not to start.  
  
As a result of the "Request Approved" stage being OOB, a large number of workflows are, by default, associated with it.
