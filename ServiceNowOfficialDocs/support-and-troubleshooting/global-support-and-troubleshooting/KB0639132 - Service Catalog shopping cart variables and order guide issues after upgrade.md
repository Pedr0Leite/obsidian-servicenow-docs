---
title: "Service Catalog shopping cart variables and order guide issues after upgrade"
aliases:
  - KB0639132
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639132
kb_number: KB0639132
last_modified: 2024-04-07
---

## Service Catalog shopping cart variables and order guide issues after upgrade

  

### Issue

Service Catalog shopping cart variables and order guide issues after upgrade | Custom code causes skipped records

  
  

# Description of the general issue

* * *

After an upgrade to a new release you may find that your Service Catalog starts acting up, showing one or several of the following symptoms:

-   Variables entered in the Order Guide are not cascaded to the Catalog Items
-   Checkout buttons on the Shopping Cart of an Order Guide are not working
-   Errors similar to:
    -   **The element type "g2:evaluate" must be terminated by the matching end-tag "</g2:evaluate>".**
    -   **The element type "j2:while" must be terminated by the matching end-tag "</j2:while>".**
    -   **The element type "j2:forEach" must be terminated by the matching end-tag "</j2:forEach>".**
    -   **org.mozilla.javascript.EcmaError: "GlideCatalogCategoryService" is not defined. Caused by error in <refname> at line _x_**
    -   **Uncaught TypeError: Cannot read property 'value' of null**
-   Errors related to Jelly and the GlideappCatalogItem object

Most of these issues happen because your instance may be using a UI Page from the previous version running, which was not upgraded because it had been modified. This mainly happens with UI Pages **com.glideapp.servicecatalog\_cat\_item\_guide\_view** and **com.glideapp.servicecatalog\_cat\_item**, please check if these are in the Skipped upgrade list. This is found on the **System Diagnostics > Upgrade Monitor** page, where you can query records from specific plugins by adding a filter on "Plugin contains catalog", for example.

You also may want to have a look at other UI Pages and UI Macros you have customized, use the following URLs to find them:

-   UI Pages in the category **Service Catalog**: 
    -   https://<your-instance>.service-now.com/sys\_ui\_page\_list.do?sysparm\_query=category%3Dcatalog
-   UI Macros in the Category name **Service Catalog**:
    -   https://<your-instance>.service-now.com/sys\_ui\_macro\_list.do?sysparm\_query=category%3Dcatalog

# Workaround/Fix

* * *

You can verify if these UI Pages or Macros are to blame by simply reverting to the out-of-box, OOB, version, please check [Resolve a skipped update](https://docs.servicenow.com/csh?topicname=t_ResolveASkippedUpdate.html&version=latest "Resolve a skipped update") for more information on how to do this.

If the OOB version works, then you will have to review your customization to the UI Page to see if it is still needed and port it to the new version if that is the case.
