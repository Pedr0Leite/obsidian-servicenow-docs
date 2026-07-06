---
title: "Admin user is being asked to elevate to \"admin\" role after logging in"
aliases:
  - KB0687701
tags:
  - servicenow
  - support-kb
  - elevated-privilege
  - high-security
  - roles
  - security
  - impersonation
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687701
kb_number: KB0687701
last_modified: 2024-04-18
---

## Admin user is being asked to elevate to "admin" role after logging in

  

### Issue

# Symptoms

* * *

An admin user is asked to elevate to admin role when logging in. Users are not able to see the impersonate option before elevating the roles and might be asked to elevate to the admin role again once the session is timed out.

# Release

* * *

All supported releases.

# Cause

* * *

When the High Security plugin is enabled in the instance, users can make certain user roles elevated by checking the **Elevated Privilege** checkbox in the sys\_user\_role record form. This option sets the roles to session-specific privileges.

# Resolution

* * *

If it is the admin role that is having the issue, uncheck the Elevated Privilege checkbox in the admin sys\_user\_role record to resolve the issue.

1.  Make sure that the High Security plugin is enabled.
    
2.  Navigate to the sys\_user\_role table.
    
3.  Search for and select the admin record or navigate to the following link:
    
    https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_user\_role.do?sys\_id=2831a114c611228501d4ea6c309d626d
    
4.  Uncheck the **Elevated Privilege** checkbox.
    
5.  Save the record.
    
6.  Flush the cache and log in to the instance again after making this change.

## Related

- [[KB0694783 - User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list]] - same Elevated Privilege mechanism blocking a different feature
- [[t_ElevateToAPrivilegedRole]] - official docs on elevating to a privileged role
- [[t_ForceAdmManElev]] - official docs on forcing administrator manual elevation
- [[KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[KB0745206 - Developer tab is not displayed in System Settings for admin user]]
