---
title: "sh_hr_va.admin role is not visible after installing the Human Resources: Virtual Agent Conversations application"
aliases:
  - KB0996152
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996152
kb_number: KB0996152
last_modified: 2025-01-03
---

## sh\_hr\_va.admin role is not visible after installing the Human Resources: Virtual Agent Conversations application

  

### Summary

1.  As an admin install the Human Resources: Virtual Agent Conversations plugin.
2.  Navigate to the sys\_user\_role table.
3.  You cannot see the sh\_hr\_va.admin

### Related Links

This is working as expected.

sh\_hr\_va.admin role can only be added by a user who already has this role in the instance.

If no user has this role, then a case has to be opened with the ServiceNow Customer Support Team requesting to grant the role to specific user profiles.

Once this is added to a user profile, the users can then assign the role to any user within the instance.

![](sys_attachment.do?sys_id=8e9e6bb21b223014b09633f2cd4bcbd9)

```
While granting a role, if the related application has Scoped administration enabled, a user needs to have the 'Assignable By' role to be able to assign this role to another user.
```
