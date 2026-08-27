---
title: Threat Lookup - Have I been pwned? flow
description: The Threat Lookup - Have I been pwned? flow performs a lookup on selected observables. If the observables are of a type recognized by Have I been pwned?, the observables are scanned for malware, and the results are returned.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/security-incident-response/threat-lookup-haveibeenpwned-wf.html
release: australia
product: Security Incident Response
classification: security-incident-response
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Have I been pwned? integration setup, Have I been pwned? integration, Security Incident Response integrations, Security Incident Response, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - sir
  - security-incidents
  - investigation
  - soar
  - type-concept
---

# Threat Lookup - Have I been pwned? flow

The [[tisc-threat-lookup|Threat Lookup]] - Have I been pwned? flow performs a lookup on selected [[c_Observables|observables]]. If the observables are of a type recognized by Have I been pwned?, the observables are scanned for [[threat-intelligence-malware|malware]], and the results are returned.

Role required: sn\_si\_admin

This flow is triggered by the [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]] when you perform a threat lookup on one or more observables, and the Have I been pwned? implementation is selected. For more information, see [[perform-lookups-on-observables|Perform lookups on observables]].

For information, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

## Related

- [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]]
- [[perform-lookups-on-observables|Perform lookups on observables]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[c_Observables|Observables]]
- [[threat-intelligence-malware|Malware]]
