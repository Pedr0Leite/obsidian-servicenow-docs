---
title: "Employee Center Portal Blank on Mobile Browsers After Yokohama Upgrade"
aliases:
  - KB2653594
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653594
kb_number: KB2653594
last_modified: 2026-01-01
---

## Employee Center Portal Blank on Mobile Browsers After Yokohama Upgrade

  

### Issue

After upgrading to the Yokohama release, the Employee Center Portal displays as blank (only the Virtual Agent is visible) when accessed via Chrome or Safari on mobile browsers. Firefox displays the portal correctly. The issue does not occur in the Now Mobile App.

### Release

Any

### Cause

Known issue tracked under PRB1903526, affecting Employee Center Portal rendering on mobile browsers after the Yokohama upgrade.

### Resolution

-   Upgrade to Yokohama Patch 6, which includes the fix for PRB1903526.
-   Apply the patch in a sub-production environment first, validate the resolution, and then upgrade production.
