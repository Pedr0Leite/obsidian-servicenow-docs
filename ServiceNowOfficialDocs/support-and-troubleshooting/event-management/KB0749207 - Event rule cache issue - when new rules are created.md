---
title: "Event rule cache issue - when new rules are created"
aliases:
  - KB0749207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749207
kb_number: KB0749207
last_modified: 2024-04-07
---

## Issue

-   Create an event rule
-   On the event that matches the rule, click on 'check process of event' related link
-   The newly created event rule is not found in the retrieved list

## Resolution

-   When the issue happened, we couldn't get enough details to log a PRB.
-   Customer leveraged a script that refreshes the cache periodically.

  

Script:

gs.cacheFlush("em\_match\_rule\_cache");   
gs.cacheFlush("em\_match\_field\_cache");   
gs.cacheFlush("em\_compose\_field\_cache");
