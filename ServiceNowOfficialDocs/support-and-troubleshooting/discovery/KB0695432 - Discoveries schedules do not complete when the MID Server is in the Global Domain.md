---
title: "Discoveries schedules do not complete when the MID Server is in the Global Domain"
aliases:
  - KB0695432
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695432
kb_number: KB0695432
last_modified: 2024-04-07
---

## Discoveries schedules do not complete when the MID Server is in the Global Domain

  

### Issue

# Symptoms

* * *

Discoveries from a specific MID Server start but do not advance. Discovery Status stays at one item in the "Discovery Log" page, zero items in the "Devices" page, and one item in the "ECC Queue" page. Deleting the MID Server and Re-Installing does not fix the issue. Discoveries for other MID Servers do advance without issue.

# Cause

* * *

The affected Discovery Schedule is found in the "global" domain.

# Resolution

* * *

Discovery runs within the selected domain and does not span across the global domain. Change the Discovery Schedule moving it in the correct domain which the schedule belongs to.
