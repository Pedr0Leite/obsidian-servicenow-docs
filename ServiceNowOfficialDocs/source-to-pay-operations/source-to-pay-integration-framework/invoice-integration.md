---
title: Invoice integration
description: Invoices are created either manually in Source-to-Pay \(S2P\) or through an external supplier portal. Generic API synchronizes invoices created from a supplier portal into S2P.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/source-to-pay-integration-framework/invoice-integration.html
release: australia
product: Source-to-Pay Integration Framework
classification: source-to-pay-integration-framework
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Source-to-Pay integration framework, Integration with third-party applications, Integrations, Source-to-Pay Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - s2p
  - integration
  - erp
  - framework
  - type-concept
---

# Invoice integration

[[invoices|Invoices]] are created either manually in Source-to-Pay \(S2P\) or through an external [[supplier|supplier]] portal. Generic API synchronizes invoices created from a supplier portal into S2P.

## Process flow

-   When the matching and [[invoice-approvals|invoice approvals]] process, if applicable, is complete, an asynchronous call to the ERP system is triggered.
-   If there is an integration error, an integration error purchasing task is created on the [[purchase-order-table|purchase order]]. This contains the error message from the ERP system to inform the procurement specialist what must be updated.
-   Similar to [[purchase-order-integration-2|purchase order integration]], an invoice is not created in the ERP system until the integration error is resolved in S2P. At this juncture, the status of the invoice and invoice line in S2P is set to Pending Review.
-   On successful invoice creation in the ERP system, an ERP number and ERP line number are returned and synchronized back to the appropriate record in S2P.
-   In case of manual invoice creation, the user has to manually confirm the invoice to trigger the ERP system integration.

**Note:** No additional configurations are required for invoice integration to function.

## Related

- [[invoices|Invoices]]
- [[supplier|Supplier]]
- [[invoice-approvals|Invoice approvals]]
- [[purchase-order-table|Purchase order]]
- [[purchase-order-integration-2|Purchase order integration]]
