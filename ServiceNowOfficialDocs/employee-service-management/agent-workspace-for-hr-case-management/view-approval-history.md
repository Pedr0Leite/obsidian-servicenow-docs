---
title: View approval history in Agent Workspace for HR Case Management
description: Review the approval history in the activity stream. Get a better understanding of when the approval request was created, who were the approvers, and when was the request rejected or approved.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/agent-workspace-for-hr-case-management/view-approval-history.html
release: australia
product: Agent Workspace for HR Case Management
classification: agent-workspace-for-hr-case-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Working with approvers for a case in Agent Workspace for HR Case Management, Using Agent Workspace for HR Case Management, Agent Workspace, HR Service Delivery, Employee Service Management]
tags:
  - employee-service-management
  - hr
  - agent-workspace
  - case-management
  - type-task
---

# View approval history in Agent Workspace for HR Case Management

Review the approval history in the [[activity-lxp|activity]] stream. Get a better understanding of when the approval request was created, who were the approvers, and when was the request rejected or approved.

## Before you begin

-   Role required: sn\_hr\_core.case\_writer
-   Ensure that the following plugins are installed: Human Resources Scoped App:Core, Human Resources Scoped App:[[hr-lifecycle-events-landing-page-1|Lifecycle Events]], Human Resources Scoped App:Lifecycle Events for Enterprise, HRSD Configurable Workspace, and Human Resources Scoped app Workspace.

## Procedure

1.  Navigate to **All** &gt; **HR [[case-management-workspace|Case Management]]** &gt; **[[agent-ws-hr-case-mgmt-landing-page|Agent Workspace for HR Case Management]]**.

2.  Open a case that is in Ready state.

3.  Activity stream contains the approval history, for example, when was the approval request created, who were the approvers, and when was the request rejected or approved.

    **Note:**

    -   Approval history appears in activity stream only when the **glide.workflow.user\_approval\_history** property in **sys\_properties.list** is set to true.
    -   If this property is set to true in [[hr-service-delivery|HR Service Delivery]] workspace, it will be also to be true for all other installations within ServiceNow AI Platform.

## Related

- [[activity-lxp|Activity]]
- [[hr-lifecycle-events-landing-page-1|Lifecycle Events]]
- [[case-management-workspace|Case management]]
- [[agent-ws-hr-case-mgmt-landing-page|Agent Workspace for HR Case Management]]
- [[hr-service-delivery|HR Service Delivery]]
