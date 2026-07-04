---
title: "Flow fails during Lookup Record when no records are found"
aliases:
  - KB0954943
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954943
kb_number: KB0954943
last_modified: 2025-08-05
---

## Flow fails during Lookup Record when no records are found

  

### Issue

When a flow contains a lookup record action but returns no records, it generates an error. This also causes an error with the flow. 

### Release

Any release

### Resolution

This behavior is as expected. To avoid this, consider using lookup records (plural) instead of lookup record. This avoids the error if no records are returned.

You can add an if-condition after the lookup to address the output.

-   If record count is 0, cancel the flow
-   If count is greater than 0, continue
