---
aliases:
  - "generateCatalogItemFromUIAction"
area: "Scripts"
source: custom
tags:
  - ui-action
  - script-include
  - glide-ajax
  - catalog-item
  - cart-api
  - scripts
---

# generateCatalogItemFromUIAction

A UI Action + Script Include pair: the UI action's client-callable `redeploy()` fires a `GlideAjax` call to a `FJCatalogUtilsAjax` script include, which uses the `Cart` API (`addItem`, `setVariable`, `getCart`, `placeOrder`) to programmatically re-order a catalog item for the current user with pre-populated variables, then redirects to the new request. Pattern for "re-order"/"repeat this request" buttons.

```javascript

//UI Action
function redeploy() {
    var userID = gs.getUserID();
    var itemSysID = gs.getProperty('PROPERTY NAME'); //is the sysid of the item
    var obj = {};

    //Variables to autopopulate on the server-side
    obj['who_are_you_requesting_this_for'] = userID;
    obj['requestor'] = userID;

    var ajax = new GlideAjax('FJCatalogUtilsAjax');
    ajax.addParam('sysparm_name', 'createCatalogItem');
    ajax.addParam('sysparm_item_sys_id', itemSysID);
    ajax.addParam('sysparm_array_of_objects', obj);
    ajax.addParam('sysparm_user_sys_id', sysID);
    ajax.getXML(getAnswer);

    function getAnswer(response) {
        var answer = response.responseXML.documentElement.getAttribute("answer");
        answer = (answer == 'false') ? false : answer;

        if(!answer){
            answer = JSON.parse(answer);
            var disMessage = 'created request: ' + answer.number;
            
            gs.addInfoMessage(disMessage);
            action.setRedirectURL(answer.sysid);
            action.setReturnURL(current);
        }else{
            gs.addInfoMessage('There was an error on the Server Side');
        }
}
}


//SI
function createCatalogItem(){
var itemSysID = this.getParameter('sysparm_item_sys_id');
var arrOfObjs = this.getParameter('sysparm_array_of_objects');
var userSysID = this.getParameter('sysparm_user_sys_id');

try{
    arrOfObjs = JSON.parse(arrOfObjs);

    var cart = new Cart();
    var item = cart.addItem(itemSysID); //Refresh a client in stock

    arrOfObjs.forEach(function(obj){
        var variable = Object.keys(obj);
        var value = Object.values(obj);
        cart.setVariable(itemSysID, variable, value);
    })

    var cartGR = cart.getCart();
    cartGR.requested_for = userSysID;
    cartGR.update();
    var newSerReq = cart.placeOrder();
    newSerReq.update();
    
    return {'sysid':newSerReq, 'number':newSerReq.number};
}catch(e){
    gs.log('[FJCatalogUtilsAjax] createCatalogItem: ' + e);
    return false;
}
}
```

## Related

- [[Possible Ways for Making an Attachment Mandatory S]]
- [[Server and Client Script]]
