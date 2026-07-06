---
title: "Inbound SOAP API connection returns 302 error"
aliases:
  - KB0749537
  - Inbound SOAP API connection returns 302 error
tags:
  - servicenow
  - support-kb
  - soap
  - inbound-integration
  - sso-redirect
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749537
kb_number: KB0749537
last_modified: 2025-11-05
---

## Inbound SOAP API connection returns 302 error

  

### Issue

Inbound SOAP API call to the instance returns a response code of 302. 

### Release

ALL

### Cause

The resource path is incorrect. Request to the instance comes in like this:  
uri=/table\_name.do?SOAPchange.do?SOAP&displayvalue=all

System will process it as a SOAP request only when SOAP query parameter is sent. However, the 2 query parameters sent are:  
SOAPchange.do?SOAP=  
displayvalue=all

This is why this request is treated as a UI transaction and is redirected to the SSO login page with a response code of 302

### Resolution

Make sure the end point is in the correct format. It should be /table\_name.do?SOAP&displayvalue=all

## Related

- [[KB0748481 - How to use custom WSDL for Inbound SOAP requests to ServiceNow]]
- [[c_SOAPWebService|SOAP web service]]
