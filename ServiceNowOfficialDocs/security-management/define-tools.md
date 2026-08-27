---
title: Define tools
description: Define tools as legitimate software that is used to perform attacks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/define-tools.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Tools, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Define tools

Define tools as legitimate software that is used to perform attacks.

## Before you begin

Role required: sn\_ti.admin

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Tools**.

2.  Click **New**.

3.  Complete the fields in the form as appropriate.

    |Field|Description|
    |-----|-----------|
    |**Name**|Enter a descriptive name to identify the tool.|
    |**Source**|Specifies the threat source from which this record is created.|
    |**Description**|A description that provides more details and context about the tool, potentially including its purpose and its key characteristics.|
    |**Aliases**|Alternative names to identify this tool.|
    |**Source ID**|Unique identifier for this object in the threat source.|
    |**Created Time in Source**|Specifies the time the object is created in the source.|
    |**Modified Time in Source**|Specifies the time the object is modified in the source.|

4.  Click **Submit**.


## What to do next

Click any of the following related lists to view additional information about objects associated with the tool object.

<table id="table_kbz_d22_xmb"><thead><tr><th>

Related Links and Related Lists

</th><th>

Description

</th></tr></thead><tbody><tr><td>

External References

</td><td>

Lists external references which refer to non-STIX information. This property is used to provide one or more external object identifiers.

</td></tr><tr><td>

Associated Kill Chain Phases

</td><td>

Lists kill chain phases associated with this object.

</td></tr><tr><td>

Associated Types

</td><td>

Lists indicator types associated with this object.

</td></tr><tr><td>

[[attack-patterns|Attack Patterns]]

</td><td>

Lists the attack patterns that help categorize attacks that are associated with this object.

</td></tr><tr><td>

[[threat-intelligence-campaigns|Campaigns]]

</td><td>

Lists campaigns associated with this object.

</td></tr><tr><td>

[[threat-intelligence-course-actions|Course of Actions]]

</td><td>

Lists the associated course of actions with this object that are technical or automated responses \(applying patches, reconfiguring firewalls\) to prevent an attack.

</td></tr><tr><td>

[[threat-intelligence-identities|Identities]]

</td><td>

List of identities associated with this object.

</td></tr><tr><td>

[[indicator|Indicators]]

</td><td>

Lists related [[c_IoCs|Indicators of Compromise]] \(IoC\) that have been identified by the threat source associated with this object.

</td></tr><tr><td>

[[threat-intelligence-infrastructure|Infrastructure]]

</td><td>

Lists systems, software services, and any associated physical or virtual resources that are associated with this object.

</td></tr><tr><td>

[[threat-intelligence-intrusion-sets|Intrusion Set]]

</td><td>

Lists a set of adversarial behaviors and resources with common properties associated with this object.

</td></tr><tr><td>

[[threat-intelligence-locations|Locations]]

</td><td>

Lists locations that provide geographic context to this object.

</td></tr><tr><td>

[[threat-intelligence-malware|Malware]]

</td><td>

Lists malicious code associated with this object.

</td></tr><tr><td>

[[threat-actors|Threat Actors]]

</td><td>

Lists individuals, groups, or organizations who act with malicious intent associated with this object.

</td></tr><tr><td>

[[vulnerabilities|Vulnerabilities]]

</td><td>

Lists a weakness or defect in a software or hardware that attackers exploit which is associated with this object.

</td></tr><tr><td>

Show [[stix-relationships|Relationships]]

</td><td>

Opens the [[stix-visualizer|STIX Visualizer]] where you can view the relationship of the STIX object.Show Relationships appears only when the object has an associated object.

</td></tr></tbody>
</table>**Parent Topic:**[[tools|Tools]]

## Related

- [[tools|Tools]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-course-actions|Course of actions]]
- [[threat-intelligence-identities|Identities]]
- [[indicator|Indicators]]
- [[c_IoCs|Indicators of compromise]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[threat-intelligence-intrusion-sets|Intrusion set]]
- [[threat-intelligence-locations|Locations]]
- [[threat-intelligence-malware|Malware]]
- [[threat-actors|Threat actors]]
- [[vulnerabilities|Vulnerabilities]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
