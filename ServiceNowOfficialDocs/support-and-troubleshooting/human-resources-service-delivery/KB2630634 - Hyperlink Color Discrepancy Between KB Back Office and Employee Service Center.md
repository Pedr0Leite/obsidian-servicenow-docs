---
title: "Hyperlink Color Discrepancy Between KB Back Office and Employee Service Center"
aliases:
  - KB2630634
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630634
kb_number: KB2630634
last_modified: 2026-01-01
---

## Hyperlink Color Discrepancy Between KB Back Office and Employee Service Center

  

### Issue

-   Hyperlinks in Knowledge Base (KB) back office articles display in black, while the same hyperlinks in the Employee Service Center (ESC) portal appear in blue.
-   The hyperlink color in ESC does not match the color defined in the KB article, causing inconsistent user experience.
-   Expected behavior: hyperlink colors should be consistent across KB and ESC as defined in the article content.

### Release

Any Release

### Cause

-   Discrepancy caused by custom widgets and theme overrides in the ESC portal.
-   Out-of-box (OOB) widget displays expected behavior.
-   Root cause linked to a known product defect (PRB1822090), fixed in employee-center-bundle 36.0.4 and later plugin versions.

### Resolution

-   Update Employee Center plugins to the latest available versions.
-   Remove any custom theme or widget overrides affecting hyperlink color.
-   After plugin upgrade and cleanup, hyperlink colors display consistently in KB and ESC portals.
