---
title: "Source Request UI Action Visible to Users Without the Asset Role"
aliases:
  - KB3021886
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3021886
kb_number: KB3021886
last_modified: 2026-06-08
---

## Source Request UI Action Visible to Users Without the Asset Role

  

### Issue

The Source Request UI action on the Requested Item (RITM) or task record is visible to users who do not have the asset role. When those users select the button, an access error appears because the sourcing form requires the asset role to load correctly. 

### Symptoms

-   Log in as a user who does not have the asset role.
-   Open a Requested Item (RITM) that has sourcing enabled (hardware model mapped to the catalog item).
-   Verify that the Source Request button is visible.
-   Select Source Request.
-   An access error appears when the sourcing form attempts to load.

### Release

ALL

### Cause

The visibility condition on the Source Request UI action does not check for the asset role. In the base system, the condition evaluates the following:

```
current.parent.sys_class_name == "sc_request" && !current.parent.sourced 
&& !current.isNewRecord() 
&& (gs.getSession().getProperty('user_agent_browser') == 'ie' 
&& gs.getSession().getProperty('user_agent_version') < 10) 
&& current.canRead()
```

For ACLs, the system checks whether the user has read access to the `sc_task` record. As a result, the Source Request button is visible to users who can read the record, regardless of whether they have the asset role.

Because the role check is absent from the UI action condition, users without the asset role can see the button. When they select it, the sourcing form attempts to load records from the `alm_sourcing_request` table, stockrooms, and Transfer Orders. The system returns an access control error because those records require the asset role or equivalent.

### Resolution

To prevent users without the asset role from seeing the Source Request UI action, update the UI action condition to include a role check.

1.  Log in as an administrator.
2.  Navigate to System Definition > UI Actions.
3.  Search for the Source Request UI action associated with the RITM or task table.
4.  In the Condition field, add a check to verify that the current user has the asset role. For example:

```
   gs.hasRole('asset')
```

5.  Select Update to save the change.
6.  Log in as a user without the asset role and confirm that the Source Request button is no longer visible on the RITM record.

Note: Test this change in a non-production instance before applying it to your production environment.
