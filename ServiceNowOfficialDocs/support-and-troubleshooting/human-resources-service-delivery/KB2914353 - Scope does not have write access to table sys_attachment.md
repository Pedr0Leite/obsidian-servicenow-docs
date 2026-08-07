---
title: "Scope does not have write access to table sys_attachment"
aliases:
  - KB2914353
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2914353
kb_number: KB2914353
last_modified: 2026-03-24
---

## Scope does not have write access to table sys\_attachment

  

### Issue

Error in Flow in HR scope - Scope does not have write access to table sys\_attachment.

### Release

All

### Cause

This is the expected behaviour because by default HR scope does not have Cross Scope privileges to write in the sys\_attachment record.

### Resolution

You will need to add Cross Scope privileges like the following to ensure that HR scope has the right access.

![](/sys_attachment.do?sys_id=2600638697773658f03d739c1253af4d)
