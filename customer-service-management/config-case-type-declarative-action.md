---
title: Configure case type declarative actions
description: Configure declarative actions that enable agents to create cases and case tasks from different locations within CSM Configurable Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-case-type-declarative-action.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring customer service case types, Customer service case types, Case management, Organize agent workspaces, Configure, Customer Service Management]
---

# Configure case type declarative actions

Configure [[migration-form-declarative-actions|declarative actions]] that enable agents to create [[csm-cases-case-tasks-overview|cases and case tasks]] from different locations within [[csm-workspaces-configure|CSM Configurable Workspace]].

## Before you begin

Role required: admin

## About this task

The [[customer-service-case-types|Customer Service Case Types]] plugin includes declarative actions that enable agents to create cases and case tasks using the [[csm-case-type-select-modals|case type selector]] and [[csm-case-task-type-select-modal|case task type selector]]. These declarative actions are disabled by default.

|Action label|Location|Action|
|------------|--------|------|
|**Create Case**|Appears on the Case Task list views.|Displays the case task type selector.|
|**Create Case**|Appears on the Tasks related list tab on case and case type records.|Displays the case task type selector.|
|**Create Case**|Appears on the Case and Case Type list views.|Displays the case type selector.|

Declarative actions are stored in the Action Assignment \[sys\_declarative\_action\_assignment\] table.

## Procedure

1.  Navigate to **All** &gt; **Now Experience Framework** &gt; **Declarative Actions** &gt; **Form Actions**.

    The system displays the Action Assignments list.

2.  Filter the list to display the actions for the CSM Case Types application.

    If necessary, configure the list to display the **Application** column.

3.  For each of the desired declarative actions, set the **Active** field to true.

## Related

- [[csm-case-type-select-modals|Case type selector]]
- [[csm-case-task-type-select-modal|Case task type selector]]
- [[migration-form-declarative-actions|Declarative actions]]
- [[csm-cases-case-tasks-overview|Cases and case tasks]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[customer-service-case-types|Customer service case types]]
