---
title: MFA Metrics
description: View the different MFA metrics to understand the MFA adoption and usage.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/mfa-metrics.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring MFA, Multi-factor authentication, Authentication, Access Management]
---

# MFA Metrics

View the different [[faq-familiar-with-mfa|MFA metrics]] to understand the MFA adoption and usage.

MFA related [[ca-metrics|metrics]] are available in [[sec-center-v2|Security Center]]. Security Center is a free application that you can download from the ServiceNow Store. For more information about Security Center, see [Security Center landing page](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sec-center-landing.md).

On Security Center, use the bar at the top of the page to navigate between the [[sc-monitor-console|security monitoring console]] sections and select **[[sc-metrics|Security Metrics]]** tab.

Following are the MFA metrics:

-   [[users|Users]] enrolled for MFA: Total count of users enrolled to use MFA.
-   Users using MFA bypass: Total count of users who are circumventing multi factor [[c_Authentication|authentication]].
-   High privileged non-mfa user: Total count of high-[[privileged-users|privileged users]] that are not using MFA.
-   Active MFA users: Total count of MFA users that are active on your instance.
-   Locked out MFA users: Total count of MFA users who are locked out on your instance.
-   Local logins not protected by MFA: Users that logged in without MFA.

For more information about Security Metrics, see [Security metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-metrics.md).

## Related

- [[faq-familiar-with-mfa|MFA metrics]]
- [[ca-metrics|Metrics]]
- [[sec-center-v2|Security Center]]
- [[sc-monitor-console|Security monitoring console]]
- [[sc-metrics|Security metrics]]
- [[users|Users]]
- [[c_Authentication|Authentication]]
- [[privileged-users|Privileged Users]]
