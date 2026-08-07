---
title: "HAMP: ASN Imported Assets Ignored Due to Duplicate Purchase Order Number on proc_po Table"
aliases:
  - KB3024341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3024341
kb_number: KB3024341
last_modified: 2026-05-17
---

## HAMP: ASN Imported Assets Ignored Due to Duplicate Purchase Order Number on proc\_po Table

  

### Issue

 

When processing an Advanced Shipment Notification (ASN) import in Hardware Asset Management (HAM), imported assets are not created. The following message is logged:

Asset can not be processed since PO {PO Number} is not in pending delivery or ordered status

This occurs despite the intended Purchase Order having a current State of Pending Delivery.

### Symptoms

 

-   ASN import records are skipped and assets are not created.
-   The import log displays the message: `Asset can not be processed since PO {PO Number} is not in pending delivery or ordered status`.
-   The Purchase Order referenced in the ASN import row visibly shows a State of Pending Delivery or Ordered when viewed in the platform.
-   No errors or exceptions are thrown — the record is silently ignored.

### Facts

 

-   This behavior originates from the `ASNTransform` Script Include, specifically the `validatePO` function.
-   The `validatePO` function queries the Purchase Order \[`proc_po`\] table where the Number field matches the PO Number on the import set row, then validates whether the returned record's State is `pending delivery` or `ordered`.
-   The query does not enforce an order or explicitly target the most recent record — it processes the first record returned.
-   If the State does not match either expected value, the function logs the rejection message and the asset is not processed.
-   The Number field on the Purchase Order \[`proc_po`\] table is expected to be unique, but the platform does not enforce uniqueness with a constraint by default.

### Release

All Releases

### Cause

 

Two records exist on the Purchase Order \[`proc_po`\] table with the same PO Number:

-   An older Purchase Order with a State of Canceled.
-   A newer Purchase Order (the intended target) with a State of Pending Delivery.

Because the `validatePO` function queries by PO Number and processes the first record returned, the older Canceled record is evaluated first. Since its State is neither `pending delivery` nor `ordered`, validation fails and the asset import is rejected — even though the correct, active Purchase Order is in a valid state.

### Resolution

 

Resolve the duplicate Purchase Order condition using one of the following options.

Option 1: Remove the Duplicate Record (Recommended)

1.  Navigate to **Procurement > Purchase Orders**.
2.  Search for the affected PO Number.
3.  Identify the duplicate record with a State of Canceled.
4.  Confirm the Canceled record is no longer needed and has no dependent records (e.g., associated receipt lines or asset records).
5.  Delete the Canceled Purchase Order record.
6.  Re-run the ASN import and confirm the assets are now processed successfully.

Option 2: Update the PO Number on the Duplicate Record

If the duplicate Canceled record cannot be deleted (e.g., it is retained for audit or historical purposes):

1.  Navigate to **Procurement > Purchase Orders**.
2.  Open the duplicate Canceled Purchase Order record.
3.  Modify the Number field to a unique value (e.g., append a suffix such as `-DUP` or `-CANCELED`).
4.  Save the record.
5.  Re-run the ASN import and confirm the assets are now processed successfully.

After resolving the immediate issue, consider implementing a business rule or unique index on the Number field of the Purchase Order \[`proc_po`\] table to prevent duplicate PO Numbers from being created in the future. Evaluate the impact on existing integrations and import processes before applying any uniqueness enforcement.

### Related Links

 

-   [Import assets using an advanced shipment notification](https://docs.servicenow.com/bundle/latest/page/product/hardware-asset-management/concept/ham-asn-import.html)
-   [Hardware asset purchase orders](https://docs.servicenow.com/bundle/latest/page/product/hardware-asset-management/concept/ham-purchase-orders.html)
