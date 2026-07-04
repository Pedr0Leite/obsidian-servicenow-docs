---
title: "Function isPlaybookInReview is missing on Script Include AssetUtils "
aliases:
  - KB0964407
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964407
kb_number: KB0964407
last_modified: 2024-05-21
---

## Function isPlaybookInReview is missing on Script Include AssetUtils

  

### Issue

Install Plugin:

Software Asset Management - SaaS License Management  
Software Asset Management - SaaS License Management Integrations 

This will add Business rule 'Recalculate potential savings async'

  

**Steps to produce:**

-   Navigate to  Software Asset  Licensing  Software Entitlements
-   Open any record with below filter condition:   
          ~ software\_model.product.ignore\_installs = true AND  
          ~ software\_model.product.subscription\_software = true.
-   Update any field on the form.
-   Click on update button.
-   Observe error on form:   
    “Exception (TypeError: Cannot find function isPlaybookInReview in object function () {...}. (sys\_script.63839ade73812300278a97f8faf6a7aa.condition; line 1)) occured while evaluating'Condition: current.cost.changes() || global.AssetUtils.isPlaybookInReview(current); Filter Condition: software\_model.product.ignore\_installs=true^software\_model.product.subscription\_software=true^EQ' in business rule 'Recalculate potential savings async' on alm\_license: Asset001 - SAP SuccessFactors; skipping business rule”.

![](sys_attachment.do?sys_id=e7f128831b307410aefc11751a4bcbda)

### Release

-   Installed plugin: Software Asset Management – SaaS License Management v5.0.1.
-   Instance release version: Quebec

### Cause

-   The condition on business rule - 'Recalculate potential savings async' is checking for function 'isPlaybookInReview' on script include 'AssetUtils' which is not found.
-   Business Rule:   
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=63839ade73812300278a97f8faf6a7aa
-   Script Include:   
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=3596241c475520003ecf706eecde2726

### Resolution

**Workaround:** 

-   Open business rule: Recalculate potential savings async   
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=63839ade73812300278a97f8faf6a7aa
-   Remove "|| global.AssetUtils.isPlaybookInReview(current)" from condition
-   Open list of sys\_update\_xml table  
    https://<instance>.service-now.com/sys\_update\_xml.list
-   Search for above mentioned BR in “name” field
-   Update “Replace on upgrade” to true

![](sys_attachment.do?sys_id=077df5c1db303c1013b5fb2439961901)

  

### Related Links

Fix will be released in next patch of Software Asset Management – SaaS License Management plugin on store.

Please refer PRB PRB1504545.
