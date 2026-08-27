---
title: "On em_alert_history table, for some records the \"Alert Valid Time End\" (vt_end) field is showing in year 8994"
aliases:
  - KB0814749
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814749
kb_number: KB0814749
last_modified: 2024-04-08
---

## On em\_alert\_history table, for some records the "Alert Valid Time End" (vt\_end) field is showing in year 8994

  

### Issue

On em\_alert\_history table, for some records the "Alert Valid Time End" (vt\_end) field is showing in year 8994

### Resolution

em\_alert\_history table is mainly used for Impact Calculation and Event Management dashboard.  
  
Every time when there is a change to an em\_alert record, an em\_alert\_history record is created.

We only record the start of each change on em\_alert records, but not the end.

Thus vt\_start is accurate, but for vt\_end:

\> on the latest em\_alert\_history for an alert, vt\_end is year 8994

\> on previous em\_alert\_history for the alert, vt\_end equals to vt\_start of next em\_alert\_history.  
  

As em\_alert\_history is mainly for impact calculation, it's not recommended to use this table for other purpose to avoid confusions.
