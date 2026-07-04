---
title: "When Domain is changed to TOP, no entry is visible in Select criteria in Task filter under Dynamic Scheduling configurations in FSM."
aliases:
  - KB0997636
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997636
kb_number: KB0997636
last_modified: 2024-08-28
---

## When Domain is changed to TOP, no entry is visible in Select criteria in Task filter under Dynamic Scheduling configurations in FSM.

  

### Issue

When Domain is changed to TOP, no entry is visible in Select criteria in Task filter under Dynamic Scheduling configurations in Field service management, even though these tables are not domain separated.

### Cause

The table has the domain\_master=user attribute. We do not ship this OOB.Since the table is domain separated the records are not visible in other domains.

It was found that customer has added this configuration manually for enabling 'domain aware' of this table, matching\_dimension\_for\_assignment.

The references used for the domain is 'user' field which is blank on few records. That is the reason, those records are not visible in the TOP domain. 

### Resolution

Either select any other column for the domain reference or make sure the column is populated with some value in order to derive the domain.

A BR can be created to populate user field on this record to fix this issue.
