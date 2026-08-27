---
title: "Mutliple asset records got created automatically."
aliases:
  - KB0814016
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814016
kb_number: KB0814016
last_modified: 2025-06-09
---

## Mutliple asset records got created automatically.

  

### Issue

Sometimes there will be number of assets that will be created automatically with some 'ABC' user. The user would have just created a hardware model and that would in turn triggered asset creation.

Why the assets would get created automatically and how to avoid this.

### Release

All Versions.

### Cause

The below business rule is being called when there an insertion of update happening on "cmdb\_hardware\_product\_model" table.

-   Sync model category (https://Instance\_name.service-now.com/sys\_script\_list.do?sysparm\_query=nameSTARTSWITHSync%20model%20category&sysparm\_view=)

 updateAssetsOnCategory();  
  
function updateAssetsOnCategory() {  
var categories = (current.cmdb\_model\_category + '').split(',');  
var old = (previous.cmdb\_model\_category + '');  
for (var check in categories) {  
if (old.indexOf(categories\[check\]) < 0) {  
var ac = new AssetandCI();  
ac.createMultipleAssets(categories\[check\]);  
}  
}  
}

-    It, in turn, calls the below code to create multiple assets from **AssetandCI** script include

createMultipleAssets : function(categoryId) {  
var category= new GlideRecord('cmdb\_model\_category');  
category.query("sys\_id", categoryId);  
  
if (!category.next() || category.asset\_class.nil() || category.enforce\_verification || category.cmdb\_ci\_class == '')  
return;  
  
var ci = new GlideRecord(category.cmdb\_ci\_class);  
if (!ci.isValid()) return;  
ci.addQuery('asset', '').addOrCondition('asset', null);  
ci.addQuery('model\_id.cmdb\_model\_category', 'CONTAINS', category.sys\_id);  
ci.query();  
  
while (ci.next()) {  
if (ci.model\_id != null && !ci.model\_id.nil() && ci.model\_id.asset\_tracking\_strategy == 'do\_not\_track')  
continue;  
var asset = new GlideRecord(category.asset\_class);  
asset.initialize();  
asset.ci = ci.sys\_id;  
asset.model\_category = category.sys\_id;  
// inherit values from CI for shared fields  
var sync = new AssetAndCISynchronizer();  
sync.syncRecordsWithoutUpdate(ci, asset, 'alm\_asset', true);  
// insert assert record and stick its reference in the CI  
ci.asset = asset.insert();  
ci.update();  
}  

-   So, when a new hardware product model is created/updated, it will check if there are already CIs associated with that Model Category and if there are no assets linked to them, it will create new Asset.

### Resolution

1.  The CIs will have a model\_id field that points to a particular cmdb\_hardware\_product\_model record and they may or may not have assets linked to them.
2.  When a particular model is created/modified, its "Model category" is matched against all the CIs which has the same "Model Category"(linked via CI's model\_id field).
3.  If there is no "Asset" already present to these specific CIs, the intended behavior is to create the asset depending on cmdb\_hardware\_product\_model configuration "Asset tracking strategy".
4.  If you select `"**Don't create Asset**" on the Model record`, then the Assets will not get created.
5.  Otherwise, the asset will be created for the CIs.

![](sys_attachment.do?sys_id=4414a489dbc8f0d016d2a345ca961999)
