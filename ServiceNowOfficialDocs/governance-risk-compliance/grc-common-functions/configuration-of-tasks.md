---
title: My tasks in the workspace
description: GRC administrators can configure the tasks for the individual users and user groups in the GRC Landing Page Configurations module. Based on these configurations, the workspace users can view the individual user tasks, user group tasks, my items, and watchlist on the Tasks page in the workspace view.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/grc-common-functions/configuration-of-tasks.html
release: australia
product: GRC Common Functions
classification: grc-common-functions
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Common GRC features, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - grc
  - attestation
  - evidence
  - scoping
  - type-concept
---

# My tasks in the workspace

GRC administrators can configure the tasks for the individual users and user groups in the GRC [[admin-config-using-grc-common|Landing Page Configurations module]]. Based on these configurations, the workspace users can view the individual user tasks, user group tasks, my items, and watchlist on the Tasks page in the workspace view.

The roles required to configure and view the workspaces are listed below.

|Role|Actions associated with the role for the workspace|
|----|--------------------------------------------------|
|sn\_grc.admin, sn\_grc\_workspace.task\_admin|Configure the Tasks Page Configuration records in all the workspaces.|
|sn\_grc.business\_user|View the Tasks page in the [[risk-portal|Risk Portal]] workspace.|
|sn\_audit\_ws.supervisor, sn\_audit\_ws.auditor,|View the Tasks page in the [[audit-management-overview-ws|Audit workspace]].|
|sn\_compliance.admin|Configure and view the [[tasks-page|Tasks page in the Compliance workspace]].|
|sn\_oper\_res.admin|Configure and view the Tasks page in the [[grc-opres-landing-page|Operational Resilience]] workspace.|
|sn\_privacy.admin|Configure and view the Tasks page in the Privacy workspace.|
|sn\_grc\_reg\_change.it\_admin|View the Tasks page in the Compliance workspace.|
|sn\_risk\_workspace.IT\_risk\_manager and sn\_risk\_workspace.operational\_risk\_manager,|View the Tasks page in the [[risk-workspace|Risk workspace]].|
|sn\_vdr\_risk\_asmt.vendor\_risk\_manager|View the Tasks page in the Vendor Management workspace.|

Based on the tasks that were set up by the administrators, the tasks are displayed under the following tabs in the configuration records for workspaces:

-   My pending tasks
-   My group's tasks
-   My items
-   Watchlist
-   [[confidential-records|Confidential records]]

You can view the Tasks page in the following workspaces:

-   Audit Workspace
-   Operational Resilience workspace
-   Policy and Compliance Workspace: Displayed under the Policy and Compliance module.
-   Privacy Workspace
-   [[reg-change-mgmt-landing-page|Regulatory Change Management]] Workspace in Policy and Compliance Workspace
-   Risk Workspace
-   Risk Portal
-   Vendor Management Workspace

    **Note:** My items and Watchlist are not displayed in the Vendor Management Workspace.


-   **[Monitor my tasks in the Tasks page in the workspace](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/grc-common-functions/configure-my-tasks-in-ws.md)**  
Configure and monitor the tasks that are related to an assigned user in the workspace. Configure the landing pages and the widgets that are displayed in the workspaces using the Landing Page Configurations module. The configurations performed using the Landing Page Configurations module help you to filter the data that is displayed in different workspaces.

**Parent Topic:**[Common Governance, Risk, and Compliance features](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/grc-common-functions/common-grc-features.md)

## Related

- [[admin-config-using-grc-common|Landing Page Configurations module]]
- [[risk-portal|risk portal]]
- [[audit-management-overview-ws|Audit Workspace]]
- [[tasks-page|Tasks page in the Compliance Workspace]]
- [[grc-opres-landing-page|Operational Resilience]]
- [[risk-workspace|risk workspace]]
- [[confidential-records|Confidential records]]
- [[reg-change-mgmt-landing-page|Regulatory Change Management]]
