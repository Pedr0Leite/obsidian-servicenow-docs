---
title: "Why is the maintenance flag on the alert not reflecting the maintenance mode of the CI?"
aliases:
  - KB0718114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718114
kb_number: KB0718114
last_modified: 2024-04-07
---

## Why is the maintenance flag on the alert not reflecting the maintenance mode of the CI?

  

### Issue

# Resolution

* * *

The scheduled job "Event Management - Maintenance Calculator" makes an entry in the "em\_impact\_maint\_ci" table for the Ci's that are in maintenance. If this table does not have the entry the alert generated with the Ci will not have the maintenance flag checked.

Please ensure that the scheduled job is active and there is no rules restricting the job to make an entry in to the  "em\_impact\_maint\_ci" table.
