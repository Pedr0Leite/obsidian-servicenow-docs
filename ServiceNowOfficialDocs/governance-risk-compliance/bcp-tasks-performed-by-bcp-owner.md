---
title: Structured workflows for BCPs
description: Perform the structured workflows that are outlined in this section to create a business continuity plan in Business Continuity Workspace \(also known as BCM Configurable Workspace\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/bcp-tasks-performed-by-bcp-owner.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 8
breadcrumb: [Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Structured workflows for BCPs

Perform the structured workflows that are outlined in this section to create a business continuity plan in Business Continuity Workspace \(also known as [[bcm-workspace|BCM Configurable Workspace]]\).

Business continuity plan owner creates a business continuity plan as per the plan template, adds an asset and scope to the plan, creates documentation sections, adds the related plan and recovery team, adds a loss scenario with recovery strategy and recovery task, and generates and saves the PDF of the analysis for reference.

-   For information on creating a business continuity plan, see [[create-bcp-plan-in-uib-ws|Create a business continuity plan]]. For information on adding an asset and scope to the plan, see [[add-asset-plan-scope-for-bcp-uib-ws|Add asset and scope to the BCP]].
-   For information on creating a documentation section, see [[create-documentation-section-bcp|Create documentation sections]]. For information on adding the related plan and recovery team, see [[add-related-plans-recovery-teams-bcp-uib-ws|Add associated plans and recovery teams]].
-   For information on adding a loss scenario, recovery strategy, and recovery task, see [[add-loss-scenario-recovery-task-bcp-uib-ws|Add loss scenarios]], [[create-new-recovery-strategy-for-loss-scenario-uib-ws|Add recovery strategies for dependencies]], and [[add-a-recovery-task|Add recovery tasks]].
-   For information on generating and saving the PDF, see [[generate-pdf-for-bcp|Generate BCP reports in PDF or Microsoft Word format]].

## Hierarchical plan structure enhancement

Starting with BCM, version 9.x.x, the hierarchical structure of parent-child plans verifies logical organization and execution of recovery tasks. With this enhancement, when an event is triggered, only relevant child plans are brought into the scope, allowing plan execution and dependencies to cascade downward in a controlled manner.

Parent plans are excluded to prevent the inclusion of unrelated scenarios that may require subsequent cancellation. This approach confirms that only relevant plans are considered, maintaining a focused and efficient recovery process.

The system also performs cyclic dependency checks automatically, ensuring that the hierarchy always flows one directionally—from parent plans to child plans.

Implementing the hierarchical plan structure offers these key benefits:

-   Logical task execution: Only after the necessary tasks in the parent plans have been completed, tasks in the child plans are executed, ensuring a controlled and sequential recovery process.
-   Avoidance of circular dependencies: The system is designed to prevent circular dependencies, maintaining a unidirectional flow from parent to child plans and avoiding potential conflicts.
-   Parallel execution: Tasks within the same plan can be executed in parallel when possible, optimizing recovery time and efficiency.

By introducing this hierarchical structure, the system provides an organized and manageable approach to plan management, enhancing efficiency and effectiveness in disaster recovery planning and execution.

## Nested related plans

Beginning with the Xanadu release, the handling of nested related plans has improved. This enhancement helps in managing potential cyclic dependencies by detecting and highlighting any problems that could cause cyclic dependencies during the execution of tasks.

Additionally, the refined recovery timelines enable you to monitor the planned and actual timeframes. A task may be applied to all assets within a plan or to none at all, facilitating an accurate aggregation of recovery timeframes across various levels, including assets, tasks, and plans.

## Additional information on Business Continuity Planning

-   For information on the **Planning** tab in the Home page, see [[home-page-uib-ws|Home page view]].
-   For information on business continuity planning, see [[bcp-uib|Business continuity planning]].
-   For information on the administrative tasks in business continuity planning, see [[bcp-admin-tasks|Setup for a business continuity plan]].

-   **[[states-ui-actions-bcp|States and UI actions for a BCP]]**  
When you create a business continuity plan \(BCP\), certain UI actions are associated with each state.
-   **[[recovery-strategy-and-task-templates-overview|Recovery strategy and task templates]]**  
Business continuity planners often rebuild the same recovery structures each time they author a plan. Reusable templates remove that repetition by capturing standard strategies, tasks, and task groupings once and applying them wherever they are needed.
-   **[Create a business continuity plan](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/create-bcp-plan-in-uib-ws.md)**  
Create a business continuity plan in BCM UIB Workspace.
-   **[[create-bcp-plan-from-template-in-uib-ws|Create a business continuity plan from a plan template]]**  
Create a business continuity plan from a plan template in BCM UIB Workspace so that the loss scenarios, recovery strategies, and recovery tasks defined on the template are generated automatically.
-   **[[import-cmdb-updates-in-plans|Scheduling auto-update of related assets]]**  
You can schedule an auto-update of the related assets in the plans based on the source data and relationships in the CMDB. You can receive an email notification with details of the plan dependency updates from the BCM application. Dependencies are fetched from different sources such as BIA upstream dependency, BIA downstream dependencies, and CMDB.
-   **[Add asset and scope to the BCP](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/add-asset-plan-scope-for-bcp-uib-ws.md)**  
Add an asset and the scope to the business continuity plan \(BCP\). You can then view the primary elements in the BCM Configurable Workspace.
-   **[Create documentation sections](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/create-documentation-section-bcp.md)**  
Create a documentation section in the business continuity plan. You can then document the recovery capabilities of your business continuity plan in BCM UIB Workspace.
-   **[Add associated plans and recovery teams](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/add-related-plans-recovery-teams-bcp-uib-ws.md)**  
Add your business continuity associated plans and recovery teams to your business continuity plan. You can then view the details in BCM UIB Workspace.
-   **[Add loss scenarios](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/add-loss-scenario-recovery-task-bcp-uib-ws.md)**  
Add a loss scenario and define the related asset dependencies in your business continuity plan. You can then view the details of the assets in BCM UIB Workspace and then plan a recovery strategy for an identified loss scenario.
-   **[Add recovery strategies for dependencies](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/create-new-recovery-strategy-for-loss-scenario-uib-ws.md)**  
Add a recovery strategy for the related asset dependencies and estimate the time to implement the strategy. You can then get the assets up and running quickly in an identified loss scenario.
-   **[[configure-recovery-strategy-template-uib-ws|Configure a recovery strategy template]]**  
Configure a reusable recovery strategy template so business continuity planners can apply a pre-defined strategy to loss scenarios without re-entering the implementation details each time.
-   **[[mapping-recovery-tasks-to-phases|Mapping recovery tasks to phases]]**  
Starting with BCM, version 9.x.x, BCM administrators set up active phases for plans and events, enhancing recovery and event task management. BCM managers then map these phases to recovery and event tasks, executing them in a desired, logical sequence.
-   **[Add recovery tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/add-a-recovery-task.md)**  
Add a recovery task as part of the planned recovery strategy. You can add one or more recovery tasks for a loss scenario and those recovery tasks are displayed in the loss scenario itself. Automate the recovery tasks in a plan for a faster recovery.
-   **[[create-reco-task-tem-groups|Apply Task templates and Task template groups]]**  
Save individual tasks or groups of tasks for reuse across plans. You can add templates to new plans or inserted into existing ones. You can also generate templates directly from tasks and plans that already exist in the system.
-   **[[create-quick-recovery-task|Create a quick recovery task]]**  
Create a quick recovery task from Recovery tasks or as part of the planned recovery strategy for a business continuity plan. Using the quick insert feature, you can create tasks without navigating to a separate form. Tasks can be ordered, inserted in sequence \(before, after, or in parallel with existing tasks\), and dependencies are updated automatically.
-   **[[view-gantt-chart-for-reco-tasks|Visualize recovery tasks on Gantt chart]]**  
Use the Gantt chart component on recovery task pages to provide a visual timeline view of tasks associated with the current plan. Customize the view by adding, removing, or reordering columns as needed. The chart is implemented as a UI page to enable customizations and to support multiple versions without requiring changes to existing page behavior.
-   **[[syn-ast-be-lo-sce-and-rec-stgy|Synchronize assets between loss scenarios and recovery strategies]]**  
Use the asset syncing fields in the plan template to configure whether assets synchronize to loss scenarios, to recovery strategies, or both. Syncing is a two-step process: assets flow from the plan to loss scenarios first, and then from loss scenarios to recovery strategies.
-   **[[automate-the-recovery-tasks|Automate recovery tasks]]**  
Automate the manual recovery task within the business continuity plan. You can classify the manual recovery task as an automated task first and then attach an automated flow to it.
-   **[[submit-bcp-for-review|Submit the BCP for approval]]**  
Submit the business continuity plan \(BCP\) for an approval. You can then view the details in BCM UIB Workspace.
-   **[[relationship-view-bcp|Visualize 360° relationships for the BCP]]**  
Visualize the 360° relationships for a business continuity plan \(BCP\) and its associated entities in BCM UIB Workspace. You can access the 360° view at any time while working on the business continuity plan.
-   **[Generate BCP reports in PDF or Microsoft Word format](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/generate-pdf-for-bcp.md)**  
Generate a PDF or Microsoft Word copy of a business continuity plan in the BCM Configurable Workspace and save it for a future reference.

**Parent Topic:**[[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]]

## Related

- [[create-bcp-plan-in-uib-ws|Create a business continuity plan]]
- [[add-asset-plan-scope-for-bcp-uib-ws|Add asset and scope to the BCP]]
- [[create-documentation-section-bcp|Create documentation sections]]
- [[add-related-plans-recovery-teams-bcp-uib-ws|Add associated plans and recovery teams]]
- [[add-loss-scenario-recovery-task-bcp-uib-ws|Add loss scenarios]]
- [[create-new-recovery-strategy-for-loss-scenario-uib-ws|Add recovery strategies for dependencies]]
- [[add-a-recovery-task|Add recovery tasks]]
- [[generate-pdf-for-bcp|Generate BCP reports in PDF or Microsoft Word format]]
- [[home-page-uib-ws|Home page view]]
- [[bcp-uib|Business continuity planning]]
- [[bcp-admin-tasks|Setup for a business continuity plan]]
- [[states-ui-actions-bcp|States and UI actions for a BCP]]
- [[recovery-strategy-and-task-templates-overview|Recovery strategy and task templates]]
- [[create-bcp-plan-from-template-in-uib-ws|Create a business continuity plan from a plan template]]
- [[import-cmdb-updates-in-plans|Scheduling auto-update of related assets]]
- [[configure-recovery-strategy-template-uib-ws|Configure a recovery strategy template]]
- [[mapping-recovery-tasks-to-phases|Mapping recovery tasks to phases]]
- [[create-reco-task-tem-groups|Apply Task templates and Task template groups]]
- [[create-quick-recovery-task|Create a quick recovery task]]
- [[view-gantt-chart-for-reco-tasks|Visualize recovery tasks on Gantt chart]]
- [[syn-ast-be-lo-sce-and-rec-stgy|syn ast be lo sce and rec stgy]]
- [[automate-the-recovery-tasks|Automate recovery tasks]]
- [[submit-bcp-for-review|Submit the BCP for approval]]
- [[relationship-view-bcp|Visualize 360° relationships for the BCP]]
- [[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]]
- [[bcm-workspace|BCM Configurable Workspace]]
