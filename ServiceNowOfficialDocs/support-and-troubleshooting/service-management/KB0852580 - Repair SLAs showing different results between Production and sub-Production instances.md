---
title: "Repair SLAs showing different results between Production and sub-Production instances"
aliases:
  - KB0852580
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852580
kb_number: KB0852580
last_modified: 2024-04-08
---

## Repair SLAs showing different results between Production and sub-Production instances

  

### Issue

The user reported that there were different results noted repairing the same record in Production vs. in their sub-Production environment. They wanted to know why.

### Resolution

The issue here is that when the user cloned down to their sub-Production environment from Production, they checked the "Exclude audit and log data" checkbox on the clone (this can be checked by going to the "Clone history" module and opening the clone record of concern).  
  
The reason this is an issue is that Repair SLA functionality is entirely dependent on the audit history of a task record to recalculate correctly. If the above-mentioned checkbox is checked, this will skew the audit history of task records, and thus, the results of the Repair SLAs functionality in the sub-Production environment as well.
