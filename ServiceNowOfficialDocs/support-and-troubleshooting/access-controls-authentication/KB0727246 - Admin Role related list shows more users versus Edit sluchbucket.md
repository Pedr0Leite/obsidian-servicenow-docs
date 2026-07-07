---
title: "Admin Role related list shows more users versus Edit sluchbucket"
aliases:
  - KB0727246
tags:
  - servicenow
  - support-kb
  - roles
  - role-inheritance
  - admin-role
  - sys_user_has_role
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727246
kb_number: KB0727246
last_modified: 2024-04-07
---

## Admin Role related list shows more users versus Edit sluchbucket

  

### Issue

The Admin Role related list shows more users versus "Edit" slushbucket.

![](sys_attachment.do?sys_id=6cca60e6db42b450e515c2230596198b)

  

![](sys_attachment.do?sys_id=20ca60e6db42b450e515c22305961991)

### Release

All

### Cause

Admin role is being inherited by some users

### Resolution

This is expected functionality. The sluchbucket will only show users who were given the Admin role directly. It will not show users that inherit the Admin role through another role or group.

## Related

- [[KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[view-permissions-for-a-role]] - official docs on viewing effective role permissions

#

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0694783 - User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list|User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
