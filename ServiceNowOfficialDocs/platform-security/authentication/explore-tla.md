---
title: Explore Time limited authentication
description: Support time limited authentication for your ServiceNow instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/explore-tla.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Time limited authentication, Token based authentication \(User logins\), Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# Explore Time limited authentication

Support [[time-limited-authentication|time limited authentication]] for your ServiceNow instance.

**Note:** Time limited authentication is very specific to ServiceNow instance, the customized links for [[users|users]] can only be created within ServiceNow.

Admins can configure link based [[c_Authentication|authentication]] on the ServiceNow instance. The configured link can be shared with the user through [[email|Email]] or SMS and user can use those links to log in to the instance.

Login to instance with this authentication scheme is controlled through [[adaptive-authentication|Adaptive Authentication]] [[ca-policies|policies]] configured on the ServiceNow instance.

Time based authentication enables you to perform the following:

-   Admin can configure link based auth to use it within an expiry time.
-   Application team can fetch nonce to be used with link for the specific [[sc-configuration|configuration]] item using exposed scriptable API. Link generation will be taken care by Application team.
-   Application team can generate the link and send to the user through an existing channel.
-   User with the link can log in to instance one time and within expiry time specified as part of configuration.
-   Admins can configure the low privileged roles for the authentication scheme.
-   Admins can enforce MFA for the authentication scheme as a second factor for authentication with the TLA link.

## Related

- [[time-limited-authentication|Time limited authentication]]
- [[users|Users]]
- [[c_Authentication|Authentication]]
- [[email|Email]]
- [[adaptive-authentication|Adaptive authentication]]
- [[ca-policies|Policies]]
- [[sc-configuration|Configuration]]
