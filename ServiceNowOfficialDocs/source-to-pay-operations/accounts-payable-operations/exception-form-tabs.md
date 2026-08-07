---
title: Invoice exception form tabs
description: Descriptions of the tabs on the Invoice exception form, including the invoice exception information available for exception resolution.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/accounts-payable-operations/exception-form-tabs.html
release: australia
product: Accounts Payable Operations
classification: accounts-payable-operations
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [APO, Accounts Payable Operations, invoice exception, invoice automation, AP automation]
breadcrumb: [Invoice exception form, Reference, Accounts Payable Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - ap
  - invoices
  - payables
  - fsc
  - type-reference
---

# Invoice exception form tabs

Descriptions of the tabs on the [[exception-form-fields|Invoice exception form]], including the invoice exception information available for exception resolution.

<table id="table_bgh_hwr_2wb"><thead><tr><th>

Tab

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Details

</td><td>

Details about the invoice exception.

</td></tr><tr><td>

Invoice lines affected

</td><td>

Invoice lines that have exceptions.**Note:** This tab is shown only for line-level exceptions.

</td></tr><tr><td>

[[purchase-order-lines|Purchase Order Lines]]

</td><td>

Purchase order lines corresponding to the invoice lines for which the invoice exception has been raised.This tab is shown only for [[work-with-invoice-exceptions|invoice exceptions]] of type Insufficient Funds \(Quantity variance\) and Insufficient Funds \(Amount variance\).

</td></tr><tr><td>

[[receipts|Receipts]]

</td><td>

Goods receipts for all the purchase order lines of a [[purchase-order-table|purchase order]]. For more information, see [Receipts](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/receipts.md).

</td></tr><tr><td>

Related [[invoices|invoices]]

</td><td>

Related invoices from the same [[supplier|supplier]].This tab is shown only for invoice exceptions of type Insufficient Funds \(Quantity variance\) and Insufficient Funds \(Amount variance\).

</td></tr><tr><td>

Exception tasks

</td><td>

Exception tasks for the invoice exception.

</td></tr><tr><td>

Related tasks

</td><td>

If [[psm-overview|Sourcing and Procurement Operations]] is installed, the following tasks are shown:

-   Receipt. For more information, see [Receipt tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/receipt-tasks.md).
-   Milestone. For more information, see [Milestones](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/milestones.md).
-   Invoice acknowledgment. For more information, see [Invoice tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/invoice-tasks.md).

 If Sourcing and Procurement Operations is not installed, only the Milestone task is shown.

**Note:** This tab is shown only for an Insufficient Goods Receipt \(IGR\) exception.

</td></tr></tbody>
</table>**Parent Topic:**[Invoice exception form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/exception-form-fields.md)

## Related

- [[exception-form-fields|Invoice exception form]]
- [[purchase-order-lines|Purchase order lines]]
- [[work-with-invoice-exceptions|Invoice exceptions]]
- [[receipts|Receipts]]
- [[purchase-order-table|Purchase order]]
- [[invoices|Invoices]]
- [[supplier|Supplier]]
- [[psm-overview|Sourcing and Procurement Operations]]
