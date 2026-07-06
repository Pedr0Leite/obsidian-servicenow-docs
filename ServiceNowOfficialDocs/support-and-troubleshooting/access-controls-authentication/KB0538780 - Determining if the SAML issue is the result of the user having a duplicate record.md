---
title: "Determining if the SAML issue is the result of the user having a duplicate record"
aliases:
  - KB0538780
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - sys_user
  - duplicate-record
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538780
kb_number: KB0538780
last_modified: 2025-10-21
---

## Issue

Troubleshooting: Determining if the SAML issue is the result of the user having a duplicate record

The user cannot log in to the system or log in as the correct user.

## Resolution

  To solve the issue:

1.  Check the SAML logs to find out which user ID is being used. 
2.  Look up the **sys\_user** table, and check if there are duplicate user records with the same user ID.
3.  If so, delete the duplicate record.
4.  Ask the user to try to log in again.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538770 -  Determining if the SAML issue is the result of a user being locked out]]
- [[KB0538781 - Determining if an SAML issue is caused by leading or trailing spaces]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538781 - Determining if an SAML issue is caused by leading or trailing spaces|Determining if an SAML issue is caused by leading or trailing spaces]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
