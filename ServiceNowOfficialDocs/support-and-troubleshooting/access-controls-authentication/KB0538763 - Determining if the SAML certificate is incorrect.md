---
title: "Determining if the SAML certificate is incorrect"
aliases:
  - KB0538763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538763
kb_number: KB0538763
last_modified: 2025-10-21
---

## Issue

This issue is related to SAML certificates and how to proceed when a user cannot log in through SAML SSO.  
  

### Symptoms

-   No users can log in to the system.
-   A single user cannot log in to the system.
-   The user cannot not validate SAML response.
-   The user cannot log in after a clone.

## Resolution

1.  Check if a single SAML SSO or multi-SSO is in use.
2.  If using a single SAML SSO, make sure the certificate, SAML 2.0, exists and has the correct certificate content.
3.  When using a multi-SSO, make sure the certificate associated with the SSO configuration has the correct certificate content. If necessary, contact the IdP administrator for the certificate.
4.  In the certificate form, the type is set to Trust Store Cert. The PEM Certificate should be filled in if the format is PEM.
5.  If using the DER format, attach the certificate binary file.
6.  Once the certificate is corrected, try logging in to SAML again.

For more detailed information on the steps to replace or reinstall a certificate, see [Replacing a Missing Certificate](https://docs.servicenow.com/csh?topicname=t_ReplacingAMissingCertificate.html&version=latest "Replacing a Missing Certificate") and [Install the IdP Certificate](https://docs.servicenow.com/csh?topicname=t_CreateASAML2Upd1SSOConfigMultiSSO.html&version=latest "Install the IdP Certificate") in the ServiceNow product documentation.
