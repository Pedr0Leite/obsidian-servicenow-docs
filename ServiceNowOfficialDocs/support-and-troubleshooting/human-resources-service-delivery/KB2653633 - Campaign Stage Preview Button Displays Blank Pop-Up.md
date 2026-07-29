---
title: "Campaign Stage Preview Button Displays Blank Pop-Up"
aliases:
  - KB2653633
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653633
kb_number: KB2653633
last_modified: 2025-12-17
---

## Campaign Stage Preview Button Displays Blank Pop-Up

  

### Issue

In the Content Experience Builder, the Preview button (eye icon) in campaign stages intermittently fails to render content, resulting in a blank pop-up. The issue impacts the ability to preview scheduled campaign content.

### Release

Any

### Cause

Known issue tracked under PRB1826832, related to CSS display behavior in the Campaign Builde

### Resolution

-   Upgrade the Content Experiences Bundle to version 32.1.3 (January 2025 release) from the ServiceNow Store.
-   Validate the fix in a sub-production environment before upgrading production.
-   After upgrading, the Preview button should function as expected.
