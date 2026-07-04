---
title: "Flow action does not open in flow designer"
aliases:
  - KB0820551
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820551
kb_number: KB0820551
last_modified: 2024-04-08
---

## Issue

1.  1.  After trying to save an Action in flow designer the error in console appears as System Error "Null Pointer Exception"
    2.  Then reopening flow designer and selecting the action from the home tab, the action won't open and shows error as 'This action cannot be found'.

## Resolution

Remove the orphaned record's reference to action by setting its sys\_hub\_step\_instance.action to empty string, that will resolve the issue.
