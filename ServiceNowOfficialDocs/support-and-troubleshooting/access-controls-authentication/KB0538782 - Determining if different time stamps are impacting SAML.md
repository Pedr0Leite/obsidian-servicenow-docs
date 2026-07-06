---
title: "Determining if different time stamps are impacting SAML "
aliases:
  - KB0538782
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - clock-skew
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538782
kb_number: KB0538782
last_modified: 2024-05-19
---

## Issue

Troubleshooting: Determining if different time stamps are impacting SAML

  

# Problem

* * *

A user cannot log in to the system with SAML.

# Symptoms

* * *

-   No user can log in to the system.
-   The user cannot validate SAML response.

# Cause

* * *

If a user cannot log in with SAML, this may be caused by different time stamps that are affecting SAML, such as ADFS time skew. During the SAML login flow, the response is validated if it is generated in a short time range, called "clock skew**"**. The log is rejected if the response is outside of this range. The error message below may appear in the log: 

_Assertion is valid in the future, now: 2014-05-12XXXXXX_

or

_Assertion is expired, now: 2013-05-12XXXXXX_

# Resolution

* * *

To solve the issue:

1.  Set a different value for **clock skew**.
2.  Ask users to try to log in again. 
3.  If users still cannot log in, check with the IdP administrator to determine if the IdP server clock is set correctly.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538786 - Determining if the user has an older version of SAML]]
