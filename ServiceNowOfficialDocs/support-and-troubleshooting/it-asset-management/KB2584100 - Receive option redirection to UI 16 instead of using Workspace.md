---
title: "Receive option redirection to UI 16 instead of using Workspace"
aliases:
  - KB2584100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2584100
kb_number: KB2584100
last_modified: 2025-10-24
---

## Receive option redirection to UI 16 instead of using Workspace

  

### Issue

The Receive action on a Purchase Order in Asset Workspace is navigating to the po\_hardware\_item.html template in a new page.  
The submit action on the template is redirecting the user to core UI of the Purchase Order.  
But the desired behavior is it should stay in the Workspace.

### Release

The option to receive a hardware asset at your stockroom through the standardized asset receiving mechanism is available in Hardware Asset Management version 13.0.0 and later.

### Resolution

The "Receive" page of the "Purchase Order" hasn't been migrated to Seismic (Workspace) yet.  
That's the reason when user clicks on "Receive" on the workspace, it navigates to "po\_hardware\_item.html" template (UI 16) in a new page.  
And on clicking "Submit" it navigates back to "Purchase Order" in UI 16.  
But the Receive feature has been migrated to workspace with major upgrades.  
Users don't have to find the PO and POL lines to receive the asset, they can directly use the serial number or asset tag.  
Asset received POL and PO will be updated by the system upon receipt.  
Users can also look up all the assets inbound and filter against the PO or tracking number and select all and receive.  
Doc for reference:- [Receive a hardware asset at a stockroom in the Hardware Asset Workspace](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/hardware-asset-management/task/receive-assets-stockroom-hws.html)
