---
title: "ServiceMapping IP lookup mechanism in the host detection phase"
aliases:
  - KB0725711
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725711
kb_number: KB0725711
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

During the host detection phase for Service Mapping discovery, the system checks if the host being scanned is present in the CMDB. Service Mapping first starts by querying **"cmdb\_ci"** table, where "ip\_address" field is equal to the IP of the host. This will query all the child tables for **"cmdb\_ci"**, so in that case, both the host records and **"cmdb\_ci\_ip\_address"** records (associated with the host record) can match. If they are both valid (install\_status=1, operational\_status=1, discovery\_source is valid etc), we simply choose the first one.

  

#   

# Additional Information

* * *

This behavior cannot be customized as the host detection script is implemented in the Java code.
