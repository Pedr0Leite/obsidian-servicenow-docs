---
title: "Child Change Request (under Parent Release record) is causing Parent's approvals to be marked \"No longer required\""
aliases:
  - KB0827996
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827996
kb_number: KB0827996
last_modified: 2024-04-08
---

## Child Change Request (under Parent Release record) is causing Parent's approvals to be marked "No longer required"

  

### Issue

The user had a requirement with their Release records to have a workflow associated. Within the workflow on the Release record, there are some approvals needed. Additionally, a Normal Change Request is generated, and there are some separate approvals on the child Change Request.

It was noted that occasionally, the same group, group 'A', was set as an approval group on both the child Change Request and the parent Release record. This is when the issue occurred.

### Cause

The rm\_release table did not have the "close\_states" attribute set on the dictionary override for its state field.

### Resolution

As mentioned above, the rm\_release table did not have the "close\_states" attribute set on the dictionary override for its state field. 

As such, they can and should be added to resolve the issue:  

-   /nav\_to.do?uri=sys\_dictionary\_override.do?sys\_id=3aea7d910a0a0bd5001ed3913215ab45

Previously, when the state value of the Release record was being set to '4', Task Active State Management recognized this is a close state, which is the default from task (3, 4, 7), so the rm\_release record was flagged as inactive/closed.

Close states for rm\_release were modified to be set to 3 and 7, leaving a transition to '4' to not cause the rm\_release record to close unexpectedly and thus set the approvals on it to "No longer required".
