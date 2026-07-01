---
title: Threat Lookup - VirusTotal workflow
description: The Threat Lookup - VirusTotal workflow performs a lookup on selected observables. If the observables are of a type recognized by VirusTotal, the observables are scanned for malware, and the results are returned.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-lookup-virustotal-wf.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [VirusTotal integration, Threat Intelligence integrations, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Threat Lookup - VirusTotal workflow

The Threat Lookup - VirusTotal workflow performs a lookup on selected [[c_Observables|observables]]. If the observables are of a type recognized by VirusTotal, the observables are scanned for [[threat-intelligence-malware|malware]], and the results are returned.

## Before you begin

Role required: admin

## About this task

This workflow is triggered by the [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]] when you perform a [[tisc-threat-lookup|threat lookup]] on one or more observables, and the VirusTotal implementation is selected. For more information, see [[perform-lookups-on-observables|Perform lookups on observables]].

\[Omitted image "hreat-lookup-virustotal-wf.png"\] Alt text: Threat Lookup - VirusTotal workflow

For information on the activities used by this workflow, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

## Related

- [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]]
- [[perform-lookups-on-observables|Perform lookups on observables]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[c_Observables|Observables]]
- [[threat-intelligence-malware|Malware]]
- [[tisc-threat-lookup|Threat Lookup]]
