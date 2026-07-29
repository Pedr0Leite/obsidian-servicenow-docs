---
title: "Flow Designer \"foreach item in\" action does not return all the records"
aliases:
  - KB0824613
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824613
kb_number: KB0824613
last_modified: 2025-08-20
---

## Flow Designer "foreach item in" action does not return all the records

  

### Issue

The lookup records step returns the number of records but the Flow Designer step did not iterate through and return those records.

### Release

ALL

### Cause

Flow might have run as "user who initiates the session" and that user might not have access to the table

### Resolution

Change Run as in Flow properties to "System User"
