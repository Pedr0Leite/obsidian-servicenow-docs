---
title: "Lenovo Asset Warranty Records Missing Assets"
aliases:
  - KB2739298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2739298
kb_number: KB2739298
last_modified: 2026-01-28
---

## Lenovo Asset Warranty Records Missing Assets

  

### Issue

In some cases, warranty records are observed in the system without any associated assets. 

The system does not allow warranty records to be created without an asset.

A validation check is implemented in the Script Include HAMAssetWarrantyUtils to prevent warranty creation or update when an asset is not found:

Reference Script Include:  
`HAMAssetWarrantyUtils`  
`https://<instance-name>.service-now.com/sys_script_include.do?sys_id=4645ba10c7057110cc12784c95c26017`

```
// Do not create / update warranty records if asset is not found
if (gs.nil(data.asset)) {
    continue;
}
```

Because of this check, warranty records are only created when a valid asset is present.

### Release

All

### Cause

After further analysis, it was found that:

-   Warranty records are initially created correctly with associated assets.
-   Subsequently, the related alm\_hardware asset records (for example, Lenovo assets) are being deleted from the system.
-   When the asset is deleted, the warranty record remains, resulting in warranties without associated assets.

This leads to the appearance that warranties were created without assets, when in reality the asset was removed after creation.

### Resolution

1\. Investigate Asset Deletion

-   Review audit history and logs to identify why and by whom the assets were deleted.
-   Check for scheduled jobs, integrations, or cleanup scripts that may be removing assets unintentionally.

2\. Restore Deleted Assets (if applicable)

-   If assets were deleted by mistake, users can restore them using the Undelete option in ServiceNow.

3\. Clean Up Stale Warranty Records

-   If the warranties are no longer valid or the assets cannot be restored, stale warranty records can be safely cleaned up.

**Conclusion**

There is no mechanism in the system that creates warranty records without assets.  
The issue is caused by post-creation deletion of asset records, leaving orphaned warranty records behind.
