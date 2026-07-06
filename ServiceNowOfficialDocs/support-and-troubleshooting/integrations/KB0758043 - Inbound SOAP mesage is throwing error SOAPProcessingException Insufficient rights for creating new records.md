---
title: "Inbound SOAP mesage is throwing error \"SOAPProcessingException: Insufficient rights for creating new records\"
aliases:
  - KB0758043
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758043
kb_number: KB0758043
last_modified: 2024-04-26
---

## Issue

Inbound SOAP is throwing the error even for SOAP admin users.

```
"WARNING *** WARNING *** SOAP Fault: <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Header/><SOAP-ENV:Body><SOAP-ENV:Fault><faultcode>SOAP-ENV:Server</faultcode><faultstring>com.glide.processors.soap.SOAPProcessingException: Insufficient rights for creating new records</faultstring><detail>com.glide.processors.soap.SOAPProcessingException: Insufficient rights for creating new records</detail></SOAP-ENV:Fault></SOAP-ENV:Body></SOAP-ENV:Envelope> "
```

## Resolution

\-- After adding "admin" roles, web services calls are going through.

\--  Check for the options in "Customization Properties for Web Services" for the one like :"Enforce strict security on incoming SOAP requests. Checking this requires incoming SOAP requests to go through the security manager for table and field access, as well as checking SOAP users for the correct roles for using the web service"

If this has enabled, you have to disable the same test

\-- You can also directly disable the property "glide.soap.strict\_security" and check and should fix the issue

## Additional Information

Docs: [https://docs.servicenow.com/csh?topicname=c\_SOAPWebService.html&version=latest](https://docs.servicenow.com/csh?topicname=c_SOAPWebService.html&version=latest)
