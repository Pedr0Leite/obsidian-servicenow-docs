---
title: "Flow is stuck in the continue_sync state"
aliases:
  - KB0953126
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953126
kb_number: KB0953126
last_modified: 2024-01-19
---

## Flow is stuck in the continue\_sync state

  

### Issue

The Flow can stuck in continue\_sync state when using sn\_fd.FlowAPI.executeFlow() for flows that quiesce

or calling a subflow in foreground that times out while executing on Mid server

### Resolution

Please see the Fixed in versions of the related known error articles  
  

1\. The Flow can be stuck in the continue\_sync state when using sn\_fd.FlowAPI.executeFlow() for flows that quiesce

There is a problem related to this issue. Please refer to the following Known Error article

[KB0852831 - Flow stops with no clear reason and stuck in "Continue Sync" state](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=3cd3bb171b12d8103222ea89bd4bcb4f "KB0852831 - Flow stops with no clear reason and stuck in \"Continue Sync\" state")

  

2\. Calling a subflow in the foreground that times out while executing on mid. it should error out instead.

Please refer to the following Known Error article

[KB0953164 - Calling a subflow in foreground that times out while executing on mid the flow ends in state continue\_sync when it should end it state error](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=03ec18c1db9e6050fb115583ca96198c "KB0953164 - Calling a subflow in foreground that times out while executing on mid the flow ends in state continue_sync when it should end it state error")
