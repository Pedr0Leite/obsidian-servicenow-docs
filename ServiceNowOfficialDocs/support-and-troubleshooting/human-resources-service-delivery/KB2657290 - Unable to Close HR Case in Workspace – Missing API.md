---
title: "Unable to Close HR Case in Workspace – Missing API"
aliases:
  - KB2657290
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657290
kb_number: KB2657290
last_modified: 2025-12-17
---

## Unable to Close HR Case in Workspace – Missing API

  

### Issue

In HR Agent Workspace, clicking Close Complete does nothing and an error appears in the console log.  
The issue occurs only in the workspace view; the native UI works correctly.

### Release

Any

### Cause

The required API endpoint `/api/sn_hr_core/hr_rest_api/get_complete_state` was missing from the instance. This occurred due to an incomplete or corrupted installation of the Human Resources Scoped App: Core plugin.

### Resolution

-   Repair the Human Resources Scoped App: Core plugin to restore missing API resources.
-   Verify that the Close Complete action works as expected after the plugin repair.
