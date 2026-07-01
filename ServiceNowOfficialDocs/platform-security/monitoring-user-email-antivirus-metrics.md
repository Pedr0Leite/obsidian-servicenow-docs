---
title: Monitor instance metrics
description: Monitor user, export, authentication, email, and antivirus metrics for your instance. For example, you can monitor your email security by checking metrics for spam, external emails, and inbound emails from untrusted and trusted domains for your instance. Analyze these metrics to look for anomalous security behaviors that are related to activities that take place in your instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/monitoring-user-email-antivirus-metrics.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Instance Security Center, Platform Security]
tags:
  - platform-security
  - type-concept
---

# Monitor instance metrics

Monitor user, [[export|export]], [[c_Authentication|authentication]], [[email|email]], and antivirus metrics for your instance. For example, you can monitor your email security by checking [[ca-metrics|metrics]] for spam, external emails, and inbound emails from untrusted and trusted domains for your instance. Analyze these metrics to look for anomalous security behaviors that are related to activities that take place in your instance.

**Important:**

Instance Security Center \(ISC\) has reached the end of sales as of September 2024, and is no longer supported or available for new activation.

ServiceNow [[sec-center-v2|Security Center]] \(SSC\) is the recommended solution going forward. For more information, see [[instance-security-center-to-security-center-migration|Instance Security Center to ServiceNow Security Center migration]].

-   **[[instance-sec-center-user-metrics|User metrics]]**  
Analyze user metrics to look for anomalous behaviors that are related to specific types of user activity in your instance.
-   **[[instance-sec-center-export-metrics|Export metrics]]**  
Analyze export metrics to see what data is most commonly exported and which [[users|users]] export the most data.
-   **[[instance-sec-center-auth-metrics|Authentication Metrics]]**  
Analyze authentication metrics to see information related to authentication, such as infrequently used IP addresses, failed logins, and types of authentication schemes used by your users.
-   **[[instance-sec-center-adaptive-auth-metrics|Adaptive authentication metrics]]**  
Analyze adaptive authentication metrics to monitor and add insights on how [[adaptive-authentication|adaptive authentication]] is being used on your instance.
-   **[[instance-sec-center-email-metrics|Email metrics]]**  
Analyze your email metrics to look for anomalous behaviors that are related to the incoming emails to your instance. For example, if the metrics indicate a spike in spam emails from specific domains, you can define inbound actions that prevent their delivery to the instance.
-   **[[instance-sec-center-antivirus-metrics|Antivirus metrics]]**  
If the [[antivirus-protection|Antivirus Scanning]] plugin is activated, Antivirus Scanning runs in your instance to help protect it against virus infections from attachments.
-   **[[mfa-metrics-dashboard|MFA metrics dashboard]]**  
The MFA metrics dashboard shows information on your instances [[mfa-landing|multi-factor authentication]] [[sc-configuration|configuration]]. Use the dashboard to ensure your MFA configuration meets your security standards.

**Parent Topic:**[[instance-security-center|Instance Security Center]]

**Related topics**  


[Instance Security Center to ServiceNow Security Center migration]()

[Monitor security events]()

[Check the daily compliance score and configure security property settings]()

[Scan for incorrect security definitions]()

[Activate the ISC Virtual Agent interface]()

## Related

- [[instance-security-center-to-security-center-migration|Instance Security Center to ServiceNow Security Center migration]]
- [[instance-sec-center-user-metrics|User metrics]]
- [[instance-sec-center-export-metrics|Export metrics]]
- [[instance-sec-center-auth-metrics|Authentication Metrics]]
- [[instance-sec-center-adaptive-auth-metrics|Adaptive authentication metrics]]
- [[instance-sec-center-email-metrics|Email metrics]]
- [[instance-sec-center-antivirus-metrics|Antivirus metrics]]
- [[mfa-metrics-dashboard|MFA metrics dashboard]]
- [[instance-security-center|Instance Security Center]]
- [[export|Export]]
- [[c_Authentication|Authentication]]
- [[email|Email]]
- [[ca-metrics|Metrics]]
- [[sec-center-v2|Security Center]]
- [[users|Users]]
- [[adaptive-authentication|Adaptive authentication]]
- [[antivirus-protection|Antivirus Scanning]]
- [[mfa-landing|Multi-factor authentication]]
- [[sc-configuration|Configuration]]
