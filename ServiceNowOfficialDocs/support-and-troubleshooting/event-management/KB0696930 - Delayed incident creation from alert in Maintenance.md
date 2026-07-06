---
title: "Delayed incident creation from alert in Maintenance "
aliases:
  - KB0696930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696930
kb_number: KB0696930
last_modified: 2024-04-07
---

## Delayed incident creation from alert in Maintenance

  

### Issue

Alerts were created sometime back, then all of a sudden, incidents are created for them hours/days after the alerts were created.

### Release

All Releases

### Cause

Due to Maintenance Rule, when an event came into ServiceNow for a CI that is in Maintenance mode, Event Management will create an alert with 'Maintenance' flag set to true. When the related CI moves out of Maintenance mode, Event Management will also uncheck the 'Maintenance' flag on the alert.

If the alert is still in open state once itself moves out of maintenance, the 'Event Management - create/resolved incidents by alerts' scheduled job will create Incident for it.

### Resolution

Adjust the Event Management settings to meet businesses requirements.

Some Examples:

1.  Don't create alerts for CIs in maintenance.
2.  Auto-close alerts for CIs in Maintenance.
3.  Auto-close alerts when CIs moved out of maintenance.
