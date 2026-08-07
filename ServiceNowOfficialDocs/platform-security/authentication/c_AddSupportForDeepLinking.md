---
title: Add deep linking support for SAML
description: Deep linking allows instances to support direct email links to a particular record in the system.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/c\_AddSupportForDeepLinking.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Integrating SAML 2.0 with other features, SAML, Multi-Provider single sign-on \(SSO\), Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# Add deep linking support for SAML

Deep linking allows instances to support direct [[email|email]] links to a particular record in the system.

With the [[c_SAML2.0WebBrowserSSOProfile|SAML]] 2.0 integration enabled, deep-linking URLs must pass an [[c_Authentication|authentication]] check before the IdP redirects the user to the originally requested URL. For example, consider an email that contains this URL: `https://<instance name>.service-now.com/nav_to.do?uri=incident.do?sys_id=46c88ac1a9fe1981014de1c831fbcf6d`

The instance sends an authentication [[c_requestAPI|request]] to the IdP and uses the `RelayState` URL parameter to preserve the originally requested resource \(in this case, `uri=incident.do?sys_id=46c88ac1a9fe1981014de1c831fbcf6d`\). After the IdP authenticates the user, the instance reads the value of the RelayState URL parameter and redirects the user to the requested resource \(if it exists in the instance\).

To add support for deep linking verify that the [[identity-landing|identity]] provider supports the `RelayState` URL parameter.

## Related

- [[email|Email]]
- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
- [[c_Authentication|Authentication]]
- [[c_requestAPI|request]]
- [[identity-landing|Identity]]
