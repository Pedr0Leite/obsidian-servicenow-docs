---
title: "Assessment instance record not created"
aliases:
  - KB0811773
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811773
kb_number: KB0811773
last_modified: 2024-04-08
---

## Assessment instance record not created

  

### Issue

When the trigger condition is met, there should be a survey getting triggered to the User Field but it is not triggered only when the 'User Field' is defined for Request.Requested For on the RITM table

### Release

Madrid Patch 9

### Cause

Custom business rule on the task table is fired and is making to not generate the assessment based on the trigger condition.

### Resolution

Deactivating the custom Business Rule fixed the issue
