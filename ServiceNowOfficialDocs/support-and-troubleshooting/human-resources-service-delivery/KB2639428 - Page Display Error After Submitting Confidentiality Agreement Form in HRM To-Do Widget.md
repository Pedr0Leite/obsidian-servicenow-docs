---
title: "Page Display Error After Submitting Confidentiality Agreement Form in HRM To-Do Widget"
aliases:
  - KB2639428
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639428
kb_number: KB2639428
last_modified: 2026-01-02
---

## Page Display Error After Submitting Confidentiality Agreement Form in HRM To-Do Widget

  

### Issue

After submitting the Confidentiality Agreement form in the HRM To-Do widget, users intermittently encounter a page display error message. The issue occurs more frequently in test environments and is related to widget timing and handler table behavior.

### Release

Washington

### Cause

A product defect (PRB1824146) in the widget’s server script causes timing issues during form submission, especially under network latency conditions.

### Resolution

-   Upgrade to Employee Center Bundle version 36.0.5 (or later), which includes the permanent fix for PRB1824146.
-   Revert any customizations and restore the widget to its latest out-of-box (OOB) version before applying the update.
-   Avoid using temporary workarounds after the upgrade to prevent future conflicts.
