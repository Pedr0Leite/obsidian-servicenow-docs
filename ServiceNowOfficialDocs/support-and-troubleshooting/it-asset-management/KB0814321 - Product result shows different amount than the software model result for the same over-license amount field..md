---
title: "Product result shows different amount than the software model result for the same over-license amount field. "
aliases:
  - KB0814321
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814321
kb_number: KB0814321
last_modified: 2024-04-08
---

## Product result shows different amount than the software model result for the same over-license amount field. 

  

### Issue

During reconciliation, there is a discrepancy in the over-license amount.

In the Reconciliation result --> Product result shows different amount than the software model result for the same over-license amount field. 

![](sys_attachment.do?sys_id=4d23a805dbc8f0d016d2a345ca9619cd)

### Release

All Versions.

### Cause

This is because Single currency mode is the set on the instance, but glide.system.locale property was not set to the same currency code.  
This would cause currency conversion issues in aggregation.

### Resolution

If Multi-Currency mode has to be used in the instance, follow the below instructions:

1.  Set the below system properties:  
    -   glide.i18n.single\_currency = 'false'.
    -   glide.system.locale = ""
2.  Run the Reconciliation Job as a user whose Session Currency is set to USA.

If the Single Currency mode has to be used:

1.  Set the below property to true: glide.i18n.single\_currency = 'true'.
2.  Set the property i18n.single\_currency.code to the three-letter ISO currency code
3.  Set the system locale – glide.system.locale to that of Single currency code.

Single-currency mode has the following limitations:

-   Single currency mode changes the currency in the user views and does not change the number formatting. Even though users in different countries see currency values in one currency, the number formatting (as determined by the user’s locale) might not be what they expect.
-   Because currency value input is constrained to the single currency, price fields cannot be used.

The effects of rate conversions can be avoided by setting the system locale and the reference currency to be the single currency.
