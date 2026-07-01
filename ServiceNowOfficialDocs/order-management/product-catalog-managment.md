---
title: Product Catalog Management
description: Product Catalog Management enables your organization to manage your product offerings by grouping them into catalogs and categories, which streamlines the ordering process and helps manage leads, opportunities, quotes, and orders in Sales Customer Relationship Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/product-catalog-managment.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Lead-to-cash foundation, Explore, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Product Catalog Management

Product Catalog Management enables your organization to manage your product offerings by grouping them into catalogs and categories, which streamlines the ordering process and helps manage leads, opportunities, quotes, and orders in [[order-mgt-overview|Sales Customer Relationship Management]].

Product Catalog Management provides various features to implement product catalogs and categories in your organization.

-   Product catalog user interface: Launch from anywhere in lead, opportunity, quote, and order capture workflows, enabling agents to browse and find products quickly with a full catalog search function.
-   Catalog category hierarchy: Use hierarchical structures of catalogs and categories to organize products and services logically.
-   Version control: Track changes made to product information over time, helping with transparency and auditability.
-   Product offer eligibility: Filter your product catalogs, product offering categories, and product offerings so that agents sell customers only the products for which they’re eligible.

**Note:** Check your entitlements to determine if you have access to these features. Also, starting with the Yokohama release, customers can use the Business Portal with [[explore-order-management|Order Management]] to create orders using the product catalog and product configurator. For more information on this self-service portal, see [[order-mgt-business-portal|Using the Business Portal.]]

To learn more about setting up product offering catalogs, see [[som-managing-product-catalogs|Configuring product offerings and catalogs]].

## Product catalog UI

In the product offering catalog, agents and customers can do the following:

-   Browse and search product offerings by using keywords, descriptions, and industry codes​.

    Product catalog admins or managers can also [[configure-ai-search-prod-catalog|configure AI Search]] in the product catalog interface, enabling agents and customers to find relevant product offerings or service specifications by using semantic queries.

-   Review product offers that are organized by catalog category hierarchy, which streamlines catalog navigation.

\[Omitted image "som-catalog-ui.png"\] Alt text: Product catalog interface that shows the product catalog hierarchy, product tiles with images, and search option.

## Product offering catalogs and categories

Product offering catalogs and categories offer a way to organize product offerings so that agents can easily find products to create orders.

-   Product offering catalog: Hierarchical product offering structures of categories and product offerings.
-   Product offering categories: Categories are a logical grouping of product offerings.
-   Product offerings: Physical goods or non-tangible services that are configurable.
-   Characteristic and Characteristic options: Product options that are created based on customer preferences.​

\[Omitted image "l2c-product-catalog-hierarchy-2.svg"\] Alt text: Infographic shows how catalogs, categories, product offerings, product characteristics, and characteristic options are configured in Sales Customer Relationship Management

## Product offering families

A product family is a collection of product offerings that share similar or common features. You can use a product family to create a hierarchical classification of product offerings, like a category tree. A product family can have parent-child relationships, where each node in the family tree can have a parent, forming a multi-level hierarchy. With this structure, you can apply attributes, business [[rules_101|rules]], and product updates to a product family, rather than change products individually.

After you create product families, you can assign a product family to a product offering. To learn more, see [[create-product-offering-family|Create a product offering family]].

## Product offer bundling

You can create product offer bundles with an offer hierarchy using product offer relationships and relationship groups. These bundle offers can have references to a product specification or specification hierarchy at any level in the bundle. For more information, see [[som-offer-bundles-with-specs|Product offer bundling with product specifications]].

## Product offer eligibility

As a product catalog admin or manager, you can use business rules to filter the product catalog, product offering categories, and product offerings dynamically, displaying only the appropriate catalog, categories, and offerings for which a customer is eligible. These rules enable your sales agents to sell the correct products to customers based on context, such as specific customer accounts, customer location, sales contracts, and more. You define these rules using product eligibility matrices. To learn more about using the product eligibility matrices, see [[configuring-sales-eligibility|Configuring product offer eligibility]].

## Product recommendations

In Sales Customer Relationship Management, different types of product recommendations are available to your sales agents. Your agents can get product recommendations as they're generating or updating leads and opportunities, or updating quotes.

-   Product recommendations using needs analysis - When your sales agents are generating leads and opportunities, they can use product selection guides to help determine relevant products for their customers. For information on setting up needs analysis, including the product selection guides, see [[configuring-needs-analysis|Configuring needs analysis]]. For details on how your agents can get product recommendations for leads and opportunities, see [[lead-management-use-needs-analysis|Get product recommendations for leads using needs analysis]] and [[opp-mgmt-use-needs-analysis|Get product recommendations for opportunities using needs analysis]].
-   Product offering recommendations for quotes - When your sales agents are updating quotes, they can get product recommendations for upselling or cross-selling additional products for existing quote line items. For information on setting up these recommendations, see [[configuring-offer-recommendations|Configuring product offering recommendations]]. For details on how product offering recommendations work in quotes, see [[using-prod-recommendations-quote|Using product offering recommendations in quotes]].

## What to explore next

[Configuring product offerings and catalogs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/som-managing-product-catalogs.md)

## Related

- [[order-mgt-business-portal|Customer self-service using the Business Portal]]
- [[som-managing-product-catalogs|Configuring product offerings and catalogs]]
- [[configure-ai-search-prod-catalog|Configuring AI Search for the product catalog]]
- [[create-product-offering-family|Create a product offering family]]
- [[som-offer-bundles-with-specs|Product offer bundling with product specifications]]
- [[configuring-sales-eligibility|Configuring product offer eligibility]]
- [[configuring-needs-analysis|Configuring needs analysis]]
- [[lead-management-use-needs-analysis|Get product recommendations for leads using needs analysis]]
- [[opp-mgmt-use-needs-analysis|Get product recommendations for opportunities using needs analysis]]
- [[configuring-offer-recommendations|Configuring product offering recommendations]]
- [[using-prod-recommendations-quote|Using product offering recommendations in quotes]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
- [[explore-order-management|Order management]]
- [[rules_101|Rules]]
