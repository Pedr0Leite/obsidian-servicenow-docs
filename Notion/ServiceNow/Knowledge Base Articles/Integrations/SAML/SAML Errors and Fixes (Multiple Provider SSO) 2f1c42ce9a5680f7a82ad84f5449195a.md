---
aliases:
  - "SAML Errors and Fixes (Multiple Provider SSO)"
area: "Knowledge Base Articles"
source: notion-export
tags:
  - knowledge-base
  - saml
  - sso
  - integrations
  - troubleshooting
---

# SAML Errors and Fixes (Multiple Provider SSO)

### **Issue**

After SAML plugin activation and initial configuration, errors can appear that potentially generate P1 outages.

### **Release**

Instance is configured with the Multiple Provider SSO plugin

### **Resolution**

| **Error in instance log** | **Corresponding SAML Property** | **Diagnosis** | **Fix** |
| --- | --- | --- | --- |
| NotAfter: <Thu Jun 05 22:57:44 PDT 2014> | N/A | The current certificate or the SAML assertion has expired. | • Sync the SNC clock with the Identity Provider (IdP) server clock.
• Update the respective certificate record(s) in the **X509 Certificate** related list of the Identity Provider record. |
| • Unable to locate SAML 2.0 certificate.
• Could not find a digital signature stored in the ServiceNow instance. | The PEM-formatted string should be entered into the **PEM Certificate** field. | The SAML certificate does not exist. It might be inactive. | • Ensure that the correct PEM-formatted certificate is uploaded to the instance.
• Verify that the certificate is in the **X509 Certificate** related list of the respective Identity Provider record |
| Certificates don't match. Expect: <*certStr*>, actual: <*inboundCert*> | N/A | The available certificate in SNC does not match the certificate in assertion. Causes include:
• The certificate is update on the IdP but not in the SNC instance.
• The certificate is in the wrong format. | Confirm that the PEM-formatted string in one of the certificate records, listed in the **X509 Certificate** related list, matches the X509 Certificate in the SAMLResponse for the user IdP. |
| Failure to check the validity of the certificate. | N/A | The current certificate might have expired. | Update the respective SAML certificate(s) in the **X509 Certificate** related list within the Identity Provider record |
| Failure to validate signature profile. | N/A | The assertion might be signed with a different certificate. | Check if the IdP has the same certificate as the SNC instance. |
| InResponseTo attribute in SubjectConfirmationData mismatch. Expect: <*inResponseTo*>, actual: <*inResponseTo*>. | N/A | This error appears if either of the following situations occur:
• The IdP returns a SAMLResponse for a different SAMLRequest.
• A user bookmarks the URL with the SAMLRequest instead of just the instance URL
• If a null value is expected, the response might be sent to a different node when the instance has multiple nodes. | The IdP admin should confirm that the expected SAMLResponse is being returned. This situation can be a load balancer or infrastructure issue. |
| SessionIndex value not found: <*message*>... | N/A | The SessionIndex is required in the SNC instance. The IdP needs to return in in the SAMLResponse, in order to authenticate successfully. | IdP admin will need to confirm that the SessionIndex is defined in the SAMLResponse. |
| No valid SubjectConfirmation found. | N/A | Conditions could be missing due to an error on the IdP.The StatusCode in the response would contain Responder instead of the expected Success. | Review the SAMLResponse to determine if Conditions is included in the SAMLResponse.The valid subject confirmation data could be expired or not for the right audience. |
| Assertion audience mismatch. Expect: <*value on instance*>, actual: <*value returned by IdP*>.ORAudienceRestriction validation failed. No matching audience found. | Audience URI | The SNC instance configured audience URI must match the value in the IdP. | Locate <saml2:Audience> in the SAMLResponse in the logs and verify this value matches the one on the instance. |
| Assertion issuer is invalid. Expect: <*value on instance*>, actual: <*value returned by IdP*> | Identity Provider URL | The IdP entity id (issuer) does not match the value defined in the SNC instance. | • Check if the IdP or SP is not configured properly.
• Confirm that the SAML property (Identity Provider URL) is set correctly. |
| Subject is valid in the future. Now: <*now*>, NotBefore:<*notBefore*>ORSubject is expired. Now: <*now*>, NotOnOrAfter: <*notOnOrAfter*> | Clock Skew | The IdP clock is not synced with the SP clock. | Update the 'Clock Skew' field in the respective Identity Provider record that has the reported issue. |
| Assertion is valid in the future, now: <*now*>, notBefore: <*notBefore*>ORAssertion is expired, now: <*now*>, notOnOrAfter: <*notOnOrAfter*> | Clock Skew | The IdP clock is not synced with the SP clock. | Update the 'Clock Skew' field in the respective Identity Provider record that has the reported issue. |

**Additional Error Messages**

---

| **Common login or Identity Provider (IdP) Errors** | **IdP** | **Diagnosis** | **Fix** |
| --- | --- | --- | --- |
| Login requests generate an infinite loop between the system and the IdP when High Security is active. |  | • Typically the URL endpoint is an error page or logout page.
• The logout_redirect.do might create this loop when you define glide.security.url.whitelist without adding the IdP host name to the property value. | Set (or create) the system property glide.authenticate.failed_redirect to redirect failed authentication requests to this URL. |
| Authentication fails and the login request generates an infinite loop between the system and the IdP. |  | The rotating session feature of the High Security plugin can cause problems with the SAML 2.0 authentication process. SAML 2.0 redirects URLs to an IdP. When rotating sessions are enabled, any redirection causes the session to rotate and forces the instance to query the IdP again. This situation causes an endless loop of new sessions between the instance and the IdP. | Disable the rotating session feature when using SAML 2.0 for authentication. |
| The token that was used to authenticate the user or the request is signed with the signature algorithm [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256) which is not the expected signature algorithm [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1). Check the **Alert Context** tab for event details. | ADFS | Check the Alert Context tab for event details. | Navigate to the Advanced tab of the Relying Party Trust configuration dialog and verify that the algorithm is set to SHA-1 and not SHA-256. |
| urn:oasis:names:tc:SAML:2.0:status:Responder |  | Check the IdP logs during the respective login attempt. | Instance is expecting to see urn:oasis:names:tc:SAML:2.0:status:Success before any attempt to process the SAMLResponse. Please work with IdP admin to provide related logs so Support can determine what configuration on the instance/IdP needs to be updated. |

## Related
- [[Knowledge Base Articles – Integrations]]
- [[Conversational integration with Microsoft Teams -]]
- [[Integration Design - How to choose the best patter]]

- [[Integrations – SAML]]
- [[Enable Engagement Messenger on a website when thir]]
- [[SSO – SAML]]
- [[Multi-provider SSO]]