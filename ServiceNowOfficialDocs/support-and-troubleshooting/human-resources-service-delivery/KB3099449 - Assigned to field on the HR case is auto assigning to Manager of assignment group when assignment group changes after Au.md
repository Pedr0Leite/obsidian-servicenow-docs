---
title: "Assigned to field on the HR case is auto assigning to Manager of assignment group when assignment group changes after Australia upgrade"
aliases:
  - KB3099449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3099449
kb_number: KB3099449
last_modified: 2026-06-18
---

## Assigned to field on the HR case is auto assigning to Manager of assignment group when assignment group changes after Australia upgrade

  

### Issue

**Problem**  
Assigned to field on the HR case, is auto assigning to Manager of assignment group when assignment group changes after Australia upgrade.

### Release

Australia

### Cause

**Root Cause**  
The inherited flag is checked on the client script in the Australia release, causing the assigned to field to update with the assignment group manager name. This behavior is expected after the Australia upgrade, as the inherited flag was not checked before the upgrade.  
  

### Resolution

**Steps to Resolve**

Validate the issue by following the steps to reproduce: 

1.open any HR case, and try changing the assignment group.

2\. Review the client script 'Auto Fill Assigned To Field' located at

https://instance.service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=ae9af0230be1320036e62c7885673a08 to confirm the inherited flag status. 

3\. Note that this is an expected behavior post-Australia upgrade, and no further action is required.
