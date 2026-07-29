---
title: "Resolve stuck wait-for-condition action based on a date in Flow Designer "
aliases:
  - KB0958213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958213
kb_number: KB0958213
last_modified: 2025-08-27
---

## Resolve stuck wait-for-condition action based on a date in Flow Designer

  

### Issue

When using a wait-for-condition action in Flow Designer that monitors a date field, the flow does not progress automatically when the specified date is reached. 

### Release

All supported releases

### Cause

The wait-for-condition action only progresses when the source record receives an update. For example, if the condition is state=closed, the flow waits for that record to change to closed and then resolves the wait-for-condition action. 

This action does not perform regular checks on the source record. It only progresses when the record changes. If you wait for a date to be reached, the flow does not move forward unless the source record is updated. 

### Resolution

For date and time monitoring, use the duration action instead of wait-for-condition. The duration action can detect when a date or time is reached without requiring the source record to be updated.
