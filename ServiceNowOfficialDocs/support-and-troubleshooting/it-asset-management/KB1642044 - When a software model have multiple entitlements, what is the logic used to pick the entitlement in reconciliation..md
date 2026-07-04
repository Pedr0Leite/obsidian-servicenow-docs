---
title: "When a software model have multiple entitlements, what is the logic used to pick the entitlement in reconciliation."
aliases:
  - KB1642044
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1642044
kb_number: KB1642044
last_modified: 2024-05-02
---

## When a software model have multiple entitlements, what is the logic used to pick the entitlement in reconciliation.

  

### Issue

When a software model have multiple entitlements, what is the logic used to pick the entitlement in reconciliation.

### Release

NA

### Cause

Question

### Resolution

  
When you have multiple Entitlements for software with different license metric- Reconciliation will query the list of license metric based on active entitlements of this product and it will license all the devices/users that have been allocated entitlements on this license metric.  
  
If no allocation, would consume entitlements in the most efficient manner. It will pick the license metric which can license maximum installs first then once all the licenses used for this metric, it will move to next available license metric.  
  
For example, when you have License metrics per server and per core. When install is having core count as 6. Per server will need 1 license and per core needs 6 licenses.In this case, it will user per server to license the install.  
  
You can use allocation or License consumption rules should be used.  They are supported and quite useful.  [https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/create-consumption-rule.html](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/create-consumption-rule.html "https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/create-consumption-rule.html")
