---
title: Create a case task of a specific type for a customer service case
description: Customer service agents can create different types of case tasks by making selections from the case task type selector screen.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/create-case-task-specific-case-type.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Manage cases, Use, Customer Service Management]
---

# Create a case task of a specific type for a customer service case

Customer service agents can create different types of case tasks by making selections from the [[csm-case-task-type-select-modal|case task type selector]] screen.

## Before you begin

Role required:

-   sn\_customerservice\_agent
-   sn\_customerservice.consumer\_agent
-   sn\_customerservice\_manager
-   sn\_customerservice.svc\_location\_agent
-   sn\_customerservice.case\_task\_agent

## About this task

The types of case tasks that agents can create depends on the configuration of the [[customer-service-case-types|customer service case types]] and [[csm-service-definitions|service definitions]] features. For more information, see the following topics:

-   [[configure-csm-case-types|Configure customer service case types]]
-   [[manage-csm-case-types|Manage customer service case types]]
-   [[csm-service-definitions-configure|Configuring service definitions]]

In [[csm-workspaces-configure|CSM Configurable Workspace]], agents use the [[csm-case-type-select-modals|Case type selector screen]] to make selections and create cases.

## Procedure

1.  [[osp-create-case-task|Create a case task]].

    -   Select **New** from a case task list.
    -   Select **New** from the Tasks related list tab on a case record.
    -   Select the **+** icon on the related records task list in the [[csm-contextual-related-records|Dynamic Related Records]] component.
    -   Select the Task declarative action on the activity viewer.
    -   Select **Create Task** in a case playbook stage.
2.  Make a selection in the case task type selector.

    -   If you create the case task from a case task list, the **Service task** field on the case task type selector shows all of the related services where the target table is Case Task \[sn\_customerservice\_task\] and extensions of Case Task.
    -   If you create the case task from a case record, the **Case task service** field [[migration-lists|lists]] the task services related to the case service. If the case has no service, the **Service task** field shows all of the related services where the target table is Case Task \[sn\_customerservice\_task\] and extensions of Case Task.
3.  Select **Create task**

    The case task is created with the selected task service definition. If any default values have been defined in the case task service definition, these values are populated on the case task record.

## Related

- [[customer-service-case-types|Customer service case types]]
- [[csm-service-definitions|Service definitions]]
- [[configure-csm-case-types|Configuring customer service case types]]
- [[manage-csm-case-types|Manage customer service case types]]
- [[csm-service-definitions-configure|Configuring service definitions]]
- [[csm-case-type-select-modals|Case type selector]]
- [[csm-case-task-type-select-modal|Case task type selector]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[osp-create-case-task|Create a case task]]
- [[csm-contextual-related-records|Dynamic related records]]
- [[migration-lists|Lists]]
