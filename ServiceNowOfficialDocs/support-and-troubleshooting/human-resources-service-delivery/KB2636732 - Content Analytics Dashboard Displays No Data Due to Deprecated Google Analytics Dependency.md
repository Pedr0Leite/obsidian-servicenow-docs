---
title: "Content Analytics Dashboard Displays No Data Due to Deprecated Google Analytics Dependency"
aliases:
  - KB2636732
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636732
kb_number: KB2636732
last_modified: 2026-01-01
---

## Content Analytics Dashboard Displays No Data Due to Deprecated Google Analytics Dependency

  

### Issue

The Content Analytics dashboard shows “No Data to Display” or zero records across PROD, DEV, and sub-instances.

-   Metrics such as Total Session Duration, Average Time on Page, and Bounce Rate remain empty.
-   Impersonation tests confirm the issue persists for affected users in multiple environments.

### Release

Any Release

### Cause

These visualizations depend on classic Google Analytics, which was deprecated on July 1, 2023.  
As a result, metrics like Total Session Duration, Average Time on Page, and Bounce Rate are no longer supported and will be retired from Content Analytics.

### Resolution

1.  Identify widgets in the Content Analytics dashboard that rely on Google Analytics (e.g., Total Session Duration, Bounce Rate).
2.  Remove or ignore these unsupported widgets, as they will not display data.
3.  Navigate to Performance Analytics > Dashboards > User Experience Analytics for supported metrics:
    -   Verify metrics such as Page Views, Session Counts, and Engagement.
4.  Update internal documentation and dashboards to reflect the use of User Experience Analytics instead of deprecated Google Analytics metrics.
5.  For custom reporting needs, configure new indicators using available data sources.

Additional Info:

-   A defect (PRB1843383) was logged to retire unsupported Google Analytics-dependent visualizations.
-   Migration to supported dashboards is required for accurate analytics reporting
