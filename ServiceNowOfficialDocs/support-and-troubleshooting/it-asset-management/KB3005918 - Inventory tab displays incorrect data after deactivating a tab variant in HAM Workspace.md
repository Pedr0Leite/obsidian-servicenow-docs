---
title: "Inventory tab displays incorrect data after deactivating a tab variant in HAM Workspace"
aliases:
  - KB3005918
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3005918
kb_number: KB3005918
last_modified: 2026-05-07
---

## Issue

When an Inventory tab variant (for example, Donation Orders) is deactivated in the Hardware Asset Management (HAM) Workspace, the UI updates correctly. However, the Inventory Data Broker continues to return backend data for the deactivated tab's original index position. This causes the next tab in numerical order to display incorrect backend data.

## Resolution

Do not modify the original HAMAssetWorkspaceUtil Script Include. It is an out-of-box resource and may be overwritten during upgrades.

Step 1: Create a copy of the Script Include

1.  Navigate to System Definition > Script Includes.
2.  Locate the Script Include named HAMAssetWorkspaceUtil.
3.  Create a copy of this Script Include.
4.  Give the copied Script Include a distinct name, for example: HAMAssetWorkspaceUtil\_Custom.
5.  Save the copied Script Include.

Step 2: Modify the getInventoryTabs() function

1.  Open the copied Script Include.
2.  Locate the function `getInventoryTabs()`.
3.  Identify the table definitions related to Donation Orders.
4.  Remove all Donation Orders-related table references from this function.
5.  Save the Script Include.

This ensures that Donation Orders data is no longer included in the inventory tab resolution logic.

Step 3: Update the Inventory Tabs HAM Data Broker

1.  Navigate to sys\_ux\_data\_broker\_transform.
2.  Select the Inventory Tabs HAM Data Broker.
3.  Update the Data Broker script to reference the copied Script Include (for example, `HAMAssetWorkspaceUtil_Custom`) instead of the original `HAMAssetWorkspaceUtil`.
4.  Save the Data Broker configuration.

This step ensures the Data Broker aligns with the updated tab configuration and does not continue to return backend data for a deactivated tab.

After applying the workaround:

-   The deactivated Donation Orders tab is removed from the UI.
-   The Inventory Data Broker no longer returns Donation Orders backend data.
-   Remaining Inventory tabs display the correct data for their respective indices.

## Additional Information

This issue is tracked in PRB2006484 on the Now Support portal.
