---
title: "\"Run normalization job daily\" execution check and behavior (Normalization Data Services – Core Company)"
aliases:
  - KB2611554
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2611554
kb_number: KB2611554
last_modified: 2025-11-07
---

## Issue

How to check the execution of the daily scheduled job **"Run normalization job daily"** in the ServiceNow instance if that is getting success.

## Resolution

View the job execution history:

https://<instance>.service-now.com/sys\_scheduler\_job\_history\_list.do?sysparm\_query=job\_classificationLIKEnorm%5Ejob\_classification%3DRecurring.Run%20normalization%20job%20daily&sysparm\_first\_row=1&sysparm\_view=

## Additional Information

[What is the property "glide.cmdb.canonical.normalize.existing.canonical.core\_company\_records" for ?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957144)
