---
title: "  \"anonymous user error\"  during kubernetes pattern discovery"
aliases:
  - KB0754946
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754946
kb_number: KB0754946
last_modified: 2025-03-05
---

## "anonymous user error" during kubernetes pattern discovery

  

### Issue

While running kubernetes discovery the below error can be seen in discovery logs:

  
`User \“system:anonymous\” cannot get v1 at the cluster scope”,“reason”:“Forbidden”,“details”:{“name”:“namespaces”,“kind”:“v1”},“code”:403}`

### Release

All

### Cause

OpenShift kubernetes does not support basic authentication. A Bearer Token is required for Authentication.

[https://docs.openshift.com/container-platform/4.10/rest\_api/index.html](https://docs.openshift.com/container-platform/4.10/rest_api/index.html "https://docs.openshift.com/container-platform/4.10/rest_api/index.html")

### Resolution

Kubernetes credentials need to be configured with bearer token option:

[https://docs.servicenow.com/bundle/sandiego-it-operations-management/page/product/service-mapping/concept/kubernetes-discovery.html](https://docs.servicenow.com/bundle/sandiego-it-operations-management/page/product/service-mapping/concept/kubernetes-discovery.html)

### Related Links

If after configuring the credentials and Kubernetes Discovery completes successfully without discovering the Nodes with pattern steps error "Invalid username/password combo", please review this KB: [KB0994019](/kb?id=kb_article_view&sysparm_article=KB0994019)
