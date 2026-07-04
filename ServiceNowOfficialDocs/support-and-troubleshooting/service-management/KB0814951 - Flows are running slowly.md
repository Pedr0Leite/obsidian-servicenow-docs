---
title: "Flows are running slowly"
aliases:
  - KB0814951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814951
kb_number: KB0814951
last_modified: 2025-05-13
---

## Flows are running slowly

  

### Issue

The user was migrating from Workflows to Flow Designer and noticed some delays with Flow processing speed when compared to what they were used to (Workflows). They wanted to know the cause of the delays.

### Resolution

The simplest explanation would be that Flow Designer Flows runs asynchronously meaning that they run in parallel with other scheduled jobs, whereas workflows run synchronously and fire immediately upon insert/update.  
  
Flows can take additional time - say, if the event queue is very busy or backed up. All flows are started via a "flow.fire" event. So, if the event queue is lagging behind at all, this could result in Flows processing more slowly.  
  
To quickly check the status of an instance's event queue type "System Diagnostics" into the left navigator and navigate to System Diagnostics ➛ Diagnostics Page and search the page (Mac: CMD + F / Win: CTRL + F) for "Events pending". If that number is in red, this is likely the root cause of Flows processing very slowly or not at all.
