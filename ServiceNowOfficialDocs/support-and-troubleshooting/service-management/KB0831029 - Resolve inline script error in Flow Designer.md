---
title: "Resolve inline script error in Flow Designer"
aliases:
  - KB0831029
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831029
kb_number: KB0831029
last_modified: 2025-08-26
---

## Resolve inline script error in Flow Designer

  

### Issue

When using an inline script in a flow, you may get the error "fd\_data is not defined".

### Release

  Any supported release

### Cause

Data is accessed via the object fd\_data and not in combination with fd\_data.trigger.current or a similar construction.

### Resolution

To resolve this error, avoid using fd\_data on its own. Instead, use fd\_data.trigger.current or fd\_data.trigger.current.number or a similar construction to receive valid data.

### Related Links

For the latest information, refer to [Inline scripts](https://docs.servicenow.com/csh?topicname=inline-scripts.html&version=latest)
