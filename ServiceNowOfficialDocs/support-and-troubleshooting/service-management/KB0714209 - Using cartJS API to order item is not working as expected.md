---
title: "Using cartJS API to order item is not working as expected"
aliases:
  - KB0714209
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714209
kb_number: KB0714209
last_modified: 2024-04-07
---

## Using cartJS API to order item is not working as expected

  

### Issue

# Symptoms

* * *

Try to Order an item from custom cart orders but all items from default cart is being ordered

# Release

* * *

London and below

# Cause

* * *

This is a bug in the platform and it has been addressed in PRB1297366

# Resolution

* * *

The OOB order\_now API (api/sn\_sc/servicecatalog/items/{sys\_id}/order\_now) is designed for ordering only a single item

For ordering multiple items, checkout(/api/sn\_sc/servicecatalog/cart/checkout) or submit order (/api/sn\_sc/servicecatalog/cart/submit\_order) should be used.

But currently, there is a bug in the platform which orders all the items from the portal cart instead of the custom cart, if we order multiple items using checkout or submit order and a PRB1297366 was created for this issue and the Problem is in testing state.

So as a workaround, a custom web service can be created and can be used that in the apps outside of SN.

WORKAROUND:

1\. Please change the current application scope to "Service Catalog REST API" (the same scope where the OOB order\_now scripted API is present)

2\. Type "Scripted REST APIs" in the filter navigator and select the "Scripted REST APIs" under the "System Web Services"

3\. Open the record with the name "Service Catalog API"

4\. Under the "Resources" section (at the bottom), Open the record with the name "Buy Item" in a separate tab for reference.

5\. Go back to the "Resources" section and click "new"

6\. Give the following values for the fields:

Name : <your desired name> (e.g) Custom Order now

API Version: v1

HTTP Method: POST

Relative path: /items/{sys\_id}/<your desired name> (e.g) /items/{sys\_id}/custom\_order\_now

7\. Under the script section, paste the following code:

(function process(/\*RESTAPIRequest\*/ request, /\*RESTAPIResponse\*/ response) {

// implement resource here

var request\_body = request.body.nextEntry();

var quantity = '' + request\_body.sysparm\_quantity;

var noValidation = (request\_body.sysparm\_no\_validation == 'true');

var cartName = request\_body.sysparm\_cart\_name;

if (!/^\\+?(\[0-9\]\*)$/.test(quantity))

throw new sn\_ws\_err.BadRequestError("Invalid Quantity value");

else

request\_body.sysparm\_quantity = quantity;

var itemId = '' + request.pathParams.sys\_id;

request\_body.sysparm\_id = itemId;

var catItem = new sn\_sc.CatItem(itemId);

if (!catItem.canView())

throw new sn\_ws\_err.BadRequestError("Security constraints prevent ordering of Item");

if(!noValidation) {

var catUtil = new RestCatalogUtil();

if (!catUtil.checkMandatoryVariables(itemId, request\_body.variables))

throw new sn\_ws\_err.BadRequestError('Mandatory Variables are required');

}

var cart;

//If cartName is undefined then it will be falsy

if(cartName){

cart = new sn\_sc.CartJS(cartName);

}else{

cart = new sn\_sc.CartJS("cart\_" +itemId);

request\_body.sysparm\_cart\_name = "cart\_" +itemId;

}

try {

return cart.orderNow(request\_body);

}catch(e) {

gs.debug(e);

throw new sn\_ws\_err.NotFoundError("Invalid Request");

}

})(request, response);

8\. Save the record.

Now the custom scripted api can be found in the API list in the REST Explorer and it would order all the items from the custom cart.

Please make sure that this object {"sysparm\_quantity":"1","get\_portal\_messages":"true","sysparm\_cart\_name":"JJ1234"} be included in the Request body.
