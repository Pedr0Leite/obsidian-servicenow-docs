---
title: Submit new Invoice
description: Submit a new PO or Non-PO invoice through the Supplier Collaboration Portal to request payment from the accounts payable team.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/accounts-payable-operations/submit-new-invoice.html
release: australia
product: Accounts Payable Operations
classification: accounts-payable-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [APO, Accounts Payable Operations, invoice management, supplier, invoice automation]
breadcrumb: [Working with Supplier Catalog, Using Supplier Collaboration Portal in APO, Use, Accounts Payable Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - ap
  - invoices
  - payables
  - fsc
  - type-task
---

# Submit new Invoice

Submit a new PO or Non-PO invoice through the [[supplier-central|Supplier Collaboration Portal]] to request payment from the accounts payable team.

## Before you begin

Role required: [[supplier|Supplier]]

## Procedure

1.  Navigate to **Supplier Catalog** &gt; **[[invoices|Invoices]]** &gt; **Submit new invoice**.

2.  On the **Submit new invoice** form, enter the following details.

<table id="choicetable_v1q_w5z_zxb"><thead><tr><th align="left" id="d84871e96">

Question

</th><th align="left" id="d84871e99">

Description

</th></tr></thead><tbody><tr><td id="d84871e105">

**What type of invoice are you submitting?**

</td><td>

Invoice type- Choose the invoice type for processing from the drop-down list. The options are:-   PO invoice- The **[[purchase-order-table|Purchase order]]** drop-down appears. Choose the purchase order from the drop-down that you would like to associate with the invoice.
-   Non-PO invoice- Browse and attach the invoice for the [[acc-pay-mgmt-landing-page|Accounts Payable Operations]] team to create an invoice processing case.

**Note:**

    -   If you select Invoice type as Non-PO, and upload an invoice copy with purchase order, DocIntel processes the invoice as a valid PO invoice.
    -   If you select Invoice type as PO invoice and enter purchase order number but Doc Intel is unable to extract the purchase order details, then the purchase order that you selected from the **Purchase order** drop-down list will be considered and processed.
For more information on invoice case, see [Create New Invoice form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-new-invoice-form.md).

Supplier- Displays the name of the supplier associated with the [[supplier-contact|supplier contact]] based on your selection from the **My Company**tab. The **Purchase order** drop-down lists the details associated with the selected supplier.

</td></tr></tbody>
</table>3.  Click **Submit**.

    A pop-up alert message appears as "**Your invoice is submitted and we will send updates about any issues. You can review details here: &lt;&lt;Invoice case number&gt;&gt;**.

    Invoice is created.


**Parent Topic:**[Working with Supplier Catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/working-with-supplier-catalog.md)

## Related

- [[supplier-central|Supplier Collaboration Portal]]
- [[supplier|Supplier]]
- [[invoices|Invoices]]
- [[purchase-order-table|Purchase order]]
- [[acc-pay-mgmt-landing-page|Accounts Payable Operations]]
- [[supplier-contact|Supplier contact]]
