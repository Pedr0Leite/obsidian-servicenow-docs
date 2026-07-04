---
title: "Not able to edit/checkout a knowledge article - \"Uncaught DOMException: Blocked a frame with origin \"https://xxxxxxx.service-now.com\" from accessing a cross-origin frame.\".  "
aliases:
  - KB0785012
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785012
kb_number: KB0785012
last_modified: 2026-06-24
---

## Not able to edit/checkout a knowledge article - "Uncaught DOMException: Blocked a frame with origin "https://xxxxxxx.service-now.com" from accessing a cross-origin frame.". 

  

### Issue

You are unable to edit or checkout an knowledge article, Edit/Checkout.  
When you attempt this, you will get connection timeout error, the connection was reset.  
  
In browser console you see the below error:  
  
"Uncaught DOMException: Blocked a frame with origin "https://xxxxxxx.service-now.com" from accessing a cross-origin frame.".   
Which is followed by error "TypeError: Cannot read property 'location' of null".  
  
This happens consistently when attempting to checkout some Articles.

### Release

All

### Cause

The issue is the size of the KB. The max field size for the Article Text field is 65k, your KB is over 1 million characters.

### Resolution

  
You need to review the Articles where you experience this error and review the content within the Article Text field.

It maybe necessary to export the Article out of the instance to edit it's content.  
You might want to consider adding some of the content to Word documents and added as attachments to the KB Article.
