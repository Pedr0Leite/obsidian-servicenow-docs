---
title: Create a template item
description: Create one or more template items, such as a task or record, for a task plan template. When the task plan template is applied, these records are automatically created.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/create-task-plan-template-item.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Task Plan Templates, Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a template item

Create one or more template items, such as a task or record, for a task plan template. When the task plan template is applied, these records are automatically created.

## Before you begin

Role required: sn\_task\_plan.admin or sn\_task\_plan.creator role

## About this task

Template items include tasks, child cases, and child case tasks. You can also create a hierarchy of template items. For example, you can create a case as a template item and then create case tasks as child template items for that case.

You can create new template items or you can [[clone-task-plan-template-item|clone existing template items]]. When you clone a template item, it clones the hierarchy of that item.

## Procedure

1.  Navigate to **All** &gt; **[[task-plan-templates|Task Plan Templates]]** &gt; **Draft Task Plan Templates**.

2.  Select a task plan template record number to display the record.

3.  Select the Template items tab.

4.  Select **New** in the Template items tab header.

    The template item form opens in a new tab. The **Number** field displays the number of the template item. The **Task plan template** field displays the number of the parent task plan template.

    For more information about these fields, see [[task-plan-template-item-form|Template item form]].

5.  Provide a brief description of the template item in the **Short description** field.

6.  Select a table from the **Table** field in which the system creates the template item record when the task plan template is applied.

    For example, if the template item is a case task, the system should create that item in the Case Task table \[sn\_customerservice\_task\].

7.  Specify the fields and the field values that the system should use to create the template item record.

8.  Add an attachment to the template item.

9.  Select **Save**.

    The system creates the template item record and adds the Conditions tab and the Child Template Items tab to the form.


## What to do next

After creating a template item, you can [[create-task-plan-template-item-condition|create one or more conditions for the template item]]. You can also create child template items for a template item.

## Related

- [[clone-task-plan-template-item|Clone a template item]]
- [[task-plan-template-item-form|Template item form]]
- [[create-task-plan-template-item-condition|Create a template item condition]]
- [[task-plan-templates|Task Plan Templates]]
