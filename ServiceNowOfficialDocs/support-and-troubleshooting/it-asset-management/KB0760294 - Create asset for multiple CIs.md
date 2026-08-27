---
title: "Create asset for multiple CIs"
aliases:
  - KB0760294
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760294
kb_number: KB0760294
last_modified: 2025-09-09
---

## Create asset for multiple CIs

  

### Issue

Some CMDB records have empty assets. How can we create assets for multiple CMDB records?

### Release

All supported releases.

### Cause

The "Create Asset on insert" business rule creates an asset for the CI when the CI is inserted. This business rule only runs on insert.

Here are some of the reasons why a CMDB record may have an empty Asset:

-   CIs imported and import was not configured to run business rules
-   Error when creating asset (further investigation would be necessary in this case)
-   Business rule "Create Asset on insert" not active/present at time of CI insert

### Resolution

The missing assets could be created via the UI or scripts.

**Note:** Perform any testing in a non-production instance first.

**From UI**

1.  Navigate to the CI with the empty asset and click on the Mode ID, model\_id
2.  Once the cmdb\_model loads, click on the model category the CI belongs to
3.  Click on "Create Assets"

**From Scripts**

Assets can also be created via "Scripts - Background", scheduled jobs, and fix scripts with the following methods:

-   To create assets for multiple CIs:  
    AssetandCI.createMultipleAssets('<sys\_id\_of\_cmdb\_model\_category>');
-   To create an asset for a single CI:  
    AssetandCI.createAsset('<ci\_sys\_id>');

**Note:** See script include AssetandCI for other methods available.

### Related Links

-   [Asset and CI management](https://docs.servicenow.com/csh?topicname=c_ManagingAssets.html&version=latest#c_AssetandCIManagement "Asset and CI management")
-   [Create Assets manually](https://docs.servicenow.com/csh?topicname=t_CreatingAssetsManually.html&version=latest "Create Assets manually")
-   [Asset/CI synchronisation fails to insert the other record if any fields listed in alm\_asset\_ci\_field\_mapping don't exist or are empty values.](https://support.servicenow.com/kb_view.do?sysparm_article=KB0744592 "Asset/CI synchronisation fails to insert the other record if any fields listed in alm_asset_ci_field_mapping don't exist or are empty values.")
-   [Creating assets and CIs from a CMDB Model form generates incomplete records](https://support.servicenow.com/kb_view.do?sysparm_article=KB0622948 "Creating assets and CIs from a CMDB Model form generates incomplete records")
