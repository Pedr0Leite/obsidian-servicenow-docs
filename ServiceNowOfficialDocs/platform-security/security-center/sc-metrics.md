---
title: Security metrics
description: Monitor over 50 different Security Metrics to identify potential security threats or insecure behaviors. Set thresholds for email notifications, visualize, and analyze the data in multiple ways. Export the data, or create dashboards with the metrics that are most important to your organization.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/security-center/sc-metrics.html
release: australia
product: Security Center
classification: security-center
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Security monitoring console, Security Center, Platform Security]
tags:
  - platform-security
  - security-center
  - posture
  - compliance
  - risks
  - type-concept
---

# Security metrics

Monitor over 50 different Security Metrics to identify potential security threats or insecure behaviors. Set thresholds for [[email|email]] notifications, visualize, and analyze the data in multiple ways. [[export|Export]] the data, or create dashboards with the [[ca-metrics|metrics]] that are most important to your organization.

\[Omitted image "sc-metrics-1.png"\] Alt text: Security metrics

Access Security Metrics within [[sec-center-v2|Security Center]] by selecting **Security Monitoring** in the tools section. Then, select the **Security metrics** card.

## All Security Metrics dashboard

View metrics such as failed logins, exports, impersonations, and more using this dashboard. The cards above the list provide a count of the metrics that match specific criteria listed on the card. Select any of these cards to filter the list to show only those metrics that match the criteria.

Select the **+Create task** button to create a Security Task related to a metric. For details on [[security-task-manager|Security Tasks]], see [Security Tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/security-task-manager.md).

## My metrics dashboard

This is a customizable dashboard that displays information about metrics you care about most. Select **Edit** to customize your dashboard by adding visualizations, filters, headings, images, rich text, and lists. To learn about the various ways you can customize your dashboard, see [Dashboards in Platform Analytics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/analytics-center-dashboards.md).

## Metrics navigation pane

The navigation pane on the edge of the screen displays your instance metrics. Select **[[all-security-metrics|All Security Metrics]]** to view all metrics in a single list. Select any of the items under **All Security Metrics** the entry to browse the metrics organized by category.

Each category displays a dashboard similar to the security **My metrics dashboard**, with cards for the metrics in that category.

\[Omitted image "sc-metrics-example.png"\] Alt text: Dashboard for the [[data-classification|data classification]] category

-   **[Customize the My security metrics dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/customize-my-security-metrics-dashboard.md)**  
Discover the flexibility of the My security metrics dashboard, which can be customized with metrics from various sources like graphs and charts. Tailor the dashboard to suit your organization's specific requirements.
-   **[Configure Security Metrics to send email when thresholds are triggered](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/configure-security-metrics-to-send-emails-for-thresholds.md)**  
Learn how to configure Security Metrics so that your instance generates an email notification when a threshold is triggered.
-   **[All Security Metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/all-security-metrics.md)**  
Navigate to **All Security Metrics** to view a table with the data related to the Security Metrics of your instance.
-   **[Active Sessions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-active-sessions.md)**  
View the trend line of the active [[users|users]] on the ServiceNow AI Platform.
-   **[Adaptive authentication Security Metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-adaptive-authentication.md)**  
Use [[authentication-policies|authentication policies]] to evaluate [[c_Authentication|authentication]] requests and deny or allow access to your instance based on the specified policy conditions.
-   **[Antivirus](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/antivirus.md)**  
Displays the trend of when events occur on potentially infected files. See when they are discovered, placed into quarantine, restored, or deleted.
-   **[Authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-metrics-authentication.md)**  
View trends for metrics related to authentication schemes, such as [[mfa-landing|Multi-Factor Authentication]]\(MFA\) use, web service accounts, and biometric scanner usage.
-   **[Data Classification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/data-classification-security-metrics.md)**  
Access the Security Metrics for data classification on your ServiceNow instance.
-   **[Authentication metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/authentication.md)**  
View metrics related to authentication on your instance from a dashboard.
-   **[Email](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/email.md)**  
Displays data related to spam emails that are being received externally.
-   **[Export](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/export.md)**  
Discover the data that is commonly exported, and which users do the exporting.
-   **[Integration Accounts](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/integration-accounts.md)**  
View the trends about the [[integration-accounts|integration accounts]] that are created on the ServiceNow AI Platform.
-   **[Privileged Identity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/privileged-identity.md)**  
Analyze data related to metrics for users with [[privileged-identity|privileged identity]].
-   **[Privileged Users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/privileged-users.md)**  
View the trend line for the [[privileged-users|privileged users]] \(active and inactive\) and their activity on the ServiceNow AI Platform.
-   **[Session management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/session-management.md)**  
View metrics related to user sessions and the frequency of lockouts of the sessions.
-   **[Users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/users.md)**  
View the trend line for total users \(active and inactive\) and their activity on the ServiceNow AI Platform.

**Parent Topic:**[Security monitoring console](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-monitor-console.md)

## Related

- [[email|Email]]
- [[export|Export]]
- [[ca-metrics|Metrics]]
- [[sec-center-v2|Security Center]]
- [[security-task-manager|Security Tasks]]
- [[all-security-metrics|All Security Metrics]]
- [[data-classification|Data Classification]]
- [[users|Users]]
- [[authentication-policies|Authentication policies]]
- [[c_Authentication|Authentication]]
- [[mfa-landing|Multi-factor authentication]]
- [[integration-accounts|Integration Accounts]]
- [[privileged-identity|Privileged Identity]]
- [[privileged-users|Privileged Users]]
