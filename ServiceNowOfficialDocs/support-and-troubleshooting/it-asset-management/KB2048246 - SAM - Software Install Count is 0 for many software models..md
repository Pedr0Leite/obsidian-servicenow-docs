---
title: "SAM - Software Install Count is \"0\" for many software models."
aliases:
  - KB2048246
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2048246
kb_number: KB2048246
last_modified: 2026-03-27
---

## SAM - Software Install Count is "0" for many software models.

  

### Issue

SAM - Software Install Count is "0" for many software models even though we installs available in software installs table.

### Release

Any Version

### Resolution

-   This is expected behaviour as per the design, these Slack models are subscription models, ignore installs will be true for this product.
-   Schedules Job: SAM - Get install count for software model  
        https://instance\_name.service-now.com/sys\_script\_include.do?sys\_id=aa672bac0f473300d505579ac4767e16

runJobForRecord: function(smGr) {  
var PRODUCT\_SAP\_NAMED\_USER = '5e73bc41dbab570024cd68461b9619f5';  
if (smGr.getValue('product') === PRODUCT\_SAP\_NAMED\_USER || smGr.product.ignore\_installs) {  
smGr.setValue('install\_count', 0);  
smGr.setWorkflow(false);  
smGr.update();  
return;  
}

-   The function checks whether the product field of the smGr matches the PRODUCT\_SAP\_NAMED\_USER value or whether the product.ignore\_installs field is true.
-   If either condition is met, it performs the following:
-   -   Sets the install\_count to 0
