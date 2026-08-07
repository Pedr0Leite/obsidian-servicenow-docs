---
title: "Shopping Cart not displayed in Service Catalog on CMS site"
aliases:
  - KB0551793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551793
kb_number: KB0551793
last_modified: 2024-04-07
---

## Shopping Cart not displayed in Service Catalog on CMS site

  

### Issue

Shopping Cart not displayed in Service Catalog on CMS site 

Problem

* * *

Users within a CMS site do not have a shopping cart when searching categories.  
  
![](/sys_attachment.do?sys_id=a33ff826db0ab450e515c22305961908)  
  
Also, when they drill into an item they do not see the cart or buttons displayed on the cart (Order Now, Add to cart ,or Continue Shopping).  
  
![](/sys_attachment.do?sys_id=bb3ff826db0ab450e515c22305961920)

Symptoms

* * *

CMS users do not see a shopping cart when searching Service Catalog categories. User can select a catalog item, but there is no method to request an item as the following are not displayed:  

-   Shopping cart
-   **Order Now** button
-   **Add to Cart** button
-   **Edit Cart** button
-   **Proceed to Checkout** button
-   **Continue Shopping** button

The issue only affects the CMS Service Catalog. The issue does not occur within the non-CMS Service Catalog.

Cause

* * *

This is a CMS configuration issue. A CMS Site record has a **Use external cart** option that omits the default cart when rendering catalog pages within a site that contains catalog pages. 

![](/sys_attachment.do?sys_id=333ff826db0ab450e515c22305961943)

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If you use an external cart, the no cart option&nbsp;on a service catalog item has no effect. The external cart appears for all items.</td></tr></tbody></table>

If the site record has the **Use external cart** option selected, a block needs to be included in the site so users can interact with their catalog cart. For more information, see [Catalog Cart Block](https://docs.servicenow.com/csh?topicname=c_CatalogCartBlock.html&version=latest "Catalog Cart Block") in the product documentation.

Resolution

* * *

1.  Navigate to **Content Management > Sites**.
2.  Select site record of the CMS site that has the issue.
3.  Ensure the that **Use external cart** option is not selected.
4.  Retest and verify that users see the Shopping Cart as expected when searching within catalog categories.  
      
    ![](/sys_attachment.do?sys_id=ff3ff826db0ab450e515c22305961953)  
      
    Users should also see the Shopping Cart when selecting an item.  
      
    ![](/sys_attachment.do?sys_id=084ff826db0ab450e515c223059619e7)

For more information about the external cart feature, see [Create a Site](https://docs.servicenow.com/csh?topicname=t_CreateANewSite.html&version=latest "Create a Site") in the product documentaiton.
