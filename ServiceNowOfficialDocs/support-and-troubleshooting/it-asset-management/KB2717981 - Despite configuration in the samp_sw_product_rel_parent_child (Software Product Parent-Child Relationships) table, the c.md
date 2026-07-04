---
title: "Despite configuration in the samp_sw_product_rel_parent_child (Software Product Parent-Child Relationships) table, the child product has not inherited the lifecycle of the parent. Why?"
aliases:
  - KB2717981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2717981
kb_number: KB2717981
last_modified: 2026-05-22
---

## Despite configuration in the samp\_sw\_product\_rel\_parent\_child (Software Product Parent-Child Relationships) table, the child product has not inherited the lifecycle of the parent. Why?

  

### Summary

This kb article provides more information regarding the relatively new feature within servicenow SAMP content where you can create parent-child relationships between software products so that your child products can inherit life-cycle dates from their parent products.

[Create parent-child relationships between software products](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/create-parent-child-relationships-between-software-products.html "Create parent-child relationships between software products")  
  
Customers can create the parent-child configurations in the table: samp\_sw\_product\_rel\_parent\_child and run the job : SAM - Generate Software Lifecycle Report

This configuration will enable child products to inherit OOTB or custom lifecycles defined for the parent product in the sam\_sw\_product\_lifecycle or the sam\_custom\_sw\_product\_lifecycle table.

There are however a few points to note for this functionality :

1\. The details inherited details will be visible only in the : sam\_sw\_product\_lifecycle\_report 

2\. It is a product design feature that we never inherit dates in the table: sam\_sw\_product\_lifecycle. This table holds raw lifecycle dates; it contains dates from content or custom lifecycles only.

3\. As per the current functionality of this feature, only End of (support, extended support and life) is inherited.  General availability is an example which will NOT be inherited.

4\. Additionally, the lifecycle report is calculated only for those software models that have discovery models and related software installations.
