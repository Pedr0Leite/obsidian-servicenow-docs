---
title: "Organizational Chart Displays Incorrect Users in Manager Hub"
aliases:
  - KB2633225
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633225
kb_number: KB2633225
last_modified: 2026-01-01
---

## Organizational Chart Displays Incorrect Users in Manager Hub

  

### Issue

The Organizational Chart in Manager Hub sometimes shows one user more or less than expected. In some cases, viewing the org chart for a team member still displays the logged-in user’s chart. Both issues occur on the my\_org\_chart page using the Organization Chart (CD) widget.

### Release

Any Release

### Cause

The Organization Chart (CD) widget only displays users who have a value in the employment\_start\_date field of their HR profile. Users without this field populated are skipped in the hierarchy.

### Resolution

Populate Required Field

-   Navigate to the HR profile of affected users.
-   Add a valid date in the employment\_start\_date field.
-   Save changes.

Validate Org Chart

-   Refresh the my\_org\_chart page.
-   Confirm that the org chart now displays the correct hierarchy.

Alternative Option

-   Use the Organization Chart (EC) widget (available in Employee Center Pro), which does not require the employment start date field.

Best Practice

-   Ensure all relevant HR profiles have complete data for fields used in org chart logic.
-   Avoid customizing read-only portals that restrict widget changes.
