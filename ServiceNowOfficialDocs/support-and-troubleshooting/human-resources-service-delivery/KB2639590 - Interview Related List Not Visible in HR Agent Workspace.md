---
title: "Interview Related List Not Visible in HR Agent Workspace"
aliases:
  - KB2639590
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639590
kb_number: KB2639590
last_modified: 2026-01-03
---

## Interview Related List Not Visible in HR Agent Workspace

  

### Issue

Interview records entered in HR Cases are not visible in HR Agent Workspace, but are visible in the Native view. Other related lists display correctly; the issue is isolated to the Interview related list.

### Release

Any Release

### Cause

A rendering issue occurs when the End Date column in the Interview related list is empty and appears first in the display order. This triggers a date formatting bug, resulting in console errors such as:

-   `RangeError: Invalid time value`
-   `TypeError: Cannot read properties of null (reading 'shadowRoot')`

### Resolution

-   Change the user preference to a long date/time format (e.g., `MM/DD/YYYY 9:00:01`).
-   Rearrange columns so that empty date fields (e.g., End Date) are not the first column in the display order.
-   Monitor PRB1930125 for the permanent fix in a future release.
