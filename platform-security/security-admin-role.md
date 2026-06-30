---
title: Security\_admin role
description: The security\_admin role is an elevated privilege role provided with High Security Settings that lets users create and change access controls and change High Security Settings.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/security-admin-role.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Elevated privilege roles, Security Roles, Access Management]
---

# Security\_admin role

The security\_admin role is an elevated privilege role provided with [[c_HighSecuritySettings|High Security Settings]] that lets [[users|users]] create and change access controls and change High Security Settings.

In the base system, only the default System Administrator \(admin\) user has the security\_admin role. Since it requires elevating privileges, the admin user does not have this role at login. After elevating privileges, the admin user has the security\_admin role for the duration of the user session. See [[t_ElevateToAPrivilegedRole|Elevate to a privileged role]] for more information.

To maintain high security, the security\_admin role requires elevating privileges. Limit the users and groups to which you assign this role.

**Parent Topic:**[[c_ElevatedPrivilege|Elevated privilege roles]]

**Related topics**  


[Elevate to a privileged role]()

[Force administrators to manually elevate]()

## Related

- [[t_ElevateToAPrivilegedRole|Elevate to a privileged role]]
- [[c_ElevatedPrivilege|Elevated privilege roles]]
- [[c_HighSecuritySettings|High Security Settings]]
- [[users|Users]]
