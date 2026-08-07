---
title: "How to remove the sn_hr_sp.esc_admin role from the admin role"
aliases:
  - KB0755910
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755910
kb_number: KB0755910
last_modified: 2024-04-07
---

## How to remove the sn\_hr\_sp.esc\_admin role from the admin role

  

### Issue

When trying to remove the sn\_hr\_sp.esc\_admin from the admin role this fails.

Editing contains a related list and removing the role will not actually remove it.

### Release

Madrid

### Cause

The sn\_hr\_sp.esc\_admin is a scoped role but the admin role is in the global scope. Edit is only available when you are in the scope of the role but you can only modify the sn\_hr\_sp.esc\_admin role when you are in the 'Human Resources: Service Portal' scope.

### Resolution

1.  . Make sure you have both the admin role and the sn\_hr\_sp.esc\_admin role explicitly assigned to yourself. The sn\_hr\_sp.esc\_admin role should not be inherited. Otherwise, you could lock yourself out of the 'Human Resources: Service Portal' scope. If that happens contact support to give you the role again.
2.  Set yourself to the 'Human Resources: Service Portal' scope
3.  Navigate to the 'admin' role
4.  In the 'Contains Roles' related list select 'sn\_hr\_sp.esc\_admin'
5.  Under 'Actions on selected rows' click delete
6.  Confirm the delete.
