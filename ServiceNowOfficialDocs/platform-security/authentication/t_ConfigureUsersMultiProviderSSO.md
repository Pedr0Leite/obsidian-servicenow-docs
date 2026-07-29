---
title: Configure users for Multi-Provider SSO
description: Administrators can configure Multi-Provider SSO for individual users or for all users who belong to a company. You cannot configure Multi-Provider SSO for groups.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/t\_ConfigureUsersMultiProviderSSO.html
release: australia
product: Authentication
classification: authentication
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multi-Provider SSO configurations, Multi-Provider single sign-on \(SSO\), Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-task
---

# Configure users for Multi-Provider SSO

Administrators can configure Multi-Provider SSO for individual [[users|users]] or for all users who belong to a company. You cannot configure Multi-Provider SSO for groups.

## Before you begin

Role required: sso\_config\_admin, business\_rule\_admin, script\_include\_admin

## Procedure

1.  Navigate to **All** &gt; **Multi-Provider SSO** &gt; **[[identity-landing|Identity]] Providers**.

2.  Right-click an identity provider record and select **Copy sys\_id**.

3.  Copy the data to your clipboard.

4.  Navigate to a user record or a company record.

5.  Configure the form and add the **SSO Source** field.

6.  In the **SSO Source** field, enter one of the following:

    -   **[[c_SAML2.0WebBrowserSSOProfile|SAML]] users**: enter **sso:** followed by the sys\_id of the identity provider's record.
    -   **SSO Federation users**: enter **federation:** followed by the sys\_id of the federation record.
7.  Click **Update**.

## Related

- [[users|Users]]
- [[identity-landing|Identity]]
- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
