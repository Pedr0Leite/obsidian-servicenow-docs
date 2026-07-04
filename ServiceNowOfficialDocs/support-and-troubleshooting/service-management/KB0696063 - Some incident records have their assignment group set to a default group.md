---
title: "Some incident records have their assignment group set to a default group"
aliases:
  - KB0696063
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696063
kb_number: KB0696063
last_modified: 2024-04-07
---

## Some incident records have their assignment group set to a default group

  

### Issue

Some incident records have their assignment group set to a default group

### Release

Kingston+

### Cause

The script inside a record producer is setting the assignment group field.

### Resolution

The assignment group is being set by the Script inside the record producer.

  

So all incident records created from this record producer will have the assignment group set to " IT Executive Management"
