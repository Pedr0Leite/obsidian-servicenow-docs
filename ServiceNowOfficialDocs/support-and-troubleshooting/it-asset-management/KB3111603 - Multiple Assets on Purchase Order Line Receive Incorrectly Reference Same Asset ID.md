---
title: "Multiple Assets on Purchase Order Line Receive Incorrectly Reference Same Asset ID"
aliases:
  - KB3111603
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3111603
kb_number: KB3111603
last_modified: 2026-06-23
---

## Multiple Assets on Purchase Order Line Receive Incorrectly Reference Same Asset ID

  

### Issue

When receiving multiple distinct assets from a single Purchase Order Line (POL) through the import asset template in Hardware Asset Management, all staging rows are incorrectly stamped with the same asset ID after the receive operation completes. This breaks the association between staging records and their corresponding asset records.

### Symptoms

-   After receiving multiple assets (with distinct serial numbers or asset tags) from the same PO line, inspection of the staging records shows all rows point to the same `asset_id` value
-   The `asset_id` typically references only the first asset created for that PO line, not the distinct assets for subsequent rows
-   Downstream receive logic cannot correctly identify which physical asset corresponds to each staging row
-   When re-receiving existing assets, the system may move the wrong physical asset into the stockroom

### Facts

-   Affected component: Hardware Asset Management (HAM) – POL Receive import flow
-   Affected areas: Asset Workspace > Import Assets (staging-to-asset association)
-   Condition: Issue occurs when receiving 2+ assets from the same PO line where each asset has a distinct serial number or asset tag
-   Workaround available: Use serial number or asset tag as the primary identifier for downstream asset matching logic; these values are correctly stamped on each staging row

### Release

This is a known product defect being addressed in Hardware Asset Management v16.0.0.

PRB2038406

### Cause

During the POL receive write-back process, the system queries for the newly created asset record using only the `purchase_line` field as a filter, combined with a limit of 1. Since all assets for the same PO line share the same `purchase_line` value, the database query returns the first asset found in row order on each iteration of the staging-to-asset matching loop. This results in all staging rows receiving the same (incorrect) asset ID reference.

Root cause: Asset matching query lacks serial\_number and asset\_tag filters to distinguish between multiple assets on the same PO line.

### Resolution

#### Until HAM v16.0.0 is available:

Use serial number or asset tag as the reliable identifier for downstream asset operations. These fields are correctly populated on each staging row during import, even though the asset\_id references may be incorrect.

Steps to verify your environment:

1.  Navigate to Hardware Asset Workspace > Import Assets
2.  Create an import record with a stockroom configured
3.  Add 3+ staging rows for the same PO line, each with a distinct serial number (e.g., SN-001, SN-002, SN-003) and status = "Ready to Receive"
4.  Select all rows and click Receive
5.  After the background job completes, inspect the staging rows:
    -   If all rows show the same `asset_id` value, you are experiencing this issue
    -   If each row shows a distinct `asset_id`, your environment is not affected

Temporary workaround: When performing downstream asset processing (such as moving assets to a stockroom or updating asset records post-receive), validate asset identity using the staging row's serial\_number or asset\_tag fields rather than relying on the asset\_id field for multi-asset POL receives. This ensures you are operating on the correct physical asset until the permanent fix is applied.
