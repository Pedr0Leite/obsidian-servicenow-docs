---
title: "Developer tab is not displayed in System Settings for admin user"
aliases:
  - KB0745206
tags:
  - servicenow
  - support-kb
  - elevated-privilege
  - high-security-plugin
  - admin-role
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745206
kb_number: KB0745206
last_modified: 2024-10-01
---

## Developer tab is not displayed in System Settings for admin user

  

### Issue

# Symptoms

A user who possesses the admin role cannot see the Developer tab in the System Settings popup

# Release

All supported releases

# Cause

When the High Security plugin is enabled in the instance, users can make certain user roles elevated by checking the Elevated Privilege checkbox in the sys\_user\_role record form. This option sets the roles to session-specific privileges.

# Resolution

Uncheck the Elevated Privilege checkbox in the admin sys\_user\_role record to resolve the issue.

1.  Make sure that the High Security plugin is enabled.
2.  Navigate to the sys\_user\_role table.
3.  Search for and select the admin record or navigate to the following link:
4.  https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_user\_role.do?sys\_id=2831a114c611228501d4ea6c309d626d
5.  Uncheck the Elevated Privilege checkbox.
6.  Save the record.
7.  Flush the cache and log in to the instance again after making this change.

Additional Information

Refer to the [Elevated privilege roles](https://docs.servicenow.com/csh?topicname=c_ElevatedPrivilege.html&version=latest "Elevated privilege roles") product documentation which states: **The use of elevated privilege on the admin role is not supported and may cause unexpected behavior.**

## Related

- [[KB0687701 - Admin user is being asked to elevate to admin role after logging in]] - same elevated-privilege-on-admin-role root cause
- [[KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
