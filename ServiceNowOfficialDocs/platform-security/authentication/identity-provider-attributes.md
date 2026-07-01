---
title: Identity Provider Attributes Filter
description: Use the Identity Provider attributes that are received from the Security Assertion Markup Language \(SAML\) response and OpenID Connect \(OIDC\) from the Identity Provider \(IdP\) as a filter criteria for authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/identity-provider-attributes.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Filter criteria, Adaptive authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# Identity Provider Attributes Filter

Use the [[identity-landing|Identity]] Provider attributes that are received from the Security Assertion Markup Language \([[c_SAML2.0WebBrowserSSOProfile|SAML]]\) response and OpenID Connect \(OIDC\) from the Identity Provider \(IdP\) as a [[adaptive-auth-filter-criteria|filter criteria]] for [[c_Authentication|authentication]].

To fetch all the attributes from an IdP through the SAML and OIDC response, you should perform a test connection with the IdP. After a successful test connection, the attributes are added in a new tab in the Identity Provider [[sc-configuration|configuration]] page.

For more information see the following topics:

-   [Identity Provider attributes for Security Assertion Markup Language](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/idp-attributes-saml.md)
-   [Identity Provider attributes for OpenID Connect](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/idp-attributes-oidc.md)

## Related

- [[identity-landing|Identity]]
- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[c_Authentication|Authentication]]
- [[sc-configuration|Configuration]]
