---
title: "SSL certificate of the instance for third party integration"
aliases:
  - KB0788812
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788812
kb_number: KB0788812
last_modified: 2026-06-14
---

## SSL certificate of the instance for third party integration

  

### Summary

How to get SSL certificate of the instance to setup an Integration with 3rd party tool.

### Release

Any

### Instructions

Using OpenSSL command we can get the SSL certificate.

  
openssl s\_client -connect instancename.service-now.com:443 -showcerts
