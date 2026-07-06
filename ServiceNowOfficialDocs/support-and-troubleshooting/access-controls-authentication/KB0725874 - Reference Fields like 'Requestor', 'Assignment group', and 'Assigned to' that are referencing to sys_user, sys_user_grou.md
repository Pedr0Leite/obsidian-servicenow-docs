---
title: "Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form."
aliases:
  - KB0725874
tags:
  - servicenow
  - support-kb
  - acl
  - reference-field
  - sys_user
  - sys_user_group
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725874
kb_number: KB0725874
last_modified: 2024-04-07
---

## Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys\_user, sys\_user\_group are not available on the form.

  

### Issue

Reference Fields like 'Requestor' (a reference to sys\_user table), 'Assignment group' (a reference to sys\_user\_group table), 'Assigned to' (a reference to sys\_user table) are not visible to non-admin users (than admin) on a ServiceNow Form.

However, all 'admin' users can see these fields on the form.

### Release

All releases

### Cause

These affected fields like 'Requestor', 'Assignment group', and 'Assigned to' are referenced to user(sys\_user) and groups (sys\_user\_group) table. If the users do not have access to the User/Group table, then the referenced fields from the User/Group table will not be visible to such users on the form.

### Resolution

Create the necessary Read/Write ACLs on Group(sys\_user\_group) and User(sys\_user) tables to grant access to other role users so that the non-admin users can have access to these fields on the forms.

## Related

- [[KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task]] - same sys_user ACL root cause
- [[KB0720034 - Non-role (ESS) users are not able to see group (sys_user_group) records]]
- [[KB0746724 - Reference field is hidden from layout]]
- [[access-control-rules]] - official docs on ACL rule evaluation
