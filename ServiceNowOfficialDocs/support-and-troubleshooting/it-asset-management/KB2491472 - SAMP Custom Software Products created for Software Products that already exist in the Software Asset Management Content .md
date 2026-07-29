---
title: "SAMP | Custom Software Products created for Software Products that already exist in the Software Asset Management Content Library"
aliases:
  - KB2491472
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2491472
kb_number: KB2491472
last_modified: 2026-05-12
---

## SAMP | Custom Software Products created for Software Products that already exist in the Software Asset Management Content Library

  

### Issue

Custom Software Product \[samp\_custom\_sw\_product\] records have been created for software products that already exist in the Software Asset Management Content Library.

### Symptoms

Depending on when these were created and how they were used, any of the below symptoms can be true where the Custom Software Product is being referenced instead of the software product already existing in the Software Asset Management Content Library on the below record types.

-   Software Entitlements
-   Software Installations
-   Software Models
-   Reconciliation → Software Model Results
-   Reconciliation → Product Results
-   Software Usage
-   Software Reclamation Candidates

### Facts

-   Custom software products are meant to be created for any publicly available software product that does not exist in the Software Asset Management Content Library. 
-   Custom software products enable you to normalize and account for software products that aren’t part of the Content Library yet.
-   When content sharing is opted into, the Software Asset Management application submits content requests for your custom software products.
-   When your custom software product is added as a software product in the Content Library, a Custom Software Product Suggestion record is created.
-   Product suggestions enable you to consolidate your custom software products with corresponding software products in the Content Library.
-   Consolidating these software products updates all references to your custom software products with references to the software products in the Content Library. 
-   When a Custom software product is created for software product that already exists in the Content Library, then no Product Suggestion record will be created and the Software Asset Management application continues to use the custom software product.

### Release

All Releases

### Cause

Custom Software Product \[samp\_custom\_sw\_product\] records were created by Users.

### Resolution

A Custom Software Product Suggestion won't be created since these software product already exists in the Content Library, however the below background script can be used to manually create a Product Suggestion that can be Accepted to consolidate and update all the references to the custom software product with the software product from the Content Library.

**Prerequisites**

Before you can run the background script, you'll need these values from the Custom Software Product and the Content Library Software Product to plugin to the script.

**I. The Custom Software Product's Name.**

**II. The Custom Software Product's Publisher's Name.**

-   Note, Custom software product's have two Publisher fields, **Publisher (manufacturer)** and **Publisher (publisher)**.
-   **Publisher (manufacturer)** references a record on the **core\_company** table.
-   **Publisher (publisher)** references a record on the **samp\_sw\_publisher** table.
-   If you find the Publisher field you're looking at is empty, check the other Publisher field through Show XML on the record or add both Publisher fields to list view.

**III. The Content Library Software Product's Sys ID.**

-   Content Library software products are located on the **samp\_sw\_product** table.

**Procedure**

1\. Follow the steps in the below background script to set the Custom software product's name, Custom software product's publisher's name, and the Content Library software product's Sys ID parameters and then run the script.

```
// Background Script to Create a SW Product Suggestion record. //
/*
Parameter 1: The Name of the Publisher on the Custom Software Product
Parameter 2: The Name of the Custom Software Product
Parameter 3: The Sys ID of the Content Library Software Product that will be "Suggested"
*/

// 1. Set the Name of the Publisher on the Custom SW Product
var customSwProdPubName = "<custom sw product publisher name here>";

// 2. Set the Name of Custom SW Product
var customSwProdName = "<custom sw product name here>";

// 3. Set the Sys ID of the Content Library SW Product
var contentSwProdSysId = "<content library sw product sysID here>";

// 4. Click [Run Script] in 'global' scope

var suggMapGr = {publisher_name: customSwProdPubName, product_name:customSwProdName,suggested_product: contentSwProdSysId};

process(suggMapGr);

function process(suggMapGr) {
gs.print(suggMapGr.publisher_name);
gs.print(suggMapGr.product_name);
gs.print(suggMapGr.suggested_product);
var encQ = "active=true^status=none^prod_name=" + suggMapGr.product_name + "^publisher.name=" + suggMapGr.publisher_name + "^ORmanufacturer.name=" + suggMapGr.publisher_name;
var prodGr = new GlideRecord(SampCustomSoftwareProductSuggestionHandler.CUSTOM_PRODUCT);
prodGr.addEncodedQuery(encQ);
prodGr.query();
if (!prodGr.next()) {
gs.print("No Custom SW Product Found");
return;
}

// check existing suggestion
gs.print("Checkig for existing Suggestion");
var suggGr = new GlideRecord(SampCustomSoftwareProductSuggestionHandler.CUSTOM_PRODUCT_SUGG);
suggGr.addQuery('custom_product', prodGr.getUniqueValue());
suggGr.query();
if (suggGr.hasNext()) {
gs.print("Existing Suggestion");
return;
}

// suggested product
var suggProd = new GlideRecord('samp_sw_product');
suggProd.get(suggMapGr.suggested_product);

gs.print("Suggested Product - " + suggProd);

// insert suggestion
suggGr = new GlideRecord(SampCustomSoftwareProductSuggestionHandler.CUSTOM_PRODUCT_SUGG);
suggGr.setValue('custom_product', prodGr.getUniqueValue());
suggGr.setValue('custom_publisher', prodGr.getValue('publisher'));
suggGr.setValue('custom_product_type', prodGr.getValue('product_type'));
suggGr.setValue('custom_function_type', prodGr.getValue('function_type'));
suggGr.setValue('custom_subscription_software', prodGr.getValue('subscription_software'));
suggGr.setValue('suggested_product', suggProd.getUniqueValue());
suggGr.setValue('suggested_publisher', suggProd.getValue('publisher'));
suggGr.setValue('suggested_product_type', suggProd.getValue('product_type'));
suggGr.setValue('suggested_function_type', suggProd.getValue('function_type'));
suggGr.setValue('suggested_subscription_software', suggProd.getValue('subscription_software'));
suggGr.setValue('status', 'new');
suggGr.insert();
}
```

2\. After running the background script, go to the **Custom Software Product Suggestion \[samp\_custom\_sw\_product\_suggestion\]** table and open the suggestion record that was just created.

3\. Confirm the Custom Software Product and the content library Software Product on the Suggestion record look correct.

4\. Click the **'Accept'** suggestion button.

All references to the custom software product will be updated with references to the corresponding software product in the Content Library and the custom software product will be set to Active = false.

### Related Links

ServiceNow Product Documentation

[Add custom software products in Workspace](https://www.servicenow.com/docs/csh?topicname=add-custom-software-products-workspace.html&version=latest)

[View custom software product suggestions in workspace](https://www.servicenow.com/docs/csh?topicname=view-custom-software-product-suggestions-workspace.html&version=latest)
