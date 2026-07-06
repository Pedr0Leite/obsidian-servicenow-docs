---
title: "Discovery updates CI of \"name\" field with FQDN and \"ip_address\" field with WLAN IP"
aliases:
  - KB0759309
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759309
kb_number: KB0759309
last_modified: 2024-04-07
---

## Issue

-   Discovery towards the IP Switch updates the CI of "name" field with "FQDN" and "ip\_address" field with WLAN IP.

![](sys_attachment.do?sys_id=f73cc8bcdb08b0d0fec4fb2439961980)

## Resolution

-   In order to resolve this issue, set the below 2 properties to "false"

1.  glide.discovery.hostname.include\_domain
2.  glide.discovery.enforce\_ip\_sync

-   Once set rerun the discovery and CI gets updated with right values.

![](sys_attachment.do?sys_id=7f3cc8bcdb08b0d0fec4fb2439961981)
