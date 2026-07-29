---
title: Manually set up entities for Sustainable IT data centers
description: Create entities for data centers and add them to an entity type. The entity type is then added to the metric definitions that enables the metric definitions to collect data from various data centers.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/environmental-social-governance/set-up-entities-for-sustainable-it.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Methods to set up entities for Sustainable IT, Configure Sustainable IT, Configure, Operational Sustainability Management \(formerly Environmental, Social, and Governance\)]
tags:
  - environmental-social-governance
  - esg
  - sustainability
  - reporting
  - carbon
  - type-task
---

# Manually set up entities for Sustainable IT data centers

Create entities for data centers and add them to an entity type. The entity type is then added to the metric definitions that enables the metric definitions to collect data from various data centers.

## Before you begin

Role required: sn\_esg.admin

## About this task

To gather emissions data pertaining to your data centers, it is necessary to give a unique name to your entities and associate a location in such a way that they can retrieve data from all of your datacenter locations. For instance, if you want to use the metric definition named Energy from coal, it implies that you want the coal energy emissions data from four locations, for example, Bangalore, New York, Paris, and Berlin when the metrics are executed. To accomplish this task, you must create entities with names such as New York, Bangalore, and so on. To use the Sustainable IT application, when you create entities, it is mandatory to add a location to them. You can then group the entities within an entity type. For example, you can call the entity type "Data centers." This entity type is then added to the metric definition named Energy from coal.

## Procedure

1.  Navigate to **All** &gt; **Operational Sustainability Management** &gt; **Operational Sustainability Workspace** &gt; **Lists** &gt; **Scoping** &gt; **All Entities**.

2.  Create entities with names such as `Paris data center`.

    For information on how to create an entity, refer to [[create-entity|Create an entity]]. The name that you use when creating an entity is the name that is displayed on the [[sustainable-it-dashboard|Sustainable IT dashboard]]. It is important to provide a value in the **Location** field on the entity form. If a particular datacenter has multiple locations, you can name the entities accordingly.

3.  Create an entity type called `Data center`.

    For information on how to create an entity, refer to [[create-entity-type|Create an entity type]]. The name that you use when creating an entity is the name that is displayed on the Sustainable IT dashboard.

4.  Add the entities that you created to the Data center entity type.

5.  Add the entity type to the metric definition that you would use to collect metrics.


## Result

When the metrics are executed, data from all four entities is collected and displayed on the Sustainable IT dashboard.

**Parent Topic:**[[methods-to-set-up-entities|Methods to set up entities for Sustainable IT]]

## Related

- [[create-entity|Create an entity]]
- [[create-entity-type|Create an entity type]]
- [[methods-to-set-up-entities|Methods to set up entities for Sustainable IT]]
- [[sustainable-it-dashboard|Sustainable IT dashboard]]
