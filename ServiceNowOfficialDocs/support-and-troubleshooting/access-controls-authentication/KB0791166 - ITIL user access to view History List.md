---
title: "ITIL user access to view History > List "
aliases:
  - KB0791166
tags:
  - servicenow
  - support-kb
  - acl
  - sys_history_set
  - auditing
  - roles
  - itil
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791166
kb_number: KB0791166
last_modified: 2024-04-07
---

## Issue

ITIL User is not able to access History > List from Form Context Menu

## Resolution

To view a history list, the following requirements must be met.  
1\. Auditing: Auditing for the table must be enabled to view a history list.  
2\. ACLs: By default, the List history option is only available to users with the admin user role. To enable this option to non-admins, create a custom read ACL rule granting read access to the Record History \[sys\_history\_set\] table.  
3\. Roles: At least one of the roles that the user has must be included in the glide.history.role property, which includes the itil role by default.  
https://docs.servicenow.com/csh?topicname=r\_HistoryList.html&version=latest

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — general ACL evaluation background for custom read ACLs
- [[KB0753582 - The non-admin users are not able to access to a table]] — same pattern of granting read ACL on a restricted system table
- [[r_HistoryList]] — official docs on History List requirements (auditing, ACLs, roles)
