---
title: "Some roles are not  visible and cannot be exported from the [sys_user_role] list table"
aliases:
  - KB0753001
tags:
  - servicenow
  - support-kb
  - acl
  - roles
  - sys_user_role
  - admin-overrides
  - export
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753001
kb_number: KB0753001
last_modified: 2024-04-07
---

## Some roles are not visible and cannot be exported from the \[sys\_user\_role\] list table

  

### Issue

The record count on \[sys\_user\_role\] list table is not matching the list of Roles being displayed and exported to XML or Excel for example. Some Roles are being hidden such as the 'maint' and 'nobody' roles even when logged in as an admin.

### Release

All releases from London

### Cause

From the London release, the **read ACL** on the \[sys\_user\_role\] table has been modified and the **Admin overrides** checkbox is no longer selected:  
/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=b05cb4ae0a0a0aa70084b2b90bf17793

### Resolution

To display and export all roles including the 'maint, 'nobody', and 'security\_admin' roles from the \[sys\_user\_role\] table:

1.  Navigate to System Security>Access Control (ACL).
2.  Ensure the ACL for \[sys\_user\_role\] with **read** operation is **Active** and has the **Admin overrides** checkbox selected:  
    /nav\_to.do?uri=sys\_security\_acl.do?sys\_id=b05cb4ae0a0a0aa70084b2b90bf17793

## Related

- [[KB0751561 - How to Grant "Partner" Role to Existing User]] — related role administration workflow
- [[KB0758037 - Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by "security_admin" Role]] — another sys_user_role read ACL change from the London release
- [[KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected]] — Admin Overrides checkbox behavior in more depth
- [[Role-Mgmt-V2]] — official docs on the role management data model
