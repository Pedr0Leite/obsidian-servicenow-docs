---
title: "Content Analytics Reports Display \"No Data Available\" in Employee Center"
aliases:
  - KB2651010
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651010
kb_number: KB2651010
last_modified: 2025-12-16
---

## Content Analytics Reports Display "No Data Available" in Employee Center

  

### Issue

Content Analytics reports for Content Publishing records in Employee Center show “No data available” for all content types (Rich Text, Banners, Events, etc.). Content Analytics is enabled and a Content Delivery Profile is active, but expected profiles are not available as options.

### Release

Any 

### Cause

Backend flows and tracking profiles were present, but data migration and dashboard population were impacted by defects in analytics processing.

### Resolution

-   Upgrade Content Publishing plugins to the latest available version to ensure compatibility with analytics features.
-   Apply defect fixes via update sets provided by ServiceNow:
    -   PRB1895477 (resolves “no clicks” issue)
    -   PRB1917731 (fixes Content Library Overview visualizations)
-   Import and commit the update sets in the affected instance.
-   If the instance is cloned, reapply the update sets after the clone process.
-   Validate dashboards such as Top Pages and Content Library Overview to confirm data is displayed correctly.
