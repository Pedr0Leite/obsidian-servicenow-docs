---
title: "SAML Errors and Fixes (SAML 2.0 / SAML 2.0 Update 1)"
aliases:
  - KB0759251
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759251
kb_number: KB0759251
last_modified: 2023-10-10
---

## SAML Errors and Fixes (SAML 2.0 / SAML 2.0 Update 1)

  

### Issue

After SAML plugin activation and initial configuration, errors can appear that potentially generate P1 outages.

### Release

Instance is configured with the SAML 2.0 / SAML 2.0 Update 1 plugin (Multiple Provider SSO is not configured/enabled)

### Resolution

| Error in instance log | Corresponding SAML Property | Diagnosis | Fix |
| --- | --- | --- | --- |
| NotAfter: <Thu Jun 05 22:57:44 PDT 2014> | N/A | The current certificate or the SAML assertion has expired. | 
-   Sync the SNC clock with the Identity Provider (IdP) server clock.
-   Update the "SAML 2.0" certifitcate record.

 |
| 

-   Unable to locate SAML 2.0 certificate.
-   Could not find a digital signature stored in the ServiceNow instance.

 | The PEM-formatted string should be entered into the **PEM Certificate** field. | The SAML certificate does not exist. It might be inactive. | 

-   Ensure that the correct PEM-formatted certificate is uploaded to the instance.
-   Verify that the certificate has the name **SAML 2.0**. No other names are allowed.

 |
| Certificates don't match. Expect: <_certStr_\>, actual: <_inboundCert_\> | N/A | The available certificate in SNC does not match the certificate in assertion. Causes include:  

-   The certificate is update on the IdP but not in the SNC instance.
-   The certificate is in the wrong format.

 | Confirm that the PEM-formatted string in the **SAML 2.0** certificate record matches the X509 Certificate in the SAMLResponse for the user IdP. |
| Failure to check the validity of the certificate. | N/A | The current certificate might have expired. | Update the **SAML 2.0** certificate record. |
| Failure to validate signature profile. | N/A | The assertion might be signed with a different certificate. | Check if the IdP has the same certificate as the SNC instance. |
| InResponseTo attribute in SubjectConfirmationData mismatch. Expect: <_inResponseTo_\>, actual: <_inResponseTo_\>. | N/A | This error appears if either of the following situations occur:  

-   The IdP returns a SAMLResponse for a different SAMLRequest.
-   A user bookmarks the URL with the SAMLRequest instead of just the instance URL
-   If a null value is expected, the response might be sent to a different node when the instance has multiple nodes.

 | The IdP admin should confirm that the expected SAMLResponse is being returned. This situation can be a load balancer or infrastructure issue. |
| SessionIndex value not found: <_message_\>... | N/A | The SessionIndex is required in the SNC instance. The IdP needs to return in in the SAMLResponse, in order to authenticate successfully. | IdP admin will need to confirm that the SessionIndex is defined in the SAMLResponse. |
| No valid SubjectConfirmation found. | N/A | Conditions could be missing due to an error on the IdP.  
The StatusCode in the response would contain Responder instead of the expected Success. | Review the SAMLResponse to determine if Conditions is included in the SAMLResponse.  
The valid subject confirmation data could be expired or not for the right audience. |
| Assertion audience mismatch. Expect: <_value on instance_\>, actual: <_value returned by IdP_\>.  
OR  
AudienceRestriction validation failed. No matching audience found. | The audience URI that accepts the SAML2 token. (Normally, it is your instance URI. For example: https://demo.service-now.com.) | The SNC instance configured audience URI must match the value in the IdP. | Locate <saml2:Audience> in the SAMLResponse in the logs and verify this value matches the one on the instance. |
| Assertion issuer is invalid. Expect: <_value on instance_\>, actual: <_value returned by IdP_\> | The Identity Provider URL that issues the SAML2 security token with user info. | The IdP entity id (issuer) does not match the value defined in the SNC instance. | 

-   Check if the IdP or SP is not configured properly.
-   Confirm that the SAML property (the Identity Provider URL that issues the SAML2 security token with user info) is set correctly.

 |
| Subject is valid in the future. Now: <_now_\>, NotBefore:<_notBefore_\>  
OR  
Subject is expired. Now: <_now_\>, NotOnOrAfter: <_notOnOrAfter_\> | The number in seconds before _notBefore_ constraint, or after _notOnOrAfter_ constraint, to consider still valid. | The IdP clock is not synced with the SP clock. | 

**If SAML 2.0 / SAML 2.0 Update 1 plugin is configured**  
Update the SAML property glide.authenticate.sso.saml2.clockskew to a larger value. The default is 60 seconds. Some cases require a setting of 180. You may also need to check the time on your IdP server.

**If Multiple Provider SSO plugin is configured**  
Update the 'Clock Skew' field in the respective Identity Provider record that has the reported issue.

 |
| Assertion is valid in the future, now: <_now_\>, notBefore: <_notBefore_\>  
OR  
Assertion is expired, now: <_now_\>, notOnOrAfter: <_notOnOrAfter_\> | The number in seconds before _notBefore_ constraint, or after _notOnOrAfter_, to consider still valid. | The IdP clock is not synced with the SP clock. | 

**If SAML 2.0 / SAML 2.0 Update 1 plugin is configured**  
Update the SAML property glide.authenticate.sso.saml2.clockskew to a larger value. The default is 60 seconds. Some cases require a setting of 180. You may also need to check the time on your IdP server.

**If Multiple Provider SSO plugin is configured**  
Update the 'Clock Skew' field in the respective Identity Provider record that has the reported issue.

 |

  
  
Additional Error Messages

* * *

| Common login or Identity Provider (IdP) Errors | IdP | Diagnosis | Fix |
| --- | --- | --- | --- |
| Login requests generate an infinite loop between the system and the IdP when High Security is active. |   
 | 
-   Typically the URL endpoint is an error page or logout page.
-   The logout\_redirect.do might create this loop when you define glide.security.url.whitelist without adding the IdP host name to the property value.

 | Set (or create) the system property glide.authenticate.failed\_redirect to redirect failed authentication requests to this URL. |
| Authentication fails and the login request generates an infinite loop between the system and the IdP. |   
 | The rotating session feature of the High Security plugin can cause problems with the SAML 2.0 authentication process. SAML 2.0 redirects URLs to an IdP. When rotating sessions are enabled, any redirection causes the session to rotate and forces the instance to query the IdP again. This situation causes an endless loop of new sessions between the instance and the IdP. | Disable the rotating session feature when using SAML 2.0 for authentication. |
| The token that was used to authenticate the user or the request is signed with the signature algorithm [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256) which is not the expected signature algorithm [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1). Check the **Alert Context** tab for event details. | ADFS | Check the Alert Context tab for event details. | Navigate to the Advanced tab of the Relying Party Trust configuration dialog and verify that the algorithm is set to SHA-1 and not SHA-256. |
| urn:oasis:names:tc:SAML:2.0:status:Responder |   
 | Check the IdP logs during the respective login attempt. | Instance is expecting to see urn:oasis:names:tc:SAML:2.0:status:Success before any attempt to process the SAMLResponse. Please work with IdP admin to provide related logs so Support can determine what configuration on the instance/IdP needs to be updated. |
