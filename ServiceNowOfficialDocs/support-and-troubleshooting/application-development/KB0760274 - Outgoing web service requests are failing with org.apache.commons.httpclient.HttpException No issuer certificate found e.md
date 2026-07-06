---
title: "Outgoing web service requests are failing with \"org.apache.commons.httpclient.HttpException: No issuer certificate found <endpoint FQDN or certificate subject>\" error against an endpoint which is configured with self-signed or expired certificate."
aliases:
  - KB0760274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760274
kb_number: KB0760274
last_modified: 2024-04-08
---

## Outgoing web service requests are failing with "org.apache.commons.httpclient.HttpException: No issuer certificate found " error against an endpoint which is configured with self-signed or expired certificate.

  

### Issue

When you're doing tests against a secure endpoint (https), which is configured for a **self-signed**, **expired**, or **issuer-broken certificate**, your requests might fail even if you have set the "**com.glide.communications.trustmanager\_trust\_all**" system property to "**true**" and the "**com.glide.communications.httpclient.verify\_hostname**" system property to "**false**" on a New York instance.

This might be valid for both SOAP, REST, and even any other kind of connection which would use secure HTTP (HTTPS) protocol.

### Release

New York and onwards.

### Cause

There is a recent change on New York release for a fix to a known problem about outgoing HTTP requests, and this change is causing the previously configured scenarios to fail.

  

Previously, when the "**com.glide.communications.httpclient.verify\_hostname**" system property was set to "**false**", it was implicitly evaluating the value of "**com.glide.communications.httpclient.verify\_revoked\_certificate**" system property value as "**false**", but with the recent change on the New York release, it needs to be explicitly set.

### Resolution

In addition to setting "**com.glide.communications.httpclient.verify\_hostname**" system property to "**false**", and setting the "**com.glide.communications.trustmanager\_trust\_all**" system property to "**true**", please create/set the value of "**com.glide.communications.httpclient.verify\_revoked\_certificate**" system property (type: **true | false**) to "**false**".

**Caution:** Trusting all certificates and accepting revoked/expired certificates is a dangerous and risky operation, and shouldn't be carried out on production instances. If outgoing secure HTTP connections are an issue on your production instance, then the ultimate solution is to install a valid, and trusted certificate on the **external** endpoints, which might be managed by a different administrator.

### Related Links

Additional validation against the endpoint can also be performed by running the following command where curl command is installed. If the below error message is observed, then SSL handshake can not be completed:

  

```

$ curl --verbose https://<REPLACE_WITH_FQDN_OF_ENDPOINT>/

* Trying ...
* TCP_NODELAY set
* Connected to <FQDN_OF_ENDPOINT> (<IP_ADDRESS>) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
* CAfile: /etc/ssl/cert.pem
CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to <FQDN_OF_ENDPOINT>:443 
* stopped the pause stream!
* Closing connection 0
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to <FQDN_OF_ENDPOINT>:443
```
