---
title: Add recovery strategies for dependencies
description: Add a recovery strategy for the related asset dependencies and estimate the time to implement the strategy. You can then get the assets up and running quickly in an identified loss scenario.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/create-new-recovery-strategy-for-loss-scenario-uib-ws.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Structured workflows for BCPs, Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Add recovery strategies for dependencies

Add a recovery strategy for the related asset dependencies and estimate the time to implement the strategy. You can then get the assets up and running quickly in an identified loss scenario.

## Before you begin

Role required: sn\_bcm.program\_manager or sn\_bcm.planner

## Procedure

1.  Navigate to **Workspaces** &gt; **Business Continuity Workspace**.

2.  In the [[list-view-uib-ws|List view]], navigate to the loss scenario in the plan record.

3.  Navigate to the **Recovery strategies** tab and select **New**.

    The Create new Recovery strategy form is displayed as shown in the example.

    \[Omitted image "loss-scenarios-create-new-reco-strategy.png"\] Alt text: Create new Recovery strategy form.

4.  To apply a pre-defined recovery strategy template, select **Add recovery strategy template**, choose the template, then select **Add**.

    Recovery strategy templates pre-fill the **Estimated time to implement**, **Maximum duration of use**, and **Estimated % of operations achieved** fields. You can still adjust the values on the loss scenario record after the template is applied.

5.  On the form, fill in the fields.

    For more information on the fields in the form, see [[create-new-recovery-strategy-form|Create Recovery strategy form]].

6.  Select **Save**.

    You can save the recovery strategy as shown in the example.

    \[Omitted image "loss-scenarios-save-reco-strategy-reco-task.png"\] Alt text: Saving recovery strategy.

    The **Recovery tasks** tab is displayed in the Recovery strategy form.

    Starting with the Australia release of the application, the Recovery strategies record has the following related lists:

    -   Task template groups
    -   Task templates
    -   Loss scenarios
    -   Plan templates

## What to do next

You can add one or more recovery tasks as part of the recovery strategy as the next step.

On the recovery strategy **Recovery tasks** tab, select **Add groups** or **Add tasks** to populate the strategy with reusable templates. The element-definition filter inherited from the parent loss scenario is applied automatically.

\[Omitted image "recovery-strategy-with-tasks-from-group.png"\] Alt text: Recovery strategy Recovery tasks tab with tasks added from a task template group, each pre-populated with Plan loss scenario and Plan recovery strategy.

For information on creating reusable recovery strategy templates, see [[configure-recovery-strategy-template-uib-ws|Configure a recovery strategy template]].

-   **[Create Recovery strategy form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/create-new-recovery-strategy-form.md)**  
Use the Create New Recovery strategy form in BCM UIB Workspace to add details about the recovery strategy for the identified loss scenario.

**Parent Topic:**[[bcp-tasks-performed-by-bcp-owner|Structured workflows for BCPs]]

## Related

- [[create-new-recovery-strategy-form|Create Recovery strategy form]]
- [[configure-recovery-strategy-template-uib-ws|Configure a recovery strategy template]]
- [[bcp-tasks-performed-by-bcp-owner|Structured workflows for BCPs]]
- [[list-view-uib-ws|List view]]
