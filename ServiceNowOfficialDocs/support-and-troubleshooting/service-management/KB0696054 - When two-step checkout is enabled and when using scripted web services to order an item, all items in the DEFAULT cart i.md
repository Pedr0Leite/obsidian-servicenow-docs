---
title: "When two-step checkout is enabled and when using scripted web services to order an item, all items in the DEFAULT cart is being ordered instead of the specified item in the request body. "
aliases:
  - KB0696054
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696054
kb_number: KB0696054
last_modified: 2024-04-07
---

## When two-step checkout is enabled and when using scripted web services to order an item, all items in the DEFAULT cart is being ordered instead of the specified item in the request body.

  

### Issue

# Symptoms

* * *

When two-step checkout is enabled and when we use scripted web services to order an item (by passing in the custom cart with the sys\_id of the item as a parameter to n\_sc.CartJS), all items in the DEFAULT cart is being ordered instead of the specified item in the request body. 

# Release

* * *

Kingston

# Cause

* * *

This is a bug in the platform and a PRB1297366 is created to fix the issue. 

# Resolution

* * *

The dev team is working on a fix for this issue at the time of this writing (PRB1297366).

However, we have a workaround to resolve the issue.

WORKAROUND:

 we can make use of the OOB REST API named "Buy Item", which has this endpoint,

POST [https://<instance-name>.service-now.com/api/sn\_sc/servicecatalog/items/{sys\_id}/order\_now](https://instancename.service-now.com/api/sn_sc/servicecatalog/items/{sys_id}/order_now)

One modification is required to get over the issue and it is to add this parameter along with other parameters to the request body,

'get\_portal\_messages': 'true'

Now it will directly order the item specified in the request body rather than all the items in the DEFAULT/portal cart.

To test the endpoint, please navigate to "System Web services" -> "REST" -> "REST API EXPLORER"

2\. Select theNamespace -> sn\_sc

3\. Click on the API named "Buy Item (POST)"

4\. Give the sys\_id of the item being ordered.

5\. Please provide variable values, if any, for the item.

6\. Add the quantity (sysparm\_quantity) and the above mentioned parameter, 'get\_portal\_messages': 'true'.

Click send.

Now we can see from the response that it orders only the item being specified and not all the items in the DEFAULT cart.
