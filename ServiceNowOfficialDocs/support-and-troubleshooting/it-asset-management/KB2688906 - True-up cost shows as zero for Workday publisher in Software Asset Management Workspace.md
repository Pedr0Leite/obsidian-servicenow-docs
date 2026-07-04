---
title: "True-up cost shows as zero for Workday publisher in Software Asset Management Workspace"
aliases:
  - KB2688906
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688906
kb_number: KB2688906
last_modified: 2026-05-15
---

## True-up cost shows as zero for Workday publisher in Software Asset Management Workspace

  

### Issue

The true-up cost displays as zero for the Workday publisher in the Software Asset Management Workspace.

### Release

Not applicable

### Cause

The true-up cost does not display because the subscription records for the Workday publisher do not have entitlements associated with their software models, or the entitlements do not have a specified **Per unit cost** value, or both. Without this information, the system cannot calculate the true-up cost using the following formula: True-up cost = (actionable rights count × average cost per right) + total active reserved entitlement cost

### Resolution

To resolve this issue, complete the following steps:  
1\. Navigate to the software model associated with the Workday subscription and verify that an entitlement is added to it.  
2\. Open the entitlement record and confirm that the **Per unit cost** field has a value. This field is required for the true-up cost calculation.  
3\. After adding or updating the entitlement, run reconciliation to populate the true-up cost.  
  
After reconciliation completes, the true-up cost field in the Software Asset Management Workspace should populate with the calculated value.  
  
Note: If the true-up cost still displays as zero after completing these steps, verify that the reconciliation completed without errors and that the subscription record is correctly linked to the software model.
