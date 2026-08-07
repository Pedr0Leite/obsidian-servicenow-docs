---
title: "Nutanix Pattern Discovery Error 401 - Unauthorized Bad credentials"
aliases:
  - KB0789251
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789251
kb_number: KB0789251
last_modified: 2024-04-07
---

## Nutanix Pattern Discovery Error 401 - Unauthorized Bad credentials

  

### Issue

Nutanix pattern discovery error "401 Unauthorized Bad credentials".

### Release

All currently supported environments.

### Cause

The nutanix pattern makes use of "Nutanix API Query". The "Nutanix API Query" uses MID server script include "NutanixAPIQuery", found in table ecc\_agent\_script\_include.

The NutanixAPIQuery uses the "Basic Auth" credentials to make rest calls to the target IP addresses. Error 401 is returned by the nutanix API. Error 401 means that the basic authentication user does not have access to the API element requested.

### Resolution

Provide at least read-only access to all API elements as listed below:

-   /PrismGateway/services/rest/v2.0/tasks/list
-   /api/nutanix/v3/clusters/list
-   /PrismGateway/services/rest/v2.0/hosts
-   /PrismGateway/services/rest/v2.0/clusters
-   /PrismGateway/services/rest/v2.0/vms
-   /PrismGateway/services/rest/v1/vms
-   /PrismGateway/services/rest/v1/storage\_pools
-   /PrismGateway/services/rest/v2.0/storage\_containers
-   /api/nutanix/v3/categories/list
-   /api/nutanix/v3/categories/{category\_keys}/list
-   /api/nutanix/v3/category/query

The above list is found on document [Nutanix Acropolis discovery.](https://docs.servicenow.com/csh?topicname=nutanix-pattern.html&version=latest "Nutanix Acropolis discovery")

Note: The first request collects a list of clusters from the IP provided. The next queries are done directly to the clusters. Permission may need to be set per cluster.

### Related Links

The "Nutanix REST API" can be used to test permissions, or any REST API tool:

-   [https://portal.nutanix.com/#/page/docs/details?targetId=Web-Console-Guide-Prism-v55:man-rest-api-c.html](https://portal.nutanix.com/#/page/docs/details?targetId=Web-Console-Guide-Prism-v55:man-rest-api-c.html)

The following links may also be helpful:

-   [https://www.nutanix.dev/](https://www.nutanix.dev/)
-   [https://www.nutanix.dev/reference/prism\_element/v2/](https://www.nutanix.dev/reference/prism_element/v2/)
