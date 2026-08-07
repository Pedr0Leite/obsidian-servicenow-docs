---
title: "When creating a new SLA Definition in the global scope, the scope is switched to something else on insert"
aliases:
  - KB0824663
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824663
kb_number: KB0824663
last_modified: 2024-04-08
---

## When creating a new SLA Definition in the global scope, the scope is switched to something else on insert

  

### Issue

Whenever the user was creating a new SLA Definition in the global scope, when saving the record, the scope would be set to HR unexpectedly.

### Resolution

It was found that a custom Business Rule was setting the scope to HR. When the custom Business Rule was disabled, the issue subsided, and newly created SLAs in the global scope inserted properly into the global application.
