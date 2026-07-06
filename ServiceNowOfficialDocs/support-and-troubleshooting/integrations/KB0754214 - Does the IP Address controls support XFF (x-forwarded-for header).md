---
title: "Does the IP Address controls support XFF (x-forwarded-for header)"
aliases:
  - KB0754214
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754214
kb_number: KB0754214
last_modified: 2024-06-27
---

## Does the IP Address controls support XFF (x-forwarded-for header)

  

### Issue

It is possible to configure IP Access Control in the platform. Some of our customers requested if it would also be possible to use XFF (X-Forwarded-For header) to be set on redirected requests.

### Release

All

### Cause

XFF is applicable in a highly secure environment where IP Access Control is enabled.

### Resolution

XFF (X-Forwarded-For header) for IP authentication is supported for instances that are not using ADC Load Balancers.

[KB1648260 - XFF (X-Forwarded-For) header considerations for instances behind ADC Load Balancer](/kb?id=kb_article_view&sysparm_article=KB1648260)

If instance is not using ADC Load Balancer or on-premise then the below logic applies.

If XFF contains multiple IPs, then:

\- If any of the IPs are on the allow list, then access is allowed  
\- Otherwise, if any of the IPs are on the deny list, then access is denied  
\- Else if no matches then access is allowed
