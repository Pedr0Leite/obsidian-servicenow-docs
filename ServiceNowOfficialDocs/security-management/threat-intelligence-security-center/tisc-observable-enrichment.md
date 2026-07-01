---
title: Observable Enrichment
description: The Enrich Observable WhoIs workflow performs enrichment on selected observables. If the observables are of a type recognized by the WhoisXML API Integration, the observables are enriched.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/tisc-observable-enrichment.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Run Enrichment operations in TISC, Observables, TISC Library Repository, Threat Intelligence Security Center Library, Use, Threat Intelligence Security Center, Security Operations]
tags:
  - security-management
  - threat-intelligence
  - stix
  - taxii
  - iocs
  - type-concept
---

# Observable Enrichment

The [[enrich-observable-whois-wf|Enrich Observable WhoIs workflow]] performs enrichment on selected [[c_Observables|observables]]. If the observables are of a type recognized by the [[whois-landing-page|WhoisXML API Integration]], the observables are enriched.

**Note:** The [[tisc-landing-page|Threat Intelligence Security Center]] supports Observable Enrichment only for the [[tisc-whoisxml-integration|WHOIS Integration]].

-   **[Run Have I Been Pwned enrichment integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-hibp-enrichment-integration.md)**  
Run the Have I Been Pwned \(HIBP\) enrichment on an email address or domain name observable to determine whether it has been involved in a known data breach.
-   **[Whois integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-whoisxml-integration.md)**  
Submit Whois lookups on domain names and URLs to gather [[threat-intel-landing-page|threat intelligence]] and assess potential security risks. Use this integration to obtain registration details, ownership information, and other contextual data for suspicious domains.
-   **[Shodan integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-shodan.md)**  
Configure [[shodan-lookups|Shodan integration]] to enable automated discovery and analysis of internet-connected devices in your network [[threat-intelligence-infrastructure|infrastructure]].

**Parent Topic:**[Run Enrichment operations in TISC](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-unified-experience-capabilities-and-modal-screens.md)

## Related

- [[enrich-observable-whois-wf|Enrich Observable WhoIs workflow]]
- [[c_Observables|Observables]]
- [[whois-landing-page|WhoisXML API integration]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[tisc-whoisxml-integration|Whois integration]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[shodan-lookups|Shodan integration]]
- [[threat-intelligence-infrastructure|Infrastructure]]
