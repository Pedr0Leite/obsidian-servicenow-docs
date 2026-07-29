---
title: "Resolve flow failures caused by security rules for the system user"
aliases:
  - KB0861124
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861124
kb_number: KB0861124
last_modified: 2025-10-14
---

## Resolve flow failures caused by security rules for the system user

  

### Issue

In Flow Designer, running a flow as a system user fails and presents the following error message: 

_The requested flow operation was prohibited by security rules._

![](sys_attachment.do?sys_id=7baa7f839796a6d024a7739c1253afe2)

This does not happen when running a flow as the user who initiated the session. 

### Cause

A user record with sys\_id = 'system' in the sys\_user table is conflicting with the platform's internal system user. This custom record does not exist in a standard instance and causes the error. 

### Resolution

Delete the user record with sys\_id = system and run the flow again.
