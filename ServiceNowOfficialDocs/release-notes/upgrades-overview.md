---
title: Upgrade to the Australia release
description: Upgrading and patching your instance requires planning, testing, and validation. To ensure a safe and effective upgrade, read the release notes, create upgrade plans, and test your upgrade on non-production instances before upgrading your production instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/release-notes/upgrades-overview.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Australia release notes]
tags:
  - release-notes
  - type-concept
---

# Upgrade to the Australia release

Upgrading and patching your instance requires planning, testing, and validation. To ensure a safe and effective upgrade, read the release notes, create upgrade plans, and test your upgrade on non-production instances before upgrading your production instance.

**Important:** These topics contain in-depth explanations about upgrades. For a step-by-step reference of upgrade steps, refer to the [[upgrades-planning-checklist|Upgrade planning checklist]].

<table id="table_sqt_d3p_d2b"><tbody><tr><td>

\[Omitted image "phase1-book.png"\] Alt text: Release notes

</td><td>

-   **[[upgrades-phase-1|Phase 1 - Read the release notes and plan your upgrade]]**

Before you begin the upgrade process, it is essential to read the release notes for your target version so you understand the required upgrade and migration tasks. This information helps you plan a safe and effective upgrade.


</td></tr><tr><td>

\[Omitted image "phase2-checklist.png"\] Alt text: Upgrade checklist

</td><td>

-   **[[upgrades-phase-2|Phase 2 - Prepare for the development instance upgrade]]**

For a better understanding of your production upgrade duration, request a full clone of your production instance \(including large tables and attachments\) onto a non-production instance. Confirm your current and target release versions, because you will later use this information when scheduling your upgrade in Now Support.


</td></tr><tr><td>

\[Omitted image "phase3-calendar.png"\] Alt text: Calendar with an upgrade date

</td><td>

-   **[[upgrades-phase-3|Phase 3 - Verify your upgrade configurations and schedule the development instance upgrade in Now Support]]**

Check the configuration of the **Check distribution for possible upgrade** scheduled job to view how often and when it runs. Review information about timing your upgrade in coordination with the **Check distribution for possible upgrade** scheduled job. Then, schedule your upgrade in Now Support.


</td></tr><tr><td>

\[Omitted image "phase4-upgrade-progress-checkmark.png"\] Alt text: Upgrade progress screen

</td><td>

-   **[[upgrades-phase-4|Phase 4 - Upgrade and validate the development instance]]**

Track the progress of your upgrades with the Upgrade Monitor. For your first non-production instance upgrade \(your development instance\), use the Upgrade Monitor to process the skipped list of records that were not addressed in the upgrade. Then identify your update sets and perform functional testing.


</td></tr><tr><td>

\[Omitted image "phase5-recursive-arrow.png"\] Alt text: Upgrade other instances

</td><td>

-   **[[upgrades-phase-5|Phase 5 - If applicable: Upgrade and validate your other non-production instances, such as your test instance]]**

After you've configured and refined your development instance, request to upgrade any other non-production instances you have, such as a test instance. Immediately after the upgrade is complete, apply the post-upgrade changes made to your development instance, including activating optional plugins, installing and upgrading applications, and applying update sets.


</td></tr><tr><td>

\[Omitted image "phase2-checklist.png"\] Alt text: Upgrade checklist

</td><td>

-   **[[upgrades-phase-6|Phase 6 - Prepare to upgrade the production instance]]**

After you have configured and refined your test environment to be a good representation of your production environment, prepare to upgrade your production instance.


</td></tr><tr><td>

\[Omitted image "phase4-upgrade-progress-checkmark.png"\] Alt text: Upgrade progress screen

</td><td>

-   **[[upgrades-phase-7|Phase 7 - Upgrade the production instance]]**

After you have upgraded your development, non-production, and test instances, upgrade your production instance last. Then validate that the upgrade was complete, apply update sets and fix scripts, and perform post-upgrade user acceptance testing \(UAT\).


</td></tr></tbody>
</table>

## Related

- [[upgrades-planning-checklist|Upgrade planning checklist]]
- [[upgrades-phase-1|Phase 1 - Read the release notes and plan your upgrade]]
- [[upgrades-phase-2|Phase 2 - Prepare for the development instance upgrade]]
- [[upgrades-phase-3|Phase 3 - Verify your upgrade configurations and schedule the development instance upgrade in Now Support]]
- [[upgrades-phase-4|Phase 4 - Upgrade and validate the development instance]]
- [[upgrades-phase-5|upgrades phase 5]]
- [[upgrades-phase-6|Phase 6 - Prepare to upgrade the production instance]]
- [[upgrades-phase-7|Phase 7 - Upgrade the production instance]]
