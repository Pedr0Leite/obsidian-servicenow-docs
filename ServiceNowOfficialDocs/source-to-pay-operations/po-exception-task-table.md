---
title: Purchase Order Exception Task table
description: Purchase order exception tasks are individual tasks assigned to users as part of resolving a purchase order exception.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/po-exception-task-table.html
release: australia
topic_type: reference
last_updated: "2026-06-08"
reading_time_minutes: 1
breadcrumb: [Master data tables for Purchase Order Management, Reference, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - type-reference
---

# Purchase Order Exception Task table

[[purchase-order-exception-table|Purchase order exception]] tasks are individual tasks assigned to users as part of resolving a purchase order exception.

## sn\_poem\_exception\_task table

The Purchase Order Exception Task \(sn\_poem\_exception\_task\) table contains the following fields.

|Field|Data type|Description|
|-----|---------|-----------|
|Sourcing event|Reference|The sourcing event associated with this exception task.|
|Sourcing request|Reference|The [[sourcing-request|sourcing request]] linked to this exception task.|
|External signer|Reference|The external party required to sign off on or approve the resolution of this task.|
|Purchase line|Reference|The purchase line linked to this exception task.|
|Supplier|Reference|The [[supplier|supplier]] associated with the purchase order exception.|
|Supplier location|Reference|The specific location or site of the supplier relevant to this task.|
|Negotiation|Reference|The negotiation record related to this exception task.|
|Purchase|Reference|The parent purchase record associated with this task|
|Purchase order line|Reference|The specific line item on the [[purchase-order-table|purchase order]] associated with this task.|
|Sub type|String|Category of the exception task.|
|Related case|Reference|The exception case associated with this task.|
|Purchase order|Reference|The purchase order related to this exception task.|
|Cost allocation|Reference|The cost allocation record that determines how costs for this exception are distributed.|
|Primary contact|Reference|The main point of contact for resolving this exception on the buyer side.|
|Supplier contact|Reference|The supplier's point of contact for this exception task.|
|Shipment details|Reference|The shipment record containing delivery and logistics information relevant to this task.|

**Parent Topic:**[[master-data-tables-for-pom|Master data tables for Purchase Order Management]]

## Related

- [[master-data-tables-for-pom|Master data tables for Purchase Order Management]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[sourcing-request|Sourcing request]]
- [[supplier|Supplier]]
- [[purchase-order-table|Purchase order]]
