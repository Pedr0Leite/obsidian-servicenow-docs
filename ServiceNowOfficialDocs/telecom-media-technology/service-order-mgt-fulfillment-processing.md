---
title: Approving and fulfilling service orders
description: Learn how your organization can perform post-approval service order fulfillment. By using this application, you can ensure that your service orders are fulfilled correctly.OM revamp project - This topic is obsolete and has been removed from the SOM bundle on Oct 7, 2025.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/telecom-media-technology/service-order-mgt-fulfillment-processing.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Use, Sales Customer Relationship Management for Telecommunications, Telecommunications, Media, and Technology \(TMT\)]
tags:
  - telecom-media-technology
  - type-concept
---

# Approving and fulfilling service orders

Learn how your organization can perform post-approval service order fulfillment. By using this application, you can ensure that your service orders are fulfilled correctly.

Your service order manager and order fulfillment agent must do the approval and fulfillment tasks that are described in the following table.

<table id="id_e3m_wwq_ytb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Review a service order and approve or reject it for fulfillment.

</td><td>

A service order manager approves or rejects a service order for fulfillment. If it's approved, the sold product and [[sales-crm-order-decomposition|order decomposition]] processing can take place. If it's rejected, more investigation is needed. To learn more, see:-   [[approve-reject-service-order-fulfillment|Approve or reject a service order for fulfillment]]
-   [[service-order-mgt-sold-product-creation|Sold product creation for service orders]]
-   [[service-order-mgt-order-decomposition|Service order decomposition]]

</td></tr><tr><td>

Review the service specifications and domain service orders that are associated with the approved service order.

</td><td>

A service order manager reviews the domain service orders that were generated for the service order line item. To learn more, see:-   [[service-order-mgt-review-update-service-order-product-specifications|Review and update the service specifications for a service order line item]]
-   [[service-order-mgt-review-resource-orders|Review the domain resource orders that are associated with a service order]]

</td></tr><tr><td>

Use the Orchestration Plan UI to review the domain orders and order tasks that are associated with the approved service order.

</td><td>

A service order manager reviews the orchestration state and hierarchical structure for a selected service order, its associated order line items, domain orders, and order tasks. By using the Orchestration Plan UI, the service order manager can see how much progress has occurred in the fulfillment process. To learn more, see [Order fulfillment](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/reviewing-orchestration-plans-order-fulfillment.md).

</td></tr><tr><td>

Review and update the fulfillment tasks that are associated with a service order.

</td><td>

An order fulfillment or service order agent does the tasks that are required for post-approval customer order fulfillment, including marking the order tasks as complete. The order fulfillment or service manager then creates the order fallout records for the order tasks that can't be completed.To learn more, see:

-   [[service-order-mgt-service-order-tasks|Review and update the service order fulfillment tasks]]
-   [Managing order fallout](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/fallout-management-overview.md)

</td></tr><tr><td>

Follow up on the tasks that couldn't be completed by examining the order fallout records and reassigning them for more investigation.

</td><td>

An order fulfillment or service manager reviews the tasks that couldn't be completed in the order fallout records, and reassigns the order tasks to fulfillment agents for investigation and resolution. To learn more, see, [Review a fallout record](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/select-order-fallout-records-review.md).

</td></tr></tbody>
</table>

## Related

- [[approve-reject-service-order-fulfillment|Approve or reject a service order for fulfillment]]
- [[service-order-mgt-sold-product-creation|Sold product creation for service orders]]
- [[service-order-mgt-order-decomposition|Service order decomposition]]
- [[service-order-mgt-review-update-service-order-product-specifications|Review and update the service specifications for a service order line item]]
- [[service-order-mgt-review-resource-orders|Review the domain resource orders that are associated with a service order]]
- [[service-order-mgt-service-order-tasks|Review and update the service order fulfillment tasks]]
- [[sales-crm-order-decomposition|Order decomposition]]
