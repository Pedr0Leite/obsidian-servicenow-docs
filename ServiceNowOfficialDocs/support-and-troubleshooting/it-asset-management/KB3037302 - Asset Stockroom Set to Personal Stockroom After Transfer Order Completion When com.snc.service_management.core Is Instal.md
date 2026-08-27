---
title: "Asset Stockroom Set to Personal Stockroom After Transfer Order Completion When com.snc.service_management.core Is Installed"
aliases:
  - KB3037302
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3037302
kb_number: KB3037302
last_modified: 2026-05-22
---

## Asset Stockroom Set to Personal Stockroom After Transfer Order Completion When com.snc.service\_management.core Is Installed

  

 

## Issue

When processing Transfer Orders to completion with the plugin `com.snc.service_management.core` installed, the stockroom of the asset may be incorrectly set to a personal stockroom instead of the intended destination stockroom.

## Symptoms

-   After completing a Transfer Order, the asset's stockroom is updated to a personal stockroom instead of the intended destination stockroom.

## Facts

-   This behavior only occurs when the plugin `com.snc.service_management.core` is installed.
-   When a Transfer Order is processed, the destination stockroom specified on the Transfer Order should be assigned as the stockroom for the asset.
-   An exception applies when the Transfer Order was created via a Service Order Task — in that scenario, different stockroom assignment logic is expected.

## Release

All Versions

## Cause

Bad demo data can be installed to the `alm_stockroom` table. These demo records have the **Type** field set to **Field Agent**, and the **Manager** field is empty.

When Transfer Order completion logic runs — on Transfer Orders that were not created via a Service Order Task — it evaluates stockroom records and can incorrectly select one of these malformed demo records instead of the destination stockroom specified on the Transfer Order.

## Resolution

Delete the bad demo data from the `alm_stockroom` table. Use the link below to navigate directly to a filtered list of the affected records on your instance. Replace `<instance_name>` with your instance name before opening the URL.

**Note:** Review the records returned by the filter before deleting to confirm they are demo data records that are not in use in your environment.

The filtered list targets stockroom records where **Type** is set to **Field Agent** and **Manager** is empty:

`https://<instance_name>.service-now.com/alm_stockroom_list.do?sysparm_query=type%3De2aa2b3f3763100044e0bfc8bcbe5dde%5EmanagerISEMPTY&sysparm_first_row=1&sysparm_view=`

Once the records are identified, delete them. After the bad demo data has been removed, process the Transfer Order again to confirm the asset is assigned to the correct destination stockroom.

## Related Links

[Transfer orders for Asset Management](https://docs.servicenow.com/en-US/bundle/utah-it-asset-management/page/product/asset-management/concept/transfer-orders-for-am.html)
