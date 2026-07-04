---
title: "The KB Article is showing KB Block Number and description."
aliases:
  - KB2651155
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651155
kb_number: KB2651155
last_modified: 2026-01-01
---

## The KB Article is showing KB Block Number and description.

  

### Issue

In the Employee Center portal, some Knowledge Base (KB) articles display the KB Block Number and description in the article description when navigating taxonomies.  
This behavior is inconsistent and not expected; the KB Block Number and description should not appear in either navigation or search views.

### Release

Any

### Cause

The issue is caused by a product defect tracked under PRB1822691. Investigation revealed the defect was previously addressed in PRB1676881 and fixed in Employee Center version 31.0.3.

### Resolution

-   Upgrade the Employee Center application to version 31.0.3 or later.
-   The fix for this defect is included in version 31.0.3 and subsequent releases.
