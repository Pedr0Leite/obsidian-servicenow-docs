---
title: Define threat notes
description: Define threat notes that convey information to provide further context or analysis that is not available in existing objects.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/define-threat-notes.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Threat notes, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Define threat notes

Define threat notes that convey information to provide further context or analysis that is not available in existing objects.

## Before you begin

Role required: sn\_ti.admin

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Threat Notes**.

2.  Click **New**.

3.  Complete the fields in the form as appropriate.

    |Field|Description|
    |-----|-----------|
    |**Abstract**|Specify a brief summary of the note content.|
    |**Content**|Specifies the content of the note.|
    |**Authors**|Specifies the name of the author \(example, an analyst\).|
    |**Source**|Specifies the threat source from which this record is created.|
    |**Source ID**|Unique identifier for this object in the threat source.|
    |**Created Time in Source**|Specifies the time the object is created in the source.|
    |**Modified Time in Source**|Specifies the time the object is modified in the source.|

4.  Click **Submit**.


## What to do next

Click any of the following related lists to view additional information about objects associated with the threat notes.

<table id="table_wlq_2td_xmb"><thead><tr><th>

Related Links and Related Lists

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Show [[stix-relationships|Relationships]]

</td><td>

Opens the [[stix-visualizer|STIX Visualizer]] where you can view the relationship of the STIX object.Show Relationships appears only when the object has an associated object.

</td></tr><tr><td>

Associated Objects

</td><td>

Lists of objects that the threat notes apply to.

</td></tr><tr><td>

Associated [[indicator|Indicators]]

</td><td>

Lists of indicators that the threat notes apply to.

</td></tr><tr><td>

Associated [[c_Observables|Observables]]

</td><td>

Lists observables associated with this object.

</td></tr></tbody>
</table>**Parent Topic:**[[threat-intelligence-threat-notes|Threat notes]]

## Related

- [[threat-intelligence-threat-notes|Threat notes]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
- [[indicator|Indicators]]
- [[c_Observables|Observables]]
