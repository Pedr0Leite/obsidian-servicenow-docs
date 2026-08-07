---
title: Old Inbound integrations experience
description: Old experience - Inbound integrations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/old-inbound-integrations.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [OAuth Inbound, OAuth authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# Old Inbound integrations experience

Old experience - [[inbound-integrations|Inbound integrations]].

**Note:**

You can perform the [[oauth-inbound|OAuth inbound]] [[sc-configuration|configuration]], depending on the following type of grant type:

-   [OAuth authorization code grant flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/c_OAuthAuthorizationCodeFlow.md)

    **Note:** For authorization code flow, user needs to complete the [[c_Authentication|Authentication]] by local login, SSO or MFA and then provide consent.

-   [Password grant](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/t_AuthorizeAccessEndpiont.md)
-   [JWT bearer grant flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/create-jwt-endpoint.md)
-   [ID token flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/add-OIDC-entity.md)
-   [OAuth implicit grants](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/c_OAuthImplicitGrants.md)
-   [Client Credentials](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/client-credentials.md)

Configure [[oauth-inbound-and-outbound|OAuth]] integration that includes the following enhancements from Zurich release:

-   Increase client secret length up-to 4096 characters to meet security requirements of third-party systems.
-   Provide a JSON Web Key Set \(JWKS\) URL to automatically manage and update the public key for JSON Web Tokens \(JWT\) signature validation.
-   [[c_requestAPI|Request]] OAuth tokens using the JWT grant type signed with Elliptic Curve Digital Signature Algorithm \(ES\) signing algorithms, including ES256, ES384, and ES512, for inbound JSON Web Tokens \(JWT\).
-   Customize the JWT ID \(JTI\) claim name in both inbound OpenID Connect \(OIDC\) and [[jwt-bearer|JWT Bearer]] flows.

## Related

- [[inbound-integrations|Inbound integrations]]
- [[oauth-inbound|OAuth Inbound]]
- [[sc-configuration|Configuration]]
- [[c_Authentication|Authentication]]
- [[oauth-inbound-and-outbound|OAuth]]
- [[c_requestAPI|request]]
- [[jwt-bearer|JWT Bearer]]
