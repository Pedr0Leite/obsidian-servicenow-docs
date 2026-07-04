---
title: "Serial and Asset Tag Not Auto-Populated During PO Receive When Asset Model or State Changes"
aliases:
  - KB2684788
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2684788
kb_number: KB2684788
last_modified: 2026-05-21
---

## Serial and Asset Tag Not Auto-Populated During PO Receive When Asset Model or State Changes

  

### Issue

The purchase order (PO) receiving process sometimes fails to automatically populate the serial number and asset tag for certain PO line items within the `po_receive.do` popup. This issue typically arises when the model associated with an asset has been changed—either through manual updates or automated processes like Discovery or import jobs—prior to the asset being received against its purchase order. This alteration breaks the expected linkage between the asset's model and the model specified on the original PO line.

This problem is frequently observed with assets that are in the "In Transit" or "In Use" states. It can affect specific PO line items, sometimes appearing as the final item in a receiving batch. Consequently, users are often forced to manually enter serial numbers and asset tags, which significantly increases the risk of data entry errors, inconsistencies, or the creation of duplicate asset records. The behavior has been reproduced in out-of-box (OOB) instances, particularly when automated asset discovery or import processes update asset models, leading to their exclusion from the expected results in the Capture Asset Tag popup during the receiving process.

### Release

All Procurement

### Cause

The core of this issue lies within the Capture Asset Tag popup's logic, which employs strict filtering criteria. For an asset to be displayed and its serial number/asset tag auto-populated, it must meet several conditions, including a precise match between the `asset.model` and the `purchase_line.model`. Additional checks are performed on the `purchase_line` and `install_status`.

When automated processes such as Discovery or import jobs update an asset's model, or if the model is changed manually:

1.  The asset's current model no longer aligns with the model recorded on the original PO line item.
2.  Due to this mismatch, the asset is excluded from the filtered results presented in the Capture Asset Tag popup.
3.  Consequently, the system cannot auto-populate the serial number or asset tag for that specific PO line.
4.  This failure results in validation errors for the affected PO line, preventing its automated processing within the receiving workflow.

This behavior represents an out-of-box (OOB) interaction where automated asset onboarding processes (like Discovery creating normalized models) can conflict with the PO receiving workflow's rigid model matching requirements.

### Resolution

As there is no automated fix currently available for this OOB behavior, the recommended approach involves manually managing the affected PO lines during the receiving process. The general strategy is to deselect problematic PO lines to allow the system to process the valid items, and then address the deselected lines separately.

### Steps:

1.  Navigate to the Purchase Order you need to receive. Typically, this is done via Procurement > Orders > Purchase Orders, and then selecting the specific PO number. From there, you would usually access the Receive action or form.
2.  Within the PO Receive interface (often accessible via `po_receive.do`), identify the PO line item(s) where the serial number and asset tag are not populating and are failing validation.
3.  For each affected PO line, uncheck the checkbox located next to it. This action deselects the line item, signaling to the system that it should not be processed in the current automated receiving batch.
4.  Add the Stockroom value on each line and reserver tp user if needed to proceed with submitting the receiving process for the remaining valid (checked) PO lines. 
    
    5\. After processing the valid lines, you will need to manually handle the deselected PO line(s). You have two primary options:
    
    | Option | Description | When to Use |
    | --- | --- | --- |
    | Correct Asset Model | Update the `asset.model` field on the affected asset record to match the model specified on the PO line item. You can then retry receiving the line later. | Use this if the model change was an error and the PO is intended as the primary onboarding record. |
    | Close/Cancel PO Line | Mark the PO line item as Closed or Cancelled. This signifies that the PO is no longer required for this item. | Use this if the asset has already been successfully onboarded through another process (e.g., Discovery or a separate import), and the PO is now redundant for this item. |
    

### Related Links

-   Enhancement Request: A customer-submitted enhancement request is pending review to address the handling of model mismatches within the PO Receive process. You can track its status here: [Idea for model mismatch handling in PO Receive](https://support.servicenow.com/ideas?id=view_idea&sysparm_idea_id=a0311664937532d85736b25d6cba107d&sysparm_idea_table=x_snc_com_ideation_idea&sysparm_module_id=enhancement_requests).
-   Platform Updates: It is advisable to monitor future ServiceNow platform releases for potential updates that may address the OOB conflict between Discovery/asset normalization processes and the PO receiving workflow.
-   **Affected Releases**: This behavior is considered an OOB limitation and has been observed across various recent releases. **Type**: Known Limitation (workaround available).
