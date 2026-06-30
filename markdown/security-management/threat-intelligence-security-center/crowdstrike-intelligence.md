---
title: Configure and enable CrowdStrike Falcon Intelligence integration
description: Set up CrowdStrike Falcon Intelligence integration to perform threat lookups on observables in Threat Intelligence Security Center.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/crowdstrike-intelligence.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [TISC CrowdStrike Falcon Intelligence integration, Threat Lookup, TISC Enrichment integrations, TISC Integrations, Integrate, Threat Intelligence Security Center, Security Operations]
---

# Configure and enable CrowdStrike Falcon Intelligence integration

Set up [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]] to perform threat lookups on [[c_Observables|observables]] in [[tisc-landing-page|Threat Intelligence Security Center]].

## Before you begin

Role required: sn\_sec\_tisc.admin

**Note:** The Threat Intelligence Security Center and VirusTotal [[tisc-threat-lookup|Threat Lookup]] plugins must be installed and active.

Download the [[virustotal-landing-page|VirusTotal integration]] from the ServiceNow Store. Confirm you have a valid VirusTotal account before use. For more information, see [[download-app-first-time|Download the integration from the ServiceNow Store]].

## About this task

This integration requires downloading the app from the ServiceNow Store and configuring API credentials from your CrowdStrike account.

Obtain the API Client ID and API Client Secret under your CrowdStrike Falcon Intelligence profile. In the CrowdStrike Falcon Intelligence portal API Scopes, enable the **Read** setting for [[indicator|Indicators]] \(Falcon Intelligence\).

## Procedure

1.  Navigate to **Workspaces** &gt; **Threat Intelligence Security Center** &gt; **Integrations** &gt; **Enrichment Integrations** &gt; **All Integrations** &gt; **Threat Lookup**.

2.  Select **[[tisc-config-new-enrich|Configure New Enrichment]]** to configure **CrowdStrike Falcon Intelligence** integration.

3.  Fill in the fields on the Configure New Enrichment form.

    |Field|Description|
    |-----|-----------|
    |Name|Name for the new enrichment integration. For example, CrowdStrike Falcon Intelligence.|
    |Vendor Name|Name of the vendor. The details of the selected vendor is populated by default. For example, CrowdStrike Falcon Intelligence.|
    |Integration Type|Type of integration that you selected. For example, Threat Lookup.|
    |Description|Description for the new enrichment integration.|
    |**Integration Configuration**|
    |Client ID|The client ID that you obtained from CrowdStrike.|
    |Client Secret|The client secret key that you obtained from CrowdStrike.|

4.  Select **Save** to apply the changes.

    The integration details are validated, and by default the CrowdStrike Falcon Intelligence integration's status is inactive.

5.  Select **Enable** to enable the CrowdStrike Falcon Intelligence integration.


## Result

After you configure it, CrowdStrike Falcon Intelligence can be selected for performing lookups on observables in Threat Intelligence Security Center.

**Parent Topic:**[TISC CrowdStrike Falcon Intelligence integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-crowdstrike-falcon-intelligence-integration.md)

**Related topics**  


[Threat Lookup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-threat-lookup.md)

[Configure and enable VirusTotal Integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-virustotal-integration.md)

## Related

- [[download-app-first-time|Download an application from the ServiceNow Store for the first time]]
- [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]]
- [[c_Observables|Observables]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[virustotal-landing-page|VirusTotal integration]]
- [[indicator|Indicators]]
- [[tisc-config-new-enrich|Configure new enrichment]]
