---
title: "When coping a date/time field to a new field, the value is off by 1 hour"
aliases:
  - KB0722354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722354
kb_number: KB0722354
last_modified: 2024-04-07
---

## When coping a date/time field to a new field, the value is off by 1 hour

  

### Issue

When coping the value of planned\_end\_date from task\_sla to custom field on incident, there is a 1 hour difference. 

### Release

ALL

### Cause

The value on the incident record is from the database, which matches the value on the task\_sla. However, the incident does not update on load to account for timezone changes as the task\_sla does.

### Resolution

When setting the value on the incident record use getDisplayValue() or implement a client script to update the display value when the incident loads.
