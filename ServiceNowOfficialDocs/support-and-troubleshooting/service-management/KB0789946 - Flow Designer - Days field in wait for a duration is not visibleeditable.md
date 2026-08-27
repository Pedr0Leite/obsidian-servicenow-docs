---
title: "Flow Designer - Days field in \"wait for a duration\" is not visible/editable"
aliases:
  - KB0789946
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789946
kb_number: KB0789946
last_modified: 2024-04-08
---

## Flow Designer - Days field in "wait for a duration" is not visible/editable

  

### Issue

Wait for condition does not have day/s field.

### Cause

PRB1322904

### Resolution

Use hour/s field to define days with max value = 999. If more hours are required, create multiple wait for a duration action.
