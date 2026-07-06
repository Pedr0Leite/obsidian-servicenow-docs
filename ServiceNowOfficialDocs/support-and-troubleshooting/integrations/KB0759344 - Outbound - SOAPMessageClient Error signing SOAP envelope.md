---
title: "Outbound - SOAPMessageClient : Error signing SOAP envelope"
aliases:
  - KB0759344
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759344
kb_number: KB0759344
last_modified: 2023-08-03
---

## Outbound - SOAPMessageClient : Error signing SOAP envelope

  

### Issue

WS-Security profile for Outbound SOAP Secured Web Service generates the following error for non-admin users:

SEVERE \*\*\* ERROR \*\*\* SOAP Msg Outbound - SOAPMessageClient : Error signing SOAP envelope   
org.apache.ws.security.WSSecurityException: General security error; 

### Cause

The user trying to generate a SOAP request does not have access to the certificate table - /sys\_certificate\_list.do

As part of web service creation, the user will need to use a certificate to sign the request.

### Resolution

Create a Read ACL on the table "sys\_certificate\_list" to allow the non-admin users to access the table.
