---
title: "Flow Designer throws 'PlanRecursionException' exception"
aliases:
  - KB0827009
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827009
kb_number: KB0827009
last_modified: 2026-03-16
---

## Issue

Your Flow might not be working as expected and you might see the following exceptions in the logs:

```
2020-06-01 15:14:50 (731) worker.4 worker.4 txid=1bf4470fdb01 DEBUG: Flow Designer: Trigger with id 0d2d4729db1c5c1c6ff19ae8db9619fcfiring2020-06-01 15:14:50 (736) worker.4 worker.4 txid=1bf4470fdb01 Complex type redefined: FlowDesigner:FDCollection2020-06-01 15:14:50 (741) worker.4 worker.4 txid=1bf4470fdb01 Flow self recursion Prohibited. Plan id f6a67ee5dbd45c1c6ff19ae8db96199e2020-06-01 15:14:50 (741) worker.4 worker.4 txid=1bf4470fdb01 SEVERE *** ERROR *** Failed while firing trigger 0d2d4729db1c5c1c6ff19ae8db9619fc2020-06-01 15:14:50 (742) worker.4 worker.4 txid=1bf4470fdb01 DEBUG: Flow Designer: com.snc.process_flow.exception.PlanRecursionException: Plan recursion has been encountered
```

## Resolution

Make sure that there are no recursions in the flow.
