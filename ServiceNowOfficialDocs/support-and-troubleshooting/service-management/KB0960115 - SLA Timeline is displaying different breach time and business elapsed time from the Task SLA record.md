---
title: "SLA Timeline is displaying different breach time and  business elapsed time from the Task SLA record"
aliases:
  - KB0960115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960115
kb_number: KB0960115
last_modified: 2026-06-24
---

## SLA Timeline is displaying different breach time and business elapsed time from the Task SLA record

  

### Issue

You have observed that the SLA timeline and SLA audit are showing different values of breach of SLA.

### Release

All

### Cause

  
SLA Timeline is working as designed. The timeline is designed to build information about the task from the audit history and refers to the current SLA definition to pull data for the SLA timeline.

### Resolution

  
The SLA timeline is functioning as designed.   
  
The SLA timeline is dependent on audit history and the current values on the sla definition. It uses these values to build the task sla in memory when you click on the Show Timeline related link.  
  
You should define your sla definition to have all the values you expect the task sla to use. This will ensure the timeline and even repair sla take the values into consideration.  
  

### Related Links

[https://docs.servicenow.com/bundle/paris-it-service-management/page/product/service-level-management/concept/c\_SLATimeline.html](https://docs.servicenow.com/bundle/paris-it-service-management/page/product/service-level-management/concept/c_SLATimeline.html)

The SLA timeline receives information about the task from the audit history and refers to the current SLA definition to pull data for the SLA timeline. The SLA timeline displays task SLA information as though the SLA repair is already executed, irrespective of whether it is executed or not.
