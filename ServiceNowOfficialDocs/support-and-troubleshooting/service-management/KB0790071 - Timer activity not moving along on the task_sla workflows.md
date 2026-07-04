---
title: "Timer activity not moving along on the task_sla workflows"
aliases:
  - KB0790071
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790071
kb_number: KB0790071
last_modified: 2024-04-08
---

## Timer activity not moving along on the task\_sla workflows

  

### Issue

Timer activity not moving along on the task\_sla workflows

### Cause

It is expected behavior that when a workflow receives a 'pause' event, all timer activities currently running will be paused,  
which will include both types: "Timer" and "SLA Percentage Timer" activities.

### Resolution

Add a timer on the task record (ie incident) workflow instead of the task\_sla

### Related Links

[Service Level Agreement (SLA) process example](https://docs.servicenow.com/bundle/quebec-it-service-management/page/product/service-level-management/task/t_SLAProcessExample.html "Service Level Agreement (SLA) process example")
