---
title: Rebuild state flows
description: You can rebuild state flows when a mismatch between existing and new sys\_ids occurs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-management-for-the-enterprise/c\_RebuildStateFlows.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
tags:
  - service-management-for-the-enterprise
  - type-concept
---

# Rebuild state flows

You can rebuild state flows when a mismatch between existing and new sys\_ids occurs.

When you use an XML file to import a state flow record into an instance, the system attempts to match the incoming states with existing states by comparing sys\_ids. Because the sys\_ids of items in a choice list can vary between instances, the system can fail to match the states, even though they are otherwise identical.

When matching fails, the start and end states of affected records are left blank or contain numeric values. To repair these records navigate to **State Flows** &gt; **Admin** &gt; **Rebuild State Flows**. This module runs a script that compares the numerical value of each item in the **State** field choice list until it finds a match in the imported state flow record.

**Parent Topic:**[[c_StateFlowCustomization|State flow customization]]

## Related

- [[c_StateFlowCustomization|State flow customization]]
