---
title: "Sharing cookie between 2 domains"
aliases:
  - KB0787412
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787412
kb_number: KB0787412
last_modified: 2024-04-08
---

## Sharing cookie between 2 domains

  

### Issue

We have 2 URLs [https://aaaa.com](https://aaaa.com) [https://bbbb.com](https://bbbb.com) Both are pointing to the same instance (for example, one to the old CMS the other to the Service Portal).

Customers could want to achieve the functionality to help user’s login to one domain if they are logged on to the other and vice versa.

### Release

All releases

### Cause

ServiceNow does not support sharing cookies between instances, even if it is possible as it could be unsafe for our customers to read cookies between all instances.

### Resolution

Just in case, if it is needed to share cookies across subdomains it is required need to scope the cookie at the domain level (e.g. .example.com). It applies when you want the cookie is available to all the subdomains of .example.com

Most modern browsers adhere to a defined "web security model". The model effectively governs the behaviour of browsers with regards to security, on things like cookies (specifically how they will be sent back to any given website). The model also has the rule that "browsers don't send cookies to domain names that didn't set them."

That being said, domain.com should be able to set cookies for js.domain.com. js.domain.com, however, can only set cookies for itself. But this is all depending on what browser you're using.

Additionally, if you want to create a simple authentication portal to pass an unencrypted HTTP header as a cookie. Here is official documentation link:

[https://docs.servicenow.com/csh?topicname=r\_ASPNETCSharpRdrctCks.html&version=latest](https://docs.servicenow.com/csh?topicname=r_ASPNETCSharpRdrctCks.html&version=latest)
