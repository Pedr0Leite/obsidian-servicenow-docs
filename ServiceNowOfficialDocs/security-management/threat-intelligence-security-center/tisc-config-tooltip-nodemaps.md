---
title: Configure tooltips for nodemaps
description: Use this section to configure tooltips for node map relationships on the investigation canvas.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/tisc-config-tooltip-nodemaps.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Administer, Threat Intelligence Security Center, Security Operations]
tags:
  - security-management
  - threat-intelligence
  - stix
  - taxii
  - iocs
  - type-task
---

# Configure tooltips for nodemaps

Use this section to configure tooltips for node map [[stix-relationships|relationships]] on the investigation canvas.

## Before you begin

Role required: sn\_sec\_tisc.admin

## Procedure

1.  Navigate to **Workspaces** &gt; **[[tisc-landing-page|Threat Intelligence Security Center]]** &gt; **Administration** &gt; **Nodemap Controls** &gt; **Tooltip Configuration**.

2.  Select the desired object from the list.

    By default, the following three records are provisioned in the base system.

    1.  [[c_Observables|Observables]]
    2.  [[indicator|Indicators]]
    3.  Objects
3.  Select **Observable** as an example record.

4.  Add one or more values to the observable record, if required.

    Similarly add values to indicators and [[tisc-other-objects|other objects]].

    **Note:** Each object supports a maximum of six values.

5.  Select **Save** to apply the changes.

6.  Go to the **Investigation Canvas** section and select **Refresh** icon.

    The same values configured on the **Tooltip Configuration** page will be displayed on each node map.

## Related

- [[stix-relationships|Relationships]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[c_Observables|Observables]]
- [[indicator|Indicators]]
- [[tisc-other-objects|Other Objects]]
