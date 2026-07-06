---
title: "Scripted Web Service uses var cart = new Cart(); and some records are not created as expected when making multiple calls in a short period of time"
aliases:
  - KB0789957
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789957
kb_number: KB0789957
last_modified: 2025-08-28
---

## Scripted Web Service uses var cart = new Cart(); and some records are not created as expected when making multiple calls in a short period of time

  

### Issue

Several inbound web service calls are made into a scripted web service in a short period of time.  For some of the calls the expected record is not created (sc\_request table) and no record number is returned to the client.

The following is seen for some of the calls in the node logs:

2019-12-17 12:05:52 (488) API\_INT-thread-4 F9F5A2D5DBF5849026A25C77DC96190B txid=f1f5a2d5dbf5 \*\*\* Script: Can not checkout empty cart  
2019-12-17 12:05:52 (489) API\_INT-thread-4 F9F5A2D5DBF5849026A25C77DC96190B txid=f1f5a2d5dbf5 \*\*\* Script: CP Submit API: {}

The scripted web service uses the Cart API, e.g.:

var cart = new Cart();

### Release

NA

### Cause

A race condition is created by calling the Cart API multiple times for the same user in a short period of time.

### Resolution

To resolve this issue consult this blog post:

[https://community.servicenow.com/community?id=community\_blog&sys\_id=38ccee25dbd0dbc01dcaf3231f961977](https://community.servicenow.com/community?id=community_blog&sys_id=38ccee25dbd0dbc01dcaf3231f961977)

The current coding is causing a race condition, i.e.:

var cart = new Cart();  
  
You will need to follow that blog and create a unique cart ID:  
  
var cart = new Cart(generateId());  
  
OR  
  
var cartId = GlideGuid.generate(null);  
var cart = new Cart(cartId);
