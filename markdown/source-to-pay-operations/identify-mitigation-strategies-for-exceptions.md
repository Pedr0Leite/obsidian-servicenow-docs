---
title: Identify mitigation strategies for purchase order exceptions
description: The Define PO exception mitigation strategy workflow assesses the material delivery gap caused by an exception. It then identifies alternative suppliers with open lines for the affected product model and proposes order adjustments to mitigate the shortfall.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/identify-mitigation-strategies-for-exceptions.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Identify and execute mitigation strategies for purchase order exceptions, Using agentic workflows in Now Assist for Purchase Order Management \(POM\), Now Assist for POM, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
---

# Identify mitigation strategies for purchase order exceptions

The Define PO exception mitigation strategy workflow assesses the material delivery gap caused by an exception. It then identifies alternative suppliers with open lines for the affected product model and proposes order adjustments to mitigate the shortfall.

## Before you begin

Role required: Fulfiller for Now Assist for POM \[sn\_poem\_gen\_ai\_now\_assist\_fulfiller\]

Users must be assigned this role alongside the Operational Buyer role to use this agentic workflow.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[purch-order-mgmt-ws|Source-to-Pay Workspace]]**.

2.  Select the **[[purchase-order-mgmt-landing-page|Purchase order management]]** tab.

3.  Use any of the following steps:

    -   Select the **Now Assist** button on any of the [[purchase-order-exception-table|purchase order exception]] cards.
    -   [[view-purch-order-exception|View a purchase order exception]]. Select the **Now Assist** button on the exception record.
    The Now Assist panel opens and the agentic workflow begins analyzing the exception and building a mitigation strategy by:

    -   Outlining the material delivery gap caused by the exception.
    -   Locating open [[purchase-order-lines|purchase order lines]] with alternative suppliers for the same product model.
    -   Recommending order adjustments that can help offset the shortfall.
4.  Review the proposed solution and either accept it or request specific changes to the alternative [[supplier|supplier]] orders.


## Result

The agentic workflow then creates the appropriate order revision \(a [[purchase-requisition|purchase requisition]] of type Order Revision\) reflecting the approved changes.

**Parent Topic:**[[mitigation-strategies-for-po-exceptions|Identify and execute mitigation strategies for purchase order exceptions]]

## Related

- [[view-purch-order-exception|View a purchase order exception]]
- [[mitigation-strategies-for-po-exceptions|Identify and execute mitigation strategies for purchase order exceptions]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[purchase-order-lines|Purchase order lines]]
- [[supplier|Supplier]]
- [[purchase-requisition|Purchase requisition]]
