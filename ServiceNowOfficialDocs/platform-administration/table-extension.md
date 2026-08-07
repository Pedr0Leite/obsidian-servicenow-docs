---
title: Table extension
description: Partition and preserve data sets for extended periods without overwriting.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/table-extension.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Applying database rotation techniques, Data Management, Tables and data, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Table extension

Partition and preserve data sets for extended periods without overwriting.

Table extension is based around a base table and a number of shards. The shards are given a duration which determines the period of time across which data is written to each shard. Shards in a table extension don't rotate. Instead of the oldest shard being truncated and re-used, an extension creates new shards indefinitely. This way, data remains logically separated across shards due to creation date and no data is ever deleted.

An advantage of table extension is to partition data across tables. It also allows you to archive data while ensuring that tables stay reasonably-sized. The working set of data is reduced when a date is known for the query.

The disadvantage is that table extension requires a union query when you query for a time range that spans multiple tables. Union queries are less efficient than queries against a single table.

Consider using table extension when you have sequentially-written tables or insert-only type tables \(there are exceptions to this parameter\). Table extension is also useful in tables where data is needed for long periods of time.

-   **[[t_TableExtensionExample|Apply table extension]]**  
Preserve data sets using table extension.

**Parent Topic:**[[c_DatabaseRotation|Applying database rotation techniques]]

**Related topics**  


[Activate database rotation]()

[Table rotation]()

## Related

- [[t_TableExtensionExample|Apply table extension]]
- [[c_DatabaseRotation|Applying database rotation techniques]]
