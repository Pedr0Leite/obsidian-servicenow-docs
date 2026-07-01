---
title: CrowdStrike Falcon Intelligence integration overview
description: CrowdStrike Falcon Intelligence provides cyber security intelligence that easily integrating with Security Operations.The Threat Lookup - CrowdStrike Falcon Intelligence flow designer performs a lookup on selected observables. If the observables are of a type recognized by CrowdStrike Falcon Intelligence, the observables are scanned for malware, and the results are returned.The Integration Configuration feature allows you to quickly activate and set up third-party security integrations, including the CrowdStrike Falcon Intelligence integration. Before you can use the CrowdStrike Falcon Intelligence, you must download it from the ServiceNow Store and add the appropriate API key and ID.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/crowdstrike-intell-integration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [CrowdStrike Falcon Intelligence integration, Threat Intelligence integrations, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# CrowdStrike Falcon Intelligence integration overview

CrowdStrike Falcon Intelligence provides cyber security intelligence that easily integrating with [[security-operations-landing-page|Security Operations]].

**Note:** The [[threat-intel-landing-page|Threat Intelligence]] plugin is required to implement the [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]].

**Related topics**  


[Submit an IoC Lookup request from the Security Incident Catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/t_SubmitThrtScnReqFromCat.md)

## Threat Lookup - CrowdStrike Falcon Intelligence flows

The [[tisc-threat-lookup|Threat Lookup]] - CrowdStrike Falcon Intelligence flow designer performs a lookup on selected [[c_Observables|observables]]. If the observables are of a type recognized by CrowdStrike Falcon Intelligence, the observables are scanned for [[threat-intelligence-malware|malware]], and the results are returned.

This flow is triggered by the [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]] when you publish one or more observables to a watchlist, and the CrowdStrike Falcon Intelligence implementation is selected. After they are published, the watchlists can be viewed in the CrowdStrike Falcon Host software.

Role required: admin

\[Omitted image "flows-crowdstrike-threat.png"\] Alt text: Threat Lookup - CrowdStrike Falcon Intelligence sub flow

For information on the activities used by this flow designer, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

## Activate and configure the CrowdStrike Falcon Intelligence integration

The Integration Configuration feature allows you to quickly activate and set up third-party security integrations, including the CrowdStrike Falcon Intelligence integration. Before you can use the CrowdStrike Falcon Intelligence, you must download it from the ServiceNow Store and add the appropriate API key and ID.

### Before you begin

Role required: admin

-   The Threat Intelligence plugin must be installed and activated before you can use the CrowdStrike Falcon Intelligence integration.
-   Obtain the API Client ID and API Client Secret under your CrowdStrike Falcon Intelligence profile.
-   If you are upgrading CrowdStrike Falcon Intelligence integration from a previous version, then you must delete the existing configuration and set up a new configuration. The integration supports OAUTH2 authentication. This update requires you to enter the **API Client ID** and the **API Client Secret** to authenticate and complete the configuration.
-   In the CrowdStrike Falcon Intelligence portal **API Scopes**, enable the **Read** setting for **[[indicator|Indicators]] \(Falcon X\)** or **IOCs \([[c_IoCs|Indicators of Compromise]]\)**.

### Procedure

1.  [[download-app-first-time|Download the integration from the ServiceNow Store]].

2.  In your instance, navigate to **Security Operations** &gt; **Integrations** &gt; **Integration Configurations**.

    The available security integrations appear as a series of cards.

3.  In the CrowdStrike Falcon Intelligence card, click **Configure**.

4.  On the form, fill in the fields to complete the configuration:

<table id="table_ifn_tlk_mnb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

**Name**

</td><td>

Name of the integration, for example, `demo-1`.

</td></tr><tr><td>

**API Client ID**

</td><td>

The client ID that you obtain from the settings section of your account profile in CrowdStrike Falcon Intelligence portal.

</td></tr><tr><td>

**API Client Secret**

</td><td>

The client secret key that you obtain from the settings section of your account profile in CrowdStrike Falcon Intelligence portal.

</td></tr></tbody>
</table>5.  Click **Submit**.


### Result

After it is configured, CrowdStrike Falcon Intelligence can be selected for performing lookups on observables in Threat Intelligence and on observables in security incidents.

**Related topics**  


[[perform-lookups-on-observables|Perform lookups on observables]]

## Related

- [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[download-app-first-time|Download an application from the ServiceNow Store for the first time]]
- [[perform-lookups-on-observables|Perform lookups on observables]]
- [[security-operations-landing-page|Security Operations]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[crowdstrike-intell-landing-page|CrowdStrike Falcon Intelligence integration]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[c_Observables|Observables]]
- [[threat-intelligence-malware|Malware]]
- [[indicator|Indicators]]
- [[c_IoCs|Indicators of compromise]]
