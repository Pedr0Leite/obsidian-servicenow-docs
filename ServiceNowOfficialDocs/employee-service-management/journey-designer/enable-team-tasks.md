---
title: Enable team tasks
description: Enable team tasks to allow managers to add tasks to the Lifecycle Events activity sets that appear in the Skills widget on the Journey detail page. Enabling this feature gives managers and AI agents the flexibility to tailor journeys to individual employee needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/journey-designer/enable-team-tasks.html
release: australia
product: Journey Designer
classification: journey-designer
topic_type: task
last_updated: "2026-01-13"
reading_time_minutes: 1
breadcrumb: [Configure Journey designer features, Configure, Journey designer, Employee Journey Management, HR Service Delivery, Employee Service Management]
tags:
  - employee-service-management
  - journey-designer
  - custom
  - milestones
  - workflow
  - type-task
---

# Enable team tasks

Enable team tasks to allow managers to add tasks to the [[hr-lifecycle-events-landing-page-1|Lifecycle Events]] [[activity-lxp|activity]] sets that appear in the Skills widget on the Journey detail page. Enabling this feature gives managers and AI agents the flexibility to tailor journeys to individual employee needs.

## Before you begin

Role required: \[sn\_jny.admin\]

## Procedure

1.  Navigate to **All** &gt; **[[jny-dsgnr-landing-page-1|Journey designer]]** &gt; **Administration** &gt; **Manage Journey Configurations**.

2.  Select the journey configuration for which you want to enable team tasks.

    The Journey Configuration record appears.

3.  Select the **LE activity sets can be personalized** check box.

4.  In the **Excluded LE activity sets** field, specify the activity sets to which managers cannot add tasks.

5.  Select **Update** to save the changes you made to the journey configuration.


## Result

You enabled [[jny-team-tasks|team tasks]] for the selected journey configuration. Managers are able to add tasks to activity sets for new journeys that are created using the configuration you modified.

To learn how to add tasks to activity sets from the [[employee-center-landing-page|Employee Center]], see [Add tasks to an activity set using Journey designer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-designer/add-tasks-activity-set.md).

**Parent Topic:**[Configure Journey designer features](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-designer/jny-dsgnr-configuration.md)

## Related

- [[hr-lifecycle-events-landing-page-1|Lifecycle Events]]
- [[activity-lxp|Activity]]
- [[jny-dsgnr-landing-page-1|Journey designer]]
- [[jny-team-tasks|Team tasks]]
- [[employee-center-landing-page|Employee Center]]
