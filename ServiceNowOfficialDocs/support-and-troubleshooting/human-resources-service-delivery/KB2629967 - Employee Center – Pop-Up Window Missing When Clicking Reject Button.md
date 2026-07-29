---
title: "Employee Center – Pop-Up Window Missing When Clicking Reject Button"
aliases:
  - KB2629967
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2629967
kb_number: KB2629967
last_modified: 2025-12-16
---

## Employee Center – Pop-Up Window Missing When Clicking Reject Button

  

### Issue

On the Employee Center (ESC) portal, some users do not see a pop-up window when clicking the Reject button on the main page.  
The pop-up is expected to appear for all users to provide a rejection reason, but this behavior is inconsistent.  
The issue does not occur for admin users.

### Release

Any Release

### Cause

The pop-up for rejection comments is controlled by user roles.  
Users without the roles sn\_request\_write or sn\_request\_comments\_write will not see the pop-up, even if they have write access in other areas.

### Resolution

-   Verify whether affected users have the roles sn\_request\_write or sn\_request\_comments\_write.
-   If missing, assign one of these roles to the user.
-   After adding the role, test the Reject button in My Active Items to confirm the pop-up appears as expected.
-   No additional configuration changes are required once the correct role is assigned.
