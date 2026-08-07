---
title: "Why content disappears from Multi-row Variable Set when using in a catalog item"
aliases:
  - KB0783791
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783791
kb_number: KB0783791
last_modified: 2024-04-08
---

## Why content disappears from Multi-row Variable Set when using in a catalog item

  

### Issue

While using a Multi-row Variable Set (MRVS) in a catalog item, the user added the content to the cart and/or to the wish list. However, the content in the multi-row variable set disappears. The user wanted to know why this is.

### Resolution

The solution to this issue is two-pronged:

First, the user is using the deprecated SC Cart widget. Second, the "Additional options, JSON format" section needs to be updated to the current code within (the user had some different code in this section).

As mentioned, the reason the user is facing this issue is that they are using a deprecated widget with deprecated code.  
  
So, to fix the issue, navigate to the below URL:

-   https://INSTANCE.service-now.com/sp\_config?id=page\_edit&p=sc\_cart&table=sp\_instance&sys\_id=db57132adbe9a300b71930ca7c96194f

Then, at the bottom of the page, change the "Widget" value from "SC Shopping Cart Deprecated" to "SC Shopping Cart"  
  
Once the user has done that, please also, just above where the widget used on the page is selected, look into the "Additional options, JSON format" section and replace the code currently present:  
  

```
            {    "cartTemplate": {        "value": "small_shopping_cart.html",        "displayValue": "small_shopping_cart.html"    },    "auto_update_cart": {        "value": "false",        "displayValue": "false"    }}
```

  
... with the below, correct and current code:  
  
`{"cartTemplate": "large_shopping_cart_v2.html"},"auto_update_cart": {"displayValue": "true","value": true}`  
  
In doing these two changes, the user will then be able to navigate properly with the current widget and will be able to see the MRVS values remain in-tact.  
  
So, post performing the changes, the user can go ahead and order the item with a MRVS inside of it and view the cart. From there, the user will see the new UI (per the changes in the widget). Once the New UI populates, the user can click into the name of the item being ordered, whereby they will see the MRVS (and other variables) with their correct values.
