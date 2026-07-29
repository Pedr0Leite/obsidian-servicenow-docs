---
title: "Setting redirect pages for the Service Catalog \"Continue Shopping\" button"
aliases:
  - KB0547287
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547287
kb_number: KB0547287
last_modified: 2024-04-30
---

## Issue

This article describes how to set the redirect page for the **Continue Shopping** button for a catalog, either when using the catalog on a standard platform or when using the catalog in a CMS site.

**Note** – This article applies to releases starting with Eureka. For releases prior to Eureka, use the **_glide.sc.continue.shopping.target_** Service Catalog property.

  

## Resolution

You can define redirect pages for each catalog using the '**Continue Shopping' page** field on the **Maintain Catalogs** module.

![](/sys_attachment.do?sys_id=717ef062db0ab450e515c2230596196d)

By default, this field is empty so clicking the **Continue Shopping** button redirects users back to the Service Catalog home or category page that they were last browsing.

For example, within the Technical Catalog, to redirect the user to all items under the **Hardware** category, set the '**Continue Shopping' page** field to catalog\_home.do?sysparm\_catalog=742ce428d7211100f2d224837e61036d&sysparm\_view=catalog\_technical\_catalog.

  

Using Redirects with a CMS page

* * *

If you have a CMS page featuring the Service Catalog, you can update the redirect function by updating the **CMS 'Continue Shopping' page** field for that catalog's site record.

![](/sys_attachment.do?sys_id=b57ef062db0ab450e515c2230596198f)

For example, to set the redirect for the **Employee Self-Service** site to a new Knowledge record with a pre-populated short description, set this field to kb\_knowledge.do?sys\_id=-1&sysparm\_query=short\_description=hello.

  

Video Tutorial

* * *

  

  

Related Links

* * *

-   [Managing Multiple Service Catalogs](https://docs.servicenow.com/csh?topicname=c_MultipleServiceCatalogs.html&version=latest "Managing Multiple Service Catalogs")
-   [Content Management](https://docs.servicenow.com/csh?topicname=c_ContentManagementSystem.html&version=latest "Content Management")
