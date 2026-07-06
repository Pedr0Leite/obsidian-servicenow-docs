---
title: "Outbound REST Message fails with \"Socket Error\" when the endpoint requires SNI support"
aliases:
  - KB0815903
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815903
kb_number: KB0815903
last_modified: 2024-04-08
---

## Outbound REST Message fails with "Socket Error" when the endpoint requires SNI support

  

### Issue

Outbound REST Message fails with "Socket Error" when the endpoint requires SNI support

Here's how you can use openssl to validate if the endpoint requires SNI support:

Run the folllowing command:  
openssl s\_client -state -debug -connect api.provider.com:443

If api.provider.com utilizes and requires SNI, you’ll see output similar to this (note the error: SSL3 alert read:fatal:handshake failure):

SSL\_connect:SSLv2/v3 write client hello A  
read from 0x7fc699703c80 \[0x7fc69b806600\] (7 bytes => 7 (0x7))  
0000 - 15 03 01 00 02 02 28B B B B B B B B B B B B B B B B B B B B B B B B B B B B B ……(  
SSL3 alert read:fatal:handshake failure  
SSL\_connect:error in SSLv2/v3 read server hello A

### Release

SNI support is available in ServiceNow from the Jakarta version onwards.

### Cause

The end point requires SNI support from the client and on the instance the support for SNI is disabled.

That is **glide.outbound.tls\_sni.enabled** is set to false

### Resolution

To enable SNI on the instance create a system property named **glide.outbound.tls\_sni.enabled** and set the value to **true**.

### Related Links

See the below article for a good explanation on SNI and when to enable it on the instance:

[Endabling SNI - Service Name Indication on the ServiceNow instance](https://developer.servicenow.com/blog.do?p=/post/enabling-sni-server-name-indication-in-your-jakarta-instance/ "Endabling SNI - Service Name Indication on the ServiceNow instance")
