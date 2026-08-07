---
title: " Flow fails to delete user roles due to inherited role restrictions"
aliases:
  - KB0996223
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996223
kb_number: KB0996223
last_modified: 2025-08-04
---

## Flow fails to delete user roles due to inherited role restrictions

  

### Issue

A flow action that includes deleting user roles fails with the error "Unknown error occurred while deleting the record."

### Release

Any release

### Cause

By default, admins cannot delete - either manually or using a script - the records in the User Roles \[sys\_user\_has\_role\] table where the Inherited property value equals true. 

Here's how inherited roles work:

-   Roles with Inherited = false contain roles termed as Inherited = true
-   Deleting a role with Inherited = false automatically removes all associated roles with Inherited = true
-   This is expected default behavior

The flow error occurs because:

1.  The flow attempts to delete all roles for a specific user
2.  This includes both roles with Inherited = true and Inherited = false
3.  The system blocks deletion of inherited roles (Inherited = true)

### Resolution

To resolve the error, filter the flow to target only non-inherited roles.

1.  In the flow, locate the step that looks up sys\_user\_has\_role records for the user.
2.  Add a condition: Inherited = false.
3.  Run the flow.

The flow only fetches and deletes the roles that are not inherited (Inherited = false) from the user profile. The system also deletes the associated roles that have Inherited = true.
