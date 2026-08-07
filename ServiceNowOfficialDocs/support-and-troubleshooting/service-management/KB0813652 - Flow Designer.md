---
title: "Flow Designer"
aliases:
  - KB0813652
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813652
kb_number: KB0813652
last_modified: 2024-04-08
---

## Flow Designer

  

### Issue

-   Receiving the value from a glide\_list in the flow designer. Flow designer which handles users from being active=true to active=false and then the flow should remove the user where they added in the field "reviewer" (glide\_list).

### Release

-   NY Patch 4 Hotfix 1

### Cause

-   The field u\_reviewer is of type glide\_list. If you reference it this way (u\_reviewer.toString), it will just return the Sys ID. It's not a simple text field, it's a field referencing another table (sys\_user). To get the values you need to reference the object and loop through this.

### Resolution

-   You can use the following code to get the value from the reviewer/watchlist field.
-   var gr = new GlideRecord('kb\_knowledge');  
    gr.get('2c057fc31bb544d0979ca688bd4bcb6d');  
    gs.log("Referencing u\_reviewer: " + gr.u\_reviewer.toString());  
    var listReviewer = gr.u\_reviewer.getDisplayValue();  
    gs.log("listReviewer: " + listReviewer);  
    var arrReviewer = listReviewer.split(',');  
    for (var i=0; i<arrReviewer.length; i++) {  
    gs.log('Value ' + (i+1) + ': ' + arrReviewer\[i\]);  
    }
