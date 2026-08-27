---
title: "Software Installation Table inconsistently populating Normalized Product"
aliases:
  - KB0784609
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784609
kb_number: KB0784609
last_modified: 2024-04-08
---

## Issue

What populates normalized product on the software install records?

## Resolution

The business rule "Create a Software Normalization" populates the norm\_product field on the install record.  
This is the excerpt of the code that populates it:  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
current.discovery\_model = gr.sys\_id;  
if(!gs.nil(gr.norm\_product) && gr.norm\_product.product\_type.toString() === 'licensable' && !gr.norm\_product.ignore\_installs) {  
current.setValue("norm\_product", gr.getValue('norm\_product'));  
current.setValue("norm\_publisher", gr.getValue('norm\_publisher'));  
} else {  
current.setValue("norm\_product", "NULL");  
current.setValue("norm\_publisher", "NULL");  
}  
}  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Per the business rule, we need the following condition to be met to populate the normalized product field on the install record:  
1\. The discovery model associated to it should not have product as empty.  
2\. The discovery model associated to it should have product type licensable.  
3\. The discovery model's normalized publisher should not have ignore installs as true  
  
If even one of these fail we do not populate the filed normalized product on the install software record.
