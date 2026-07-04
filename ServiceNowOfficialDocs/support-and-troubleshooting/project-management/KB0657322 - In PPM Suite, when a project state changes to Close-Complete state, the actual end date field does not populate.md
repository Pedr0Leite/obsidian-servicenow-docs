---
title: "In PPM Suite, when a project state changes to Close-Complete state, the \"actual end date\" field does not populate"
aliases:
  - KB0657322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657322
kb_number: KB0657322
last_modified: 2024-09-27
---

## In PPM Suite, when a project state changes to Close-Complete state, the "actual end date" field does not populate

  

### Issue

In PPM Suite, when a project state changes to Close-Complete state, the "actual end date" field does not populate.

### Cause

Customized Recalculate Business Rule

  

### Resolution

In an out of the box instance, the population of the actual start and actual end dates is part of recalculation which is done by the recalculate business rule. You have a customized version of this business rule:

  

https://XXXX.service-now.com/sys\_script.do?sys\_id=15ef1178dba80f40db69fb5aaf9619b6

  

which runs only when the planned dates change. When a task gets closed, the planned dates don't change. As a result, this business rule doesn't run and the parent dates don't get updated.

  

Revert to the out of the box version of the recalculate business rule or, at a minimum, make it also trigger when actual start date, actual end date, or actual duration change.
