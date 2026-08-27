---
title: "How the HAM asset reclaim process works in Hardware Asset Management"
aliases:
  - KB2616160
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2616160
kb_number: KB2616160
last_modified: 2026-05-21
---

## How the HAM asset reclaim process works in Hardware Asset Management

  

### Summary

The asset reclaim process in Hardware Asset Management (HAM) systematically reclaims assets assigned to users and returns hardware to stock for repair, redeployment, or disposal. This article explains the key components of the process, including reclamation requests, reclamation lines, task stages, and the business rules that update asset state at each stage.

**Key components and flow**

**Reclamation request**

Any user with an assigned asset can initiate an asset reclaim request. When created, the request enters an approval workflow before being processed.

**Reclamation lines**

Creating a reclamation request automatically generates one or more Hardware Asset Reclamation Line \[sn\_hamp\_asset\_reclaim\_line\] records — one for each asset involved. These records track asset-specific reclaim details and progress.

**Reclamation stages and tasks**

Each reclamation line generates a set of task stages, managed in the Hardware Asset Reclamation Task \[sn\_hamp\_asset\_reclaim\_task\] table. The standard stages are:

-   Schedule Shipment — arranges return logistics.
-   Receive Asset — confirms physical receipt and verifies the asset.
-   Evaluate Asset — assesses condition to determine whether the asset goes to repair, redeployment, or disposal.

Each stage must be closed complete before the next stage is triggered. If any stage is rejected or closed with a different outcome, subsequent stages do not proceed.

**Business rules triggered on task completion**

Closing the Receive Asset task triggers the business rule "Update asset after closing receive task," which makes the following updates:

-   Sets the asset State to In Stock
-   Sets Substate to Pending Repair
-   Clears the Assigned to field
-   Assigns the stockroom location from the preceding Schedule Shipment task

Closing the Evaluate Asset task triggers a separate business rule that updates the asset state based on the evaluation outcome — repair, redeployment, or disposal.

**Process flow summary** 

| Step | Description | Table/Rule |
| --- | --- | --- |
| 1\. Request Initiation | User initiates `asset_reclaimation_request` to start reclaim process | `asset_reclaimation_request` (form) |
| 2\. Line Creation | System creates one or more `sn_hamp_asset_reclaim_line` entries tied to individual assets | `sn_hamp_asset_reclaim_line` |
| 3\. Task Stage Creation | For each reclamation line, tasks are created in stages: Schedule Shipment, Receive, Evaluate | `sn_hamp_asset_reclaim_task` |
| 4\. Task Stage Progression | Tasks must be closed complete sequentially for next to start; rejection stops flow | Task status controls workflow |
| 5\. Asset State Update | Business rules update asset state/substate and assignment after Receive and Evaluate tasks | `Update asset after closing receive task` and related BR for Evaluate task |

**Note**: Unexpected behavior in this process may be caused by custom logic or a custom business rule.

### Release

Beginning with the Xanadu release, with the HAM plugin installed

### Related Links

[Submit an asset reclamation request](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/hardware-asset-management/task/submit-asset-reclamation-request.html)

[Explanation of reclaim asset record producer](https://www.servicenow.com/community/ham-forum/ham/m-p/2620005)

[Asset Reclamation Flow to reclaiming assets (Video Demo)](https://www.youtube.com/watch?v=oqWVaW27T80)
