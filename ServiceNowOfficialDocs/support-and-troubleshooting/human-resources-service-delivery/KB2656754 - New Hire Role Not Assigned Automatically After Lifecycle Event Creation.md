---
title: "New Hire Role Not Assigned Automatically After Lifecycle Event Creation"
aliases:
  - KB2656754
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656754
kb_number: KB2656754
last_modified: 2026-01-03
---

## New Hire Role Not Assigned Automatically After Lifecycle Event Creation

  

### Issue

The sn\_hr\_sp.hrsp\_new\_hire role was not automatically assigned to new hire candidates after the HR lifecycle event was created, preventing access to the Onboarding portal.

### Release

Any

### Cause

The scheduled job Update Client Roles depends on the HR Admin user having the sn\_hr\_core\_admin role. This role was removed from the HR Admin user profile, causing the job to fail.

### Resolution

-   Verify that the HR Admin user has the sn\_hr\_core\_admin role.
-   If missing, restore the sn\_hr\_core\_admin role to the HR Admin user profile.
-   Confirm that the scheduled job Update Client Roles runs successfully and assigns the sn\_hr\_sp.hrsp\_new\_hire role to new hires.
