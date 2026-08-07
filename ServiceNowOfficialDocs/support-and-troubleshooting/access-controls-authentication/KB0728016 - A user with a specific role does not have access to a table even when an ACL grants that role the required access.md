---
title: "A user with a specific role does not have access to a table even when an ACL grants that role the required access"
aliases:
  - KB0728016
tags:
  - servicenow
  - support-kb
  - acl
  - elevated-privilege
  - roles
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728016
kb_number: KB0728016
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

A user with a specific role does not have access to a table even when an ACL grants that role the required access

# Release

* * *

Jakarta, Kingston, London

# Cause

* * *

One of the possible causes of this behavior is that the user role that is expected to grant the user access because of the ACL has "elevated privilege" checked on the sys\_user\_role table

# Resolution

* * *

1.  Navigate to sys\_user\_role.list
2.  Search for the role in the "Name" column
3.  Notice that "elevated privilege" is checked for that role and hence the user needs to "elevate role" in order to pass corresponding ACL
4.  Uncheck "elevated privilege" and see the ACL is granting the access as expected

**NOTE:**

To use an elevated role, you must meet these conditions:

-   The elevated role must be assigned to you.
-   You must manually elevate to a specific elevated role to get its privileges, even if you are already elevated to a second elevated role that contains the first elevated role.
    
    For example, if elevated role A contains elevated role B, even if you elevate to role A, you must still elevate to role B to get its privileges.
    

# Additional Information

* * *

Learn more about elevated privilege roles using the below document:

[https://docs.servicenow.com/csh?topicname=c\_ElevatedPrivilege.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ElevatedPrivilege.html&version=latest)

## Related

- [[KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[KB0687701 - Admin user is being asked to elevate to admin role after logging in]]
- [[KB0745206 - Developer tab is not displayed in System Settings for admin user]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0694783 - User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list|User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list]]
