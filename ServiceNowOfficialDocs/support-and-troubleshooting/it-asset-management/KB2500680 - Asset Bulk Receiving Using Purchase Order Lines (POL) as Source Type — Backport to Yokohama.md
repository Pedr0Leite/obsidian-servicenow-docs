---
title: "Asset Bulk Receiving Using Purchase Order Lines (POL) as Source Type — Backport to Yokohama"
aliases:
  - KB2500680
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2500680
kb_number: KB2500680
last_modified: 2026-05-20
---

## Asset Bulk Receiving Using Purchase Order Lines (POL) as Source Type — Backport to Yokohama

  

### Issue

This article describes how to enable asset bulk receiving using Purchase Order Lines (POL) as a source type in the Yokohama release. This feature was introduced in the Zurich release. For more information about the Zurich feature, see [Import assets for receiving](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/hardware-asset-management/task/import-assets-for-receive-ham.html) in the ServiceNow documentation.   
  

### Release

Yokohama Patch 5 Hot Fix 1 with Hardware Asset Management (HAM) 13.0.0 and Asset Common App 13.0.0

### Resolution

Two solutions are available to enable purchase order (PO) receiving in the Yokohama release. Select the solution that matches your receiving method.

Before you begin

Verify that you have the admin role or the required permissions to import update sets on your instance.

* * *

Solution 1: Enable receiving using a UI action

1.  Download the [update set](sys_attachment.do?sys_id=3e5bc564970d431c539e35d11153af26) file for UI action-based PO receiving.
2.  Log in to your Yokohama instance as an administrator.
3.  Navigate to System Update Sets > Retrieved Update Sets.
4.  Select Import Update Set from XML and upload the update set file.
5.  Open the imported update set and select Preview Update Set.
6.  After the preview completes, select Commit Update Set.
7.  Verify that the Script Include **POReceiveManager** is now accessible from All application scopes.

What this update changes: The Script Include POReceiveManager is updated so that the Accessible from value changes from _This application scope only_ to _All application scopes_.

* * *

Solution 2: Enable receiving using the import feature

1.  Download the [update set](sys_attachment.do?sys_id=225bc564970d431c539e35d11153af21) file for import-based PO receiving.
2.  Log in to your Yokohama instance as an administrator.
3.  Navigate to System Update Sets > Retrieved Update Sets.
4.  Select Import Update Set from XML and upload the update set file.
5.  Open the imported update set and select Preview Update Set.
6.  After the preview completes, select Commit Update Set.
7.  Verify that the Script Include **ImportAssetReceivingUtils** is available and active.

* * *

Compatibility

This update set is created and tested on Yokohama Patch 5 Hot Fix 1 with HAM 13.0 and Asset Common App 13.0.
