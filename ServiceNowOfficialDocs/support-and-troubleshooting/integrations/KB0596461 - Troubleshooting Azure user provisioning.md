---
title: "Troubleshooting Azure user provisioning"
aliases:
  - KB0596461
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596461
kb_number: KB0596461
last_modified: 2025-05-08
---

## Issue

Customer has selected Azure as their Identity Provider and noted that users are not being imported or user information is missing.

## Resolution

For Cause #1: For more information, see [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0960680](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960680)  
  
For Cause #2: Customer needs to update the instance so the needed reference field values exist on the instance. Servicenow development may need to to work with Azure to allow updates to reference fields when values do not exist.

### Errata: SOAP payload

Azure SOAP calls are made to the sys\_user table directly.

With SOAP debugging enabled you would see entries like the following:

13:38:23.276 Debug API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D DEBUG: GetIntegrationSessionTimeout: session inactivity timeout changed by installation exit. Inactive\_interval= 300 seconds   
13:38:23.276 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D \*\*\* Start #988,770, path: /sys\_user.do, user: <your-user>   
13:38:23.277 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor: initial session inactivity timeout is 60 seconds   
13:38:23.277 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor: initial soap request timeout is 60 seconds   
13:38:23.277 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor: session inactivity timeout changed to 60 seconds   
  
\*Note: I reformated the XML payload for readability\*  
13:38:23.280 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor:   
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
<s:Body>  
<insert xmlns="http://www.service-now.com/sys\_user">  
<active>1</active>  
<email>first.last@domain.com</email>  
<first\_name>First</first\_name>  
<last\_name>Last</last\_name>  
<phone>123-456-7890</phone>  
<user\_name>first.last@domain.com</user\_name>  
<title>Educator</title>  
<city>Vancouver</city>  
<country>Canada</country>  
<state>British Columbia</state>  
<street>123 Test Street</street>  
<zip>123456</zip>  
<employee\_number>567890</employee\_number>  
</insert>  
</s:Body>  
</s:Envelope>  
  
13:38:23.281 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D Created SOAPProcessorThreadc58050ba3760ee00836b53b543990e85   
13:38:24.485 Info SOAPProcessorThreadc58050ba3760ee00836b53b543990e85 4D8010BA3760EE00836B53B543990E9D Background message, type:info, message: Primary email device created for First Last   
13:38:24.489 Info SOAPProcessorThreadc58050ba3760ee00836b53b543990e85 4D8010BA3760EE00836B53B543990E9D released semaphore   
13:38:24.489 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor: session inactivity timeout changed to 61 seconds   
13:38:24.489 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D Sending response   
13:38:24.489 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D Response bytes sent: 250   
13:38:24.489 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D SOAPProcessor done   
13:38:24.490 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D Memory transaction: 7mb total: 374mb free: 52% Allocated: 786mb   
13:38:24.490 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D \*\*\* End #988,770, path: /sys\_user.do, user: <your-user>, total transaction time: 0:00:01.234, transaction processing time: 0:00:01.234, network: 0:00:00.000, chars: 250, ncompressed chars: 381, SQL time: 453 (count: 424), business rule: 19 (count: 2), phase 1 form length: 0, largest chunk written: 240, request parms size: 56, largest input read: 562   
13:38:24.494 Info API\_INT-thread-2 4D8010BA3760EE00836B53B543990E9D #988770 /sys\_user.do -- total transaction time: 0:00:01.234, transaction processing time: 0:00:01.234, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: 40.76.95.148, chars: 250, uncompressed chars: 381, SQL time: 454 (count: 426), business rule: 19 (count: 2), phase 1 form length: 0, largest chunk written: 240, request parms size: 56, largest input read: 562

### Errata: SAMLResponse payload

There are cases where the SAMLResponse has user information.

A new feature of the MultiSSO plugin, as of the Geneva release, is to parse that user information to create/update users. For more information, see [SAML User Provisioning](https://docs.servicenow.com/csh?topicname=c_SAMLUserProvisioning.html&version=latest "SAML User Provisioning").

2016-07-13 12:00:26 (735) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: SAML Response xml: <?xml version="1.0"?>  
<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="\_0ff1f353-e142-4163-b8b5-df1bce0d31e5" Version="2.0" IssueInstant="2016-07-13T19:00:26.515Z" Destination="https://<instance-name>.service-now.com/navpage.do" InResponseTo="SNC45f5d2fc01d553385a2450732cb3980d">  
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">https://sts.windows.net/59762c14-55e8-4b58-806e-f6cc47d75b19/</Issuer>  
<samlp:Status>  
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>  
</samlp:Status>  
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="\_17195cc0-a97c-4eca-8632-b1ef960dfd91" IssueInstant="2016-07-13T19:00:26.485Z" Version="2.0">  
<Issuer>https://sts.windows.net/59762c14-55e8-4b58-806e-f6cc47d75b19/</Issuer>  
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">  
<ds:SignedInfo>  
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>  
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>  
<ds:Reference URI="#\_17195cc0-a97c-4eca-8632-b1ef960dfd91">  
<ds:Transforms>  
<ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>  
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>  
</ds:Transforms>  
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>  
<ds:DigestValue>r+PtAm4bKxgnup1Vv5CDF+C0kCxnOBXdk7rc3RsIXmk=</ds:DigestValue>  
</ds:Reference>  
</ds:SignedInfo>  
<ds:SignatureValue>1Zey66vBz+WpR7wO+wcS7ews1q2WSA0LWWQTk4CK4Q0eU7zGWoueIPrXJK13AWPYTtrdKItjLhxmhOjniqHpCuC0cXmfmx5oNG2AUmHqG5hdoY/z9UrntZcSIasuiZ0RcGtzy/fSYqYgluC2fuJFVEClB9jjpLWke0jY0NZfkdqXgC2geieNVvLfRTfLcCGLVgyvS6oOg7rFtdpv4XWFDpUtWnJxd59t21AERiDWmHSRPUvomOP2gTqXTwFLk7HTMnFmli8aur/lgsjyyreymaSlTt2A1Irc9wmbb3rPVC9Z3ZQaTjkdfwFz2Iwn3XSvH0L7dq2wk69mg1esQe5p7A==</ds:SignatureValue>  
<KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">  
<X509Data>  
<X509Certificate>MIIC8DCCAdigAwIBAgIQQksZGlYJwYZFNvapl011AjANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0xNjA3MDcyMjUyMDBaFw0xOTA3MDcyMjUyMDBaMDQxMjAwBgNVBAMTKU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3XcADqajZXmR5if0VuWYjLl9k7oFXJgATYTbt4NMpq1v1mFwipdA/EbKNW4yjfylGjyMbuBwmlfCKL2gTYa2IYdrt/hMPupMBQx1tTrMovh7f7OsKGGiltdK+JmoLNtfAyDFk43K+W1oNbkpq5JggDTCRaM7XYWYFjmYhY0eq0UZUgnUaPJZcFZGVtCcQLEDZyY4ZD1YdzFvb1JAkrFo1zzYdOoyM+RsrPkCYRpIJmw1NZpkm1Cm/6c7mpGZHSdLlDuen+IBvuKq4XpEKhB1/HWfCRM3VbTctmLfJqXvu3au2u1GUqzID0kArB5PQxi3ND+a4zS5pW3SKPQ5IE80NQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQDdO9Jv4eBo/MLimUNiZnU6wBk6OJPVWo9F+P7JcKP9XaZJjuQ0MgafaBMMiFx/37BYmRVmEToq40JvnuVcpvnrMJ7fZlgj54zNF4GtEXaCqzcnvWDzZyn/3bmOeJzGWK2ITxTis/99tFmLDsvqB9rhH14GWzjw5ZYxy9xj7HgKTo5Knhyh5MmkSp1KHg+tS3bfEOaBvGlGFY2mkPe58fz8rGOhCdIz9GbedmdS3Vc0uFJsfrth4NL5tHpoGs4rkyNxPefB50d9RePts2ZMUFTLkn/0n2EvDtIhrjX3VzVsTNWBLjzHIsvrfpk0wg4p/R7zDO7qYn2tZiqdZctljARA</X509Certificate>  
</X509Data>  
</KeyInfo>  
</ds:Signature>  
<Subject>  
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"><user>@<domain></NameID>  
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">  
<SubjectConfirmationData InResponseTo="SNC45f5d2fc01d553385a2450732cb3980d" NotOnOrAfter="2016-07-13T19:05:26.485Z" Recipient="https://<instance-name>.service-now.com/navpage.do"/>  
</SubjectConfirmation>  
</Subject>  
<Conditions NotBefore="2016-07-13T18:55:26.485Z" NotOnOrAfter="2016-07-13T19:55:26.485Z">  
<AudienceRestriction>  
<Audience>https://instancename.service-now.com</Audience>  
</AudienceRestriction>  
</Conditions>  
<AttributeStatement>  
<Attribute Name="http://schemas.microsoft.com/identity/claims/tenantid">  
<AttributeValue>59762c14-55e8-4b58-806e-123456789</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.microsoft.com/identity/claims/objectidentifier">  
<AttributeValue>d74d3157-41c5-4298-898f-123456789</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.microsoft.com/identity/claims/displayname">  
<AttributeValue>First Last</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.microsoft.com/identity/claims/identityprovider">  
<AttributeValue>https://sts.windows.net/59762c14-55e8-4b58-806e-123456789/</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname">  
<AttributeValue>First</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname">  
<AttributeValue>Last</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress">  
<AttributeValue>first.last@domain.com</AttributeValue>  
</Attribute>  
<Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name">  
<AttributeValue>first.last@domain.com</AttributeValue>  
</Attribute>  
</AttributeStatement>  
<AuthnStatement AuthnInstant="2016-07-13T18:27:25.888Z" SessionIndex="\_17195cc0-a97c-4eca-8632-b1ef960dfd91">  
<AuthnContext>  
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</AuthnContextClassRef>  
</AuthnContext>  
</AuthnStatement>  
</Assertion>  
</samlp:Response>  
  
...  
2016-07-13 12:00:26 (807) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: SAML User Import Table: u\_imp\_saml\_user\_abj0sslhgb  
2016-07-13 12:00:26 (809) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found some attributes!  
2016-07-13 12:00:26 (809) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.microsoft.com/identity/claims/tenantid, value : 59762c14-55e8-4b58-806e-123456789  
2016-07-13 12:00:26 (810) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.microsoft.com/identity/claims/objectidentifier, value : d74d3157-41c5-4298-898f-123456789  
2016-07-13 12:00:26 (811) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.microsoft.com/identity/claims/displayname, value : First Last  
2016-07-13 12:00:26 (812) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.microsoft.com/identity/claims/identityprovider, value : https://sts.windows.net/59762c14-55e8-4b58-806e-123456789/  
2016-07-13 12:00:26 (813) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname, value : First  
2016-07-13 12:00:26 (815) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname, value : Last  
2016-07-13 12:00:26 (818) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress, value : first.last@domain.com  
2016-07-13 12:00:26 (819) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Found saml attribute pair name: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name, value : first.last@domain.com  
2016-07-13 12:00:26 (819) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Calling loadImportSet!  
2016-07-13 12:00:26 (870) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Number of attributes : 9  
2016-07-13 12:00:26 (871) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.microsoft.com/identity/claims/displayname, value : First Last  
2016-07-13 12:00:26 (871) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_m\_ms\_displayname  
2016-07-13 12:00:26 (872) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field sso\_source, value : sso:d3582cf437a46a00ff667c1643990ed7  
2016-07-13 12:00:26 (873) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : sso\_source  
2016-07-13 12:00:26 (873) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.microsoft.com/identity/claims/tenantid, value : 59762c14-55e8-4b58-806e-123456789  
2016-07-13 12:00:26 (874) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_m\_laims\_tenantid  
2016-07-13 12:00:26 (875) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.microsoft.com/identity/claims/identityprovider, value : https://sts.windows.net/59762c14-55e8-4b58-806e-123456789/  
2016-07-13 12:00:26 (876) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_m\_entityprovider  
2016-07-13 12:00:26 (878) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.microsoft.com/identity/claims/objectidentifier, value : d74d3157-41c5-4298-898f-123456789  
2016-07-13 12:00:26 (879) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_m\_jectidentifier  
2016-07-13 12:00:26 (879) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname, value : First  
2016-07-13 12:00:26 (880) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_x\_aims\_givenname  
2016-07-13 12:00:26 (881) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name, value : first.last@domain.com  
2016-07-13 12:00:26 (884) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_x\_ty\_claims\_name  
2016-07-13 12:00:26 (885) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname, value : Last  
2016-07-13 12:00:26 (886) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_x\_claims\_surname  
2016-07-13 12:00:26 (886) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress, value : first.last@domain.com  
2016-07-13 12:00:26 (887) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Field DBName : http\_schemas\_x\_s\_emailaddress  
2016-07-13 12:00:26 (888) Default-thread-1 108036DA37E82E00FF667C1643990E05 \*\*\* Script: Calling SNC.SSOUtil.createOrUpdateSAMLImportUserTable!
