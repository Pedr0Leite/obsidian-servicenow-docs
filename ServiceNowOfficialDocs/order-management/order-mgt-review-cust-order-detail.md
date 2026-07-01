---
title: Cancel orders
description: Cancel an inflight order, or order line item when a customer requests it or your internal personnel determine an order cancellation is necessary.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/order-mgt-review-cust-order-detail.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Inflight order changes, Order Management, Use, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Cancel orders

[[cancel|Cancel]] an inflight order, or order line item when a customer requests it or your internal personnel determine an order cancellation is necessary.

## Before you begin

Role required: order\_approver, order\_viewer, sn\_ind\_tmt\_orm.order-fulfillment\_agent, or sn\_ind\_tmt\_orm.order\_fulfillment\_manager

## About this task

You can only cancel orders that are in the In progress state. You can delete orders or order line items from orders that are in Draft or New states. To learn more, see [[delete-orders|Delete orders]].

## Procedure

1.  Navigate to  **Workspaces** &gt; **CSM/FSM Configurable Workspace** .

2.  Select the List icon \[Omitted image "list-outline-24.svg"\] Alt text:.

3.  Navigate to **Customer Orders** &gt; **All** or **Service Orders** &gt; **All** to cancel a product or service order respectively.

4.  Select an order you want to cancel.

    **Note:** If the **PONR** option is selected, the **Cancel Order** button is turned off because it is too far along in the process to request a cancellation.

5.  Select **Cancel Order**.

    When you request an order cancellation, the following actions take place:

    -   The **State** field changes to Assessing Cancellation.
    -   The **Version** field increments to the next version number.
    -   The **Revision Operation** field is set to Cancel.
    -   Notification messages appear if there are any conditions that are preventing cancellation of the order. A designated manager must approve the order cancellation.
6.  In the customer order, make the required changes, and then select **Save**.


## What to do next

A designated manager must approve the order cancellation. To learn more, see [[review-and-approve-or-decline-order-cancellation-requests|Review and approve order revisions or cancellation requests]].

**Parent Topic:**[[inflight-order-change-mgt-overview|Managing inflight order changes and cancellation requests]]

**Related topics**  


[[order-mgt-configuring|Configuring Order Management]]

[[explore-order-management|Order management]]

## Related

- [[delete-orders|Delete orders]]
- [[review-and-approve-or-decline-order-cancellation-requests|Review and approve order revisions or cancellation requests]]
- [[inflight-order-change-mgt-overview|Managing inflight order changes and cancellation requests]]
- [[order-mgt-configuring|Configuring Order Management]]
- [[explore-order-management|Order management]]
- [[cancel|Cancel]]
