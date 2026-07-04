---
title: "Software Entitlement Total Cost Displays Incorrect Currency for Read-Only Users"
aliases:
  - KB2980978
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2980978
kb_number: KB2980978
last_modified: 2026-04-26
---

## Issue

When a user whose role results in read-only fields on the \`alm\_license\` (Software Entitlement) form views an entitlement record, the \*\*Total cost\*\* field displays in the user's session currency (e.g., GBP) instead of the stored currency (e.g., USD). This is a display-level bug caused by incorrect currency fallback logic in the \*\*\`CalculateTotalCost\` UI script\*\* and the \*\*"Update total\_cost on load" Classic UI client script\*\*.

## Resolution

Updated Fix — Two Scripts Need Changes

**Script 1: CalculateTotalCost (Primary Culprit — UI Script)**  
Table: sys\_ui\_script  
Name: CalculateTotalCost  
sys\_id: e23df8f5e70b0300ab270558d2f6a93b

Current (Defective) — inside getTotalcost() function, in the else block:

currencyCode = g\_form.getValue('unit\_cost.currency\_type') || NOW.currency.code;  
and:

var currency = g\_form.getValue('unit\_cost.currency');  
Fixed: (Apply this)

currencyCode = g\_form.getValue('unit\_cost.currency\_type') || singleCurrencyCode || NOW.currency.code;  
and:

var currency = g\_form.getValue('unit\_cost.currency') || singleCurrencyCode;  
Why: The singleCurrencyCode parameter already carries the record's actual stored currency (g\_scratchpad.unitCostCurrency), populated server-side by the existing display business rule "Get locale info on display" using current.unit\_cost.getCurrencyCode(). This value is always correct regardless of the user's role or ACL restrictions.

**Script 2: "Update total\_cost on load" (Client Script)**  
Table: sys\_script\_client  
Name: Update total\_cost on load  
sys\_id: d0ea34ef10544110f877013b02dc6025  
Type: onLoad client script for alm\_license

Change 1 — currencyCode fallback:

Current (Defective):  
currencyCode = g\_form.getValue('unit\_cost.currency\_type') || NOW.currency.code;  
Fixed:  
currencyCode = g\_form.getValue('unit\_cost.currency\_type') || g\_scratchpad.unitCostCurrency || NOW.currency.code;

Change 2 — unitCostCurrency variable (prevents false mismatch triggering unnecessary GlideAjax call):

Current (Defective):  
var unitCostCurrency = g\_form.getValue('unit\_cost.currency');  
Fixed:  
var unitCostCurrency = g\_form.getValue('unit\_cost.currency') || g\_form.getValue('unit\_cost').split(';')\[0\];

When unit\_cost.currency is empty (ACL-read-only), the mismatch comparison unitCostCurrency !== totalCostCurrency would always be true, unnecessarily triggering the GlideAjax database update. This fallback extracts the currency from the unit\_cost field value (format: USD;500).

3.Impact  
The fix is low risk and backward compatible. It only adds an additional fallback step (the record's stored currency from g\_scratchpad) before the final fallback to the user's session currency (NOW.currency.code). When unit\_cost.currency\_type is populated (normal scenario), the behavior is unchanged. The fix only activates when unit\_cost.currency\_type is empty due to read-only rendering.
