---
title: "Some publishers are not showing in \"Run Reconciliation\" Publishers drop down list and How is \"Run Reconciliation\" Publishers drop down list retrieved? "
aliases:
  - KB0953096
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953096
kb_number: KB0953096
last_modified: 2025-06-17
---

## Text

## Description

Some publishers are not showing in "**Run Reconciliation**" **Publishers** drop down list and How is "**Run Reconciliation**" **Publishers** drop down list retrieved? 

## Explanation

This is the code responsible on retrieving the publishers in "**samp\_run\_reconciliation\_by\_publisher"** UI page rendered when you navigate to **"Run Reconciliation"** UI Module:  
https://Instance\_Name.service-now.com/sys\_ui\_page.do?sys\_id=0074b4f33b132200e724ea2b34efc48b  
  
`<g:evaluate var="jvar_publishers">`  
`var result = [];`  
`var entitlement = new GlideAggregate("alm_license");`  
`entitlement.addNotNullQuery("model");`  
`entitlement.addNotNullQuery("model.manufacturer.sys_id");`  
`entitlement.addQuery("software_model.sw_product_type", ReconciliationConstants.PRODUCT_TYPE_LICENSABLE_VALUE);   ``entitlement.addQuery("software_model.product.ignore_installs", "false");`  
`entitlement.setNoLimit(true);`  
`entitlement.setGroup(true);`  
`entitlement.groupBy("model.manufacturer");`  
`entitlement.query();`  
  
`while (entitlement.next()) {`  
`var obj = {`  
`'text': entitlement.getDisplayValue("model.manufacturer"),`  
`'id': entitlement.getValue("model.manufacturer")`  
`};`  
`result.push(obj);`  
`}`  
`var stringify = JSON.stringify(result);`  
`stringify;`  
`</g:evaluate>`  
  

Based on the logic defined, the publishers will only qualify to show in the publishers drop down list when the following conditions are fulfilled:  
There are entitlements associated with software models which are associated with products from this manufacturer with "Product Type" is Licensable and with "ignore\_installs" equals false.

  
For ease, you could also run the same logic to retrieve the publishers as a **Background Script in global scope** on your instance which will print the list of the publishers/manufacturers that are qualified to show in the "Publishers" drop down list: 

  
`var entitlement = new GlideAggregate("alm_license");`  
`entitlement.addNotNullQuery("model");`  
`entitlement.addNotNullQuery("model.manufacturer.sys_id");`  
`entitlement.addQuery("software_model.product.sw_product_type", "licensable");`  
`entitlement.addQuery("software_model.product.ignore_installs", "false");`  
`entitlement.setNoLimit(true);`  
`entitlement.setGroup(true);`  
`entitlement.groupBy("model.manufacturer");`  
`entitlement.query();`  
  
`while (entitlement.next()){`  
`gs.print(entitlement.getDisplayValue('model.manufacturer'));`  
`}`
