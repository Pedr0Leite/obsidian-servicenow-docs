---
title: "Time Cards did not generate from a Time Sheet Policy when set to auto create"
aliases:
  - KB0712042
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712042
kb_number: KB0712042
last_modified: 2025-04-07
---

## Time Cards did not generate from a Time Sheet Policy when set to auto create

  

### Issue

Time cards did not auto-generate from the define time sheet policy.

### Release

Kingston +

### Cause

The Auto Generate Time Cards scheduled job on the Schedule Script Executions \[sysauto\_script\] table is not active.

### Resolution

To have time cards autogenerate from a time sheet policy, please activate the Auto Generate Time Cards scheduled script as mentioned above.
