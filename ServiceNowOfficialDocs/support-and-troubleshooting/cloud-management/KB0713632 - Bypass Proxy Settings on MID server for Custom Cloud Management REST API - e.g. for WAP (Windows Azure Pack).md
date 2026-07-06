---
title: "Bypass Proxy Settings on MID server for Custom Cloud Management REST API - e.g. for WAP (Windows Azure Pack) "
aliases:
  - KB0713632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713632
kb_number: KB0713632
last_modified: 2024-04-07
---

## Bypass Proxy Settings on MID server for Custom Cloud Management REST API - e.g. for WAP (Windows Azure Pack)

  

### Issue

# Description

* * *

To build custom Cloud Management API, it's necessary extend MID Server Script Include CloudRESTAPIInvoker, as in its description:

Abstracted class for making REST API calls. Classes that implement this need to extend this object and provide overrides for getEndpointUrl to return the targeted endpoint, and for getHeaders and/or getParameters if there are headers and/or parameters to send with a request.  
  
  
CloudRESTAPIInvoker uses another MID Server Script Include CloudAPIBase to check if MID server is configured with proxy.   
If MID server is using proxy, then the Custom API is forced to use proxy as well, by default.  
This may break custom implementation like WAP (Windows Azure Pack), where the API is pointing to local servers, and the connection should not be going through web proxy.

# Workaround

* * *

Create a new MID Server Script Include based on CloudRESTAPIInvoker, but without the proxy section starting at line: 

if (cloudApiBase.\_useProxy()) {

Also make sure to update the first two lines and the second last line to reflect new script include name.

Then, build custom API to extend this new file.
