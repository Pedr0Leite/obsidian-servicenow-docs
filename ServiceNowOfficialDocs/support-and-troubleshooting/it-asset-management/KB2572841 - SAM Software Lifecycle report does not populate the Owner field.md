---
title: "SAM Software Lifecycle report does not populate the Owner field"
aliases:
  - KB2572841
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2572841
kb_number: KB2572841
last_modified: 2026-05-15
---

## Issue

The scheduled job SAM - Generate Software Lifecycle Report does not populate the Owner field on Lifecycle report records in the `sam_sw_product_lifecycle_report` table.

## Resolution

The Owner field is populated only when both of the following conditions are met.  
[https://<instance-name>.service-now.com/now/nav/ui/classic/params/target/sys\_script\_include.do%3Fsys\_id%3Debe4342843680210d1fcb3d52bb8f27b](https://alliantcredituniondev.service-now.com/now/nav/ui/classic/params/target/sys_script_include.do%3Fsys_id%3Debe4342843680210d1fcb3d52bb8f27b)  

Condition 1 — Software Model with a null database option

A Software Model must exist for the product, the `database_option` field on that Software Model must be null, and the Owner field on the Software Model must be populated.

The script include evaluates this at line 553:

`var modelGR = new GlideRecord(global.ReconciliationConstants.SOFTWARE_MODEL_TABLE); modelGR.addQuery('product', product); modelGR.addNullQuery('database_option'); modelGR.query();`

The Owner value is retrieved at line 568:

`var owner = modelGR.getValue('owner');`

To verify this condition, navigate to Software Asset Management > Software Models, locate the Software Model for the affected product, and confirm that the Owner field is populated and the Database Option field is empty.

Condition 2 — Active lifecycle record with matching attributes

At least one active record must exist in the `sam_sw_product_lifecycle` table with a matching combination of Product, Publisher, Version, Edition, and Full Version.

The script include evaluates this at line 559:

`var lifecycleGR = new GlideRecord(global.ReconciliationConstants.SOFTWARE_PRODUCT_LIFECYCLE_TABLE); lifecycleGR.addQuery('active', true); lifecycleGR.addQuery('norm_product', product); global.SamLifeCycleUtils.queryVersionAndEdition(lifecycleGR, modelGR); lifecycleGR.query();`

To verify this condition, navigate to Software Asset Management > Lifecycle, and confirm that an active record exists matching the Product, Publisher, Version, Edition, and Full Version of the affected product.

If either condition is not met, the Owner field remains empty on the Lifecycle report record.

**Workaround**

This behavior is a known product limitation (PRB1943803). The Owner field is not populated when no active lifecycle record exists for the product version, even if a Software Model with an owner is present.

As a workaround, ensure that an active record exists in the `sam_sw_product_lifecycle` table for the affected product version, edition, and publisher combination. Once an active lifecycle record is present and the Software Model has the Owner field populated, re-run the **SAM - Generate Software Lifecycle Report** scheduled job to populate the Owner field on the report records.
