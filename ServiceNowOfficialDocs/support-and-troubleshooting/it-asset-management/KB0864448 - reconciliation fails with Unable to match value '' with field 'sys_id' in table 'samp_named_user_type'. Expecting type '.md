---
title: "reconciliation fails with Unable to match value '' with field 'sys_id' in table 'samp_named_user_type'. Expecting type 'GUID"
aliases:
  - KB0864448
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864448
kb_number: KB0864448
last_modified: 2024-04-08
---

## Issue

Reconcilliation runs and fail at 100% with the following stacktrace in system logs:

The following error is seen in the log:  
\[2020-11-11T21:38:40.069Z\]: Unable to match value '' with field 'sys\_id' in table 'samp\_named\_user\_type'. Expecting type 'GUID'  
\-------- STACK TRACE ---------  
at \[global\] 'Schema' \[sys\_script\_include:4e115aed73512300bb513198caf6a749\]:258 (checkFieldType)  
at \[global\] 'GlideQueryActions' \[sys\_script\_include:89cffabe29300010fa9b76addd33871b\]:46 (checkWhere)  
at \[global\] 'GlideQueryActions' \[sys\_script\_include:89cffabe29300010fa9b76addd33871b\]:5 (anonymous)  
at \[global\] 'GlideQueryEvaluator' \[sys\_script\_include:d52b3c8a08013300fa9b4300d8d67a76\]:112 (anonymous)  
at \[global\] 'GlideQueryEvaluator' \[sys\_script\_include:d52b3c8a08013300fa9b4300d8d67a76\]:110 (executePlan)  
at \[global\] 'GlideQueryEvaluator' \[sys\_script\_include:d52b3c8a08013300fa9b4300d8d67a76\]:287 (executeSelectQuery)  
at \[global\] 'GlideQueryEvaluator' \[sys\_script\_include:d52b3c8a08013300fa9b4300d8d67a76\]:217 (createQuerySession)  
at \[global\] 'GlideQueryEvaluator' \[sys\_script\_include:d52b3c8a08013300fa9b4300d8d67a76\]:259 (anonymous)  
at \[global\] 'Stream' \[sys\_script\_include:9f50ba7773a31300bb513198caf6a791\]:373 (forEach)  
at \[global\] 'SamNamedUserForSAPLicenseCalculator' \[sys\_script\_include:b5116875b8a20010fa9b0ec03c472815\]:179 (anonymous)  
at \[global\] 'SamNamedUserForSAPLicenseCalculator' \[sys\_script\_include:b5116875b8a20010fa9b0ec03c472815\]:24 (anonymous)  
at \[global\] 'PrototypeServer' \[sys\_script\_include:d22e7bdbc0a8016500a18e024bfc9aa3\]:4 (anonymous)  
at \[global\] 'SamLicenseCalculatorFactory' \[sys\_script\_include:88047545f8613300fa9baef77f61fae6\]:60 (anonymous)  
at \[global\] 'SamProductCalculator' \[sys\_script\_include:8a6dbe2887522300ede6f64936cb0b2c\]:288 (anonymous)  
at \[global\] 'SamProductCalculator' \[sys\_script\_include:8a6dbe2887522300ede6f64936cb0b2c\]:161 (anonymous)  
at \[global\] 'SamProductCalculator' \[sys\_script\_include:8a6dbe2887522300ede6f64936cb0b2c\]:65 (anonymous)  
at \[global\] 'SamProductCalculator' \[sys\_script\_include:8a6dbe2887522300ede6f64936cb0b2c\]:58 (anonymous)  
at \[global\] 'SamProductCalculator' \[sys\_script\_include:8a6dbe2887522300ede6f64936cb0b2c\]:46 (anonymous)  
at \[global\] 'SamPublisherCalculator' \[sys\_script\_include:30bbdf9587f52300923aa75fe5cb0b97\]:308 (anonymous)  
at \[global\] 'SamPublisherCalculator' \[sys\_script\_include:30bbdf9587f52300923aa75fe5cb0b97\]:305 (anonymous)  
at \[global\] 'SamPublisherCalculator' \[sys\_script\_include:30bbdf9587f52300923aa75fe5cb0b97\]:248 (anonymous)  
at \[global\] 'ReconciliationEngine' \[sys\_script\_include:6761b0dd0b1232001a17650d37673a77\]:107 (anonymous)  
at \[global\] 'ReconciliationEngine' \[sys\_script\_include:6761b0dd0b1232001a17650d37673a77\]:44 (anonymous)  
at 'SAM - Software License Reconciliation Wo' \[sys\_trigger:26c75aef1b9824905baafee58d4bcb68\]:1

## Resolution

There are 2 ways to resolve this depending on what the user's licensing needs are:

1) User wants to use the "Named user" license metric to create the entitlement - In this case the user can do either of the following :

-   Delete the existing entitlement of license metric "Named User" associated to this model and then recreate this entitlement with license metric "Named User" using a software model with Product = Named Users only.
-   Update the software model on this existing entitlement of license metric "Named User" to point to the Product = Named Users

2) User wants to use the existing product in the software model to create the entitlement :

-   If this product does not have the Named User or SAP license metric field showing up and populated on the software model form, this product is not eligible to be licensed by either Named User or Engine Measurement license metrics. The user will have to use Common metric group with Per User/Per Device license metrics to license this product based on their licensing needs.

  

## Additional Information

The customer is expected to initially follow this document to Deploy the ABAP program for SAP - [https://docs.servicenow.com/bundle/madrid-software-asset-management/page/product/software-asset-management2/concept/sap-publisher-pack.html](https://docs.servicenow.com/bundle/madrid-software-asset-management/page/product/software-asset-management2/concept/sap-publisher-pack.html)

This will help automatically pull in all the required data from SAP to create the software models.

SAM currently supports only 2 license metrics for licensing SAP products :

1) Named User - Software model used to create an entitlement of this license metric must only have product = Named Users

2) Engine Measurement - There are a list of products(or Engines) that are supported for this license metric (attached to the KB for reference). For the latest updated list please refer to this [link](https://support.sap.com/en/my-support/systems-installations/system-measurement/engine-self-declaration-product-measurement.html "link"). (SAP account needed to view the link)

NOTE : For SAP products that do not fall in any of the above two categories, the product is not eligible to be licensed by either Named User or Engine Measurement license metrics. The user will have to use Common metric group with Per User/Per Device license metrics to license this product based on their licensing needs. Reconciliation will fail if the user tries to use a software model associated with such a product to create an entitlement with metric group SAP and License metric Named User.
