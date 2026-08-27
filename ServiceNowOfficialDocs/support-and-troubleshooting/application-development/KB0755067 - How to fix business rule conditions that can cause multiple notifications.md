---
title: "How to fix business rule conditions that can cause multiple notifications"
aliases:
  - KB0755067
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755067
kb_number: KB0755067
last_modified: 2025-10-29
---

## How to fix business rule conditions that can cause multiple notifications

  

### Issue

Business rules that have incorrect conditions can process events that then trigger multiple email notifications. This article shows where the errors are in the advanced condition and how to change it.

### Release

All supported releases

### Cause

If a business rule that triggers an event contains an incorrect condition, the system skips the invalid condition and evaluates any remaining conditions. This can result in multiple notifications being sent. 

### Resolution

The business rule on the Record History \[sys\_history\_set\] table with the advanced condition is: 

!current.id.demand\_manager.changes() && (current.updated != previous.updates)

The error is in the second part of the condition:

current.updated != previous.updates

There is no updated field in the sys\_history\_set table. The correct statement should be:

current.updates != previous.updates
