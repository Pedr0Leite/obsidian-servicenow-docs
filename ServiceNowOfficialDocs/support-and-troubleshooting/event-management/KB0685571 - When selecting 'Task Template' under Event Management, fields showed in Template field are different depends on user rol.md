---
title: "When selecting 'Task Template' under Event Management, fields showed in Template field are different depends on user role."
aliases:
  - KB0685571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685571
kb_number: KB0685571
last_modified: 2024-04-07
---

## When selecting 'Task Template' under Event Management, fields showed in Template field are different depends on user role.

  

### Issue

When selecting 'Task Template' under Event Management, fields showed in Template field are different depends on user role.

Steps to reproduce:

1.  Impersonate a user who has admin role.
2.  Go to Event Management > Task Template, and click New.
3.  Make sure the table is set to incident, and click '-- choose field --' in Template field. All incident fields are shown.
4.  Impersonate a user who doesn't have an admin role but has evt\_mgmt\_admin role.
5.  Go to Event Management > Task Template, and click New.
6.  This time, only six fields of incident (category, impact, priority, short description, subcategory and urgency) are shown in Template field.

### Release

All

### Cause

The limitation of the incident's displayed fields for the choice-list (drop-down menu) derives from the ACL (security) limitation to the incidents table, for a user with role ITIL\_ROLE, which is one of the roles assigned to a user with evt\_mgmt\_admin role.

### Resolution

In order to view the full list of incident's fields, an ITIL\_admin role is required. The solution is to assign such a role to the user that needs it, or to ask the administrator (with system\_admin) role to perform the task instead.
