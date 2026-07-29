---
title: "SSL/TLS encryption on instances"
aliases:
  - KB0563633
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563633
kb_number: KB0563633
last_modified: 2026-04-30
---

## SSL/TLS encryption on instances

  

### Issue

Protecting the security and privacy of our customers is among our top priorities, so ServiceNow utilizes SSL/TLS to encrypt communications for all customer instances. In order to continue to provide best-in-class protection, we regularly renew our certificates used for SSL/TLS encryption. A short lifespan for SSL certificates reduces our exposure window and also gives us greater flexibility to deal with unforeseen security issues. Since so many recent headlines have featured exposures in the SSL protocol and the surrounding technologies (Heartbleed, POODLE, root CA compromises, unauthorized disclosures) ServiceNow views this as a necessary step in order to stay ahead of current and future threats.

### Regarding SSL certificate changes

-   ServiceNow currently rotates/renews its certificates every 6 months, and provides 14-day notification of this activity**.** This is an industry best practice and it enables ServiceNow to provide improved security for our customers.
-   It is recommended that customers and their third party systems should trust the root certificate provided by our certificate vendor, Digicert, instead of hard-coding an existing ServiceNow certificate and having to change that manually when the certificate itself is renewed.
-   Due to Google's [announcement](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1702083) that certificates issued by Entrust will no longer be accepted by Chrome browsers, ServiceNow will be issuing the new certificate for instances (also known as \*.service-now.com certificate or the wildcard certificate) from Digicert instead of Entrust. It is recommended that customers and their third party systems should be configured to also trust the root certificates from Digicert to ensure a seamless transition. 

### Determining if your instance is affected by the regular 6 month certificate update 

All customers utilizing the ServiceNow web application use the new SSL certificate, but for the most part, this is a transparent change.

The only customers likely to require manual intervention are those who have integrations, caching or proxy servers that have hard-coded the current ServiceNow SSL certificate (and/or its intermediate and root certificates).

-   Some inbound integrations (services connecting to your ServiceNow instance) may have the current SSL certificate hard-coded. Contact the service owner of any integration that connects to your ServiceNow instance to verify that it will properly handle the SSL certificate change. Please note that it is technically impossible for ServiceNow to determine which 3rd party systems connecting to an instance have hardcoded the current certificate. This is similar to a user saving a password in their browser, it is only possible to check if the password they provided is correct or not, it is not possible to determine how that password is kept. 
-   If you access your ServiceNow instance by a URL other than https://<instance-name>.service-now.com/ or other than a Custom URL deployed through your instance (see [here](https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/integrate/authentication/concept/custom-url.html "Custom URL documentation")), you may be accessing your instance through a proxy. Please contact your IT department or network administrator to verify that the proxy can handle the SSL certificate change properly.

Normal web browsers like Internet Explorer, Firefox, Chrome, or Safari are **NOT** affected.

Inbound certificate based authentication for MID servers are **NOT** affected as all related certificates for this functionality should be created and maintained by customers.

#### Preparing for SSL certificate upgrade

-   Use updated web browsers and maintain software patch levels.
-   Read the information provided by ServiceNow and communicate this change to any members of your organization who could be affected.
-   **ServiceNow recommends not hardcoding the ServiceNow certificate. Hardcoded certificates will likely cause interrupted access during a certificate change until the old certificate is manually replaced by the new and correct certificate.**

### Facts

You may review the existing certificate information by using the following comments:

openssl s\_client -tls1\_3 -connect <instancename>.service-now.com:443

openssl s\_client -tls1\_2 -connect <instancename>.service-now.com:443

Please note that the tls 1\_3 version will only return successful results if TLS 1.3 is available for the instance.

### Release

All releases.

### Resolution

#### Obtaining Help for SSL Certificate Changes

If you believe there is a problem with the SSL certificate change, please contact [ServiceNow Technical Support](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260 "ServiceNow Technical Support"). Please note that Support cannot help you in determining which third-party systems may be affected as it is technically impossible for ServiceNow to determine which 3rd party systems connecting to an instance have hardcoded the current certificate.

#### SSL Certificates

If you have determined that you might be impacted by the SSL certificate change, please create a Case for support. In order to not be affected by the certificate rotation, we suggest you add both the existing \*.service-now.com certificate and the upcoming \*.service-now.com certificate to the trust store of your third party applications.

Digicert Root CA will be available on most of the trust stores and browsers. In case you need the root CA please download from digicert [\- Digicert Root CA.](https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem?_gl=1*12xh6b*_gcl_au*MTUwMzA1Mzg2MS4xNzMxNDU1MDgw)

### Related Links

Related KBs:  
[How to determine where your data center is hosted? - KB0538621](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538621)

[OCSP requirements for MID servers for Entrust & Digicert - KB1709661](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1709661)

[ServiceNow Replacing Entrust Certificate Authority (CA) - KB1702083](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1702083) (this change was completed early 2025)
