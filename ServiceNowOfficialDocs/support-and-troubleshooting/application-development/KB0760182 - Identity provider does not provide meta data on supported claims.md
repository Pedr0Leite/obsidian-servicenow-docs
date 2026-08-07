---
title: "Identity provider does not provide meta data on supported claims"
aliases:
  - KB0760182
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760182
kb_number: KB0760182
last_modified: 2024-04-08
---

## Identity provider does not provide meta data on supported claims

  

### Issue

While registering OIDC provider, the configuration fails with error “Identity provider does not provide metadata on supported claims. Cannot confirm these required claims: aud, iss, and {0} "

  

![](sys_attachment.do?sys_id=6af52378db0078d022e0fb2439961995)

  

  

### Release

London, Madrid

### Cause

Below are the mandatory claims which are supposed to be sent included in metadata configuration

1.  iss
2.  aud
3.  user claim

Some OIDC providers does not declare these claims in well-known url page.

### Resolution

1\. Configure the OIDC provider to provide the mentioned mandatory claims
