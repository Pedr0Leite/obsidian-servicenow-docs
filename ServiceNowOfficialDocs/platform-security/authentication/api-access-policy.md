---
title: API access policy
description: API access policy defines the permissions and duration of access to an API.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/api-access-policy.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# API access policy

API access policy defines the permissions and duration of access to an API.

API access policy enables you to restrict access to inbound ServiceNow® APIs based on the [[c_Authentication|authentication]] type and the specified [[adaptive-auth-filter-criteria|filter criteria]] of the access policy.

Following are the three level auth policy support for the non-interactive sessions:

-   **REST API**: Admin can define a global API auth policy or API specific auth policy.
-   **SOAP API**: Admin can define a global API auth policy or API specific auth policy.
-   **System/Export Processor**: Admin can define five base system auth profiles, which can be used to apply auth profile to processors API auth policy or processor specific auth policy.

**Note:** If you add a global auth policy, then the policy applies for all the REST APIs, SOAP APIs, or System/Export Processors.

Following are the plugins auto-installed for API [[ca-policies|policies]] and authentication scope:

-   com.glide.rest.policy
-   com.glide.soap.policy
-   com.glide.processor.policy
-   com.glide.rest.auth.scope

You can configure the default Global Blocking Policy or create a custom API access policy according to your security requirements. And apply filter criteria that contain filter conditions or queries that are used as policy inputs for an authentication policy.

The following API access policies are supported in ServiceNow®:

-   [REST API access policies](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/inbound-authentication-profile.md)
-   [SOAP API access policies](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/soap-api-access-policies.md)

For information about policies related to [[export|export]] processors, see [Access policy for System or Export Processors](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/api-auth-policy-export-processors.md).

## Related

- [[c_Authentication|Authentication]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[ca-policies|Policies]]
- [[export|Export]]
