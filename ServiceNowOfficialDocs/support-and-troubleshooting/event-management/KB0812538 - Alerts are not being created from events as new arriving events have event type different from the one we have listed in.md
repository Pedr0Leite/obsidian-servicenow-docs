---
title: "Alerts are not being created from events as new arriving events have event type different from the one we have listed in em_event_type."
aliases:
  - KB0812538
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812538
kb_number: KB0812538
last_modified: 2024-04-08
---

## Alerts are not being created from events as new arriving events have event type different from the one we have listed in em\_event\_type.

  

### Issue

Alerts are not being created from events as new arriving events have event type different from the one we have listed in em\_event\_type. So the new events never get processed event though Event Management - Process Events is running for every 5 secs.

### Release

Affected version(s): New York

### Cause

  
\=>It is cache problem. it looks like the new arriving events have event type different from the one we have listed in em\_event\_type.

### Resolution

  
\=>It is cache problem. it looks like the new arriving events have event type different from the one we have listed in em\_event\_type.  
The code tries to add those types to the table , and because cache is not refreshing it tries to do it multiple time and fails because of unique constrain.  
  
\=>In order to resolve this problem please clean the cache do a cache.do .

### Related Links

A PRB PRB1383770 has already opened  to add refresh mechanism to em\_event\_type cache.
