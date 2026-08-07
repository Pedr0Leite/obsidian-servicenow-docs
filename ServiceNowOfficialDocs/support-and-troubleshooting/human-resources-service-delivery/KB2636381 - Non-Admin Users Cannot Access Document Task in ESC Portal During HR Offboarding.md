---
title: "Non-Admin Users Cannot Access Document Task in ESC Portal During HR Offboarding"
aliases:
  - KB2636381
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636381
kb_number: KB2636381
last_modified: 2026-01-01
---

## Non-Admin Users Cannot Access Document Task in ESC Portal During HR Offboarding

  

### Issue

For HR offboarding, OOB automatic document task creation works for admin users, but non-admin users cannot load the document task in the ESC portal under My Task.

-   Non-admin users have the required role and can view the document task in the `sn_doc_task` table.
-   However, they cannot access or sign the document via the portal widget.

### Release

Any Release

### Cause

The To-dos task Line Item widget required specific roles (e.g., `snc_internal`) shipped with the Explicit Roles plugin. Non-admin users lacked the correct reader role, preventing widget access.

### Resolution

-   Reviewed the widget configuration and identified role-based restrictions.
-   Added the sn\_doc\_reader role to the To-dos task Line Item widget (`/sp_widget.do?sys_id=a4716c8f53d3130030f3ddeeff7b1288`).
-   This change ensures:
    -   Non-admin users can view document tasks under My Task in the ESC portal.
    -   Users can open and sign documents directly through the portal interface.
-   After applying this update, document tasks became accessible and fully functional for non-admin users.
