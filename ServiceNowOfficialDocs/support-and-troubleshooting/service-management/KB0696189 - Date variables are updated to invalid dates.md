---
title: "Date variables are updated to invalid dates"
aliases:
  - KB0696189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696189
kb_number: KB0696189
last_modified: 2024-04-07
---

## Date variables are updated to invalid dates

  

### Issue

Date variables are set correctly when a catalog request is created, however, when a task from a custom table is updated, the custom variable editor changes the variable to an invalid date.

### Release

Jakarta+

### Cause

A custom variable editor exists

### Resolution

Remove the variable editor from the form
