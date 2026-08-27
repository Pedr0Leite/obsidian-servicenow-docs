---
title: "Stockroom and Location values after removing the asset from work order task"
aliases:
  - KB0869541
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869541
kb_number: KB0869541
last_modified: 2025-04-29
---

## Stockroom and Location values after removing the asset from work order task

  

### Issue

When removing assets using the Asset Usage tab on wm\_task (WOT). The Asset Location should be moved to the corresponding stockroom for that Assignment Group.The Asset is being moved, that State is changing to "In stock" Substate "Defective". Stockroom & Location is left blank.

### Release

Paris Patch 5

### Resolution

OOB, when the asset is removed from the work order task by the agent, it will move back to field agent's personal stockroom with the state "In stock" and Substate "Defective". If there is a location specified for the personal stockroom, the location of the removed part will be updated to that location.
