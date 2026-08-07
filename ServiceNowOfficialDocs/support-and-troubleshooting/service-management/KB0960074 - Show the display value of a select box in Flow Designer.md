---
title: "Show the display value of a select box in Flow Designer"
aliases:
  - KB0960074
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960074
kb_number: KB0960074
last_modified: 2025-06-27
---

## Show the display value of a select box in Flow Designer

  

### Issue

When using Get Catalog Variables for a Select Box (a choice field in Flow Designer), the flow accesses the choice's internal value instead of its display text. 

### Cause

Flow Designer looks at the internal value in the table sc\_item\_option\_mtom.

### Resolution

Write a custom action to use the value and check the table question\_choice (value=new\_allow AND question=<sysid of question>.
