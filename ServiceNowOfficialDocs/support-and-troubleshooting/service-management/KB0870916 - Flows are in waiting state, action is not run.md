---
title: "Flows are in waiting state, action is not run"
aliases:
  - KB0870916
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870916
kb_number: KB0870916
last_modified: 2024-02-26
---

## Flows are in waiting state, action is not run

  

### Issue

A flow gets stuck in waiting state. There is no error reported, but the last action says not run.

### Cause

It could be a design problem. Check if the first action that says not-run depends on the value for an earlier action. For example a look-up record might depends on a condition: sys\_id=18->Task Record->Sys ID. If step 18 was never executed, it gets stuck at this point.

### Resolution

You need to make sure an action references a valid older action.
