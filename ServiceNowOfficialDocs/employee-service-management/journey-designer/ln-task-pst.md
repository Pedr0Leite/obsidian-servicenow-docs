---
title: Initiate a learning task from a lifecycle event
description: When a lifecycle event is triggered, a learning task is created and assigned to the subject person of the case. The task is displayed in the To-dos page in Employee Center.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/journey-designer/ln-task-pst.html
release: australia
product: Journey Designer
classification: journey-designer
topic_type: task
last_updated: "2026-03-12"
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

# Initiate a learning task from a lifecycle event

When a lifecycle event is triggered, a [[exploring-learning-exp|learning]] task is created and assigned to the subject person of the case. The task is displayed in the To-dos page in [[employee-center-landing-page|Employee Center]].

## Before you begin

Role required: sn\_jny.admin

## Procedure

1.  [[create-learning-task|Create a learning task]] template.

    For more information, see [Create a learning template](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-designer/ln-templates.md).

2.  [[configure-hr-lifecycle-event-activity-set|Configure a lifecycle event activity set]].

    For more information, see [Configure a lifecycle event activity set](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/lifecycle-events/configure-hr-lifecycle-event-activity-set.md).

3.  [[configure-hr-lifecycle-event-activity|Configure a lifecycle event activity]].

    While creating a lifecycle [[activity-lxp|activity]], make sure you select **Activity Type** as **Employee**, **Employee Activity** as **Learning task**, and **HR Template** as any learning template task. For more information, see [Configure a lifecycle event activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/lifecycle-events/configure-hr-lifecycle-event-activity.md).

    When the lifecycle event is triggered, a learning task is created and assigned to the subject person of the case.


-   **[Create a learning template](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-designer/ln-templates.md)**  
[[ln-templates|Create a learning template]] to simplify the process of creating learning tasks by populating fields automatically.

**Parent Topic:**[Configure Journey designer features](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-designer/jny-dsgnr-configuration.md)

## Related

- [[exploring-learning-exp|Learning]]
- [[employee-center-landing-page|Employee Center]]
- [[create-learning-task|Create a learning task]]
- [[configure-hr-lifecycle-event-activity-set|Configure a lifecycle event activity set]]
- [[configure-hr-lifecycle-event-activity|Configure a lifecycle event activity]]
- [[activity-lxp|Activity]]
- [[ln-templates|Create a learning template]]
