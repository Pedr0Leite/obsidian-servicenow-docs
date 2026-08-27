---
title: View the clone history page \(legacy\)
description: You can view the status and history of any instance clone request.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_ViewCloneHistory.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Manage, Instance Clone, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# View the clone history page \(legacy\)

You can view the status and history of any [[system-clone-landing|instance clone]] request.

## Before you begin

Role required: clone\_admin

## About this task

The `clone_instance` table stores records for all previously and currently scheduled clones.

## Procedure

1.  Navigate to **All** &gt; **Instance Clone** &gt; **Live Clones** &gt; **Clone History**.

    Clone history also displays the **State** for current and past clones. Clones in the **Draft** state don’t appear on the clone history table. For more information see [[clone-states|Clone states]].

2.  Select a record to view its history.

## Related

- [[clone-states|Clone states]]
- [[system-clone-landing|Instance Clone]]
