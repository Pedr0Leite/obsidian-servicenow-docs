---
title: Create a business continuity plan from a plan template
description: Create a business continuity plan from a plan template in BCM UIB Workspace so that the loss scenarios, recovery strategies, and recovery tasks defined on the template are generated automatically.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/create-bcp-plan-from-template-in-uib-ws.html
release: australia
topic_type: task
last_updated: "2026-05-30"
reading_time_minutes: 2
breadcrumb: [Structured workflows for BCPs, Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Create a business continuity plan from a plan template

Create a business continuity plan from a plan template in BCM UIB Workspace so that the loss scenarios, recovery strategies, and recovery tasks defined on the template are generated automatically.

## Before you begin

Role required: sn\_bcp.plan\_contributor or sn\_bcp.plan\_manager

## About this task

A plan template can reference recovery strategy templates, task template groups, and task templates at the plan, loss scenario, and recovery strategy levels. When you create a plan from such a template, the system creates the documentation, loss scenarios, recovery strategies, and recovery tasks in a single operation, so you do not have to add each record manually.

For information on building a plan template that pre-populates these records, see [[configure-a-bcp-template-uib-ws|Configure the business continuity plan template]] and [[bcp-admin-plan-templates|Configuring plan template]].

## Procedure

1.  Navigate to **Workspaces** &gt; **Business Continuity Workspace** &gt; **Planning** in the [[list-view-uib-ws|list view]] and select **New**.

2.  On the **Details** tab of the **Create New Plan** form, select a plan template in the **Template** field.

    The template determines which loss scenarios, recovery strategies, task template groups, and task templates are generated for the plan.

3.  Enter a name for the plan and fill in the remaining required fields.

    For more information on the fields, see [[create-new-plan-bcp-uib-ws-reference-form|Create New Plan form]].

4.  Select **Save**.

    The progress tracker on the plan record shows the creation status while the system generates the documentation, loss scenarios, recovery strategies, and recovery tasks from the template.

    \[Omitted image "plan-progress-tracker-from-template.png"\] Alt text: Plan record after creation from a template, with the progress tracker indicating that documentation, loss scenarios, and recovery tasks are being created.

5.  After the progress tracker completes, review the generated records on the plan tabs.

    The **Loss scenarios** tab lists the loss scenarios from the template. Each loss scenario contains the recovery strategies and recovery tasks defined for it, and each recovery strategy contains the recovery tasks added at the recovery strategy level. Task dependencies defined inside a task template group are preserved on the created tasks.


## Result

The plan is created in the **Draft** state with the loss scenarios, recovery strategies, and recovery tasks generated at each level. You can add more records or apply additional task template groups from the **Recovery tasks** tab. For more information, see [[add-a-recovery-task|Add recovery tasks]].

**Parent Topic:**[[bcp-tasks-performed-by-bcp-owner|Structured workflows for BCPs]]

## Related

- [[configure-a-bcp-template-uib-ws|Configure the business continuity plan template]]
- [[bcp-admin-plan-templates|Configuring plan template]]
- [[create-new-plan-bcp-uib-ws-reference-form|Create New Plan form]]
- [[add-a-recovery-task|Add recovery tasks]]
- [[bcp-tasks-performed-by-bcp-owner|Structured workflows for BCPs]]
- [[list-view-uib-ws|List view]]
