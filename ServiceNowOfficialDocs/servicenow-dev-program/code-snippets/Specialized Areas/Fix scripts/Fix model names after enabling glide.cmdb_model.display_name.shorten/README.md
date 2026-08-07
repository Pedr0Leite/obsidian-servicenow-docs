---
title: "Fix model names after enabling glide.cmdb_model.display_name.shorten"
aliases:
  - Fix model names after enabling glide.cmdb_model.display_name.shorten
tags:
  - servicenow-dev-program
  - code-snippet
  - fix-model-names-after-enabling-glidecmdb-modeldisplay-nameshorten
  - fix-scripts
---

There is a property that enables de-duplication of Manufacturer/Publisher Names from Model records (property name: [glide.cmdb_model.display_name.shorten](https://docs.servicenow.com/bundle/rome-it-service-management/page/product/asset-management/concept/c_InstalledWithModelManagement.html#r_ModelManagementProperties "glide.cmdb_model.display_name.shorten")). If this property is not active and users enter the Manufacturer/Publisher name into the Model Name field the Manufacturer/Publisher name will show twice in the Display Name.

<div style="padding-left: 2em;">

For example,  
**Manufacturer/Publisher Name:** Microsoft  
**Model Name:** Microsoft Word  
**Display Name with Property FALSE:** <span style="color: #ff0000;">Microsoft Microsoft Word</span>  
**Display Name with Property TRUE:** <span style="color: #008000;">Microsoft Word</span>

</div>

Once this property is activated, inserts/updates of Model records will trigger the business rule to recalculate the Display Name when one of the following fields is updated: Manufacturer/Publisher, Name, Version, Edition, Platform, Language. If you activate this property AFTER many models have been loaded, you may need to run a fix script to retroactively clean the existing Model Display Names.

The script below can be run as a Fix Script or as a Background Script. Normally, I would `setWorkflow(false)` for this kind of cleanup, but there are a few cascade Business Rules that need to run as this fix is implemented.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
