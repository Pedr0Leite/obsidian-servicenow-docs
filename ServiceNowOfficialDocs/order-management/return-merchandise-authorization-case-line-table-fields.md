---
title: Return Merchandise Authorization case line table fields
description: Information about Return Merchandise Authorization \(RMA\) case line table fields.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/return-merchandise-authorization-case-line-table-fields.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Return Merchandise Authorization Case Management, Order operations, Reference, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-reference
---

# Return Merchandise Authorization case line table fields

Information about [[return-merchandise-authorization|Return Merchandise Authorization]] \(RMA\) case line table [[fields|fields]].

<table id="table_mpx_fnx_rfc"><thead><tr><th>

Field

</th><th>

Type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Original quantity

 \[original\_quantity\]

</td><td>

integer

</td><td>

Original quantity of the purchased item.

</td></tr><tr><td>

Defective quantity

 \[defective\_quantity\]

</td><td>

integer

</td><td>

Quantity of defective items.

</td></tr><tr><td>

Approved quantity

 \[approved\_quantity\]

</td><td>

integer

</td><td>

Quantity of items approved for RMA.

</td></tr><tr><td>

Customer expected resolution

 \[customer\_expected\_resolution\]

</td><td>

integer

</td><td>

Customer's preferred resolution. Options are:-   Repair
-   Replacement
-   Refund

</td></tr><tr><td>

Proposed resolution

 \[proposed\_resolution\]

</td><td>

integer

</td><td>

Proposed resolution by the seller. Options are:-   Return
-   Replacement
-   Refund
-   Reject

.

</td></tr><tr><td>

Repair type

 \[repair\_type\]

</td><td>

integer

</td><td>

Location of repair. Options are:-   Onsite
-   Off-site

</td></tr></tbody>
</table>**Parent Topic:**[[return-merchandise-authorization-case-management-reference|Return Merchandise Authorization Case Management]]

## Related

- [[return-merchandise-authorization-case-management-reference|Return Merchandise Authorization Case Management]]
- [[return-merchandise-authorization|Return Merchandise Authorization]]
- [[fields|Fields]]
