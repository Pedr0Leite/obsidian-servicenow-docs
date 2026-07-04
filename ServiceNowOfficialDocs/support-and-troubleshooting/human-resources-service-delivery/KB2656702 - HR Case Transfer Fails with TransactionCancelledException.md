---
title: "HR Case Transfer Fails with TransactionCancelledException"
aliases:
  - KB2656702
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656702
kb_number: KB2656702
last_modified: 2025-12-17
---

## HR Case Transfer Fails with TransactionCancelledException

  

### Issue

Users are unable to transfer HR cases between certain services (e.g., from General HR Question to Retirement or Employee Resignation). Attempts to transfer result in:

```
com.glide.sys.TransactionCancelledException: Transaction cancelled: maximum execution time exceeded
```

### Release

Any

### Cause

Transferring cases to services like Retirement or Employee Resignation triggers a large number of workflow activity sets, exceeding system limits and causing transaction timeouts.

### Resolution

-   Do not transfer cases in Ready state, as this immediately triggers all workflows.
-   Instead:
    -   Transfer the case in Draft state (prevents workflow execution during transfer).
    -   After transfer, manually move the case to Ready via the UI.
-   Optionally, implement a business rule to set transferred cases to Draft automatically.
-   Validate that transfers complete successfully without timeouts.
