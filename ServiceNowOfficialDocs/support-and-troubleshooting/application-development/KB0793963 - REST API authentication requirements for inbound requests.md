---
title: "REST API authentication requirements for inbound requests"
aliases:
  - KB0793963
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793963
kb_number: KB0793963
last_modified: 2026-01-28
---

## REST API authentication requirements for inbound requests

  

### Issue

Learn the authentication requirements for running inbound REST API calls to a ServiceNow instance. This article covers Basic Authentication, OAuth token authentication, and supported request headers. 

### Release

All supported releases

### Resolution

### Authentication methods

Inbound REST API calls to a ServiceNow instance support the following authentication methods:

#### **Basic Authentication**

Basic Authentication uses a local user name and password to authenticate when the REST call runs. The user account must exist in the User \[sys\_user\] table.

#### **OAuth token authentication**

As an alternative to Basic Authentication, you can use OAuth token authentication for inbound REST calls.

### Supported request headers

For most ServiceNow REST APIs, the following request header values are supported:

| Header | Supported values |
| --- | --- |
| Accept | application/json, application/xml |
| Content-Type | application/json, application/xml |

For the specific values supported by each endpoint, see the [REST API reference](https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/build/applications/concept/api-rest.html).

  
  
  
  
  
  

### Related Links

[REST API reference](https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/build/applications/concept/api-rest.html "https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/build/applications/concept/api-rest.html")
