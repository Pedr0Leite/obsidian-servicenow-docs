---
title: "Assessment submitted with blank name and category"
aliases:
  - KB0818508
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818508
kb_number: KB0818508
last_modified: 2024-04-08
---

## Assessment submitted with blank name and category

  

### Issue

-   Vendor risk assessments are submitted with blank name and category.

### Release

-   NY Patch 4 HF 2.

### Cause

-   Assessment template was deleted, therefore, it was submitted blank.

### Resolution

-   The templates and categories and metrics are all like blue prints, the final assessment instances do not include the questions as copy, they simply refer to the blue prints. If any metric, category is deleted, assessment instance then cannot find them, it’s missing. Even if they're added back, the sys\_ids are different."
-   So best recommended cleaner way to do this is to create new assessments and send it again. Otherwise it will hard to do, unless customers are ready to do some scripts to fix their broken records.
