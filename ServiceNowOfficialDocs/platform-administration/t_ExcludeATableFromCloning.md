---
title: Exclude a table from cloning
description: Exclude a table to create an empty but usable table on the target instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_ExcludeATableFromCloning.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Instance Clone, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Exclude a table from cloning

Exclude a table to create an empty but usable table on the target instance.

## Before you begin

Role required: clone\_admin

For information on excluding a table from cloning, see [[clone-exclusions-guidelines|General guidelines for excluding a table from cloning]].

## About this task

## Procedure

1.  Navigate to **All** &gt; **[[Clone-UI|Clone Admin Console]]** &gt; **Clone Home**.

2.  Select the **[[clone-exclusions-preservers-cleanupscripts|Definitions]]** tab.

3.  Select **Exclusions**.

4.  Select **New**.

5.  Enter the table **Name**.

    **Note:** Entering a parent table [[hs-results|results]] in the clone process also excluding its child tables. For example, excluding the task table would also exclude the Change, Incident, and Problem tables.

6.  Select **Save**.

## Related

- [[clone-exclusions-guidelines|General guidelines for excluding a table from cloning]]
- [[Clone-UI|Clone Admin Console]]
- [[clone-exclusions-preservers-cleanupscripts|Definitions]]
- [[hs-results|Results]]
