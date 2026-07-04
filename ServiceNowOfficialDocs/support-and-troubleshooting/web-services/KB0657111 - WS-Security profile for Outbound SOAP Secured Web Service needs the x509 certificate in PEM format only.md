---
title: "WS-Security profile for Outbound SOAP Secured Web Service needs the \"x509 certificate\" in PEM format only"
aliases:
  - KB0657111
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657111
kb_number: KB0657111
last_modified: 2024-04-07
---

## WS-Security profile for Outbound SOAP Secured Web Service needs the "x509 certificate" in PEM format only

  

### Issue

WS-Security profile for Outbound SOAP Secured Web Service needs the "x509 certificate" in PEM format only

Problem

* * *

WS-Security profile for Outbound SOAP Secured Web Service allows to create "x509 certificate" in both CER and PEM format.

Symptoms

* * *

If a customer creates or update a WS-Security profile for Outbound SOAP Secured Web Service with a "x509 certificate" other than PEM, they could receive the following errors on the system logs or in the localhost:

-   Error signing SOAP envelope: java.io.IOException: Invalid keystore format: sun.security.provider.JavaKeyStore.engineLoad
-   SOAP Msg Outbound - SOAPMessageClient : Error executing SOAP request: Error signing SOAP envelope
-   Unable to extract Key from KeyStore: com.glide.certificates.DBKeyStoreFactory.getPrivateKeyFromKeyStore

Cause

* * *

WS-Security assumes the certificate is encoded in PEM format and it could not retrieve it

Resolution

* * *

Please perform the following actions to resolve your problem.

To accomplish action A:

1.  Export from the keystore the new certificate used by the secure WS, in PEM format . You will need to know the certificate alias for this operation or  
    if you have a cer X509 certificate, you could convert it as follow:  
    \> openssl x509 -inform der -in certificate.cer -out certificate.pem
2.  Import into ServiceNow the new provided keystore. We recommend in PKCS12 format.
3.  Import into ServiecNow the new x509 certificate in PEM format.
4.  Modify the WS security X509 Outbound profile for this WS call to correctly point to: a) the new keystore record, b) the new certificate record , and c) the certificate alias.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: WS-Security only allows X509 certificates in PEM format to be used.</td></tr></tbody></table>
