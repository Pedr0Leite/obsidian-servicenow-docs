---
title: Define observed data
description: Define observed data that conveys information about cyber security-related entities such as files, systems, and networks using the STIX Cyber-observable Objects \(SCOs\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/observed-data.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Observed data, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Define observed data

Define observed data that conveys information about cyber security-related entities such as files, systems, and networks using the STIX Cyber-observable Objects \(SCOs\).

## Before you begin

Role required: sn\_ti.admin

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Observed Data**.

2.  Click **New**.

3.  Complete the fields in the form as appropriate.

    |Field|Description|
    |-----|-----------|
    |**First Observed**|The initial time when the data was seen.|
    |**Last Observed**|The last time when the data was seen.|
    |**Observed Count**|The number of times that each Cyber-observable object was seen. The value must be an integer from 1 through 999,999,999.|
    |**Source**|Specifies the threat source from which this record is created.|
    |**Source ID**|Unique identifier for this object in the threat source.|
    |**Created Time in Source**|Specifies the time the object is created in the source.|
    |**Modified Time in Source**|Specifies the time the object is modified in the source.|

4.  Click **Submit**.


## What to do next

Click any of the following related lists to view additional information about objects associated with the observed data.

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

Associated [[c_Observables|Observables]]

</td><td>

Lists observables associated with this object.

</td></tr><tr><td>

[[indicator|Indicators]]

</td><td>

Lists related [[c_IoCs|Indicators of Compromise]] \(IoC\) that have been identified by the threat source associated with this object.

</td></tr><tr><td>

[[threat-intelligence-infrastructure|Infrastructure]]

</td><td>

Lists systems, software services, and any associated physical or virtual resources that are associated with this object.

</td></tr></tbody>
</table>**Parent Topic:**[[threat-intelligence-observed-data|Observed data]]

## Related

- [[threat-intelligence-observed-data|Observed data]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
- [[c_Observables|Observables]]
- [[indicator|Indicators]]
- [[c_IoCs|Indicators of compromise]]
- [[threat-intelligence-infrastructure|Infrastructure]]
