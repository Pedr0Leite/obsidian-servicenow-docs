---
title: "Compose Section Missing for HR Cases in HR Agent Workspace"
aliases:
  - KB2657075
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657075
kb_number: KB2657075
last_modified: 2025-12-16
---

## Compose Section Missing for HR Cases in HR Agent Workspace

  

### Issue

Users were unable to add comments or work notes to HR Cases (sn\_hr\_core\_case) in the HR Agent Workspace because the Compose section was missing. The issue was specific to the sn\_hr\_core\_case table, while the Compose section was visible for sn\_hr\_core\_case\_operations cases. The problem persisted across multiple instances, including production, and previous attempts to resolve via plugin updates were unsuccessful.

### Release

Any

### Cause

The Activities (filtered) field was missing from the sn\_hr\_core\_case form in the workspace\_uib view, which prevented the Compose section from displaying.

### Resolution

To resolve the issue:

-   Navigate to HR Agent Workspace > sn\_hr\_core\_case form and open the workspace\_uib view.
-   Check if the Activities (filtered) field is present on the form.
-   If missing, add the Activities (filtered) field back to the form.
-   Validate the fix in lower environments (DEV, TEST) before moving to production.
-   After approval and change management, implement the same fix in production.
-   Confirm that the Compose section is visible and functional for sn\_hr\_core\_case records.
