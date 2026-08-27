---
title: Perform threat enrichment on observables
description: You can perform threat intelligence enrichment on one or more observables to determine whether they’re associated with known security threats. The implementations that run depend on the ones you’ve activated.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/perform-enrich-on-observs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Observables, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Perform threat enrichment on observables

You can perform [[threat-intel-landing-page|threat intelligence]] enrichment on one or more observables to determine whether they’re associated with known security threats. The implementations that run depend on the ones you’ve activated.

## Before you begin

Before you can perform enrichment, you must activate the Threat Intelligence plugin. You must also install the plugin for one or more of the enrichment implementations:

-   [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]]
-   [[c_Metadefenderintegration|OPSWAT Metadefender]]
-   [Security Operations Have I been pwned?](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/activate-haveibeenpwned.md)
-   [[activate-configure-virustotal|VirusTotal]]
-   [[activate-whois|WhoIs?]]

Role required: sn\_ti.admin

## Procedure

1.  Navigate to **All** &gt; **Threat Intelligence** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Observables**.

2.  Do one of the following steps:

    -   To perform a lookup on more than one observable, select the observables, click **Actions on selected rows**, and select **[[tisc-run-threat-lookup|Run threat lookup]]**.
    -   To perform a lookup on a single observable, open the observable record, and click the **Run threat lookup** related link.
    \[Omitted image "run-threat-lookup.png"\] Alt text: Run Threat Lookup slushbucket

3.  Select the [[tisc-threat-lookup|threat lookup]] implementations you want to use, or select **All** to perform lookups using all of the active implementations, then click **Submit**.

    A message indicates that the threat lookups have begun. The [[sec-ops-integ-threat-lookup|Security Operations Integration - Threat Lookup Flow]] runs and also executes the implementation workflows for the threat lookup implementations you selected. The lookups are performed and the results are generated.

4.  When the lookups are completed, you can click the **Threat Lookup Results** tab to view the results.

    \[Omitted image "threat-lookup-results.png"\] Alt text: Threat Lookup Results

5.  To see additional details, including raw results for a specific lookup, click the **Result value**.

    **Note:** When the VirusTotal or OPSWAT Metadefender implementations are used, the details are consolidated, as shown below.

    \[Omitted image "threat-lookup-results-details.png"\] Alt text: Threat Lookup Results details


**Parent Topic:**[[c_Observables|Observables]]

**Related topics**  


[Define an observable]()

[Add a related IoC to an observable]()

[Add associated tasks to an observable]()

[Add a related observable]()

[Load more IoC data]()

[Identify observable sources]()

[Perform lookups on observables]()

## Related

- [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]]
- [[c_Metadefenderintegration|OPSWAT Metadefender integration overview]]
- [[activate-configure-virustotal|Activate and configure the VirusTotal integration]]
- [[activate-whois|Activate and configure the Security Operations Whois integration]]
- [[sec-ops-integ-threat-lookup|Security Operations Integration - Threat Lookup Flow]]
- [[c_Observables|Observables]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[tisc-run-threat-lookup|Run Threat Lookup]]
- [[tisc-threat-lookup|Threat Lookup]]
