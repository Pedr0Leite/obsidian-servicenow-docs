---
title: "Hide or Remove \"Add link in email\" Option in HR Agent Workspace"
aliases:
  - KB2648601
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2648601
kb_number: KB2648601
last_modified: 2026-01-03
---

## Hide or Remove "Add link in email" Option in HR Agent Workspace

  

### Issue

Users want to hide or remove the Add link in email option from the dropdown in HR Agent Workspace, as changing the embedded link is not possible. Attempts to locate the configuration were unsuccessful.

### Release

Any

### Cause

The visibility of the Add link in email option is controlled by configuration settings in the cxs\_table\_config table.

### Resolution

To hide or remove the option:

-   Navigate to the cxs\_table\_config table.
-   Locate the record associated with the Add link in email option.
-   In the UI Action Visibility tab, set the Visible value to false.
-   Save and publish the changes.
-   Verify that the option is no longer visible in HR Agent Workspace.
