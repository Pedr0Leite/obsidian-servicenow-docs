---
title: "HAM Purchase Order receive process does not populate serial number and asset tag"
aliases:
  - KB2672916
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2672916
kb_number: KB2672916
last_modified: 2026-05-20
---

## HAM Purchase Order receive process does not populate serial number and asset tag

  

### Issue

When you select Receive on a Purchase Order and then select the Capture Asset Tags UI action on the `po_receive.do` pop-up, serial number and asset tag values do not auto-populate for some assets. In addition, entering the same serial number either prevents the receive from completing or creates a duplicate asset record.

### Release

All Releases

### Cause

-   This behavior occurs due to one or both of the following conditions:
    
    -   The asset state has been changed to In Use, or the model linked to the asset has been changed prior to receiving. This can occur when data is imported into ServiceNow from a third-party system, or when Discovery runs and associates a new model that was not originally linked to the asset at the time the Purchase Order was created.
    -   The logic controlling the PO receive process is defined in the `POReceiveManager` script include. The Capture Asset Tags pop-up retrieves in-transit assets using strict filters on the following conditions:
        -   `purchase_line`
        -   `install_status` — must be 2 (On Order) or 9 (In Transit)
        -   `model` — must match the model on the PO line item
    
    If either condition is not met, the asset is excluded from the results and the serial number and asset tag fields do not appear during the receive process.
    

### Resolution

Scenario 1: Assets imported with "In Use" state

Assets imported from a third-party system with a state of In Use prevent the serial number and asset tag fields from displaying during the receive process. The system excludes these assets because it treats them as already active.

To resolve this:

1.  Update your integration logic to import assets in the In Transit state instead of In Use before the receive process is completed.
2.  Verify that the asset state is set to In Transit or On Order before selecting Receive on the Purchase Order.
3.  Proceed with the receive process. The serial number and asset tag fields should now populate for the affected assets.

If adjusting the integration is not feasible, you can submit an enhancement request through the [ServiceNow Idea Portal](https://www.servicenow.com/community/ideas/idb-p/ideas) to request a broader update to the PO receive logic.

* * *

Scenario 2: Asset model changed before receiving

If the model linked to an asset was changed — whether manually or through a Discovery import — before the receive process completed, the asset is excluded from the Capture Asset Tags results because the model no longer matches the PO line item.

To resolve this:

1.  Verify that the model on the asset record matches the model on the PO line item before receiving.
2.  If the model was changed by Discovery, update the asset model to match the original PO line model before proceeding.
3.  To prevent this from occurring in the future, configure Discovery so that it does not run against assets that have not yet been fully received and onboarded. This prevents Discovery from overwriting fields such as the model and causing mismatches with the PO receive process.
