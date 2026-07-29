---
title: "Event Management Alert Auto-Closure"
aliases:
  - KB0694046
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694046
kb_number: KB0694046
last_modified: 2024-04-07
---

## Issue

Is it possible to disable Event Management Alert Auto-Closure?

  

  

## Resolution

When a related event is received with 'clear', 'ok' or '0' severity, the corresponding alert will be automatically closed.

The code responsible for auto-closing the alerts based on the received related event state is a backend code that can't be modified.
