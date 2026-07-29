---
title: Define an attack pattern
description: Define an attack pattern to help categorize attacks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/define-attack-pattern.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Attack patterns, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Define an attack pattern

Define an attack pattern to help categorize attacks.

## Before you begin

Role required: sn\_ti.admin

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Attack Patterns**.

2.  Click **New**.

3.  Complete the fields in the form as appropriate.

<table id="choicetable_sq4_yvf_wmb"><thead><tr><th align="left" id="d239139e80">

Field

</th><th align="left" id="d239139e83">

Description

</th></tr></thead><tbody><tr><td id="d239139e89">

**Name**

</td><td>

Enter a descriptive name for this attack pattern.

</td></tr><tr><td id="d239139e98">

**Spec Version**

</td><td>

The version of the STIX specification used to represent this object.The value of this property must be 2.1 for STIX Objects defined according to this specification.

</td></tr><tr><td id="d239139e110">

**Source**

</td><td>

Specifies the threat source from which this record is created.

</td></tr><tr><td id="d239139e119">

**Description**

</td><td>

Enter a description of the attack pattern.

</td></tr><tr><td id="d239139e129">

**Aliases**

</td><td>

Alternative names to identify this attack pattern.

</td></tr><tr><td id="d239139e138">

**Source ID**

</td><td>

Unique identifier for this object in the threat source.

</td></tr><tr><td id="d239139e147">

**Created Time in Source**

</td><td>

Specifies the time the object is created in the source.

</td></tr><tr><td id="d239139e156">

**Modified Time in Source**

</td><td>

Specifies the time the object is modified in the source.

</td></tr></tbody>
</table>4.  Click **Submit**.


## What to do next

You can now click any of the following related lists to view additional information about objects associated with the attack pattern.

<table id="table_zdn_szf_wmb"><thead><tr><th>

Related Links and Related Lists

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Show [[stix-relationships|Relationships]]

</td><td>

Opens the [[stix-visualizer|STIX Visualizer]] where you can view the relationship of the STIX object.Show Relationships appears only when the object has an associated object.

</td></tr><tr><td>

External References

</td><td>

Lists external references which refer to non-STIX information. This property is used to provide one or more external object identifiers.

</td></tr><tr><td>

Associated Kill Chain Phases

</td><td>

Lists kill chain phases associated with this object.

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

[[tools|Tools]]

</td><td>

Lists legitimate software that is used by threat actors to perform attacks associated with this object.

</td></tr><tr><td>

[[vulnerabilities|Vulnerabilities]]

</td><td>

Lists a weakness or defect in a software or hardware that attackers exploit which is associated with this object.

</td></tr></tbody>
</table>**Parent Topic:**[[attack-patterns|Attack patterns]]

## Related

- [[attack-patterns|Attack patterns]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-course-actions|Course of actions]]
- [[threat-intelligence-identities|Identities]]
- [[indicator|Indicators]]
- [[c_IoCs|Indicators of compromise]]
- [[threat-intelligence-intrusion-sets|Intrusion set]]
- [[threat-intelligence-locations|Locations]]
- [[threat-intelligence-malware|Malware]]
- [[threat-actors|Threat actors]]
- [[tools|Tools]]
- [[vulnerabilities|Vulnerabilities]]
