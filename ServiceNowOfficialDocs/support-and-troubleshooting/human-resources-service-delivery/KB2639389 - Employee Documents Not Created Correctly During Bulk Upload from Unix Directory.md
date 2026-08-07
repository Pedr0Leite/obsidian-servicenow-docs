---
title: "Employee Documents Not Created Correctly During Bulk Upload from Unix Directory"
aliases:
  - KB2639389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639389
kb_number: KB2639389
last_modified: 2026-01-03
---

## Employee Documents Not Created Correctly During Bulk Upload from Unix Directory

  

### Issue

Employee documents are not created correctly when using ServiceNow bulk upload from a local Unix directory. Files appear in the sys\_attachment table, but the resulting employee document records are incorrect or show errors when opened.

### Release

Any Release

### Cause

The issue occurs due to missing or corrupted components in the Employee Document plugin, which prevents proper parsing and linking of uploaded files.

### Resolution

-   Verify that the Employee Document plugin is installed and active.
-   If the plugin is missing or partially removed, repair the plugin using the Plugin Manager.
-   After repairing, retry the bulk upload process to confirm that employee documents are created correctly.
