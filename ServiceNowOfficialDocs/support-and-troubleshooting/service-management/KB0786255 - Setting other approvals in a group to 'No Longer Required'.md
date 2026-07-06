---
title: "Setting other approvals in a group to 'No Longer Required"
aliases:
  - KB0786255
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786255
kb_number: KB0786255
last_modified: 2025-07-28
---

## Setting other approvals in a group to 'No Longer Required'

  

### Issue

In an approval workflow, when you want to modify the behavior where other approvals in a group change to "No Longer Required" state, when an approval is Approved/Rejected/Cancelled or to include this behavior for any other approval state other than the OOB states,

### Release

All releases

### Resolution

This can be achieved by modifying the condition on this OOB business rule 'SNC - Moot user approvals for group'. Please find the link to this business rule here: /sys\_script.do?sys\_id=253a59580a0a0b2677d435b165539c4b
