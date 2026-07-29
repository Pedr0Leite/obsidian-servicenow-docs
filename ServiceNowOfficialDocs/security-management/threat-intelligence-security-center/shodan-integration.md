---
title: Configure and enable Shodan integration
description: Before you use Shodan integration, you must download it from the ServiceNow Store.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/shodan-integration.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Shodan integration, Configure Observable Enrichment, TISC Enrichment integrations, TISC Integrations, Integrate, Threat Intelligence Security Center, Security Operations]
tags:
  - security-management
  - threat-intelligence
  - stix
  - taxii
  - iocs
  - type-task
---

# Configure and enable Shodan integration

Before you use [[shodan-lookups|Shodan integration]], you must download it from the ServiceNow Store.

## Before you begin

Role required: sn\_sec\_tisc.admin

**Important:** The [[tisc-landing-page|Threat Intelligence Security Center]] and Whois [[tisc-observable-enrichment|Observable Enrichment]] plugins must be installed and active.

Download the [[tisc-whoisxml-integration|Whois integration]] from the ServiceNow Store and verify you have a valid Whois account before use. For more information see, [[download-app-first-time|Download the integration from the ServiceNow Store]].

## Procedure

1.  Navigate to **Workspaces** &gt; **Threat Intelligence Security Center** &gt; **Integrations** &gt; **Enrichment Integrations** &gt; **All Integrations** &gt; **Observable Enrichment**.

2.  In the **Shodan** card, select **[[tisc-config-new-enrich|Configure New Enrichment]]** to configure the integration.

3.  Complete the Configure New Enrichment form.

<table id="table_iqf_n4p_tzb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name for the new enrichment integration. For example, Shodan.

</td></tr><tr><td>

Vendor Name

</td><td>

Name of the vendor.The details of the selected vendor are auto-populated and by default this field will be read only. For example, Shodan.

</td></tr><tr><td>

Integration Type

</td><td>

Type of integration that you selected. For example, Observable Enrichment.

</td></tr><tr><td>

Description

</td><td>

Description for the new enrichment integration.For example, the description for Shodan integration is, Shodan helps you to analyze banner information from connected devices all around the globe.

</td></tr></tbody>
</table>4.  Navigate to the **Integration Configuration** section.

5.  Enter \(or paste\) the **API Key** you acquired from the Shodan portal.

6.  Select **Save** to apply the changes.

    The integration details are validated, and by default the status is inactive.

7.  Select **Enable** to enable the integration.


## Result

After configuration, Shodan can be selected for performing enrichment on [[c_Observables|observables]] in Threat Intelligence Security Center.

**Parent Topic:**[Shodan integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-shodan.md)

**Related topics**  


[Configure Observable Enrichment](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/configure-observable-enrichment.md)

## Related

- [[download-app-first-time|Download an application from the ServiceNow Store for the first time]]
- [[shodan-lookups|Shodan integration]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[tisc-observable-enrichment|Observable Enrichment]]
- [[tisc-whoisxml-integration|Whois integration]]
- [[tisc-config-new-enrich|Configure new enrichment]]
- [[c_Observables|Observables]]
