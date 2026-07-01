---
title: Configuring Quote Management
description: Learn how to set up Quote Management so that your sales agents can create and manage customer quotes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configure-quote-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Configuring Quote Management

Learn how to set up Quote Management so that your sales agents can create and manage customer quotes.

Admins and Quote Management administrators complete the following configuration tasks to set up Quote Management.

<table id="table_b23_thc_zzb"><thead><tr><th>

Task

</th><th>

Description

</th><th>

Role

</th></tr></thead><tbody><tr><td>

[https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/installing-quote-management.md](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/installing-quote-management.md)

</td><td>

Install Quote Management from the ServiceNow® Store Store. It provides these key features for your agents:-   Build quotes with products and pricing, then present them to customers.
-   Use the product configurator to select simple and configurable product offerings.
-   Add pricing adjustments to products.
-   Convert quotes to product orders once customers have approved.

</td><td>

Admin

</td></tr><tr><td>



</td><td>

Set the roles for Quote Management users and your product catalog and pricing administrators.

</td><td>

Admin

</td></tr><tr><td>

[[som-managing-product-catalogs|Configuring product offerings and catalogs]]

</td><td>

Create the product offerings and catalogs, unless they've been previously defined.

</td><td>

Product catalog admin

</td></tr><tr><td>

[[som-create-price-list-line|Configuring product pricing]]

</td><td>

Define the price lists, pricing strategies, and other pricing features that you want to use, unless they've been previously defined.-   Set the [[som-create-price-list|price lists]] and pricing strategies that control how pricing is applied to quotes.
-   If you're using cost books, create the [[create-cost-books|cost books]] that define the unit costs for product offerings.

</td><td>

Pricing admin

</td></tr><tr><td>

Activate cost books and cost margins

</td><td>

Use the **sn\_quote\_mgmt\_core.enable\_cost\_margin\_calculation** system property to activate the cost book and cost margin features in Quote Management. These features enable sales agents to view product unit costs and cost margins when creating sales quotes.

</td><td>

Quote Management admin

</td></tr><tr><td>

[[som-activate-location-filter|Activate location-based transactions]]

</td><td>

Use the **sn\_sales\_common.enable\_location\_based\_transactions** system property to activate location-based transactions in Quote Management.

</td><td>

Admin

</td></tr><tr><td>

[[quote-management-configure-pdf-documents|Configure quote PDF documents]]

</td><td>

Set up PDF template, signers, and Docusign.-   [[quote-mgt-setup-pdf-document-templates|Create PDF templates]]
-   [[quote-mgt-configure-docusign-pdf|Configure DocuSign]]
-   [[quote-mgt-configure-pdf-document-signers|Set up PDF document signers]]

</td><td>

sales\_operations\_specialists

</td></tr></tbody>
</table>## What to do next

After completing the configuration tasks, you can start using Quote Management to build and manage customer quotes. See [[quote-mgmt-using|Using Quote Management]].

Optionally, configure [[configuring-advanced-approval-management|Configuring Advanced Approval Management]] to build automated approval workflows for customer quotes and other [[order-mgt-overview|Sales Customer Relationship Management]] entities.

**Related topics**  


[[quote-management|Quote Management]]

[Using Quote Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/quote-mgmt-using.md)

[[approving-or-rejecting-quotes|Approving or rejecting quotes]]

[[using-prod-recommendations-quote|Using product offering recommendations in quotes]]

[[synchronise_quote_and_opportunity|Sync quote and opportunity]]

## Related

- [[som-managing-product-catalogs|Configuring product offerings and catalogs]]
- [[som-create-price-list-line|Create a price list line]]
- [[som-create-price-list|Create and publish a price list]]
- [[create-cost-books|Create and publish a cost book]]
- [[som-activate-location-filter|Activate location-based transactions]]
- [[quote-management-configure-pdf-documents|Configure quote PDF documents]]
- [[quote-mgt-setup-pdf-document-templates|Set up PDF document templates]]
- [[quote-mgt-configure-docusign-pdf|Configure DocuSign for PDF documents]]
- [[quote-mgt-configure-pdf-document-signers|Set up PDF document signers]]
- [[quote-mgmt-using|Using Quote Management]]
- [[configuring-advanced-approval-management|Configuring Advanced Approval Management]]
- [[quote-management|Quote Management]]
- [[approving-or-rejecting-quotes|Approving or rejecting quotes]]
- [[using-prod-recommendations-quote|Using product offering recommendations in quotes]]
- [[synchronise_quote_and_opportunity|Sync quote and opportunity]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
