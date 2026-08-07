---
title: "Fix in Service Catalog for Service Portal resulted in an API change"
aliases:
  - KB0621849
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621849
kb_number: KB0621849
last_modified: 2024-04-07
---

## Fix in Service Catalog for Service Portal resulted in an API change

  

### Issue

Changes to the getCatalogItem method  

  
  

# Details

* * *

Changes were made to the getCatalogItem method in order to support the same functionality in Service Catalog and Service Catalog in Service Portal.

The **getCatalogItem** class was changed from **getCatalogItem(String itemID)** to **getCatalogItem(String itemID, boolean isOrdering)**.

The isOrdering parameter indicates whether the system does a create roles security check or a write roles security check on a Service Catalog item's variables. By default (set to false), the system does a check on write roles. When users are first ordering an item or have it in their cart, the parameter checks the create roles. If users are not in the process of ordering (for example, if they were looking at a requested item to see the variables associated with that item), then the parameter checks the write roles.

# Who this change affects

* * *

-   Any internal team or external customer who has cloned the SC catalog item widget, the order guide widget, and the shopping cart widget will be affected by this change.
-   Anyone who has used the **$sp.getCatalogItem** call in their widgets.
-   Anyone who has made these changes needs to update the method to include **isOrdering**. If the method calls are not updated, the variables will just go through a write roles check.
