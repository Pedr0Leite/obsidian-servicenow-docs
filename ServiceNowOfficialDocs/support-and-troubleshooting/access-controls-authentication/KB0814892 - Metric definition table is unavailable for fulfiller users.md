---
title: "Metric definition table is unavailable for fulfiller users"
aliases:
  - KB0814892
tags:
  - servicenow
  - support-kb
  - acl
  - metric_definition
  - roles
  - itsm
  - reporting
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814892
kb_number: KB0814892
last_modified: 2026-07-01
---

## Metric definition table is unavailable for fulfiller users

  

### Issue

Fulfiller users cannot view records in the metric\_definition table, or a report built on the metric\_definition table is not accessible to them.

### Symptoms

-   The metric\_definition table appears empty or returns no records for fulfiller users.
-   A report created on the metric\_definition table is not visible to fulfiller users.

### Release

  All supported releases.

### Cause

The base system read ACL on the metric\_definition table requires users to have either the metric\_admin or itil\_admin role. Users who do not have one of these roles cannot view records in this table.

### Resolution

Assign one of the following roles to the fulfiller user:

Option 1: Assign the metric\_admin role

1\. Navigate to User Administration > Users.  
2\. Open the user record for the fulfiller.  
3\. In the Roles tab, select Edit.  
4\. Search for metric\_admin and move it to the Roles List.  
5\. Select Save.

The user can now view the metric\_definition table and any reports built on it.

Option 2: Assign the itil\_admin role

Follow the same steps above, but assign the itil\_admin role instead. This is appropriate if the user already performs ITIL administration duties and the broader role is justified.

Note: Assign only the role that matches the user's job function. If access to the metric\_definition table is the only requirement, use the metric\_admin role.

## Related

- [[KB0851918 - Admins are unable to view the rows on the asmt_metric table.]] — similar role-gated visibility issue on a related metric table
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — general ACL/role evaluation background
- [[add-edit-metric-definition]] — official docs on the metric_definition table and its use in Service Operations Workspace

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0749023 - Unable to add roles, Insert new a row does not exist.|Unable to add roles, Insert new a row does not exist.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753001 - Some roles are not visible and cannot be exported from the [sys_user_role] list table|Some roles are not  visible and cannot be exported from the [sys_user_role] list table]]
