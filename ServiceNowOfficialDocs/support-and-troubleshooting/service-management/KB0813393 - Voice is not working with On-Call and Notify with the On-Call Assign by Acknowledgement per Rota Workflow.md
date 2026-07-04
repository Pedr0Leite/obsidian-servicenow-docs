---
title: "Voice is not working with On-Call and Notify with the On-Call: Assign by Acknowledgement per Rota Workflow"
aliases:
  - KB0813393
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813393
kb_number: KB0813393
last_modified: 2025-03-17
---

## Voice is not working with On-Call and Notify with the On-Call: Assign by Acknowledgement per Rota Workflow

  

### Issue

When the user creates an incident, workflow "On-Call: Assign by Acknowledgement per Rota" is not automatically making a call to the on-call team members. SMS is working fine, and even conference calls using Voice are working fine. It is just that the workflow mentioned earlier does not initiate voice calls. The user wanted to know why.

### Resolution

After including the Product Owners of On-Call into the discussion, it was found that a small modification needed to be made to the Notify Phone Number Group to allow other system logic to process correctly (such as the "OnCallWorkflowUtilsSNC" Script Include).

There appears to be a strict naming convention regarding the Notify Phone Number Group record Name field. The value has to be "On-Call Group" to allow the Script Include "OnCallWorkflowUtilsSNC" to process. In our case, the suffix "Notify" was added (i.e. the value of the Name field was "Notify On-Call Group", which was causing the Voice functionality to not work.  
  
The logic of how all of these pieces (the Notify Phone Number Group "Name" field value, the "OnCallWorkflowUtilsSNC" Script Include, etc) connect has been attached as a screenshot.
