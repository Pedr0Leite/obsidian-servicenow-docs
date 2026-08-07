---
title: "Does 'GlideEmailOutbound()' class supports attachments ?"
aliases:
  - KB0789188
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789188
kb_number: KB0789188
last_modified: 2024-04-07
---

## Does 'GlideEmailOutbound()' class supports attachments ?

  

Using the GlideEmailOutbound() class its methods, we can create emails from the scripts.

There are different methods available for adding the Recipients, CC, subject, body, watermark etc...

Eg:-

var mail = new GlideEmailOutbound();  
mail.addAddress('cc', '123@123.com');  
mail.addRecipient("abc@abc.com");  
mail.setSubject("Test Email");  
mail.save();

More info: [https://developer.servicenow.com/app.do#!/api\_doc?v=newyork&id=c\_GlideEmailOutboundScopedAPI](https://developer.servicenow.com/app.do#!/api_doc?v=newyork&id=c_GlideEmailOutboundScopedAPI)

**There will be a question about how to add an attachment ?**

Answer: As of now there is no attachment manipulation is available in GlideEmailOutbound from scripting layer.
