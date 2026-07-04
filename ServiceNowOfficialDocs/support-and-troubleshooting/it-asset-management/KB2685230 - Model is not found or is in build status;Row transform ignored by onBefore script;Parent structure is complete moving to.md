---
title: "\"Model is not found or is in build status;Row transform ignored by onBefore script;Parent structure is complete moving to desired state\" and state is Ignored"
aliases:
  - KB2685230
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2685230
kb_number: KB2685230
last_modified: 2025-12-16
---

## "Model is not found or is in build status;Row transform ignored by onBefore script;Parent structure is complete moving to desired state" and state is Ignored

  

### Issue

When importing the bulk import in the Enterprise Asset Management module, we see below error:

"Model is not found or is in build status;Row transform ignored by onBefore script;Parent structure is complete moving to desired state" and state is Ignored

### Symptoms

1\. Open EAM Workspace -> Admin Center -> Bulk Import -> Create Assets  
2\. Use the Excel spreadsheet.  
3\. Wait for import, see comment section that says "Model is not found or is in build status;Row transform ignored by onBefore script;Parent structure is complete moving to desired state". 

### Release

Any Version

### Cause

\[-\] The Below code from the EAMImportTransform script include is responsible for populating the model on the staging table "sn\_eam\_asset\_import\_row"  
  
EAMImportTransform.preprocessAsset = function(importSetId) {  
// Pre-populate model for each asset row  
var stagingGr = new GlideRecord(EAMImportConstants.ASSET\_STAGING\_TABLE);  
stagingGr.addQuery('sys\_import\_set', importSetId);  
stagingGr.addNotNullQuery('manufacturer');  
stagingGr.addNotNullQuery('model\_name');  
stagingGr.addNotNullQuery('model\_number');  
stagingGr.query();  
var utils = new global.AssetUtils();  
while (stagingGr.next()) {  
var modelGr = EAMImportTransform.getModelRecord(  
stagingGr.manufacturer, stagingGr.model\_name, stagingGr.model\_number  
);  
if (modelGr.next()) {  
stagingGr.setValue('model', modelGr.getUniqueValue());  
// Default quantity to 1 for serialized assets  
if (utils.getAssetOrConsumable(modelGr) !== 'consumable') {  
stagingGr.setValue('quantity', '1');  
}  
stagingGr.update();  
}  
  
\[-\]From the above code, getModelRecord() to look up an existing Model CI (product model) based on:  
\[1\]Manufacturer  
\[2\]Model Name  
\[3\]Model Number  
  
If the result contains a record ->execute the next steps.  
  
\[-\]Populate the model reference field  
stagingGr.setValue('model', modelGr.getUniqueValue());  
\[-\]Links the staging record to the actual model record in the CMDB.

### Resolution

When importing data from Excel, if no model is available in the cmdb\_model table, the flow is stopped, creating an issue.  
  
Please add models to the table first and then proceed further.
