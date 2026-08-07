---
title: E-signature for Multi-Provider SSO
description: E-signature with Multi-Provider SSO enables you to use the e-signature properties instead the SAML or OIDC properties for authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/e-signature-for-multi-provider-sso.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multi-Provider SSO configurations, Multi-Provider single sign-on \(SSO\), Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# E-signature for Multi-Provider SSO

E-signature with Multi-Provider SSO enables you to use the e-signature properties instead the [[c_SAML2.0WebBrowserSSOProfile|SAML]] or OIDC properties for [[c_Authentication|authentication]].

For single sign-on \(SSO\) verification during authentication and to require [[users|users]] to provide credentials before submitting their electronic signature, you can configure the authentication to prompt for user credentials before submitting a signature.

You can install the Approvals with e-signature \(`com.glide.e_signature_approvals`\) plugin to have the E-signature [[sc-configuration|configuration]] for SSO logins.

**Note:** You must install the [[code-signing-landing|Code Signing]] Signatures \(`com.glide.code_signing.signatures`\) to install the E-signature plugin.

## Related

- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
- [[c_Authentication|Authentication]]
- [[users|Users]]
- [[sc-configuration|Configuration]]
- [[code-signing-landing|Code Signing]]
