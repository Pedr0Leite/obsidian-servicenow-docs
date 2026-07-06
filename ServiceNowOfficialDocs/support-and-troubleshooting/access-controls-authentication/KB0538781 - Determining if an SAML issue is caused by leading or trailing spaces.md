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
