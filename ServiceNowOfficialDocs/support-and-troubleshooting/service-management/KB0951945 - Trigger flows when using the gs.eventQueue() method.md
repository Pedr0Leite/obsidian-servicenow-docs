---
title: "Trigger flows when using the gs.eventQueue() method"
aliases:
  - KB0951945
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951945
kb_number: KB0951945
last_modified: 2025-08-27
---

## Trigger flows when using the gs.eventQueue() method

  

### Issue

When setting a flow trigger condition for event creation or update on the sysevent table, events created using the gs.eventQueue() method do not start the flow as expected.

### Release

All releases

### Cause

This is expected behavior.

### Resolution

The gs.eventQueue() method is part of the GlideSystem server-side API and does not start a flow when creating event records. To resolve this limitation, use an API that directly calls the flow instead. 

### Related Links

[Developer documentation for the flow API](https://developer.servicenow.com/dev.do#!/reference/api/orlando/server/sn_fd-namespace/ScriptableFlowAPI)
