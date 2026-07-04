---
title: "'Order by' field is removed from Look up Records action after publishing the flow"
aliases:
  - KB0793200
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793200
kb_number: KB0793200
last_modified: 2024-04-08
---

## 'Order by' field is removed from Look up Records action after publishing the flow

  

### Issue

When using the "Look Up Records" step, the 'Order by' field (for sorting) is removed from Look up Records action after publishing the flow

### Release

NewYork

### Cause

The Look up Records action definition was not referring to the latest snapshot

### Resolution

The Look up Record 'Action Definition' didn't get the NewYork update, which would point to the latest snapshot of the action that had the 'Order By' input added.

  
Instead the action definition was referring to an older snapshot which did not have the 'order by' input and that was the reason the 'Order by' was removed whenever the flow is published.
