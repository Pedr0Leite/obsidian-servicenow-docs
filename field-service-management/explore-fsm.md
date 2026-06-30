---
title: Exploring Field Service Management
description: Use the Field Service Management application to manage work requests that are performed on location by field service agents. Whether you are starting or expanding your implementation of Field Service Management, learn more about available features to help create a seamless experience for your dispatchers, managers, and agents to resolve issues and fulfill requests.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/field-service-management/explore-fsm.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Field Service Management]
---

# Exploring Field Service Management

Use the [[fsm-application-landing-page|Field Service Management]] application to manage work requests that are performed on location by field service agents. Whether you are starting or expanding your implementation of Field Service Management, learn more about available features to help create a seamless experience for your dispatchers, managers, and agents to resolve issues and fulfill requests.

## Field Service Management overview

Problems that require on-site services from field technicians must be addressed and resolved fast. The costs are high if you're attempting to resolve complex on-site issues using disparate, unconnected systems with little or no automation or visibility.

With the Field Service Management application, you can get more tasks resolved faster with applications that can streamline task workflows. Help your field service teams to proactively address issues and to resolve them quickly. With Field Service Management, connect teams, processes, and systems to find the root cause of issues and resolve them in a timely manner. Empower your technicians with access to all of their tasks using the Field Service mobile application, which can be used online or offline.

**Note:** You can also [View and download the full infocard](https://downloads.docs.servicenow.com/resource/enus/infocard/fsm-landingpage-infographic.pdf) for a highlight of Field Service Management features.

## Field Service Management users

<table id="table_hhb_f1g_3cc"><thead><tr><th>

User

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Administrator

</td><td>

Configure the Field Service Management application to automate the process of assigning work order tasks to field technicians and make it ready for use.

</td></tr><tr><td>

Initiator

</td><td>

Create a new work order or can create a work order from other record types, such as problem, incident, change, or project task.

</td></tr><tr><td>

Qualifier

</td><td>

Review and qualify work orders to ensure that the work order tasks are created.

</td></tr><tr><td>

Dispatcher

</td><td>

Assign the work order tasks to the most appropriate and available agents. Dispatcher can also track agent's travel and work time, [[c_PartRequirements|part requirements]], and asset usage.Dispatchers are a part of the Field Service Management team, who manages the field teams and customer experience simultaneously to achieve positive outcome for the organization.

</td></tr><tr><td>

Manager

</td><td>

Manage and monitor the progress of work order tasks. If an agent rejects the task, you can reassign the tasks to another agent.

</td></tr><tr><td>

Agent

</td><td>

Travel to the customer location with the required parts and skills to work on the assigned task.

</td></tr></tbody>
</table>## Field Service Management workflow

The following example shows a sample Field Service Management end-to-end workflow describing different roles and stages handled by these roles starting from creating the work order and related task through the completion of the work order task. \[Omitted image "explore-fsm.png"\] Alt text: FSM exploring workflow

1.  As an administrator, you can configure the Field Service Management application to automate the process of assigning work order tasks to field technicians and make it ready for use.
2.  When the application is ready to use, the initiator creates a new work order or can create a work order from other record types, such as problem, incident, change, or project task.
3.  Then qualifier reviews and qualifies work orders to ensure that the work order tasks are created.
4.  The qualified work orders then goes to the dispatcher queue so that the dispatcher can assign the work order tasks to the most appropriate and available agents.
5.  The manager oversees and monitors the progress of work order tasks. If an agent rejects the task, you can reassign the tasks to another agent.
6.  After accepting the work order task, the agent travels to the customer location with the required parts and skills to work on the assigned task.

## Field Service Management benefits

Field Service Management provides the following benefits:

|Benefit|Feature|Users|
|-------|-------|-----|
|Simplify setup using low-code plugins and guided setup.|[[simplified-setup|Guided setup]]|Administrator|
|Optimize task scheduling, auto-assign tasks, and adapt to changing conditions.|[[schedule-optimization|Schedule Optimization]]|Administrator|
|Automatically capture critical data when creating a work order from a case, incident, problem, change request, or project task record.|[[Work-order-fsm|Integrated work order entry]]|Initiator|
|Empower customers using Field Service Management - Customer Experience to track en-route [[c_AgentLocation|agent location]] and arrival time.|[[customer-experience|Customer Experience in Field Service Management]]|Initiator|
|Find and analyze work orders with similar underlying issues using Predictive Intelligence for Field Service Management.|[[machine-learning-fsm|Work order insights powered by Predictive Intelligence]]|Manager|
|Make the most of your resources. Schedule work for technicians dynamically based on [[capacity|capacity]] and tasks.|[[capacity-management|Capacity and Reservations Management]]|Manager|
|Give dispatchers everything they need in one place to make smart and fast scheduling decisions.|[[dispatcher-activities|Dispatcher Workspace]]|Dispatcher|
|Automatically assign tasks to available field service agents with the right skills and equipment.|[[dynamic-scheduling|Dynamic scheduling]]|Dispatcher|
|Improve agent utilization by recommending the best available tasks to fill gaps in the agent's schedule.|[[fsm-task-recommendation|Intelligent Task Recommendation]]|Dispatcher|
|Support complex work for technician crews.|[[field-service-crew-scheduling|Field Service Crew Operations]]|Dispatcher|
|Optimizes contractor management, improves communication, and streamlines task allocation processes.|[[fsm-marketplace|Field Service Marketplace]]|Dispatcher|
|Efficiently schedule and manage the resource utilization for work order task based on different geographic regions.|[[territory-planning-fsm|Field Service Territory Planning]]|Territory Planner|
|Enable technicians with an intuitive, native Mobile Agent application that enables them to quickly view and record information.|[[mobile-experience-fsm|Mobile experience for Field Service Management]]|Field Service Agent|
|Achieve seamless visibility and task resolution for complex workflows across teams and business units.|[[playbooks|Playbooks for Field Service Management]]|Field Service Agent|
|Track and manage the inventory between stockrooms.|[Manage inventory in Field Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/field-service-management/work-order-management/sourcing-parts.md)|Field Service Agent|
|Enable agents to generate work order task summaries so that they can create notes faster and with more detail.|[Now Assist for Field Service Management \(FSM\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/field-service-management/now-assist-for-field-service-management-fsm/now-assist-fsm.md)|Field Service Agent|
|On-board contractor teams for outsourcing work order tasks and ensuring that service level agreements are met.|[[monitoring-analytics-fsm|Field Service Contractor Management]]|Manager|
|Monitor and enforce compliance with environment or health protocols.|[Emergency Exposure Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/field-service-management/monitoring-analytics-fsm.md)|Manager|

## What to explore next

-   [What is field service management \(FSM\)?](https://www.servicenow.com/products/field-service-management/what-is-fsm.html)
-   [[configure-fsm|Configuring Field Service Management]]
-   [[use-fsm|Using Field Service Management]]
-   [[analytics-reporting-fsm|Analytics and reporting for Field Service Management]]
-   [[fsm-reference|Field Service Management reference]]

## Related

- [[simplified-setup|Field Service Management Guided Setup]]
- [[schedule-optimization|Schedule Optimization]]
- [[Work-order-fsm|Integrated work order entry]]
- [[customer-experience|Customer Experience in Field Service Management]]
- [[machine-learning-fsm|Work order insights powered by Predictive Intelligence]]
- [[capacity-management|Capacity and Reservations Management]]
- [[dispatcher-activities|Dispatcher Workspace]]
- [[dynamic-scheduling|Dynamic scheduling]]
- [[fsm-task-recommendation|Intelligent Task Recommendation]]
- [[field-service-crew-scheduling|Field Service Crew Operations]]
- [[fsm-marketplace|Field Service Marketplace]]
- [[territory-planning-fsm|Field Service Territory Planning]]
- [[mobile-experience-fsm|Mobile experience for Field Service Management]]
- [[playbooks|Playbooks for Field Service Management]]
- [[monitoring-analytics-fsm|Monitoring and analytics for Field Service Management]]
- [[configure-fsm|Configuring Field Service Management]]
- [[use-fsm|Using Field Service Management]]
- [[analytics-reporting-fsm|Analytics and reporting for Field Service Management]]
- [[fsm-reference|Field Service Management reference]]
- [[fsm-application-landing-page|Field Service Management]]
- [[c_PartRequirements|Part requirements]]
- [[c_AgentLocation|Agent location]]
- [[capacity|Capacity]]
