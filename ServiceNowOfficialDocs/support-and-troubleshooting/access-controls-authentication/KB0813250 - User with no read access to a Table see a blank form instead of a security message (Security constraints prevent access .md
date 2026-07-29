---
title: "User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access to requested page)"
aliases:
  - KB0813250
tags:
  - servicenow
  - support-kb
  - acl
  - ui-page-acl
  - table-acl
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813250
kb_number: KB0813250
last_modified: 2024-04-08
---

## User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access to requested page)

  

### Issue

User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access to requested page)

### Release

All Supported releases

### Cause

This is expected behavior when a user navigates directly to a record. If they try to access the List, the list will display "Security constraints prevent access to requested page"

### Resolution

You can create a new ACL on the table of Type "UI Page" and Operation "read" to prevent users from seeing the form at all.

## Related

- [[KB0753582 - The non-admin users are not able to access to a table]] — root cause of missing table-level read ACLs
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — how table-level ACLs are evaluated
- [[acl-rule-types]] — official docs on ACL rule types including UI Page type

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0695387 - For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get |For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message|Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
