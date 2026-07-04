---
title: "Unable to see sn_customerservice_appointment in my agent schedule."
aliases:
  - KB0958284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958284
kb_number: KB0958284
last_modified: 2024-02-29
---

## Issue

Fllowing the documentation link below and have an event configuration of 'type' appointment:  
  
https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/concept/configure-agent-calendar.html

However, Unable to see sn\_customerservice\_appointment in agent schedule.

## Resolution

In this particular case, customer has created a filter in agent\_schedule\_task\_config record w.rt. to the appointment.

But when creating the appointment , that field was left empty.

Hence there was no condition matched and schedule was not shown.

After filling in that field value while creating appointment, issue was resolved.
