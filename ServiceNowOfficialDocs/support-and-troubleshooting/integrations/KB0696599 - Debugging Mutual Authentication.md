---
title: "Debugging Mutual Authentication "
aliases:
  - KB0696599
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696599
kb_number: KB0696599
last_modified: 2026-03-03
---

## Debugging Mutual Authentication

  

### Issue

# Mutual Authentication Debugging

* * *

Please follow Resolution steps when debugging Mutual Authentication

### Release

ANY

### Resolution

# Mutual Authentication Debugging

* * *

Please follow these steps when debugging Mutual Authentication:

1.  Validate protocol profile is setup correctly, e.g "myhttps" and port is "443"
2.  Convert the given format of the keystore to **p12**.  
    -   From pfx to p12:  
        -   keytool -importkeystore -destkeystore newCustomer.p12 -deststoretype pkcs12 -srckeystore "name.pfx"
3.  Extract public cert from this P12:  
    -   keytool -export -alias "<alias\_from\_p12>" -keystore newCustomer.p12 -rfc -file publicCert.cert
4.  Extract private key from this P12:  
    -   openssl pkcs12 -in newCustomer.p12 -nodes -nocerts -out private.pem # alterantively run this to see full output, if no "-----BEGIN PRIVATE KEY" line is seen then the private key is missing and the customer needs to regenerate a new key pair following our documentation:  openssl pkcs12 -info -in newCustomer.p12 -nodes -nocerts
5.  Try connecting via OPENSSL:  
    -   openssl s\_client -connect <Destination\_IP>:<PORT> -msg
6.  Use the Private key and validate if OPENSSL is working correctly:  
    -   openssl s\_client -showcerts -connect <Destination\_IP>:<Port> -key private.pem
7.   Leverage Public and Private keys via Curl to validate if the 3rd party is configured correctly:  
    -   curl <API\_Point>:<port> -v -H "Content-Type:application/json" -d --key private.pem:<password>

Before continuing, make sure steps 6 and 7 have a satisfactory result. If any of the previous steps fail, it means the configuration at the 3rd party is not correct and there is no need to debug at ServiceNow yet. Once this is working, start configuring ServiceNow for Mutual Auth:

8.  Add Target's public certificate as a trusted cert in the given keystore and attach it to the protocol profile in ServiceNow.

When running the test on a REST method and it shows https:// instead of the custom protocol name (which should be <8 characters and lower alphabetic letters only), ensure that the end point on the REST outbound message uses the custom protocol and has mutual authentication checked. At least in Quebec it seems to be taking the custom protocol from the message, rather than the method. If you get unexplained errors with connection refusal, set the mutual authentication checkbox on the message only, not the method.  

# Additional information

* * *

[Mutual Authentication - Overview](https://support.servicenow.com/kb_view.do?sysparm_article=KB0691876 "Mutual Authentication - Overview")

[Steps to set up Mutual Authentication: Keys](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696776 "Steps to set up Mutual Authentication: Keys")
