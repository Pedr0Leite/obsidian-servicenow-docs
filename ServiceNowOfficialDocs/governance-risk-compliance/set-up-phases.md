---
title: Set up the phases
description: Set up the phases in the Business Continuity Management application to map them to recovery and event tasks effectively. Once the phases are set up, BCM users can tag these phases to recovery tasks and event tasks and execute them in the set order, ensuring a logical execution sequence.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/set-up-phases.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Set up the phases

Set up the phases in the [[business-continuity-mangmt-overview|Business Continuity Management]] application to map them to recovery and event tasks effectively. Once the phases are set up, BCM users can tag these phases to recovery tasks and event tasks and execute them in the set order, ensuring a logical execution sequence.

## Before you begin

Role required: sn\_bcm.admin

## About this task

For information on setting up the phases, see [Set up the phases](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/set-up-phases.md).

For information and steps on mapping recovery tasks to phases, see [[mapping-recovery-tasks-to-phases|Mapping recovery tasks to phases]] and [[add-a-recovery-task|Add recovery tasks]].

For information on mapping event tasks to phases, see [[mapping-event-tasks-to-phases|Mapping event tasks to phases]] and [Mapping event tasks to phases](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/mapping-event-tasks-to-phases.md).

## Procedure

1.  Navigate to **All** &gt; **Business Continuity** &gt; **General [[Administration|Administration]]** &gt; **Active phases**.

    Recovery involves a series of phases. By default, the BCM application provides these phases as part of seed data:

    -   Preparation
    -   Recovery
    -   Recovery validation
    -   Return to normal
    -   Return to normal validation
    -   Post-incident review
    \[Omitted image "phases-seed-data.png"\] Alt text: Seed data.

2.  Select **New**.

    The Phase form is shown in the example.

    \[Omitted image "new-phase.png"\] Alt text: New phase.

3.  On the form, fill in the fields.

    For the description of the fields, see [[phase-form|Phase form]].

    A sample configuration of the phase is shown where the name of the phase is phase10, its order is 80, and the phase is active.

    \[Omitted image "preparation-phase.png"\] Alt text: Preparation phase.

    The order field is automatically populated with the next available number. For example, if the previous maximum order was 70, the new order will be 80. You can, however, manually adjust this order using inline editing if required, ensuring that the order remains unique across all phases.

    **Note:** If you try to assign an existing order to the new phase, an error message is displayed that the order already exists. Similarly, if you try to assign an existing name to a phase, the system prevents that by displaying an error message.

    The error messages are shown in the example.

    \[Omitted image "phase-error-msgs.png"\] Alt text: Error messages.

    To prevent permanent deletion, the form does not include a delete button. Instead, you can soft-delete phases by clearing the Active flag, which removes them from active use in recovery and event tasks. This approach verifies that phases are not permanently lost and can be managed effectively.

4.  Select **Submit**.

    The configured phase is shown in the [[list-view-uib-ws|list view]] of the Phases module and it can be tagged to the recovery and event tasks, allowing for more effective tracking and management of these tasks.

## Related

- [[mapping-recovery-tasks-to-phases|Mapping recovery tasks to phases]]
- [[add-a-recovery-task|Add recovery tasks]]
- [[mapping-event-tasks-to-phases|Mapping event tasks to phases]]
- [[phase-form|Phase form]]
- [[business-continuity-mangmt-overview|Business Continuity Management]]
- [[Administration|Administration]]
- [[list-view-uib-ws|List view]]
