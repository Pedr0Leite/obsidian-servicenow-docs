---
title: "Mutual Authentication: Overview"
aliases:
  - KB0691876
tags:
  - servicenow
  - support-kb
  - mutual-authentication
  - mtls
  - certificate
  - authentication
  - security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691876
kb_number: KB0691876
last_modified: 2025-07-18
---

## Mutual Authentication: Overview

  

### Issue

Mutual Authentication establishes trust by exchanging secure sockets layer (SSL) certificates.

### Data Flow

1.  Client (eg. ServiceNow) and Server (eg. a third party) will do a handshake before transmitting any data.
2.  Client will have a keystore with Public and Private Key Pair
3.  Server will have a keystore with Public and Private Key Pair
4.  Client will share the public key( a certificate) with Server and Server will keep it in its trust store.
5.  Server will share the public key( a certificate) with Client and Client will keep it in its trust store.
6.  Lets say, client initiated the handshake, it will send out its public certificate to Server.
7.  Server will check if it has this public certificate in its trust store = which it does.
8.  Server sends its public certificate to client and client will check if it has this public certificate in its trust store = which it does.
9.  Since handshake is now successful, Client will send out the payload
10.  Client will encrypt the payload using Server's Public Certificate from its trust store.
11.  Server receives this payload and decrypts this payload from the private key in Server's keystore.
12.  Server responds with payload encrypted using Client's Public Certificate from its trust store.
13.  Client receives this payload and decrypts this payload from the private key in Client's keystore.

![Data flow between Client and Server](/sys_attachment.do?sys_id=052ccd8693feea14080af35d6cba1029 "Data flow between Client and Server")

### Example

**Step 1:** Generate Keystore Pair (Public and private key), self-signed:

C:\\Program Files\\Java\\jre1.8.0\_162\\bin>keytool -genkey -alias Keystore\_alias -keyalg R  
SA -validity enter\_Validity\_in\_Days -keystore Keystore\_name.keystore -storepass Keystore\_Password -keypass Key\_Password  
What is your first and last name?  
  \[Unknown\]:  ..........  
What is the name of your organizational unit?  
  \[Unknown\]:  ..........  
What is the name of your organization?  
  \[Unknown\]:  ..........  
What is the name of your City or Locality?  
  \[Unknown\]:  ..........  
What is the name of your State or Province?  
  \[Unknown\]:  ..........  
What is the two-letter country code for this unit?  
  \[Unknown\]:  ..........  
Is CN=vab, OU=servicenow, O=servicenow, L=sydney, ST=nsw, C=61 correct?  
  \[no\]:  yes

**Step 2**: Extract the public certificate from the above keystore pair:

C:\\Program Files\\Java\\jre1.8.0\_162\\bin>keytool -export -alias Keystore\_alias -keystore  
 Keystore\_name.keystore -storepass Keystore\_Password -file Cert\_name.cer  
  
Certificate stored in file <snclient.cer>  
  
Warning:  
The JKS keystore uses a proprietary format. It is recommended to migrate to PKCS  
12 which is an industry standard format using "keytool -importkeystore -srckeyst  
ore snclient.keystore -destkeystore snclient.keystore -deststoretype pkcs12".

### Release

### Resolution

### Related Links

-   Debugging Mutual Authentication: [KB0696599 - Debugging Mutual Authentication](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696599 "KB0696599 - Debugging Mutual Authentication")

-   Steps to set up Mutual Authentication Keys: [KB0696776 - Steps to set up Mutual Authentication: Keys](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696776 "KB0696776 - Steps to set up Mutual Authentication: Keys")

-   Configuring Mutual Authentication: [https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/administer/security/concept/c\_MutualAuthentication.html](https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/administer/security/concept/c_MutualAuthentication.html)
-   Configure Outbound Mutual Authentication in ServiceNow: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0696002](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696002)

## Related

- [[certificate-based-authentication]] - official docs on certificate-based authentication
- [[set-up-mutual-auth]] - official docs on setting up Mutual Authentication keys
- [[ui-login-mutual-auth]] - official docs on UI login with Mutual Authentication

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0714734 - Firefox Your connection is not secure.|Firefox: Your connection is not secure.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance|Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
