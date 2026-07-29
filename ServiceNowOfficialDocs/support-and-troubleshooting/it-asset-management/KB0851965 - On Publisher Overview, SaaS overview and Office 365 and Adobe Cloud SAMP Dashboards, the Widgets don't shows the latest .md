---
title: "On Publisher Overview, SaaS overview and Office 365 and Adobe Cloud SAMP Dashboards, the Widgets don't shows the latest data"
aliases:
  - KB0851965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0851965
kb_number: KB0851965
last_modified: 2026-04-06
---

## Issue

On Publisher Overview, SaaS overview and Office 365 and Adobe Cloud Dashboards, Widgets don't shows the latest data(July data).

![](/sys_attachment.do?sys_id=98dd268247c087d4b6d8aa25126d43c2)

## Resolution

1)Hop to ServiceNow instance

2)Navigate to sys\_user table and search for 'sam.pa.jobs.scheduler' User ID and set the Active status to 'True'

3)Run the Reconciliation on all the Publishers and observe the latest data on the SAMP Dashboards.
