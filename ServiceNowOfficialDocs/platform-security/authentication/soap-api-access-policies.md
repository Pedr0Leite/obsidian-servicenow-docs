---
title: SOAP API access policies
description: SOAP API access policies allow you to restrict access to inbound SOAP APIs based on the authentication type and the specified filter criteria of the access policy.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/soap-api-access-policies.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [API access policy, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# SOAP API access policies

SOAP API access policies allow you to restrict access to inbound SOAP APIs based on the [[c_Authentication|authentication]] type and the specified [[adaptive-auth-filter-criteria|filter criteria]] of the access policy.

The SOAP API access policies enables you to have the ability to apply the inbound authentication profile and API access [[ca-policies|policies]] to inbound SOAP and scripted SOAP APIs.

You can leverage ServiceNow API access policies like IP range and role based restrictions to allow or disallow inbound SOAP API calls based on the authentication.

As an admin, you can perform the following actions to apply the policies.

-   [[activate-soap-api-access-policy|Activate SOAP API Access Policy]] and Authentication Profile plugins. For more information, see [Activate SOAP API access policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/activate-soap-api-access-policy.md).
-   Create SOAP API Access Policies and associate those policies with an authentication profile. For more information, see [Create SOAP API access policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/create-soap-api-access-policy.md) and [Create an authentication profile](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/create-an-authentication-profile.md).

    **Note:** The policies are applicable to SOAP table API or scripted SOAP API. Besides the standard `http` and `WSSE` authentication profile.

-   Create [[authentication-policies|authentication policies]] such as IP range, role-based restrictions and associate this policy to the authentication profile. For more information, see [Create an API authentication policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/create-api-authentication-policy.md).

## Related

- [[c_Authentication|Authentication]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[ca-policies|Policies]]
- [[activate-soap-api-access-policy|Activate SOAP API access policy]]
- [[authentication-policies|Authentication policies]]
