---
title: " Determining if the SAML issue is the result of a user being locked out"
aliases:
  - KB0538770
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - locked-out
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538770
kb_number: KB0538770
last_modified: 2025-10-21
---

## Issue

The user cannot log in to the system, and the account appears to be locked.

## Resolution

To solve the issue:

1.  Open the user account.
2.  Determine if the affected account is locked out. If so, the **Locked out** field should be checked. 
3.  Uncheck the **Locked out** field.
4.  Click **Save**.
5.  Ask the user to try to log in again.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record]]
- [[KB0538781 - Determining if an SAML issue is caused by leading or trailing spaces]]
