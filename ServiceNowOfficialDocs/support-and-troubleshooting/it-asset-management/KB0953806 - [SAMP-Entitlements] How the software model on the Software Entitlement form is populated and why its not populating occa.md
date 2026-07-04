---
title: "[SAMP-Entitlements] How the software model on the Software Entitlement form is populated and why its not populating occassionally"
aliases:
  - KB0953806
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953806
kb_number: KB0953806
last_modified: 2026-03-27
---

## \[SAMP-Entitlements\] How the software model on the Software Entitlement form is populated and why its not populating occassionally

  

### Summary

When creating a new Software Entitlements, and once we enter the PPN (Publisher Part Number), it might not populate the software model.

We do have the client script on the entitlement form that would try to check the matching model, and if not, it will create the new one and populate it on the form.

**Client Script Name**: Create software model if not exist  
https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=471a2353cb403200f2de77a4634c9cb5

The above script makes use of GlideAjax to call a script include SoftwareModelAPI and find/create a new model.  
**Script Include**: SoftwareModelAPI  
https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=567fa869670122007d59cbb35685ef19

### Release

All Jakarta++

### Instructions

1\. Check if these client script or script includes are OOB.

2\. Make sure if we are waiting for atleast 5-6 secs on the entitlement form once we enter PPN.

3\. Open the browser console and check the network if there are any latency in GlideAjax or errors.
