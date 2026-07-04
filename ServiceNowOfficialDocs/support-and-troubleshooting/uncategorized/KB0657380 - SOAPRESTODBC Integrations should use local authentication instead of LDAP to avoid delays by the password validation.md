---
title: "SOAP/REST/ODBC Integrations should use local authentication instead of LDAP to avoid delays by the password validation"
aliases:
  - KB0657380
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657380
kb_number: KB0657380
last_modified: 2024-04-07
---

## SOAP/REST/ODBC Integrations should use local authentication instead of LDAP to avoid delays by the password validation

  

### Issue

When users connect to an instance, ServiceNow authentication follows the Authentication mechanisms available.  
**However, the LDAP authentication could cause additional overhead** (for example, some latency between the instance and the LDAP server), especially if the amount of requests are significant on integration users.

The following example uses SOAP UI, for a 'get' operation using /incident.do?SOAP on the very same record.  
  
With a user authenticating **with local credentials**:

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><br></td><td style="vertical-align: middle; text-align: left;">Mon Dec 11 19:21:03 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 208ms (502 bytes)<br>Mon Dec 11 19:21:04 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 211ms (502 bytes)<br>Mon Dec 11 19:23:05 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 209ms (502 bytes)<br>Mon Dec 11 19:24:50 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 210ms (502 bytes)<br>Mon Dec 11 19:27:51 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 213ms (502 bytes)<br>Mon Dec 11 19:29:18 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 209ms (502 bytes)</td></tr></tbody></table>

  

  

  

  

  

That is an average of 210 ms. Note the times are consistent.

With a user authenticating **via**

**LDAP server gives a different performance**:

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><br></td><td style="vertical-align: middle; text-align: left;">Mon Dec 11 20:15:30 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 2034ms (502 bytes)<br>Mon Dec 11 20:15:46 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 719ms (502 bytes)<br>Mon Dec 11 20:15:54 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 685ms (502 bytes)<br>Mon Dec 11 20:18:11 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 927ms (502 bytes)<br><strong>Mon Dec 11 20:19:14 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in <span style="color: #ff0000;">3131ms</span> (502 bytes)</strong><br>Mon Dec 11 20:19:40 GMT 2017:INFO:Got response for [ServiceNowSoap.get:Request 1] in 1010ms (502 bytes)</td></tr></tbody></table>

  

  

  

  

  

  

  

That is an average of 1418 ms. Note the times are not consistent and it has an extra 1208 ms.  

  

  

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp; Some operations will use the authentication cached data. However, after a few minutes, the delay is again visible. You can force the delay by performing a /cache.do on the instance.</td></tr></tbody></table>

  

  

You will recognize this problem because:

-   The user record on the sys\_user table has the source field defined with value starting with "ldap:"
-   Integrations using this user have a longer response times and, for the same data, times are not consistent.
-   Some inbound integrations like Web Services could **timeout** even when the instance does not have outages, for example, **java.net.SocketTimeoutException: Read timed out.**
-   These integrations timing out will not appear on the transaction logs.
-   Integration could show errors of invalid passwords even if the password has not changed or looks valid.
-   You could see 'read timeout' or general timeouts (for example, LDAP: connection timeout) on the instance logs from calls to the LDAP Server, especially from the LDAP monitoring system.
-   Some integrations start queuing up and causing contention on the semaphores available on the API queue from the instance.

### Cause

External authentication requires a call to the external LDAP server to validate the user password. If the connection times out or has a delay, the validation can take up to the timeout set on the [LDAP connection properties](https://docs.servicenow.com/csh?topicname=t_ConfigureLDAPConnectionMonitoring.html&version=xxx "LDAP connection properties").

### Resolution

Ensure that users used on integrations are using local authentication instead of LDAP authentication. If you still want to use a local database, ensure the sys\_user.source field is empty or does not start with "ldap:"

![Clear the source and set the password to avoid LDAP authentication](sys_attachment.do?sys_id=07c8e06edb02b450e515c2230596197d "Clear the source and set the password to avoid LDAP authentication")

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Clear the source field and set the user password to start using the local authentication. Also ensure the user is not refreshed by the LDAP server, otherwise, the Source will be reset on the next LDAP update.<br></td></tr></tbody></table>
