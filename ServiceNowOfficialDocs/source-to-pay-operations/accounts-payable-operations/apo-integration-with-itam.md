---
title: IT Asset Management purchase order invoice processing
description: When IT Asset Management integrates with Sourcing and Procurement Operations, invoice exceptions for ITAM purchase orders are handled automatically through quantity validation, discrepancy notifications, and invoice revalidation.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/accounts-payable-operations/apo-integration-with-itam.html
release: australia
product: Accounts Payable Operations
classification: accounts-payable-operations
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [APO, Accounts Payable Operations, invoice exception, invoice processing, purchase order, PO, integration, integration, ITAM]
breadcrumb: [Integrate, Accounts Payable Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - ap
  - invoices
  - payables
  - fsc
  - type-concept
---

# IT Asset Management purchase order invoice processing

When IT Asset Management integrates with [[psm-overview|Sourcing and Procurement Operations]], [[work-with-invoice-exceptions|invoice exceptions]] for ITAM purchase orders are handled automatically through quantity validation, discrepancy notifications, and invoice revalidation.

In IT Asset Management \(ITAM\), assets are created when you acknowledge the receipt of the requested items. As part of the Better Together integration, all the received asset is handled within IT Asset Management \(ITAM\).

After receiving of the goods is completed, receiving slips are generated in ITAM. You can view the created assets in the **Assets** tab of the ITAM [[purchase-order-table|purchase order]]. For more information, see [Receiving assets in IT Asset Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/itam-spo-receiving-assets.md).

During the invoicing process, [[acc-pay-mgmt-landing-page|Accounts Payable Operations]] checks if the purchase order originates from ITAM using the reference field. It validates the received quantity against the purchase order using the receiving slips and if discrepancies are found, then insufficient goods receipt exception is triggered. APO automatically triggers an email and notifies the ITAM 'Assigned to' user mentioned in the ITAM PO about the exception. Once the exceptions are resolved, APO automatically re-validates the [[invoices|invoices]]. The invoice status changes from “Review Needed” to “Review Complete”.

The benefits of Better Together integration with ITAM are:

-   Leverage APO functionalities and process invoices faster and efficiently
-   Automated exception handling for ITAM-PO invoices becomes more accurate and timely
-   Operational efficiency and reduced manual intervention

## Plugin dependencies for the APO-ITAM better together feature

The following are the plugin dependencies that are required to use Asset Management Integration for Accounts Payable Operations:

-   [[acc-pay-case-mgmt-overview|Invoice Case Management]] \[sn\_ap\_cm\]
-   Accounts Payable Operations \[sn\_ap\_apm\]
-   [[acc-pay-invoice-processing|Accounts Payable Invoice Processing]] \[sn\_pr\]
-   Accounts Payable Operations with Document Intelligence \[sn\_ap\_ic\]
-   Asset Management Integration for Sourcing and Procurement Operations plugin \[sn\_spend\_asset\]
-   Source-to-Pay Common Architecture \[sn\_shop\]
-   [[source-to-pay-integration-framework|Source-to-Pay Integration Framework]] \[sn\_spend\_intg\]
-   [[supplier-common|Supplier Common Architecture]] \[sn\_slm\]
-   Common Service Delivery \[sn\_spend\_sdc\]
-   [[purch-order-mgmt-ws|Source-to-Pay Workspace]] \[sn\_spend\_workspace\]
-   [[supplier-central|Supplier Collaboration Portal]] \[sn\_supplier\_sp\]
-   [[erp-integration-framework|ERP Integration Framework]] \[sn\_fcms\_intg\]
-   Finance Common Architecture \[sn\_fin\]

## Related

- [[psm-overview|Sourcing and Procurement Operations]]
- [[work-with-invoice-exceptions|Invoice exceptions]]
- [[purchase-order-table|Purchase order]]
- [[acc-pay-mgmt-landing-page|Accounts Payable Operations]]
- [[invoices|Invoices]]
- [[acc-pay-case-mgmt-overview|Invoice Case Management]]
- [[acc-pay-invoice-processing|Accounts Payable Invoice Processing]]
- [[source-to-pay-integration-framework|Source-to-Pay integration framework]]
- [[supplier-common|Supplier Common Architecture]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[supplier-central|Supplier Collaboration Portal]]
- [[erp-integration-framework|ERP Integration Framework]]
