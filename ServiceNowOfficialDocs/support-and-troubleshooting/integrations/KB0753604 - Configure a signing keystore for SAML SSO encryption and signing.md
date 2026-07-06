---
title: "Configure a signing keystore for SAML SSO encryption and signing"
aliases:
  - KB0753604
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753604
kb_number: KB0753604
last_modified: 2026-01-14
---

## Configure a signing keystore for SAML SSO encryption and signing

  

### Issue

This article explains how to configure a signing keystore for encryption and signing in a SAML SSO Identity Provider configuration using base system keystores or custom keystores.

ServiceNow provides two base system keystores for SAML encryption and signing. For detailed configuration information, see [SAML 2.0 configuration using Multi-Provider SSO.](https://www.servicenow.com/docs/bundle/zurich-platform-security/page/integrate/single-sign-on/task/t_CreateASAML2Upd1SSOConfigMultiSSO.html)

### Release

All supported releases; Beginning with Washington DC for separate signing and encryption keystores 

### Resolution

To view available keystores, go to the **X.509 Certificates** list view. Two base system keystores are available: 

### SAML 2.0 SP Keystore (deprecated)

This keystore provides 128-bit support and is deprecated.

To use this keystore, configure the Identity Provider record in the Encryption and Signing section:

1.  Set Signing/Encryption Key Alias to saml2sp.
2.  Set Signing/Encryption Key Password to saml2sp.
3.  Set Signing Signature Algorithm to [http://www.w3.org/2000/09/xmldsig#rsa-sha1.](http://www.w3.org/2000/09/xmldsig#rsa-sha1.)
4.  Select the appropriate checkboxes based on your requirements:
    -   Encrypt Assertion
    -   Sign AuthnRequest
    -   Sign LogoutRequest
5.  Select **Save**.

### SAML 2.0 Keystore\_Key2048\_SHA256 

The **SAML 2.0 Keystore\_Key2048\_SHA256** or **SAML 2.0 Keystore\_Key2048\_SHA256\_FIPS** keystore provides 256-bit support.

To use this 256-bit keystore:

From the X.509 Certificates list view:

1.  Set SAML 2.0 SP Keystore Active to **false**.
2.  Set SAML 2.0 Keystore\_Key2048\_SHA256 Active to **true**, **or** Set SAML 2.0 Keystore\_Key2048\_SHA256\_FIPS Active to **true**
3.  Set the system property glide.authenticate.sso.saml2.keystore value to the sys\_id of the keystore record in the sys\_certificate table:
    -   SAML 2.0 Keystore\_Key2048\_SHA256 base system sys\_id: 3685fc22930212003c5537ae867ffb91
    -   SAML 2.0 Keystore\_Key2048\_SHA256\_FIPS base system sys\_id: c60ad24b732220103a5b0dd43cf6a7db 

Configure the Identity Provider record in the Encryption and Signing section:

1.  Set Signing/Encryption Key Alias to saml2sp.
2.  Set Signing/Encryption Key Password to saml2sp.
3.  Set Signing Signature Algorithm to [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256.](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256.)
4.  Select the appropriate checkboxes based on your requirements:
    -   Encrypt Assertion
    -   Sign AuthnRequest
    -   Sign LogoutRequest
5.  Select **Save**. 

#### **Export the signing certificate**

After you configure the keystore, export the signing certificate to provide to your Identity Provider:

1.  Open your Identity Provider record.
2.  Select **Generate Metadata**.
3.  Locate the signing certificate in the <ds:X509Certificate> XML element.

**Example metadata output:**

<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://<instance-name>.service-now.com">   
<SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">   
<KeyDescriptor use="signing" >   
<ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIDoTCCAomgAwIBAgIERs1yFjANBgkqhkiG9w0BAQsFADCBgDELMAkGA1UEBhMCVVMxCzAJBgNV   
BAgTAkNBMRQwEgYDVQQHEwtTYW50YSBDbGFyYTETMBEGA1UEChMKU2VydmljZU5vdzEdMBsGA1UE   
CxMUUGxhdGZvcm0gRGV2ZWxvcG1lbnQxGjAYBgNVBAMTEVBsYXRmb3JtIFNlY3VyaXR5MB4XDTE2   
MDMwOTIyNTYyMVoXDTI2MDMwNzIyNTYyMVowgYAxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEU   
MBIGA1UEBxMLU2FudGEgQ2xhcmExEzARBgNVBAoTClNlcnZpY2VOb3cxHTAbBgNVBAsTFFBsYXRm   
b3JtIERldmVsb3BtZW50MRowGAYDVQQDExFQbGF0Zm9ybSBTZWN1cml0eTCCASIwDQYJKoZIhvcN   
AQEBBQADggEPADCCAQoCggEBAMdREVxdscrxy9ap/UnDsdihJjoKxY6qpxvLUHUGKjTsSNNu/6Fd   
hh4y5hkYLklY0vEdXStqwvqJjqiCn1LPPo/WjWBAv1kVZXiA0pbaxRaX0wtQ2zo4ddIpCc6/UFOZ   
QxPTk+974KPKiA9wDa9/mSqfLfzPmDrSPGLvbiQACTHozLTXxMv+z7pJg77muWIHet5pdrUThF9w   
8iANYTRie+dl+LxEyF5U5tdQXlFgRo5qBQQvSDVL+FbjiX+XllNLwP2RX7IwZChxi6B8dgkAuXTX   
dII309L9NXy3E8pefhAJgSe5FnkGaQk/HlqOBtgKdp9/Rf5Uy6fz0ZJmEqKzM+8CAwEAAaMhMB8w   
HQYDVR0OBBYEFNF7CaQY7kZQM5ulSV8bOAl2mgdNMA0GCSqGSIb3DQEBCwUAA4IBAQC+f3HXbp/2   
IaF/bmUICCkVragGpX4IslJPxjdShUA7qwIZ8YNZZHT9R8bRrcOIRy83fKiXDmlWYSgiuA3cckH4   
WSvwCHOCSi0H72/L9QRjqcrlzpzoCFP1v57tzGOPyAsRr/kU7v01g6bCKlnXPhXpX6EA5m0h37vQ   
rV++9aXSiThRbatOkRVow4NohbkVZA8zhn6kxSI3nwM1xRO30dtb8iQGo/2/J9d2pzLKnvC3pFVF   
W7GRabHJ8Zv5k/9f45/9F8l/9+v8g+OaqEdQuAdymHbeFQ732vd/4MuJWHylQGcyQz7ytJUqr7j4   
epX6Li/sQdXGaLxLM+rEKFMY7uB/</ds:X509Certificate></ds:X509Data></ds:KeyInfo>   
</KeyDescriptor>   
<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://<instance-name>.service-now.com/navpage.do"/>   
<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>   
<AssertionConsumerService isDefault="true" index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<instance-name>.service-now.com/navpage.do" />   
<AssertionConsumerService isDefault="false" index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://<instance-name>.service-now.com/consumer.do" />   
</SPSSODescriptor>   
</EntityDescriptor> 

To format this as a PEM certificate (as may be required by the IdP) encapsulate the <ds:X509Certificate> value with -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- tags as in this example:

\-----BEGIN CERTIFICATE-----   
MIIDoTCCAomgAwIBAgIERs1yFjANBgkqhkiG9w0BAQsFADCBgDELMAkGA1UEBhMCVVMxCzAJBgNV   
BAgTAkNBMRQwEgYDVQQHEwtTYW50YSBDbGFyYTETMBEGA1UEChMKU2VydmljZU5vdzEdMBsGA1UE   
CxMUUGxhdGZvcm0gRGV2ZWxvcG1lbnQxGjAYBgNVBAMTEVBsYXRmb3JtIFNlY3VyaXR5MB4XDTE2   
MDMwOTIyNTYyMVoXDTI2MDMwNzIyNTYyMVowgYAxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEU   
MBIGA1UEBxMLU2FudGEgQ2xhcmExEzARBgNVBAoTClNlcnZpY2VOb3cxHTAbBgNVBAsTFFBsYXRm   
b3JtIERldmVsb3BtZW50MRowGAYDVQQDExFQbGF0Zm9ybSBTZWN1cml0eTCCASIwDQYJKoZIhvcN   
AQEBBQADggEPADCCAQoCggEBAMdREVxdscrxy9ap/UnDsdihJjoKxY6qpxvLUHUGKjTsSNNu/6Fd   
hh4y5hkYLklY0vEdXStqwvqJjqiCn1LPPo/WjWBAv1kVZXiA0pbaxRaX0wtQ2zo4ddIpCc6/UFOZ   
QxPTk+974KPKiA9wDa9/mSqfLfzPmDrSPGLvbiQACTHozLTXxMv+z7pJg77muWIHet5pdrUThF9w   
8iANYTRie+dl+LxEyF5U5tdQXlFgRo5qBQQvSDVL+FbjiX+XllNLwP2RX7IwZChxi6B8dgkAuXTX   
dII309L9NXy3E8pefhAJgSe5FnkGaQk/HlqOBtgKdp9/Rf5Uy6fz0ZJmEqKzM+8CAwEAAaMhMB8w   
HQYDVR0OBBYEFNF7CaQY7kZQM5ulSV8bOAl2mgdNMA0GCSqGSIb3DQEBCwUAA4IBAQC+f3HXbp/2   
IaF/bmUICCkVragGpX4IslJPxjdShUA7qwIZ8YNZZHT9R8bRrcOIRy83fKiXDmlWYSgiuA3cckH4   
WSvwCHOCSi0H72/L9QRjqcrlzpzoCFP1v57tzGOPyAsRr/kU7v01g6bCKlnXPhXpX6EA5m0h37vQ   
rV++9aXSiThRbatOkRVow4NohbkVZA8zhn6kxSI3nwM1xRO30dtb8iQGo/2/J9d2pzLKnvC3pFVF   
W7GRabHJ8Zv5k/9f45/9F8l/9+v8g+OaqEdQuAdymHbeFQ732vd/4MuJWHylQGcyQz7ytJUqr7j4   
epX6Li/sQdXGaLxLM+rEKFMY7uB/   
\-----END CERTIFICATE----- 

### Custom keystores

You can create a custom keystore instead of using the base system options. See:

-   [Create a service provider keystore for SAML](https://docs.servicenow.com/csh?topicname=t_CreatingAServiceProviderKeyStore.html&version=latest "Create a service provider keystore for SAML")
-   [Install a service provider keystore for signing SAML requests](https://docs.servicenow.com/csh?topicname=t_InstallASPKeystoreSigningSAMLReqs.html&version=latest "Install a service provider keystore for signing SAML requests") 

### Washington DC release and later

Starting with the Washington DC release, you can configure separate certificates for signing and encryption. A new system property glide.authenticate.sso.saml2.encryption.keystore works alongside the existing glide.authenticate.sso.saml2.keystore property.

![UI showing new system property for keystore after Washington release](https://support.servicenow.com/sys_attachment.do?sys_id=75d85d83c3600654a9ea601bb001314a)

A new keystore is available: SAML 2.0 Keystore\_Key2048\_SHA256\_Encryption

![X.509 Certificates list showing new keystore properties](https://support.servicenow.com/sys_attachment.do?sys_id=60bfddc3c3240654a9ea601bb0013125)

Default values for this keystore:

-   Signing/Encryption Key Alias: saml2sp
-   Signing/Encryption Key Password: saml2sp
-   Signing Signature Algorithm: [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256)

### How the properties work together

**Before Washington DC:** Both signing and encryption use the same certificate specified in glide.authenticate.sso.saml2.keystore.

Washington DC and later: You can use separate certificates:

-   glide.authenticate.sso.saml2.keystore: Contains the sys\_id for the signing certificate
-   glide.authenticate.sso.saml2.encryption.keystore: Contains the sys\_id for the encryption certificate

### Upgrade behavior

During the upgrade to Washington DC, the system automatically copies the value from glide.authenticate.sso.saml2.keystore to glide.authenticate.sso.saml2.encryption.keystore. This ensures your existing encryption and signing configuration continues to work after the upgrade.

After upgrading to Washington DC, you can configure different certificates for signing and encryption by setting each system property to point to the appropriate certificate sys\_id.

### System property reference

| 
Property

 | 

Before Washington DC

 | 

Washington DC and later

 |
| --- | --- | --- |
| 

glide.authenticate.sso.saml2.keystore

 | 

sys\_id of the certificate for signing and encryption

 | 

sys\_id of the certificate for signing only

 |
| 

glide.authenticate.sso.saml2.encryption.keystore

 | 

Not available

 | 

sys\_id of the certificate for encryption only

 |

  

### Related Links

[Install a service provider keystore for signing SAML requests](https://docs.servicenow.com/csh?topicname=t_InstallASPKeystoreSigningSAMLReqs.html&version=latest)
