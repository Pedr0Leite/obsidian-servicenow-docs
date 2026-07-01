---
title: Log session audit events
description: Use a system property to enable creations of session audit events
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-security-hardening-settings/sc-log-session-audit-events.html
release: australia
product: Instance Security Hardening Settings
classification: instance-security-hardening-settings
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Error handling and logging, Hardening settings, Platform Security]
---

# Log session audit events

Use a system property to enable creations of session audit events

When the **glide.authenticate.session\_access.log\_audit\_event** system property is set to **true**, session audit events are created in the sys\_session\_access\_audit table. Information logged will include user, session ID \(non-sensitive\), IP address, roles, and [[ca-policies|policies]].

Ensure the that the property **glide.authenticate.session\_access.log\_audit\_event** is set to **true**.

**Important:** The **glide.authenticate.session\_access.log\_audit\_event** system property is specific to Zero trust access. For more information, see [[session-access|Zero Trust Access \(ZTA\)]].

## More information

<table id="table_ajc_b43_3kb"><thead><tr><th>

Attribute

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[sc-configuration|Configuration]] name

</td><td>

**glide.authenticate.session\_access.log\_audit\_event**

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

[Error handling and logging](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-error-handling-logging.md)

</td></tr><tr><td>

Security risk

</td><td>

-   Severity score: 6.3
-   CVSS score: Medium
-   Security risk details: Information about who accessed a session will not be logged to assist in incident investigations.

</td></tr><tr><td>

Dependencies and prerequisites

</td><td>

None

</td></tr></tbody>
</table>**Parent Topic:**[Error handling and logging](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/sc-error-handling-logging.md)

## Related

- [[session-access|Zero Trust Access \(ZTA\)]]
- [[ca-policies|Policies]]
- [[sc-configuration|Configuration]]
- [[ca-system-properties|System properties]]
