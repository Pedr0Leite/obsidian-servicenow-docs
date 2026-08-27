---
title: "User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list"
aliases:
  - KB0694783
tags:
  - servicenow
  - support-kb
  - roles
  - elevated-privilege
  - ui-context-menu
  - security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694783
kb_number: KB0694783
last_modified: 2025-01-03
---

## User granted with the list\_updater role but can't see the 'Update selected' and 'Update all' Context menu in list

  

### Issue

# Description

* * *

User granted with the list\_updater role but can't see the UI Context Menu 'Update selected' and 'Update all' in list. 

# Procedure

* * *

1.  Both UI Context Menu has following condition. 
2.  **gs.hasRole('list\_updater') && !ListProperties.isRelatedList() && !RP.isPortal() && !ListProperties.isRefList()**
3.  Remove _**gs.hasRole('list\_updater')**_ from condition to make sure that other conditions are not failing. 
4.  Check _**list\_updater**_ role. If role is marked as "Elevated privilege" then this will prevent users to see UI Context menu. Untick "Elevated privilege" option then User will be able to see UI Context menu. 
5.  If its marked intentionally then User require to do "Elevate roles" then user can see Both UI Context Menus. 

# Applicable Versions

* * *

All versions 

# Additional Information

* * *

Following are documentation for understanding on Elevated privilege roles

[https://docs.servicenow.com/csh?topicname=c\_ElevatedPrivilege.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ElevatedPrivilege.html&version=latest)

[https://docs.servicenow.com/csh?topicname=t\_ElevateToAPrivilegedRole.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ElevateToAPrivilegedRole.html&version=latest)

## Related

- [[KB0687701 - Admin user is being asked to elevate to "admin" role after logging in]] - same Elevated Privilege mechanism
- [[t_ElevateToAPrivilegedRole]] - official docs on elevating to a privileged role
- [[t_ForceAdmManElev]] - official docs on forcing administrator manual elevation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691876 - Mutual Authentication Overview|Mutual Authentication: Overview]]
