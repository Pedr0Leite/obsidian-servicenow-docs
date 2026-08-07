---
title: Find alternative suppliers
description: If a supplier's inability to fulfill an order creates a shortfall, find an alternative supplier. Review open orders with other suppliers for the same material at the required location. You can then request for expedited delivery or increased quantities.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/find-alternative-suppliers.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [Address exception, Resolve purchase order exception, Find alternative suppliers, Review open orders, Purchase order exception mitigation]
breadcrumb: [Resolving purchase order exceptions, Use, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - type-task
---

# Find alternative suppliers

If a [[supplier|supplier]]'s inability to fulfill an order creates a shortfall, find an alternative supplier. Review open orders with other suppliers for the same material at the required location. You can then request for expedited delivery or increased quantities.

## Before you begin

Role required: sn\_poem\_core.operational\_buyer

## Procedure

1.  Navigate to **Workspaces** &gt; **[[purch-order-mgmt-ws|Source-to-Pay Workspace]]**.

2.  Select the **[[purchase-order-mgmt-landing-page|Purchase order management]]** tab.

3.  Select an open exception that you want to work on.

4.  From the **Address exception** list, select **Find alternative suppliers**.

    The system displays open purchase orders with other suppliers for the same material as in the Product model field of the exception.

5.  Select **Next**.

6.  In the Quick edit window, update the purchased quantity, the requested delivery date or both.

7.  Select **Save edit**.

8.  To update more fields, select **Edit full record**.


## Result

A [[purchase-order-table|purchase order]] revision is created for the alternative supplier and is assigned to the [[supplier-contact|supplier contact]].

**Parent Topic:**[[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]

## Related

- [[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]
- [[supplier|Supplier]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-order-table|Purchase order]]
- [[supplier-contact|Supplier contact]]
