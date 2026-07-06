---
title: "Determining if an SAML issue is caused by leading or trailing spaces"
aliases:
  - KB0538781
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - sys_user
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538781
kb_number: KB0538781
last_modified: 2024-10-17
---

## Issue

A single user cannot log in to the system with SAML.

### Symptoms

-   One user cannot log in.
-   Other users can log in, with the exception of a single user.

## Resolution

To solve the issue:

1.  Locate the user ID in the SAML logs.
2.  Find the user in the sys\_user table, and determine if the user ID has leading or trailing spaces.
3.  If so, remove the leading or trailing spaces, and click Save.
4.  Ask the user to try to log in again.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538770 -  Determining if the SAML issue is the result of a user being locked out]]
- [[KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record|Determining if the SAML issue is the result of the user having a duplicate record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
