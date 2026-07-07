---
title: " Determining if ADFS is receiving a signed request"
aliases:
  - KB0538765
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - adfs
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538765
kb_number: KB0538765
last_modified: 2025-10-21
---

## Issue

Determining if ADFS is receiving a signed request

This issue is related to an ADFS-signed SAML request. The user cannot log in or log out.

## Resolution

1.  Check with the ADFS administrator to see if ADFS enforces the signed request.
2.  If so, create a correct Java key store certificate record in SNC that includes the certificate from ADFS.
3.  Set glide.authenticate.sso.saml2.idp\_authnrequest\_url to **true** if the authentication request signing is required, and set to ADFS.Set glide.authenticate.sso.saml2.require\_signed\_logoutrequest to **true** if the log out request signing is required. Fill in the correct alias user/password and key store user/password.
4.  If necessary, re-import the SAML SP (SNC) metadata into ADFS (IDP)

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538763 - Determining if the SAML certificate is incorrect]]
- [[t_TestTheADFSConfiguration]] - official docs on testing the ADFS configuration
- [[t_SetUpServiceNowForADFS]] - official docs on setting up ServiceNow for ADFS
- [[t_ConfigureADFSClaimRules]] - official docs on configuring ADFS claim rules

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow|Troubleshooting SAML or SSO issues in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record|Determining if the SAML issue is the result of the user having a duplicate record]]
