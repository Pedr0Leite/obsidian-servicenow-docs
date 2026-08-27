---
title: Enforce SOAP request strict security
description: Use the glide.soap.strict\_security property to enforces web service security.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-security-hardening-settings/sc-soap-request-strict-security.html
release: australia
product: Instance Security Hardening Settings
classification: instance-security-hardening-settings
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Access control, Hardening settings, Platform Security]
tags:
  - platform-security
  - hardening
  - security
  - checklist
  - settings
  - type-reference
---

# Enforce SOAP request strict security

Use the **glide.soap.strict\_security** property to enforces [[c_WebServiceSecurity|web service security]].

If the **glide.soap.strict\_security** system property is not set to the recommended value of **true**, then [[users|users]] do not need a SOAP role to make requests of non-public pages when the high security or web service plugin is installed.

Ensure the property **glide.soap.strict\_security** is set to **true**.

## More information

<table id="table_ajc_b43_3kb"><thead><tr><th>

Attribute

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[sc-configuration|Configuration]] name

</td><td>

**glide.soap.strict\_security**

</td></tr><tr><td>

Configuration type

</td><td>

[[ca-system-properties|System Properties]] \(/sys\_properties\_list.do\)

</td></tr><tr><td>

Data type

</td><td>

Boolean

</td></tr><tr><td>

Recommended value

</td><td>

true

</td></tr><tr><td>

Default value

</td><td>

&lt;none&gt;

</td></tr><tr><td>

Fallback value

</td><td>

true

</td></tr><tr><td>

Category

</td><td>

[Access control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-access-control.md)

</td></tr><tr><td>

Security risk

</td><td>

-   Severity score: 6.8
-   CVSS rating: Medium
-   Security risk details: An unauthorized user can get access to sensitive content/data on the target instance.

</td></tr><tr><td>

Functional impact

</td><td>

None

</td></tr><tr><td>

Dependencies and prerequisites

</td><td>

None

</td></tr></tbody>
</table>To learn more about adding or creating a system property, see [Add a system property](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_AddAPropertyUsingSysPropsList.md).

**Parent Topic:**[Access control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-access-control.md)

## Related

- [[c_WebServiceSecurity|Web service security]]
- [[users|Users]]
- [[sc-configuration|Configuration]]
- [[ca-system-properties|System properties]]
