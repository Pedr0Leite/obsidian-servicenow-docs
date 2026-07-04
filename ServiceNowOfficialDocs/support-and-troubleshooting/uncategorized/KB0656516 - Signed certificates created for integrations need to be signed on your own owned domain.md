---
title: "Signed certificates created for integrations need to be signed on your own owned domain"
aliases:
  - KB0656516
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656516
kb_number: KB0656516
last_modified: 2024-04-26
---

## Signed certificates created for integrations need to be signed on your own owned domain

  

### Issue

Signed certificates created for integrations need to be signed on your own domain  

Problem

* * *

Integrations like Ebonding, Oauth, Web services, and mutual authentication, sometimes require an [asymmetric (private/public) certificates](https://en.wikipedia.org/wiki/Public-key_cryptography "asymmetric (private/public) certificates"). When working with public certificates, these integrations may need them signed by a [Certificate Authority (CA)](https://en.wikipedia.org/wiki/Certificate_authority "Certificate Authority (CA)").  
  
Cause

* * *

Most integrations would only require the SSL connection, for which the public SSL certificate on the instance is enough. However, when an integration needs a public and private key certificate, due to security policies, Servicenow does not provide new signed certificates to be used on integrations.  
  
Resolution

* * *

Customers can work with the public signed certificates available on the instance to integrate using SSL. However, when a private/public certificate is required, customers need to generate these certificates with a **common name (cn)** on a domain owned by them.  

To generate a signed certificate for your integration, you should have the following information:

-   **Common Name:** The fully-qualified domain name, or URL, that you own. **Do not use "\*.service-now.com."**
-   **Organization**: The legally-registered name for your business. If you are enrolling as an individual, enter the certificate requestor's name.
-   **Organization Unit**: If applicable, enter the DBA (doing business as) name.
-   **City or Locality**: Name of the city where your organization is registered/located. Do not abbreviate.
-   **State or Province**: Name of the state or province where your organization is located. Do not abbreviate.
-   **Country**: The two-letter International Organization for Standardization (ISO) format country code for where your organization is legally registered.

After you have the information available, perform the following steps:

1.  Generate a Java Keystore or SSL certificate to be signed.  
    The steps are provided by your Certificate Authority.
2.  Provide the required information to the Certificate Authority.
3.  [Install the signed Java Keystore or SSL certificate on the instance](https://docs.servicenow.com/csh?topicname=t_UploadACertificateToAnInstance.html&version=latest "Install the signed Java Keystore or SSL certificate on the instance"). We recommend **PEM** format for public certificates, and a **storetype jceks** for a java keystore.  
      
    

<table class="noteTable" align="left"><tbody><tr><td class="c3" style="width: 50; vertical-align: middle; text-align: center;"><img class="c2" style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4" style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Request for signed certificate should not be on ".service-now.com." Use a domain your company owns.</td></tr></tbody></table>
