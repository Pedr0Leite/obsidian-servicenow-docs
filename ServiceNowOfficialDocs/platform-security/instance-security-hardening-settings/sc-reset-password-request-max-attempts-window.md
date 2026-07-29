---
title: Control Lockout Time for Invalid Password Reset Attempts
description: The password\_reset.request.max\_attempt\_window property controls the number of minutes a user must wait to reset or change their password after exceeding the maximum number of unsuccessful attempts that is set with the password\_reset.request.max\_attempt property.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-security-hardening-settings/sc-reset-password-request-max-attempts-window.html
release: australia
product: Instance Security Hardening Settings
classification: instance-security-hardening-settings
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Authentication, Hardening settings, Platform Security]
tags:
  - platform-security
  - hardening
  - security
  - checklist
  - settings
  - type-reference
---

# Control Lockout Time for Invalid Password Reset Attempts

The **password\_reset.[[c_requestAPI|request]].max\_attempt\_window** property controls the number of minutes a user must wait to reset or change their password after exceeding the maximum number of unsuccessful attempts that is set with the **password\_reset.request.max\_attempt** property.

The **password\_reset.request.max\_attempt\_window** system property defines the number of minutes a user must wait to reset or change their password after exceeding the maximum number of unsuccessful attempts that is set with the **password\_reset.request.max\_attempt** property.

Ensure that the property **password\_reset.request.max\_attempt\_window** is set to 1440 or greater.

## More information

<table id="table_ajc_b43_3kb"><thead><tr><th>

Attribute

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[sc-configuration|Configuration]] name

</td><td>

**password\_reset.request.max\_attempt\_window**

</td></tr><tr><td>

Configuration type

</td><td>

[[ca-system-properties|System Properties]] \(/sys\_properties\_list.do\)

</td></tr><tr><td>

Data type

</td><td>

Integer

</td></tr><tr><td>

Recommended value

</td><td>

An integer greater than or equal to 1440

</td></tr><tr><td>

Default value

</td><td>

&lt;none&gt;

</td></tr><tr><td>

Fallback value

</td><td>

1440

</td></tr><tr><td>

Category

</td><td>

[Authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-authentication.md)

</td></tr><tr><td>

Security risk

</td><td>

-   Severity score:
-   CVSS rating:
-   Security risk details: A value too low increases the risk of successfully brute forcing a password as a greater number of [[c_SelfServicePasswordReset|password reset]] attempts can be made.

</td></tr><tr><td>

Functional impact

</td><td>

None

</td></tr><tr><td>

Dependencies and prerequisites

</td><td>

None

</td></tr></tbody>
</table>**Parent Topic:**[Authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-authentication.md)

## Related

- [[c_requestAPI|request]]
- [[sc-configuration|Configuration]]
- [[ca-system-properties|System properties]]
- [[c_SelfServicePasswordReset|Password Reset]]
