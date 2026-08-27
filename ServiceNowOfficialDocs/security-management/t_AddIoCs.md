---
title: View an IoC
description: IoCs, sometimes referred to as indicators, are most typically retrieved from a threat data source as STIX data. If needed, you can also create IoCs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/t\_AddIoCs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Indicators of compromise, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# View an IoC

IoCs, sometimes referred to as [[indicator|indicators]], are most typically retrieved from a threat data source as STIX data. If needed, you can also create IoCs.

## Before you begin

Role required: sn\_ti.write

## Procedure

1.  After the scheduled job has retrieved IoC data from the [[c_GetStartedWithThreatIntel|defined data source]], navigate to **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Indicators**.

    The retrieved IoCs are listed.

2.  Click the IoC you want to view.

3.  The following information displays.

<table id="table_dsg_w5w_yt"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Select classification tag

</td><td>

If you set up and activated [[create-class-group-and-tags|security tags]] to add metadata to the record, you can select one or more tags to specify the degree of sensitivity of the IoC. If you did not set up or activate security tags, this drop-down list is not displayed.

</td></tr><tr><td>

Title

</td><td>

A descriptive name for this indicator.

</td></tr><tr><td>

First Seen

</td><td>

The first date this indicator was observed in the system.

</td></tr><tr><td>

Last Seen

</td><td>

The most recent date this indicator was observed in the system.

</td></tr><tr><td>

Encountered count

</td><td>

The number to times the indicator has been encountered.

</td></tr><tr><td>

Sourced count

</td><td>

The number to times the indicator was imported from defined threat sources.

</td></tr><tr><td>

Notes

</td><td>

Any additional notes about the indicator. This field can also contain JSON key/value pairs.

</td></tr></tbody>
</table>4.  You can click any of the following related lists to view additional information.

<table id="table_bmj_3ky_fv"><thead><tr><th>

Related Links and Related Lists

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Show [[stix-relationships|Relationships]]

</td><td>

Opens the [[stix-visualizer|STIX Visualizer]] where you can view the relationship of the STIX object.Show Relationships appears only when the object has an associated object.

</td></tr><tr><td>

Related [[c_Observables|Observables]]

</td><td>

Lists observables that are linked to the current indicator.

</td></tr><tr><td>

Related Attack mode/method

</td><td>

Lists related attack modes/methods that have been identified as related to this indicator.

</td></tr><tr><td>

Associated Type

</td><td>

Lists other indicator types that are associated with this IoC.

</td></tr><tr><td>

Indicator Sources

</td><td>

Lists the sources of this indicator, along with the confidence level of the source.

</td></tr><tr><td>

Associated Tasks

</td><td>

Lists all tasks, changes, and incidents associated with the IoC.

</td></tr><tr><td>

Indicator Metadata

</td><td>

If the **Notes** field contains valid JSON key/value pairs, they are parsed and displayed. If no JSON key/value pairs are present, or if the JSON is invalid, this related list is not displayed.

</td></tr><tr><td>

[[security-annotations|Security Annotations]]

</td><td>

 

</td></tr><tr><td>

Indicator External References

</td><td>

 

</td></tr><tr><td>

Associated Kill Chain Phases

</td><td>

Lists kill chain phases associated with this object.

</td></tr><tr><td>

[[attack-patterns|Attack Patterns]]

</td><td>

Lists the attack patterns that help categorize attacks that are associated with this object.

</td></tr><tr><td>

[[threat-intelligence-campaigns|Campaigns]]

</td><td>

Lists campaigns associated with this object.

</td></tr><tr><td>

[[threat-intelligence-intrusion-sets|Intrusion Set]]

</td><td>

Lists a set of adversarial behaviors and resources with common properties associated with this object.

</td></tr><tr><td>

[[threat-intelligence-malware|Malware]]

</td><td>

Lists malicious code associated with this object.

</td></tr><tr><td>

[[threat-actors|Threat Actors]]

</td><td>

Lists individuals, groups, or organizations who act with malicious intent associated with this object.

</td></tr></tbody>
</table>
**Parent Topic:**[[c_IoCs|Indicators of compromise]]

**Related topics**  


[Add a related observable to an IoC]()

[Add a related attack mode/method to an IoC]()

[Identify associated indicator types]()

[Identify indicator sources]()

[Add associated tasks to an IoC]()

## Related

- [[c_GetStartedWithThreatIntel|Set up Threat Intelligence]]
- [[create-class-group-and-tags|Set up security tag groups and tags]]
- [[c_IoCs|Indicators of compromise]]
- [[indicator|Indicators]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
- [[c_Observables|Observables]]
- [[security-annotations|Security annotations]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-intrusion-sets|Intrusion set]]
- [[threat-intelligence-malware|Malware]]
- [[threat-actors|Threat actors]]
