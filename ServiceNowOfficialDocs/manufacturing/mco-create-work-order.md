---
title: Create a work order
description: When off-site work is required, create a work order to provide field service agents with the information they must fulfill the request. You can create a work order from scratch or from another existing work order.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-create-work-order.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Product Non-conformance without playbook, Product non-conformance, Agent management, Use, Manufacturing Commercial Operations]
tags:
  - manufacturing
  - industry
  - solutions
  - ot
  - type-task
---

# Create a work order

When off-site work is required, create a work order to provide field service agents with the information they must fulfill the request. You can create a work order from scratch or from another existing work order.

## Before you begin

Role required: [[mco-quality-issue-management|Quality Issue Management]] Admin, [[mco-product-non-conformances|product non-conformance]] submitter \(sn\_mfg\_qm.product\_non\_conformance\_submitter\), or product non-conformance resolver \(sn\_mfg\_qm.product\_non\_conformance\_resolver\)

## About this task

-   In the work order, specify the nature of the work required and identify the configuration items \(CI\) affected.
-   To create work orders for common tasks, you can use work order model templates to create all the necessary records automatically.
-   Restrict access to work orders and tasks so that users can only view and manage those assigned to their own service organization, ensuring sensitive information is securely managed within the appropriate organization.

## Procedure

1.  Navigate to **Workspaces** &gt; **CSM/FSM Configurable Workspace** &gt; **List** &gt; **Product Non Conformance Case** &gt; **Correction Actions**.

    **Note:** Work order can be created from Product Non Conformance tasks, Containment actions, [[mco-PQI-use|Product Quality Investigation]] Tasks, Corrective, and Preventive actions.

2.  Select the Correction actions record for which you want to create a work order.

3.  Select **Work Orders**.

4.  Select **New**.

    **Create New Work Order** window is displayed.

5.  On the Work Order form, fill in the fields.

    For a description of the field values, see [[work-order-form|Work order form]].

6.  Select **Save**.


## Result

The work order is created and awaits for qualification to create a work order task.

**Parent Topic:**[[mco-related-lists-product-non-conformance|Product Non-conformance without playbook]]

## Related

- [[work-order-form|Work order form]]
- [[mco-related-lists-product-non-conformance|Product Non-conformance without playbook]]
- [[mco-quality-issue-management|Quality issue management]]
- [[mco-product-non-conformances|Product non-conformance]]
- [[mco-PQI-use|Product quality investigation]]
