---
title: Configure case management
description: Configure the Customer Service Management features and components that agents and managers use to create and resolve cases.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-csm-case-management.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Configure case management

Configure the [[c_CustomerServiceManagement|Customer Service Management]] features and components that agents and managers use to create and resolve cases.

## Before you begin

Role required: csm\_guided\_setup\_user or admin

## About this task

The customer service case is the primary entity of the customer service application. An agent creates a case to identify a customer's question or issue and to track the activities related to resolving the issue. An agent also uses a case to track all of the communication to and from the customer, including the communication channels being used.

Case activities include any action that is taken to resolve an issue. This can include phone calls or emails, knowledge base research, conversations with subject matter experts, and dispatch requests to field service agents, as well as other activities.

From the [[r_CustomerServiceCaseForm|Case form]], an agent can associate and store the related information, such as the customer's name, phone number, and company; account information; product and asset information; service contract and entitlement details, and any associated service level agreements \(SLAs\).

**Note:** These steps may also apply to case type configuration.

To configure case management, use the Customer Service guided setup. The guided setup takes you through the entire setup and configuration process.

## Procedure

1.  Navigate to **All** &gt; **Customer Service** &gt; **Administration** &gt; **Guided Setup**.

2.  On the Getting Started page of the guided setup, select **Get Started**.

3.  In the [[case-management|Case Management]] category, view the list of tasks to configure the feature.

<table id="table_pz1_qqv_llb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[csm-cases-case-tasks-overview|Cases and case tasks]]

</td><td>

Cases and case tasks enable agents to capture, track, and resolve customer questions and issues. Cases store customer and issue details, while case tasks are assigned to users to complete the work required to resolve the case.

</td></tr><tr><td>

[[configure-case-form|Configure a Case form view]]

</td><td>

The case form displays detailed information about a customer issue or problem. Create a case form view to display the desired fields.

</td></tr><tr><td>

[[t_DefineSLAForCustServiceCase|Configure SLA definitions for customer service cases]]

</td><td>

Customer Service Management uses service level agreements \(SLAs\) with customer service cases. An SLA can be attached to a service contract, to a company, and to a product and can be configured to start, pause, and stop based on any customer service case attributes.

 After creating the necessary SLAs, associate them with customer service cases from the SLAs related list on the Case form.

</td></tr><tr><td>

[[configure-case-routing-assignment|Configure case routing and assignment]]

</td><td>

The case routing feature uses matching [[gamification-components-rules|rules]] and assignment rules to identify cases that meet certain conditions and then route those cases to customer service agents.Create matching rules to identify cases and then create assignment rules to route cases to agents.

</td></tr><tr><td>

[[configure-assignment-workbench|Configure assignment workbench]]

</td><td>

The assignment workbench uses configurable criteria, such as skills and availability, to evaluate the agents in a selected group and provide an overall ranking. Managers can view these results and select one button to assign a task.To configure the assignment workbench:

-   Create matching criteria.
-   [[create-assignment-wkbench-config|Create an assignment workbench configuration]].


</td></tr><tr><td>

[[configure-major-issue-management|Configure major issue management]]

</td><td>

Major issue management enables [[customer-communication|customer communication]] for issues that impact a wider audience. Use this feature to proactively identify impacted customers, create cases for these customers, provide information, and manage the resolution process.

</td></tr><tr><td>

[[c_TargetedCommunications|Targeted communications]]

</td><td>

Targeted Communications enables organizations to create and deliver articles and email communications to specific internal and external audiences. It supports targeted recipient [[migration-lists|lists]], optional email notifications, and scheduled publishing to ensure timely and relevant communication.

</td></tr><tr><td>

[[configure-special-handling-notes|Configure special handling notes]]

</td><td>

Use [[c_OnScreenAlerts|special handling notes]] to bring important case information to an agent’s attention. Create a configuration for the Case \[sn\_customerservice\_case\] table and then configure the form layout to display the notes in a pop-up window or a related list.

</td></tr><tr><td>

[[configure-case-action-status|Configure case action status]]

</td><td>

The [[case-action-status-csm-workspace|case action status]] feature enables customer service agents to easily identify cases that need attention and quickly prioritize their work. Visual indicators in the **Action Status** column on the case list highlight case status.

</td></tr><tr><td>

[[employee-create-case-for-customer|Create cases as a proxy contact]]

</td><td>

The proxy contact role allows employees to create cases on behalf of customers without requiring fulfiller access.

</td></tr><tr><td>

[[csm-extension-for-proxy-contacts|Install the CSM Extension for Proxy Contacts]]

</td><td>

The CSM Extension for Proxy Contacts installs the components required to support proxy contact functionality in CSM.

</td></tr><tr><td>

[[configure-auto-close-resolved-cases|Configure auto close resolved cases]]

</td><td>

Automatically close cases in the Resolved state if customers do not take any action.

</td></tr><tr><td>

[[configure-escalation-management|Configure escalation management]]

</td><td>

Escalating a case or account raises awareness about important customer issues, facilitates communication, and enables users to track progress toward a resolution. Create escalation templates and severity definitions to control the escalation process.

</td></tr><tr><td>

[[configure-case-digests|Configure case digests]]

</td><td>

Case digests enable agents to proactively communicate with customers and internal stakeholders about cases. -   Summaries: while a case is in progress, agents can send periodic case summaries that describe actions taken, next steps, and other case-related information.
-   [[case-digest-post-case-review|Post case reviews]]: when the work on a case has been completed, agents can [[create-case-review-document|create a post case review]] that includes information such as the root cause, mitigation plan, and preventive actions.


</td></tr></tbody>
</table>4.  To perform a task, select **Configure**.

    This button opens the page in your instance where the configuration is completed.

## Related

- [[csm-cases-case-tasks-overview|Cases and case tasks]]
- [[configure-case-form|Configure a Case form view]]
- [[t_DefineSLAForCustServiceCase|Configure SLA definitions for customer service cases]]
- [[configure-case-routing-assignment|Configure case routing and assignment]]
- [[configure-assignment-workbench|Configure assignment workbench]]
- [[configure-major-issue-management|Configure major issue management]]
- [[c_TargetedCommunications|Targeted communications]]
- [[configure-special-handling-notes|Configure special handling notes]]
- [[configure-case-action-status|Configure case action status]]
- [[employee-create-case-for-customer|Create cases as a proxy contact]]
- [[csm-extension-for-proxy-contacts|Install the CSM Extension for Proxy Contacts]]
- [[configure-auto-close-resolved-cases|Configure auto close resolved cases]]
- [[configure-escalation-management|Configure escalation management]]
- [[configure-case-digests|Configure case digests]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[r_CustomerServiceCaseForm|Case form]]
- [[case-management|Case management]]
- [[gamification-components-rules|Rules]]
- [[create-assignment-wkbench-config|Create an assignment workbench configuration]]
- [[customer-communication|Customer communication]]
- [[migration-lists|Lists]]
- [[c_OnScreenAlerts|Special handling notes]]
- [[case-action-status-csm-workspace|Case action status]]
- [[case-digest-post-case-review|Post case reviews]]
- [[create-case-review-document|Create a post case review]]
