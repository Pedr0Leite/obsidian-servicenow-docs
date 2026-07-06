---
title: "Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)"
aliases:
  - KB0713543
tags:
  - servicenow
  - support-kb
  - acl
  - elevated-privilege
  - admin-role
  - security-constraints
  - high-security-plugin
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713543
kb_number: KB0713543
last_modified: 2026-06-27
---

## Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)

  

### Issue

There are cases where admin users are having limited access to modules and/or tables and end up getting "Security constraints.." message almost everywhere. The admin might not be able to see the required modules that are usually visible to them.

### Release

All Releases

### Cause

This behavior will arise if we treat **admin** role as elevated privileged role.

In other words, if the **Elevated** **Privilege** checkbox is set to true for **admin** role in **sys\_user\_role** table, it will break the administrator's role OOB behavior.

### Resolution

Follow the below steps to revert OOB behavior of "Admin" role

-   Navigate to **User Administration** > **Roles.**
-   Lookup for the record of name **admin.** Notice whether **Elevated privilege** checkbox is not set to true.

Please note: There can be a case where you won't be able to access these and hence if you have a working instance, then kindly migrate the above record via update set to an affected instance.

### Related Links

Additional Documentation: Evaluate the admin override at the access level

[https://docs.servicenow.com/csh?topicname=t\_EvalAdmOverrideAccLevel.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EvalAdmOverrideAccLevel.html&version=latest)

## Related

- [[KB0687701 - Admin user is being asked to elevate to admin role after logging in]] - same elevated-privilege-on-admin-role root cause
- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[KB0745206 - Developer tab is not displayed in System Settings for admin user]]
- [[KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[t_EvalAdmOverrideAccLevel]] - official docs on evaluating admin override at the access level
