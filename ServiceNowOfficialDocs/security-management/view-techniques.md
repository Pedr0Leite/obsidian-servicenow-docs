---
title: Manage techniques
description: Manage the techniques that have been imported from the MITRE TAXII collections. The techniques contain various ways attackers have developed to employ a given tactic. You can review and deactivate techniques that are not relevant to your organization. In STIX, techniques are known as attack patterns.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/view-techniques.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [MITRE-ATT&amp;CK administration, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Manage techniques

Manage the techniques that have been imported from the MITRE TAXII collections. The techniques contain various ways attackers have developed to employ a given tactic. You can review and deactivate techniques that are not relevant to your organization. In STIX, techniques are known as [[attack-patterns|attack patterns]].

## Before you begin

Role required:

-   sn\_ti.admin: delete access
-   sn\_si.admin: create, write, delete access
-   sn\_ti.read: read access
-   sn\_ti.write: create, write access

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **MITRE ATT&amp;CK Repository** &gt; **Techniques**.

    \[Omitted image "techniques-list.png"\] Alt text: View the list of techniques and sub-techniques.

    The list of techniques and subtechniques are now listed.

2.  To review and deactivate techniques that are not relevant to your organization, go to the list view for the selected technique, and under the Active column, update the setting to **false**, and save the setting.

    Deactivate the techniques that aren't used by the [[tisc-other-objects|other objects]] in the [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK repository]].

3.  To prioritize a technique, assign a priority in the **Relevant Priority \(Custom\)** field.

    The base system relevant priority is set to none. The **Relevant Priority \(Custom\)** field is not imported from the MITRE-ATT&amp;CK TAXII collections but a custom field introduced in the ServiceNow AI Platform. You can use the relevant priority information to filter and prioritize techniques in the dashboards, during the data source [[mapping-logrhythm|mapping]], or when analyzing the heat map.

4.  Click a technique to view all the associated information with this technique.

    In the following illustration, you can view the details for each Account Access Removal technique, its ID, source, and other related information.

    \[Omitted image "mitre-technique-attack-pattern.jpg"\] Alt text: View the attack pattern technique and it's related information.

    **Note:** The Data Source: [[data-component|Data Component]] element introduced by MITRE replaces the previous Data Source field. Data component provides an extra sublayer of context to the [[data-sources|data sources]]. If your MITRE-ATT&amp;CK repository contains the old TAXII collections, then you can view the Data Source field. Otherwise, you can view the data sources with the additional context of data components in the Data Source: Data Component field. You can view the new data component field only when the source is Enterprise ATT&amp;CK. For more information, see [[map-the-data-source-and-data-components|data component mapping]].

5.  To view how these objects are related, click **Show [[stix-relationships|Relationships]]**.


## What to do next

You can [[view-and-extend-information|extend the information]] in some of these related list objects. For example, you can add new information for Group, Mitigation, and External References.

**Parent Topic:**[[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]

**Related topics**  


[Get started with MITRE-ATT&amp;CK framework]()

[Understand the MITRE to STIX data model]()

[Domain separation and MITRE-ATT&amp;CK]()

[Set up the MITRE-ATT&amp;CK framework]()

[Manage matrices]()

[Manage mitigations]()

[Manage groups]()

[Manage malware]()

[Manage tools]()

[Manage MITRE relationships]()

[Manage CVE and technique mapping]()

[Extend the MITRE-ATT&amp;CK data]()

[Define the data source and detection tool mapping]()

[Define the data source and data component mapping]()

[Define the technique detection coverage]()

[Map your technique detection coverage to a technique]()

[Define the mitigation coverage]()

[Map your mitigation coverage to a technique]()

[Create and map detection rules]()

[Auto-extract technique rules for importing MITRE-ATT&amp;CK information]()

[Review threat group and MITRE-ATT&amp;CK techniques mapping]()

[Threat group to technique heatmap definition]()

[Review the MITRE-ATT&amp;CK system properties]()

## Related

- [[map-the-data-source-and-data-components|Define the data source and data component mapping]]
- [[view-and-extend-information|Extend the MITRE-ATT&amp;CK data]]
- [[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]
- [[attack-patterns|Attack patterns]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[tisc-other-objects|Other Objects]]
- [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK Repository]]
- [[mapping-logrhythm|Mapping]]
- [[data-component|Data Component]]
- [[data-sources|Data Sources]]
- [[stix-relationships|Relationships]]
