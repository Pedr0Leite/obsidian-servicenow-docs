---
title: "Quick Links Not Displayed in Firefox on ESC Portal Main Menu"
aliases:
  - KB2650949
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2650949
kb_number: KB2650949
last_modified: 2026-01-01
---

## Quick Links Not Displayed in Firefox on ESC Portal Main Menu

  

### Issue

In the ESC portal, Quick Links under the "Human Resources" main menu do not display in Firefox unless the browser zoom is set to 120% or higher. The issue does not occur under "Technology" and is observed in Firefox v128.6.0 64-bit and later versions.

### Release

Any

### Cause

Known issue related to PRB1815352 where the Employee Center Menu clips Quick Links content on the right in Firefox due to column layout.

### Resolution

·  Apply the official workaround by commenting out the specific line in the client controller of the Employee Center Menu widget as recommended by the product team.

·  Ensure the workaround is applied to the out-of-box (OOB) widget, not just custom widgets.

·  Validate the fix in Firefox after applying changes.

·  Monitor for updates related to STRY59186225 for a permanent fix in future releases.
