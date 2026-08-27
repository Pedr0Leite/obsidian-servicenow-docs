---
title: Master data tables for Purchase Order Management
description: The primary data tables for Purchase Order Management store important information about purchase order exceptions, exception tasks, priority, split lines, purchase order confirmation, and confirmation lines.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/master-data-tables-for-pom.html
release: australia
topic_type: reference
last_updated: "2026-06-03"
reading_time_minutes: 1
keywords: [data tables]
breadcrumb: [Reference, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - type-reference
---

# Master data tables for Purchase Order Management

The primary data tables for [[purchase-order-mgmt-landing-page|Purchase Order Management]] store important information about [[purchase-order-table|purchase order]] exceptions, exception tasks, priority, split lines, purchase order confirmation, and confirmation lines.

-   **[[purchase-order-exception-table|Purchase Order Exception]]**  
Purchase order exceptions arise when a [[supplier|supplier]] cannot fulfill the agreed terms of a purchase order. Common causes include changes to delivery quantity or date, or a complete inability to fulfill the order. Operational buyers use the Purchase Order Management application to manage and resolve these exceptions.
-   **[[po-exception-task-table|Purchase Order Exception Task table]]**  
Purchase order exception tasks are individual tasks assigned to users as part of resolving a purchase order exception.
-   **[[po-exception-split-line-table|Purchase Order Exception Split Line Table]]**  
A purchase order exception split line is a subdivided line item created when a line item requires delivery in phases. A split line is created when a supplier selects the **Delivery plan change** exception type and the **Phased delivery** subtype.
-   **[[po-confirmation-table|Purchase Order Confirmation table]]**  
Purchase order confirmations are supplier-generated transactions that acknowledge a buyer's order and communicate the supplier's ability to fulfill it as specified.
-   **[[po-confirmation-line-table|Purchase Order Confirmation Line table]]**  
A purchase order confirmation line is a line-level response from a supplier that acknowledges a specific purchase order line or a portion of it. It confirms whether the order can be delivered under the requested terms.

**Parent Topic:**[[purchase-order-mgmt-reference|Purchase Order Management reference]]

**Related topics**  


[Purchase order exception form]()

[Delivery plan change form]()

[Create new purchase order exception form]()

## Related

- [[purchase-order-exception-table|Purchase Order Exception]]
- [[po-exception-task-table|Purchase Order Exception Task table]]
- [[po-exception-split-line-table|Purchase Order Exception Split Line Table]]
- [[po-confirmation-table|Purchase Order Confirmation table]]
- [[po-confirmation-line-table|Purchase Order Confirmation Line table]]
- [[purchase-order-mgmt-reference|Purchase Order Management reference]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-order-table|Purchase order]]
- [[supplier|Supplier]]
