---
title: "Consumer Registration page shows \"Error processing request\""
aliases:
  - KB0870375
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870375
kb_number: KB0870375
last_modified: 2025-02-20
---

## Issue

When utilizing the consumer registration portal page (/sp?id=csp\_registration), the "Error processing request" shows upon submitting the registration.

The registration attempt uses a valid email address. The instance logs show the following:

org.mozilla.javascript.EvaluatorException: GlideRecord.addQuery() - invalid table name: sn\_customer\_communities\_user (sys\_script\_include.c3013c653b0b3200b5c42479b3efc496.script; line 487)  
EvaluatorException(JavaScript evaluation error on:  
new sn\_ext\_usr\_reg.ExternalUserManagmentUtils(PORTAL\_ID).registerUser(JSON.parse(REQUEST\_OBJ));  
)

## Resolution

Activate the Customer Communities plugin (com.sn\_customer\_communities).
