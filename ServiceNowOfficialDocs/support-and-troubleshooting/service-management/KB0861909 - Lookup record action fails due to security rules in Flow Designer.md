---
title: "Lookup record action fails due to security rules in Flow Designer"
aliases:
  - KB0861909
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861909
kb_number: KB0861909
last_modified: 2025-08-06
---

## Lookup record action fails due to security rules in Flow Designer

  

### Issue

In Flow Designer, running a Lookup Record action shows an error, "The requested flow operation was prohibited by security rules." If the error details are not immediately visible, open the Show Ops Summary and find the sys\_flow\_context record to see the specific error details. If the lookup was on the Incident table, verify the flow is running as the User who initiated the session. 

![](sys_attachment.do?sys_id=9f57f048471f2a9048cb2920326d43de)

### Release

Any supported release

### Cause

The user who started the flow does not have the necessary roles. 

### Resolution

To resolve the issue:

1.  Check the user's profile who is starting the flow.
2.  Run the flow as the System User.
3.  Examine the access control lists (ACLs) configured to limit users.

### Related Links

[Creating a SC task record and displaying variables in the variable editor while running a flow as a user](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754165)

[CRUD action/step action fails with "The requested flow operation was prohibited by security rules."](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821099)

[Flow Designer Create Task fails citing security rules](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870023)
