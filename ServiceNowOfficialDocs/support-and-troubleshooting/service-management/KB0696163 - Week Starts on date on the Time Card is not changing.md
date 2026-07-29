---
title: "Week Starts on date on the Time Card is not changing"
aliases:
  - KB0696163
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696163
kb_number: KB0696163
last_modified: 2024-04-07
---

## Week Starts on date on the Time Card is not changing

  

### Issue

Changing the "Week Starts On" field on the Time Card does not save

### Release

Jakarta Patch 9c

### Cause

No Time Sheet on the time card so "Populate week starts on" Business Rule was running.

### Resolution

There is not a timesheet attached, the "Populate week starts on" Business Rule will run and assign the "Week Starts on" field with what is defined in the Time Sheet Policy.

If you have a Time Sheet and want to change the date in a Time Card, this should be changed first on the Time Sheet.
