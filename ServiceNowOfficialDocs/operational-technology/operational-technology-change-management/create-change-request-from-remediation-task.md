---
title: Create a change request from a remediation task
description: Create an Operational Technology \(OT\) change request from an OT remediation task. Creating a change request from a remediation task automatically populates the information in your change request record, such as the Site and the OT Device fields.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/operational-technology/operational-technology-change-management/create-change-request-from-remediation-task.html
release: australia
product: Operational Technology Change Management
classification: operational-technology-change-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Operational Technology Change Management, Operational Technology]
tags:
  - operational-technology
  - ot
  - change-management
  - ics
  - scada
  - type-task
---

# Create a change request from a remediation task

Create an [[operational-technology-overview|Operational Technology]] \(OT\) change request from an OT remediation task. Creating a change request from a remediation task automatically populates the information in your change request record, such as the Site and the OT Device fields.

## Before you begin

Roles required: sn\_ot\_change\_write or sn\_otvr.remediation\_owner

## Procedure

1.  Navigate to **All** &gt; **[[industrial-workspace-for-operational-technology|Industrial Workspace]]**.

2.  Open the remediation task record that you want to [[create-ot-change-request|create a change request]] from.

3.  Select the **Create OT Change** button.

    **Note:** If there's no active change model, the following error appears: `Error creating Change Request: No active change model available. Please contact your OT Change admin`.

4.  Select the OT change model that applies to your organization.

5.  Select **Next**.

6.  Complete the playbook as needed as your team works on the change request.

    For more information about the [[basic-ot-change-model|Basic OT Change Model playbook]], see [Basic OT Change Model playbook](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/operational-technology/operational-technology-change-management/basic-ot-change-model.md). For more information about the [[advanced-ot-change-model|Advanced OT Change Model playbook]], see [Advanced OT Change Model playbook](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/operational-technology/operational-technology-change-management/advanced-ot-change-model.md).

    The following fields are automatically populated depending on the conditions that you set.

    -   The **OT Device** field is auto-populated only if the [[industrial-process-manager-overview|Industrial Process Manager]] application is enabled.
    -   If the Industrial Process Manager is installed, then the site assigned to the OT device shows up in the **Site** field.
    -   If the Industrial Process Manager is enabled and there's only one entity that is associated with the OT device, then the **Equipment model entity** field is automatically populated.

        **Note:** If multiple entities are associated with an device, the **Equipment model entity** field is left empty.


**Parent Topic:**[Using Operational Technology Change Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/operational-technology/operational-technology-change-management/using-operational-technology-change-management.md)

## Related

- [[operational-technology-overview|Operational Technology]]
- [[industrial-workspace-for-operational-technology|Industrial Workspace]]
- [[create-ot-change-request|Create a change request]]
- [[basic-ot-change-model|Basic OT Change Model playbook]]
- [[advanced-ot-change-model|Advanced OT Change Model playbook]]
- [[industrial-process-manager-overview|Industrial Process Manager]]
