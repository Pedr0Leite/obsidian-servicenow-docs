---
title: "Determining if SAML issues are occurring due to customer scripts no longer working after upgrade"
aliases:
  - KB0538769
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - upgrade
  - customization
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538769
kb_number: KB0538769
last_modified: 2025-10-21
---

## Issue

After a recent instance upgrade, users cannot log in.

### Symptoms

-   No user can log in to the system.
-   One user cannot log in to the system.
-   The user cannot validate SAML response.
-   The deep linking is not working.
-   SAML is not correctly setting CMS redirection.

## Resolution

1.  Check if this occurs after a recent system upgrade.
2.  If so, confirm that the SAML2 scripts are up to date by checking the history.
3.  If any scripts were not upgraded, check with the administrator to determine what changes have been made to the scripts. 
4.  Revert to OOB scripts and apply the necessary changes or customizations, if needed.
5.  Ask users to try to log in again.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538786 - Determining if the user has an older version of SAML]]
- [[t_TroubleshootScriptIssuesWithSAML]] - official docs on troubleshooting SAML script issues

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538786 - Determining if the user has an older version of SAML|Determining if the user has an older version of SAML]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record|Determining if the SAML issue is the result of the user having a duplicate record]]
