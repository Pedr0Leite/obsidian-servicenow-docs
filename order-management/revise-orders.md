---
title: Revise orders
description: Revise order line items to update product quantity for ongoing orders.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/revise-orders.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Inflight order changes, Order Management, Use, Sales Customer Relationship Management]
---

# Revise orders

Revise order line items to update product quantity for ongoing orders.

## Before you begin

Role required: order\_approver, order\_viewer, sn\_ind\_tmt\_orm.order-fulfillment\_agent, or sn\_ind\_tmt\_orm.order\_fulfillment\_manager

## Procedure

1.  Navigate to  **Workspaces** &gt; **CSM/FSM Configurable Workspace** .

2.  Select the List icon \[Omitted image "list-outline-24.svg"\] Alt text:.

3.  Navigate to **Customer Orders** &gt; **All** or **Service Orders** &gt; **All** to revise a product or service order respectively.

4.  Select an order you're working with.

    **Note:** If the **PONR** option is selected, the **Revise item** button is turned off because it is too far along in the process to revise.

5.  Select the line items you want to revise from the **Line items** tab.

6.  Select **Revise item** on the confirmation pop-up that follows.

7.  Make the required revisions to the order line item and select **Update**.

    When you revise an order line item, the following actions take place:

    -   The **State** field changes to Revision in progress.
    -   The **Version** field increments to the next version number.
    -   The **Revision Operation** field is set to Update.
    -   If there are any associated order tasks, their state [[fields|fields]] change to On Hold.

## What to do next

A designated manager must approve the order revision. To learn more, see [[review-and-approve-or-decline-order-cancellation-requests|Review and approve order revisions or cancellation requests]].

**Parent Topic:**[[inflight-order-change-mgt-overview|Managing inflight order changes and cancellation requests]]

**Related topics**  


[[order-mgt-configuring|Configuring Order Management]]

[[explore-order-management|Order management]]

## Related

- [[review-and-approve-or-decline-order-cancellation-requests|Review and approve order revisions or cancellation requests]]
- [[inflight-order-change-mgt-overview|Managing inflight order changes and cancellation requests]]
- [[order-mgt-configuring|Configuring Order Management]]
- [[explore-order-management|Order management]]
- [[fields|Fields]]
