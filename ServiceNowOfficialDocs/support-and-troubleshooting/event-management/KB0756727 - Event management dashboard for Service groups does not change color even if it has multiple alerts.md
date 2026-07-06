---
title: "Event management dashboard for Service groups does not change color even if it has multiple alerts"
aliases:
  - KB0756727
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756727
kb_number: KB0756727
last_modified: 2024-04-07
---

## Issue

Event management dashboard for service groups does not change color even if it has multiple alerts.

## Resolution

Running the scheduled job '**Event Management - Recalculate impact for groups**' may resolve the issue.

https://<instance-name>.service-now.com/sysauto\_script.do?sys\_id=e053a3ce672823004cdb007d2685effb

This script "**EvtMgmtFixImpactForGroups**" may fix the incorrect calculation. In Madrid this script exists in your OOTB instance but it is not active. Please run this script manually and determine if this resolves the issue. In ServiceNow's New York version, the script be active and will run automatically OOTB.

Therefore, if the problem is observed again rerun the job that we provided. If the problem appears more frequently, please open a case with ServiceNow.
