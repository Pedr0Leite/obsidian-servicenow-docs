---
title: "Using Cart Layouts in Service Catalog"
aliases:
  - KB0563368
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563368
kb_number: KB0563368
last_modified: 2026-02-20
---

## Using Cart Layouts in Service Catalog

  

### Issue

Administrators may need to enable and configure Cart Layouts in Service Catalog to customize the cart and checkout experience.

This article explains how to:

-   Enable cart layout functionality
-   Configure cart layout settings
-   Understand behavior changes after enabling cart layouts

## Overview

Cart Layouts allow administrators to customize the appearance and behavior of the Service Catalog cart and checkout experience.

This functionality is available in Fuji and later releases and provides greater flexibility in configuring cart-related elements.

### Release

All

### Resolution

## Enabling Cart Layout Functionality

To enable cart layouts:

1.  Navigate to Service Catalog Properties.
2.  Locate the property:
    
        `glide.sc.use_cart_layouts`
    
3.  Set the property to true.
4.  Save the changes.

### Important Notes

-   Cart Layouts are enabled by default for new customers.
-   For upgraded instances, the feature may be disabled if cart macros were previously customized.
-   Enabling this property allows customization of cart and checkout-related widgets.

## Using Cart Layout Functionality

After enabling cart layouts, administrators can:

-   Hide price, quantity, cart, or cart-related buttons (for example, _Order Now_ or _Proceed to Checkout_)
-   Change labels of shopping cart buttons
-   Modify the order of elements or columns on the order status screen

To configure cart layouts:

1.  Navigate to:
    
        `Service Catalog > Catalog Definitions > Maintain Cart Layouts`
    
2.  Modify layout settings as needed.
3.  Save and test changes in the Service Catalog.

## Behavior Considerations

After enabling Cart Layouts:

-   Some item-specific cart settings (for example, _Omit Price_ or _No Quantity_) may not behave as expected.
-   Items may still display quantity even if “No Quantity” is selected at the item level.

If item-specific behavior is required:

1.  Ensure the cart layout property remains enabled.
2.  Clear the Use Cart Layouts option on the specific catalog item.
3.  This allows the item’s individual cart settings to override the global cart layout configuration.

* * *

## Additional Notes

-   Cart Layouts affect cart and checkout UI behavior only.
-   Changes should be tested in a lower environment before enabling in production.
-   Review customized cart macros before enabling to avoid unexpected UI behavior.
