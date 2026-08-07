---
title: "Unable to view all sys_user_preferences records as an Admin, seeing security constraints message"
aliases:
  - KB0743902
tags:
  - servicenow
  - support-kb
  - acl
  - admin-override
  - sys_user_preference
  - security-admin
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743902
kb_number: KB0743902
last_modified: 2025-08-06
---

## Unable to view all sys\_user\_preferences records as an Admin, seeing security constraints message

  

### Issue

Admin unable to view all sys\_user\_preferences records seeing security constraints message.

### Release

  All Relases

### Cause

Log in as an admin

1.  Type in the navigator filter sys\_user\_preferences.list
2.  You will be unable to view all records.
    -   An error message states: "**Number of rows removed from this list by Security constraints: #**"
3.  Elevate roles to security\_admin
4.  Still unable to view records

### Resolution

The System property "**glide.security.admin.override.accessterm**" is set to _false_, while it's _true_ in a base system. See: [Evaluate the admin override at the access level](https://docs.servicenow.com/csh?topicname=t_EvalAdmOverrideAccLevel.html&version=latest "Evaluate the admin override at the access level")

The ACL: "sys\_user\_preference" /read is blocking your access even though you have the admin override it is being ignored due to the system property being set to false.

If your business process allows, you should set "**glide.security.admin.override.accessterm**" to _true_ so the overrides in the ACLs for the admins would work.

### Related Links

The "security\_admin" role cannot be inherited, it must be added by a user that has it as not inherited like the "admin" account. We recommend taking it out of the group and adding the role to each user that has an admin account that you want to have the security\_admin role from an account that does not have it inherited from a group like the "admin" account.

[Evaluate the admin override at the access level](https://docs.servicenow.com/csh?topicname=t_EvalAdmOverrideAccLevel.html&version=latest "Evaluate the admin override at the access level")

## Related

- [[KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[KB0727246 - Admin Role related list shows more users versus Edit sluchbucket]]
- [[t_EvalAdmOverrideAccLevel]] - official docs on evaluating the admin override at the access level

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0695387 - For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get |For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0749023 - Unable to add roles, Insert new a row does not exist.|Unable to add roles, Insert new a row does not exist.]]
