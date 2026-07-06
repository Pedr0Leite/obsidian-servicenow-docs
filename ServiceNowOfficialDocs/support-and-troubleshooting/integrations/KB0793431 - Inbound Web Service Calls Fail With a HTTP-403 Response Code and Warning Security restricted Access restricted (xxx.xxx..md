---
title: "Inbound Web Service Calls Fail With a HTTP-403 Response Code and Warning: Security restricted: Access restricted (xxx.xxx.xxx.xxx not authorized)"
aliases:
  - KB0793431
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793431
kb_number: KB0793431
last_modified: 2024-04-08
---

## Inbound Web Service Calls Fail With a HTTP-403 Response Code and Warning: Security restricted: Access restricted (xxx.xxx.xxx.xxx not authorized)

  

### Issue

A web service client makes inbound calls to a ServiceNow instance.  The client receives a HTTP-403 response code.  Checking the instance node logs for the time of the failed call shows a warning message like this:

2020-01-15 10:46:46 (659) http-46 WARNING \*\*\* WARNING \*\*\* Security restricted: Access restricted (xxx.xxx.xxx.xxx not authorized)

Where xxx.xxx.xxx.xxx is an IP address.

The web service client can confirm their external IP address by going to this site - in this scenario the IP address shown at the site will match the IP address shown in the log warning message:

[https://whatismyipaddress.com/](https://whatismyipaddress.com/)

### Release

Applies to all releases.

### Cause

"IP Address Access Controls" are in use and are not allowing access for the IP address shown in the log message.

[https://docs.servicenow.com/csh?topicname=c\_IPRangeBasedAuthentication.html&version=latest](https://docs.servicenow.com/csh?topicname=c_IPRangeBasedAuthentication.html&version=latest)

### Resolution

If you want to give access to the user making these calls be sure that their IP address is allowed in "IP Address Access Controls".
