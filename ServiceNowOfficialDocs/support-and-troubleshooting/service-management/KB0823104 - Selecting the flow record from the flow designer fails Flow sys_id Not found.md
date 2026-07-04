---
title: "Selecting the flow record from the flow designer fails: Flow \"sys_id\" Not found"
aliases:
  - KB0823104
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0823104
kb_number: KB0823104
last_modified: 2025-10-15
---

## Selecting the flow record from the flow designer fails: Flow "sys\_id" Not found

  

### Issue

After moving a flow from an update set and opening the flow record from the flow designer, the error message Flow "sys\_id" Not found displays .

### Cause

The main flow has a sub flow that is not captured in the update set, which is committed to moving the main flow.

The sys\_id in the error message corresponds to a \[sys\_hub\_flow\_snapshot\] record.

The snapshot record can help determine what subflow it refers to.

### Resolution

To fix this and open the main flow without errors, capture the sub flow on a new update set, and commit the update set.
