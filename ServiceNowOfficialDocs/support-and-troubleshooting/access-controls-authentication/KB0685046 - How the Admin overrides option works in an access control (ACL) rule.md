---
title: " How the Admin overrides option works in an access control (ACL) rule"
aliases:
  - KB0685046
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - admin-overrides
  - roles
  - security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685046
kb_number: KB0685046
last_modified: 2026-06-17
---

## How the Admin overrides option works in an access control (ACL) rule

  

### Issue

Learn how the Admin overrides option works on an access control list (ACL) rule and why clearing it is not enough on its own to block users with the admin role from accessing specific data.

When you create or modify an ACL rule, one of the available fields is **Admin overrides**. This field can cause confusion: clearing the check box and adding a role does not, by itself, prevent users with the admin role from reaching the secured data.

The Admin overrides option lets users with the admin role automatically pass the permission check for the ACL rule, regardless of the script or role restrictions that apply. The nobody role takes precedence over this option. When an ACL rule is assigned the nobody role, users with the admin role cannot access the resource even when Admin overrides is selected.

Because the admin role satisfies role checks, clearing the Admin overrides check box and adding a role is not enough to block admin access. To require administrators to meet the permissions defined in the rule, clear the check box and add a condition or script that the admin role must also pass.

### Release

All supported releases

### Resolution

To require users with the admin role to meet the permissions in an ACL rule, add a condition in the condition builder, or select the **Advanced** option and add a script that prevents admin access.

For example, to prevent users with the admin role from accessing a table:

1.  Create a read ACL rule for the table you want to secure.
2.  Clear the **Admin overrides** check box.
3.  (Optional) Add a role.
4.  Add a condition in the condition builder, a script, or both. To add a script, select the **Advanced** check box and enter the script in the **Script** field.

**Example script that blocks the admin role**

  
var answer = true;   
if (gs.getUser().hasRole('admin'))   
{   
answer = false;   
}

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[t_EvalAdmOverrideAccLevel]] - official docs on evaluating admin override access level
- [[access-control-rules]] - official docs on access control rules
- [[KB0727619 - The Field actions menu for an inbound email action is not showing all fields]] - a save_as_template ACL issue resolved via the Admin overrides checkbox
