---
title: Manually create a network topology
description: Create a topology record for the network that you want to visualize in the organization of its network elements. By creating the network topology, you can visualize how the network elements are organized and connected to one another in the Telecommunications Network Inventory application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/telecom-network-inventory/telecommunications-network-inventory/create-netowrk-topology.html
release: australia
product: Telecommunications Network Inventory
classification: telecommunications-network-inventory
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Manually creating and reviewing your network asset instances, Define inventory records, Use, Telecommunications Network Inventory]
tags:
  - telecom-network-inventory
  - network-inventory
  - telecom
  - resources
  - tni
  - type-task
---

# Manually create a network topology

Create a topology record for the network that you want to visualize in the organization of its network elements. By creating the [[using-network-topology|network topology]], you can visualize how the network elements are organized and connected to one another in the [[telecom-network-inventory|Telecommunications Network Inventory]] application.

## Before you begin

Role required: sn\_ni\_core.inventory\_admin, sn\_ni\_core.inventory\_agent

## About this task

When you create a network topology record, it creates a corresponding configuration item \(CI\) record in the Network Topology \[cmdb\_ci\_network\_topology\] table. And the root nodes are stored in the Topology Root Node \[cmdb\_network\_topology\_root\_node\] table. To learn more about the topology [[uses-for-network-inventory-data|data model]], see [Data model](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/uses-for-network-inventory-data.md).

## Procedure

1.  Navigate to **Workspaces** &gt; **[[exploring-network-inventory-workspace|Network Inventory Workspace]]**.

2.  From the list icon \(\[Omitted image "lists\_icon-proactive.png"\] Alt text: List icon, go to **Inventory** &gt; **Network Topology**.

3.  Select **New**.

4.  On the **Details** tab, fill in the form.

    To learn about the fields in the [[network-topology-form|Network Topology form]], see [Network topology form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/network-topology-form.md).

5.  On the **Network Topology Root Nodes** tab, select **New** and fill in the fields to add the root node.

    |Field|Description|
    |-----|-----------|
    |Root Node|Root node for the topology.|
    |Network Topology|Network Topology that you have created.|

6.  Select **Save**.

7.  On the **Details** tab, select **Submit**.


## What to do next

You can view the topology in the Network Viewer window. To learn more, see [Viewing a network topology](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/viewing-network-topology.md).

**Parent Topic:**[Manually creating and reviewing your network asset instances](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/creating-telecommunications-network-inventory.md)

**Related topics**  


[Network topology](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/visualization-of-topology.md)

## Related

- [[using-network-topology|Network topology]]
- [[telecom-network-inventory|Telecommunications Network Inventory]]
- [[uses-for-network-inventory-data|Data model]]
- [[exploring-network-inventory-workspace|Network Inventory Workspace]]
- [[network-topology-form|Network topology form]]
