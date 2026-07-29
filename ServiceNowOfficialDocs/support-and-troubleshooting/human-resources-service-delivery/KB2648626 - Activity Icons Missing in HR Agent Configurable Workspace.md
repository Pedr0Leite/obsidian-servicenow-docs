---
title: "Activity Icons Missing in HR Agent Configurable Workspace"
aliases:
  - KB2648626
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2648626
kb_number: KB2648626
last_modified: 2026-01-03
---

## Activity Icons Missing in HR Agent Configurable Workspace

  

### Issue

In the HR Agent Configurable Workspace, several activity icons (such as attachments and response templates) are missing from HR Task records. These icons are available in the legacy workspace but not visible in the new Configurable Workspace.

### Release

Any

### Cause

The issue is due to a product defect in earlier versions of the Agent Workspace for HR Case Management plugin.

### Resolution

To restore missing icons:

-   Check the current version of the Agent Workspace for HR Case Management plugin.
-   Upgrade the plugin to version 3.2.1 or higher (recommended: 3.3.1) where the defect is fixed.
-   Validate that activity icons, including response templates, appear and function correctly in HR Task records after the upgrade.
