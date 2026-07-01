---
title: Export a snapshot of a configuration item
description: You can export a snapshot of a configuration item from its timeline.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/t\_ExportCIHistoryChanges.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [History Timeline, Knowing about History sets, Auditing]
tags:
  - platform-security
  - type-task
---

# Export a snapshot of a configuration item

You can export a snapshot of a configuration item from its timeline.

## Before you begin

The [[sc-configuration|configuration]] item must be in the Configuration Item \[cmdb\_ci\] table or a descendant of this table. [[c_AuditedTables|Auditing]] must be enabled for the table containing the CI.

Role required: admin.

## About this task

You can [[export|export]] a snapshot of the CI to an XML, PDF \(Portal\), or PDF \(Landscape\) format.

## Procedure

1.  Navigate to **All** &gt; **Configuration** &gt; **Base Items** &gt; **All** to open the configuration item list.

2.  Open a configuration item record.

3.  Open the timeline for the record.

4.  Select the bubble representing the time for which you want to export a snapshot of the CI.

5.  Click the export icon \(\[Omitted image "ExportCIHistoryChanges.png"\] Alt text: export icon\).

6.  Select the file format to use for the export.

    You can download the file to your system for viewing.

## Related

- [[sc-configuration|Configuration]]
- [[c_AuditedTables|Auditing]]
- [[export|Export]]
