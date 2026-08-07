---
title: Identify associated indicator types
description: If an IoC has no associated indicator types defined, it tracks all types of observables. However, if you associate one or more types of indicators to an IoC, it limits the types of observables that can be associated with the IoC.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/t\_IdentifyAssociatedIndicatorTypes.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Indicators of compromise, IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Identify associated indicator types

If an IoC has no associated indicator types defined, it tracks all types of [[c_Observables|observables]]. However, if you associate one or more types of [[indicator|indicators]] to an IoC, it limits the types of observables that can be associated with the IoC.

## Before you begin

Role required: sn\_ti.write

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **[[ioc-repository|IoC Repository]]** &gt; **Indicators**.

2.  Click the indicator to which you want to associate an indicator type.

3.  Click the **Associated Type** related list.

4.  Click **Edit**.

5.  As needed, use the filters to locate the indicator type you want to associate with the IoC.

6.  Using the slushbucket, add the indicator type to the **Associated Type** list.

7.  Click **Save**.


**Parent Topic:**[[c_IoCs|Indicators of compromise]]

**Related topics**  


[View an IoC]()

[Add a related observable to an IoC]()

[Add a related attack mode/method to an IoC]()

[Identify indicator sources]()

[Add associated tasks to an IoC]()

## Related

- [[c_IoCs|Indicators of compromise]]
- [[c_Observables|Observables]]
- [[indicator|Indicators]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[ioc-repository|IoC Repository]]
