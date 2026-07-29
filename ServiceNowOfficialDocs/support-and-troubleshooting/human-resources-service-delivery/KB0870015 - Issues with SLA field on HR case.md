---
title: "Issues with SLA field on HR case "
aliases:
  - KB0870015
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870015
kb_number: KB0870015
last_modified: 2026-06-25
---

## Issues with SLA field on HR case

  

### Issue

SLA Field on the HR case is not showing correct value. 

### Release

Any

### Cause

Handling multiple SLAs is not implemented in the HR product.

When there are multiple active task\_sla records associated with the same HR Case and the SLAs have different durations, they are recalculated at different times. Each time they are recalculated, the BR will update the SLA field with the latest task\_sla that has been updated.

### Resolution

Use only 1 SLA task on the case
