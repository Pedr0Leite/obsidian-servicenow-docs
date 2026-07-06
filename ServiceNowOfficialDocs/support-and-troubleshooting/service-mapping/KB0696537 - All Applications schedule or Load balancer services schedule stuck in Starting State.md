---
title: "All Applications schedule or Load balancer services schedule stuck in Starting State"
aliases:
  - KB0696537
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696537
kb_number: KB0696537
last_modified: 2026-05-22
---

## All Applications schedule or Load balancer services schedule stuck in Starting State

  

### Issue

All Applications schedule or Load balancer services schedule stuck in Starting State

### Release

Any

### Cause

When the all applications schedule runs, it creates records in the sa\_endpoint\_status table . The schedule called "Service Rediscovery Schedule Manager" is responsible for creating taks (ecc queue) for each record in the sa\_endpoint\_status table. This job is scheduled to run every 1 minute.

Cause 1 : The scheduled job might be inactive

Cause 2 : The sys\_trigger record for the scheduled job might be invalid, i.e. either the next action field is showing the past date/time or the state might be stuck in running 

### Resolution

1.  If the scheduled job "Service Rediscovery Schedule Manager" is inactive, make the job active
2.  If we are seeing symptoms from Cause 2 , Make any update in the job configuration and revert your update , so that a new sys\_trigger record is created.
