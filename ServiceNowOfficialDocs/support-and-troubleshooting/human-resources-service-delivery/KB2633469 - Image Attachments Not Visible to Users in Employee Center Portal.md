---
title: "Image Attachments Not Visible to Users in Employee Center Portal"
aliases:
  - KB2633469
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633469
kb_number: KB2633469
last_modified: 2026-01-01
---

## Image Attachments Not Visible to Users in Employee Center Portal

  

### Issue

In the Employee Center portal, image attachments for web applications and quicklinks are not visible to standard users; only text is displayed.  
Administrators can view images, but normal users see blank boxes, indicating a permissions-related issue.

### Release

Any Release

### Cause

-   Users lacked access to thumbnail records required for image display.
-   A read ACL on the sys\_attachment table was missing the snc\_internal role.
-   This role is typically added by the com.glide.explicit\_role plugin; missing configuration caused the issue.

### Resolution

-   Review ACLs on the sys\_attachment table and confirm required roles are present.
-   Add the snc\_internal role to the read ACL for sys\_attachment by importing the appropriate XML configuration or updating the ACL manually.
-   Ensure the com.glide.explicit\_role plugin is active and verify that the role persists after upgrades.
-   Validate image visibility for standard users after applying the changes.
