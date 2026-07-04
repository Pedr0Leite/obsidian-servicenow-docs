---
title: "Time worked doubled for Change Request"
aliases:
  - KB0714519
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714519
kb_number: KB0714519
last_modified: 2024-04-07
---

## Time worked doubled for Change Request

  

### Issue

Duplicate entry of time worked on a routine change request when saved.

### Release

Kingston Patch 6

### Cause

Custom business rule with a current.update() in the script.

### Resolution

Use current.setValue in place of current.update on business rules.
