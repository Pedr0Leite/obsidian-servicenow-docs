---
title: "SSO Configurations in ServiceNow When Identity Provider Uses SHA256 Signing Signature Algorithm"
aliases:
  - KB0786527
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786527
kb_number: KB0786527
last_modified: 2025-01-22
---

## Issue

When using SSO Integrations, by default the Signing Signature Algorithm in ServiceNow is configured as SHA1. But some Identity Providers like Azure uses SHA256. This article explains all the necessary SSO configurations to be made in ServiceNow instance to use SHA256.

## Resolution

To change from SHA1 to SHA256, the following has to be done (assuming you use the ServiceNow provided keystores):

  
a) Activate the SHA256 SAML2 SP Keystore file in the X509 certificate module (contact support if you need to get a copy of this certificate)  
b) Update the following property through sys\_properties.LIST: glide.authenticate.sso.saml2.keystore  
\-- Right click on the certificate in the certificate list that represents the SAML2 SP keystore for SHA256 and click on Copy sys\_id  
\-- Through the filter navigator, go to sys\_properties.LIST and select the property by the name of glide.authenticate.sso.saml2.keystore  
\-- Replace the sys\_id in the value for this property with the sys\_id copied above  
c) Update the Signing Signature Algorithm field in the Identity Provider record to http://www.w3.org/2001/04/xmldsig-more#rsa-sha256   
  
  

**Please note:** 

If you use your own ServiceProvider keystore, please ensure to update the Signing/Encryption Key Alias and Signing/Encryption Key password values in the Encryption and Signing tab of your Identity Provider record with the appropriate values.
