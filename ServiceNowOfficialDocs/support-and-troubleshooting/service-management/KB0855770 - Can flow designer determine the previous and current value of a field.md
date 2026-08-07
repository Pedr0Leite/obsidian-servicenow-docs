---
title: "Can flow designer determine the previous and current value of a field?"
aliases:
  - KB0855770
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855770
kb_number: KB0855770
last_modified: 2025-01-03
---

## Can flow designer determine the previous and current value of a field?

  

### Summary

Can flow designers determine the previous and current value of a field, like business rules?

Could a flow designer be called from a business rule?

### Release

All

### Instructions

 Flow Designer is not the best tool to use for this particular Use Case.

Flow Designer will run in the background, similar to scheduled jobs and asynchronous business rules. There will always be a delay between the actual trigger and the start of the flow. So it's not a replacement for before or after business rules.

But for use cases that you would previously have solved with an asynchronous business rule, you can consider using the flow designer.
