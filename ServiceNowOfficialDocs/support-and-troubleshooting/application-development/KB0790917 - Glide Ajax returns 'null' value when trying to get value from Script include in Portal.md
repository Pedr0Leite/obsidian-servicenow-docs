---
title: "Glide Ajax returns 'null' value when trying to get value from Script include in Portal"
aliases:
  - KB0790917
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790917
kb_number: KB0790917
last_modified: 2026-06-22
---

## Glide Ajax returns 'null' value when trying to get value from Script include in Portal

  

### Issue

Returning a message that contains an "emoji" character from Script Includes using "Glide Ajax" shows null value when the response is used in a Client Script.

### Release

All releases.

### Cause

The script include is returning the results but results are in incorrect JSON format thus causing the page to not parse them. Further, the issue is maybe causing due to the presence of emoji's in the activities.

### Resolution

Using escape and unescape for the message to display the emoji will fix the issue.  
The fix is implemented in Script include and client scripts.  
  
Example Below:  
  
`In Script include:`  
  

```
var testAjax = Class.create();testAjax.prototype = Object.extendsObject(AbstractAjaxProcessor, {getEmojis: function () {var result = this.newItem("result");result.setAttribute("message", escape("my 👍 means good."));},type: 'testAjax'});
```

  
`In Client Script:`  
  

```
function asd(serverResponse) {var result = serverResponse.responseXML.getElementsByTagName("result");var message = result[0].getAttribute("message");if(message) alert(unescape(message));}var ga = new GlideAjax("testAjax");ga.addParam("sysparm_name","getEmojis");ga.getXML(asd);
```
