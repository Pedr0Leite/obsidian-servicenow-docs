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

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0749023 - Unable to add roles, Insert new a row does not exist.|Unable to add roles, Insert new a row does not exist.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753001 - Some roles are not visible and cannot be exported from the [sys_user_role] list table|Some roles are not  visible and cannot be exported from the [sys_user_role] list table]]
