---
title: "Quick Links Widget Image Alignment Issue on Employee Center Portal"
aliases:
  - KB2653656
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653656
kb_number: KB2653656
last_modified: 2025-12-17
---

## Quick Links Widget Image Alignment Issue on Employee Center Portal

  

### Issue

On the Employee Center portal, images in the Quick Links section may appear stretched or misaligned. This issue was observed on staging and production environments after upgrading to Employee Center plugin version 35.0.2.

### Release

Any

### Cause

Known issue tracked under PRB1799131. The CSS property `background-size` in the Quick Links widget was changed from `cover` to `100% 100%` in the November release, causing image distortion.

### Resolution

-   Apply the update set provided by ServiceNow to restore correct image alignment in the Quick Links widget.
-   Validate the fix in a sub-production environment before applying to production.
-   Ensure any missing banner images are restored after applying the update set.
-   After the update, the `background-size` property will revert to the correct value, resolving the alignment issue.
