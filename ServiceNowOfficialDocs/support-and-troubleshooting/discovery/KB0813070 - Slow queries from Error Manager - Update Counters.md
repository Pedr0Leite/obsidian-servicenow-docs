---
title: "Slow queries from \"Error Manager - Update Counters\""
aliases:
  - KB0813070
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813070
kb_number: KB0813070
last_modified: 2024-04-08
---

## Slow queries from "Error Manager - Update Counters"

  

### Issue

Slow queries from job "Error Manager - Update Counters".

### Release

All currently supported environments.

### Cause

The "Error Manager - Update Counters" updates the values in "Discovery > Home" and "Discovery > Home > Schedules" (errors per schedule). It runs queries on automation\_error\_msg and updates automation\_error\_code\_stats. The queries can take longer as the automation\_error\_msg table grows.

### Resolution

1.  Lower the frequency of the "Error Manager - Update Counters" job to once every hour or even once every day (this will depend on how often these pages are used).
