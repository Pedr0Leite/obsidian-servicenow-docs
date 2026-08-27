---
title: "Outbound REST API call Fails With Error:  Response: [ERROR CODE: -1 ] No issuer certificate found for <endpoint hostname>"
aliases:
  - KB0760206
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760206
kb_number: KB0760206
last_modified: 2026-01-12
---

## Issue

Running an outbound REST API call integration that requires the use of a custom SSL certificate fails with the error:

Response: \[ERROR CODE: -1 \] No issuer certificate found for <endpoint hostname>  
  
Steps to Reproduce:

1.  Run an outbound REST integration that calls a custom SSL certificate   
    2\. Look at the Outbound HTTP Requests, note the error

## Resolution

There are two options to resolve this: 

1.  Clean up the endpoint so that the certificate chain is complete and there are no more certificate errors seen when executing the:  
    openssl s\_client -connect <endpoint hostname or IP address>:<port> -showcerts  
      
    
2.  To ignore these certificate errors (i.e. remove the tighter certificate standards) add this system property to the instance:  
    Name: **com.glide.communications.httpclient.verify\_revoked\_certificate**   
    Type: **true | false**   
    Value: **false**
