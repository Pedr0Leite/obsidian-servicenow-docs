---
title: "Duplicate Request Items are created by 'BUY ITEM' Service Catalog API when two request payloads are sent at the same time from a third party"
aliases:
  - KB0813822
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813822
kb_number: KB0813822
last_modified: 2024-04-08
---

## Duplicate Request Items are created by 'BUY ITEM' Service Catalog API when two request payloads are sent at the same time from a third party

  

### Issue

Duplicate Request Items are getting created by 'BUY ITEM' Service Catalog API when two request payloads are sent at the same time to the ServiceNow from a third party website.

REPLICATION STEPS:  
i)Go to 3rd party site which is calling the below Buy item API at the backend

 /api/sn\_sc/servicecatalog/items/{sys\_id}/order\_now(BUY ITEM)

ii) Open the order page in two separate tabs in a browser

iii) Fill out fields and submit at the same time and click submit within a gap of One second

iV)Go to the instance and validate. This creates two requests which is correct but the second request consists of two RITM's instead of one and the other one is a duplicate RITM from the first request

### Release

New York Patch 4 Hot Fix 2

### Cause

The order\_now functionality will order all the items which are present in the cart irrespective of what is the current item. In this case, since both the requests are very close to each other, the first requests add's the item to the cart, before it could delete that cart item, a new request is again checking it out. This indeed creating a duplicate RITM record which is a copy of first RITM record in first request in the second request.

### Resolution

There is a property called "glide.sc.enable\_order\_now" which needs to be set to "true" on the instance that will resolve the issue and avoid duplicate RITM records in this context.
