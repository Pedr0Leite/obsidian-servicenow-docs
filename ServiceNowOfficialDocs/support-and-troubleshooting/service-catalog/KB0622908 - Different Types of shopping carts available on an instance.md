---
title: "Different Types of shopping carts available on an instance"
aliases:
  - KB0622908
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622908
kb_number: KB0622908
last_modified: 2024-04-07
---

## Issue

Different Types of Shopping Carts Available on an Instance

  
  

# Background

* * *

Prior to Helsinki, only one shopping cart type is available for each user. This is the **DEFAULT** shopping cart. In Geneva or order releases, by navigating to sc\_cart table, the cart name shows **DEFAULT** for all users. Order Guide, Order Now and the standard checkout process all use the same **DEFAULT** cart for each user. 

During an Order Now checkout, other items on the cart are ordered in the same request. Similarly, during an Order Guide checkout, other items not part of the order guide are ordered in the same request. Admins or fulfillers may be confused why items not part of the order guide are in the same request. 

To prevent this unpredictable behavior, there are now new shopping carts available from Helsinki and later releases.

# Order Now Shopping Cart

* * *

The Order Now shopping cart uses a cart specifically for catalog items with **Order Now** enabled, or **no\_order\_now=false**. This prevents the Order Now checkout process from also checking out all the other items on the **DEFAULT** cart.

The cart name is **cart\_<sys\_id of the catalog item>**. This cart is deleted after checkout is completed. 

To enable this, set glide.sc.enable\_order\_now to **true**. If set to **false**, the Order Now process uses the **DEFAULT** cart.

This feature is available starting in Helsinki.

# Order Guide Shopping Cart

* * *

The Order Guide shopping cart creates a cart specifically for Order Guides. Only items ordered from the order guide are included in the request.

The cart name is **<sys\_id of the order guide>**. This cart is deleted after checkout is completed. 

To enable this, set glide.sc.guide.two\_step\_use\_custom\_cart to **true**. If set to **false**, the Order Guide process uses the **DEFAULT** cart. An additional requirement for this property to work is enable the **Two step** option for the order guide. 

This feature is available starting in Istanbul.
