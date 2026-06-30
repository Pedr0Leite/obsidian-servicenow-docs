---
title: Explore Purchase Order Management
description: Learn about the benefits and capabilities of Purchase Order Management \(POM\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/explore-purch-order-mgmt.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
keywords: [explore, purchase order management, POM]
breadcrumb: [Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
---

# Explore Purchase Order Management

Learn about the benefits and capabilities of Purchase Order Management \(POM\).

## Purchase Order Management overview

Purchase Order Management simplifies the flagging of purchase orders issues and its resolution.

## Purchase Order Management users

|User|Description|
|----|-----------|
|Supplier|Supplier reviews the [[purchase-order-table|purchase order]], raises exceptions when order terms can’t be met, and fulfills orders.|
|Purchase Order Management administrator|Purchase Order Management administrator is the local admin for the application and manages settings such as assignment rules and priority settings.|
|Operational Buyer|Operational Buyer can view, edit, and resolve purchase order exceptions. The buyer can also be assigned purchase order exceptions.|
|Purchase Order Management Viewer|Purchase Order Management Viewer can view purchase order exceptions but not be assigned to them and don’t have access to [[exploring-source-to-pay-operations|Source-to-Pay Operations Workspace]].|
|Purchase Order Management Collaborator|Purchase Order Management Collaborator can view, edit, and resolve assigned [[purchase-order-exception-table|purchase order exception]] tasks.|

## Purchase Order Management Workflow

A workflow for a purchase order exception might progress as follows:

1.  The [[supplier|supplier]] communicates and raises attention to issues related to purchase orders by submitting purchase order exceptions in [[supplier-central|Supplier Collaboration Portal]].
2.  The supplier can communicate different types of delivery plan changes, such delivering in a single shipment on a different date, providing multiple smaller deliveries, or rejecting a purchase order line.
3.  The operational buyer monitors the incoming exceptions and associated tasks.
4.  The operational buyer can act on the assigned purchase order exceptions.
5.  The operational buyer can update impacted order and accept a supplier proposal. Alternatively, the buyer can identify other open purchase orders with other suppliers delivering the same material in the same time frame.
6.  The operational buyer can also create, assign, and monitor tasks from the purchase order exception record. The buyer can assign tasks both to internal procurement team members and collaborators outside the procurement team.
7.  When stronger supplier leverage is required to resolve exceptions, operational buyers can create escalations to engage strategic buyers or other internal procurement stakeholders. A supplier case is created when an exception is escalated.

## Purchase Order Management benefits

<table id="table_k3r_n2y_ygc"><thead><tr><th>

Benefit

</th><th>

Feature

</th><th>

Users

</th></tr></thead><tbody><tr><td>

Provide prompt visibility for the appropriate buyer by reporting delivery plan issues related to a purchase order.

</td><td>

[[reporting-delivery-plan-issues|Reporting delivery plan issues]]

</td><td>

Suppliers

</td></tr><tr><td>

Monitor and review purchase order exceptions from a centralized interface

</td><td>

[POM landing page](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-workspace/purch-order-mgmt-tab-s2pws.md)

</td><td>

Operational buyers

</td></tr><tr><td>

Expedite detection and resolution of purchase order exceptions.

</td><td>

[[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]

</td><td>

Operational buyers

</td></tr><tr><td>

Create and assign purchase order exception tasks to other buyers and collaborators

</td><td>

[[assign-a-poe-task-to-a-collaborator|Create and assign a purchase order exception task]]

</td><td>

Operational buyers

</td></tr><tr><td>

Review and complete assigned purchase order exception tasks

</td><td>

-   [[work-on-a-purchase-order-exception|Work on a purchase order exception task]]
-   [[view-po-exception-task|View a purchase order exception task]]

</td><td>

Operational buyers, Collaborators

</td></tr></tbody>
</table>## What to explore next

To learn more about configuring and using Purchase Order Management, see:

-   [[configure-purch-order-mgmt|Configure Purchase Order Management]]
-   [[use-purch-order-mgmt|Use Purchase Order Management]]
-   [[purchase-order-mgmt-reference|Purchase Order Management reference]]

-   **[[purch-order-mgmt-ws|Source-to-Pay Workspace]]**  
The Purchase Order Management page in the Source-to-Pay Workspace enables you to manage and work on tasks related to purchase order exceptions.

**Parent Topic:**[[purchase-order-mgmt-landing-page|Purchase Order Management]]

## Related

- [[reporting-delivery-plan-issues|Reporting delivery plan issues]]
- [[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]
- [[assign-a-poe-task-to-a-collaborator|Create and assign a purchase order exception task]]
- [[work-on-a-purchase-order-exception|Work on a purchase order exception task]]
- [[view-po-exception-task|View a purchase order exception task]]
- [[configure-purch-order-mgmt|Configure Purchase Order Management]]
- [[use-purch-order-mgmt|Use Purchase Order Management]]
- [[purchase-order-mgmt-reference|Purchase Order Management reference]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-order-table|Purchase order]]
- [[exploring-source-to-pay-operations|Source-to-Pay Operations workspace]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[supplier|Supplier]]
- [[supplier-central|Supplier Collaboration Portal]]
