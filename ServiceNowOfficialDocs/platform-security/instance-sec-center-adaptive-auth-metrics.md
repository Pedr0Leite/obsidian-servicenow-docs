---
title: Adaptive authentication metrics
description: Analyze adaptive authentication metrics to monitor and add insights on how adaptive authentication is being used on your instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-sec-center-adaptive-auth-metrics.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Monitor instance metrics, Instance Security Center, Platform Security]
tags:
  - platform-security
  - type-concept
---

# Adaptive authentication metrics

Analyze adaptive authentication metrics to monitor and add insights on how [[adaptive-authentication|adaptive authentication]] is being used on your instance.

View reports, settings, and [[ca-policies|policies]] associated with adaptive authentication in on place using the adaptive authentication metrics page. Security administrators can use reports to monitor the results of their adaptive authentication policies. Use this data to gain insights and adapt your policies to improve their performance.

**Note:** The adaptive authentication metrics page requires the **Adaptive Authentication** \(com.snc.adaptive\_authentication\) plugin. For more details about this feature, see [Adaptive authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/adaptive-authentication.md).

## Metrics

\[Omitted image "isc-adaptive-auth.png"\] Alt text: Adaptive authentication metrics page in the [[instance-security-center|instance security center]]

Use the **[[ca-metrics|Metrics]]** tab to view reports relating to your adaptive authentication [[sc-configuration|configuration]]. The following reports are displayed in this tab.

-   Policy Results Rates
-   Event Failure Distribution
-   Event Success Distribution
-   Denied IP Addresses
-   [[c_Authentication|Authentication]] User Logins
-   API User Logins
-   Authentication Trend

Use the **Show** list to select a time span for the displayed reports

## Adaptive Auth Policies

Use the **Adaptive Auth Policies** tab to view the adaptive authentication policies and policy contexts on your instance. Click on any entry on these lists to view the associated record. For more details on these records, see [Adaptive authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/adaptive-authentication.md)

## Settings

Use the settings tab to view and configure adaptive authentication [[ca-system-properties|system properties]]. For more information on these properties, see [Configure adaptive authentication properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/configure-adaptive-auth-properties.md)

**Parent Topic:**[[monitoring-user-email-antivirus-metrics|Monitor instance metrics]]

## Related

- [[monitoring-user-email-antivirus-metrics|Monitor instance metrics]]
- [[adaptive-authentication|Adaptive authentication]]
- [[ca-policies|Policies]]
- [[instance-security-center|Instance Security Center]]
- [[ca-metrics|Metrics]]
- [[sc-configuration|Configuration]]
- [[c_Authentication|Authentication]]
- [[ca-system-properties|System properties]]
