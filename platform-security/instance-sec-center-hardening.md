---
title: Check the daily compliance score and configure security property settings
description: Review the Daily Compliance Score metric and security configuration properties to see if your instance complies with the suggested security requirements. You can affect the daily compliance score by updating non-compliant security properties in the Hardening Compliance Configurations page.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-sec-center-hardening.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Instance Security Center, Platform Security]
---

# Check the daily compliance score and configure security property settings

Review the Daily Compliance Score metric and security [[sc-configuration|configuration]] properties to see if your instance complies with the suggested security requirements. You can affect the daily compliance score by updating non-compliant security properties in the Hardening Compliance Configurations page.

**Important:**

Instance Security Center \(ISC\) has reached the end of sales as of September 2024, and is no longer supported or available for new activation.

ServiceNow [[sec-center-v2|Security Center]] \(SSC\) is the recommended solution going forward. For more information, see [[instance-security-center-to-security-center-migration|Instance Security Center to ServiceNow Security Center migration]].

The Daily Compliance Score is a percentage score. It is based on how compliant the current settings of your instance security properties are with the compliance values published in the [Hardening settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/security-hardening-settings.md).

Review the daily compliance score of your instance regularly. Follow these guidelines when you are evaluating your daily compliance score:

-   Greater than or equal to 90% indicates that the instance is compliant with critical security controls.
-   Greater than or equal to 50% and less than 90% indicates a moderate level of security compliance.
-   Less than 50% indicates a low level of security compliance.

-   **[[update-security-hardening-params|Adjust instance security settings to increase compliance]]**  
Using the Hardening Compliance Configuration page, harden and optimize non-compliant security properties that affect the daily compliance score of your instance. Its use ensures that your instance complies with the published [[sc-hardening|security hardening]] standards, while fulfilling your company's security requirements.
-   **[[how-daily-compl-score-trend-date-refreshed|How Daily Compliance score, trend, and graph data is refreshed]]**  
Trend and graph data in the Instance Security Center is updated after the performance analytics job executes at 02:00 local time. It appears in the Daily Compliance Score tile, in the Event ribbon tiles, and in the KPI Details page detail.
-   **[[pci-comp-score-dashboard|PCI compliance score dashboard]]**  
The PCI compliance score dashboard shows how your instance conforms to payment card industry \(PCI\) security standards. Use the dashboard to view your compliance score and modify your configuration to improve security.
-   **[[pci-config-controls-dashboard|PCI configuration controls score dashboard]]**  
Use the PCI configuration controls score dashboard to review your PCI configuration and determine which security checks are non-compliant. You can change the configuration of the non-compliant security checks from the instance security center.

**Parent Topic:**[[instance-security-center|Instance Security Center]]

**Related topics**  


[Instance Security Center to ServiceNow Security Center migration]()

[Monitor security events]()

[Scan for incorrect security definitions]()

[Monitor instance metrics]()

[Activate the ISC Virtual Agent interface]()

## Related

- [[instance-security-center-to-security-center-migration|Instance Security Center to ServiceNow Security Center migration]]
- [[update-security-hardening-params|Adjust instance security settings to increase compliance]]
- [[how-daily-compl-score-trend-date-refreshed|How Daily Compliance score, trend, and graph data is refreshed]]
- [[pci-comp-score-dashboard|PCI compliance score dashboard]]
- [[pci-config-controls-dashboard|PCI configuration controls score dashboard]]
- [[instance-security-center|Instance Security Center]]
- [[sc-configuration|Configuration]]
- [[sec-center-v2|Security Center]]
- [[sc-hardening|Security hardening]]
