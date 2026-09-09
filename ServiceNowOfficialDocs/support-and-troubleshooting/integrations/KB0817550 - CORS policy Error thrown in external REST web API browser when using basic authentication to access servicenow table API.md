---
title: "CORS policy Error thrown in external REST web API browser when using basic authentication to access servicenow table API"
aliases:
  - KB0817550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817550
kb_number: KB0817550
last_modified: 2026-08-21
---

## Issue

-   CORS policy Error thrown in the third party web browser, when using the basic authentication in REST API calls without proxy to access the servicenow table API
-   With CORS check disabled via the system property "glide.rest.cors.enabled' = false, access to the Servicenow table API via the external REST web API call without the proxy using basic authentication still fails
-   Error is thrown in the external REST web API browser, though the CORS is bypassed using browser plugin ([Bypass CORS in Browser](https://medium.com/the-crazy-coder/a-comprehensive-understanding-of-cors-all-frontend-developers-better-to-have-3ae46d35f19e "Bypass CORS in Browser"))

Error message in third party client browser:

 'http://localhost:xxxx' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '\*' when the request's credentials mode is 'include'.

Error captured in instance node logs:

2020-02-26 20:01:47 (\*\*) API\_INT-thread-1 SYSTEM txid=\*\*\*\*\*\*\* DEBUG: REST CORS - CORSEvaluator : CORS is disabled via property glide.rest.cors.enabled  
  
2020-02-26 20:01:47 (\*\*) API\_INT-thread-1 SYSTEM txid=\*\*\*\*\*\*\* WARNING \*\*\* WARNING \*\*\* Required HTTP authorization header (Authorization) not present  
  
2020-02-26 20:01:47 (\*\*) API\_INT-thread-1 SYSTEM txid=\*\*\*\*\*\*\*#\*\*\*\*\*\*\* \[REST API\] RESTAPIProcessor : User Not Authenticated

## Resolution

**NOTE:** _Make sure to test everything on sub-production instances before implementing the following recommendation on a production instance_

Setting the property value "glide.rest.cors.enabled" to true and adding the third party domain to the CORS rule in the Servicenow instance are the best practises for resolving this issue

## Additional Information

[Define a CORS rule](https://docs.servicenow.com/csh?topicname=t_DefineACORSRule.html&version=latest)
