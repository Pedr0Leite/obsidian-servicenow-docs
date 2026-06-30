---
title: Add products or services to an order in Order Management
description: Add order lines for products or service orders using the product catalog and product configurator in Order Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/som-add-products-services-to-orders.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Creating orders, Order Management, Use, Sales Customer Relationship Management]
---

# Add products or services to an order in Order Management

Add order lines for products or service orders using the product catalog and product configurator in [[explore-order-management|Order Management]].

## Before you begin

**Note:** Check your entitlements to see if the product configurator is available.

Role required: sn\_ind\_tmt\_orm.order\_agent, sn\_ind\_tmt\_orm.service\_agent

## About this task

The product catalog displays tiles that contain product information. Simple products have an **Add** button that adds the product with no options available to the order.

Products with options have a **Customize** button that opens the product configurator, which lets you select product options.

When the  product configurator opens you can select from the available options for the product or service. The product configurator consists of three columns.

-   The product hierarchy displays product catalog items and child products associated with the product.
-   The option selection displays any available options for the product, service, order lines, and order tasks.
-   The Current Selection displays the selected products options and the pricing.

Depending on your configuration, you'd either see a [[explore-servicenowcpq|CPQ Configurator]] or product configurator. To learn more about these, see [[using-servicenowcpq|Using the CPQ Configurator]] and [[using-som-product-configurator|Using the legacy product configurator]].

As you configure your product, use the following options:

<table id="table_pqy_fcs_tgc"><thead><tr><th>

Option

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Reprice

</td><td>

Resets the pricing and updates the total price when you make changes.If cascading pricing is enabled, pricing information is cascaded from parent to child line items. See [[som-activate-cascade-quantity|Control cascading quantity values in child product offerings]] for more information.

</td></tr><tr><td>

Validate Related Items

</td><td>

Validates the product and prices when changes are made.

</td></tr><tr><td>

Add

</td><td>

Adds the product to the order after you've configured it.

</td></tr></tbody>
</table>**Note:** If you added a sales agreement while creating the order, only the products listed in the sales agreement are available for selection.

## Procedure

1.  Navigate to  **Workspaces** &gt; **CSM/FSM Configurable Workspace** .

2.  Select the List icon \[Omitted image "list-outline-24.svg"\] Alt text:.

3.  Navigate to **Customer Orders** &gt; **All**.

4.  Select an order.

5.  In the **Catalog** tab, choose a catalog from the drop-down menu.

6.  Add products to your order.

    -   Select **Add** to add a simple product.
    -   Select **Customize** to add products with configurable options.
7.  Select the **Line items** tab to view products and services in your order.


**Related topics**  


[[order-mgt-filter-catalog-by-location|Filter product catalog by location]]

[[som-om-setup-product-order-lines|Set up and review order lines]]

## Related

- [[using-servicenowcpq|Using the CPQ Configurator]]
- [[using-som-product-configurator|Using the legacy product configurator]]
- [[som-activate-cascade-quantity|Control cascading quantity values in child product offerings]]
- [[order-mgt-filter-catalog-by-location|Filter product catalog by location]]
- [[som-om-setup-product-order-lines|Set up and review order lines]]
- [[explore-order-management|Order management]]
- [[explore-servicenowcpq|CPQ Configurator]]
