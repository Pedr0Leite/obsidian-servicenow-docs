---
title: "Reconciliation failed  TypeError: Cannot read property \"<sysid>\" from undefined"
aliases:
  - KB1443489
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1443489
kb_number: KB1443489
last_modified: 2026-06-20
---

## Issue

Reconciliation failed at 100%

Error is:

TypeError: Cannot read property "25eb029387e66510e81486a50cbb3514" from undefined

at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1463 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1436 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1637 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1114 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1066 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:1125 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:106 (anonymous)  
at sys\_script\_include.1e5ac217b10e0110fa9bf03fa4dd6856.script:81 (anonymous)  
at sys\_script\_include.602e129eb0276300fa9b028ca0d3b864.script:65 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:114 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:229 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:115 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:93 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:83 (anonymous)  
at sys\_script\_include.74ed3a7d8dfed010fa9b4295b8773c71.script:25  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:26 (anonymous)  
at sys\_script\_include.30bbdf9587f52300923aa75fe5cb0b97.script:439 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:832 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:772 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:57 (anonymous)  
at sys\_trigger.79c2ac6b874c3558e81486a50cbb3561:1

## Resolution

Make sure you've assigned the correct license metric to all your MS products for the recon to work. Please make sure all your MS products as listed in the following documentation:

[License metrics for Microsoft products](https://docs.servicenow.com/bundle/utah-it-asset-management/page/product/software-asset-management2/reference/mapping-ms-license-metrics.html)  
  
For example: if you refer to the software entitlements table for "windows server", as per the document the license metrics should be:

-   Per Core (with CAL)
-   User/Device CAL for CAL licensing

BUT on your instance if you use any other metric such as "Per Core", recon will fail.
