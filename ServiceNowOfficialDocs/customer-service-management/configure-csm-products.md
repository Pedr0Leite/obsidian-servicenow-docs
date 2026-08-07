---
title: Configure product data
description: Configure product data including product models, sold products, install base items and installed products.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-csm-products.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Product data, Set up your environment, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Configure product data

Configure product data including [[product-models|product models]], [[sold-product|sold products]], [[install-base-item|install base items]] and [[installed-products|installed products]].

## Before you begin

Role required: admin

## About this task

-   **Product models:** A product is a type of good or service that your company sells and supports. Product models identify different types of products, such as service, hardware, software, or consumables.

    **Note:** Product models require the Model Management plugin \(com.snc.model\).

-   **Sold products:** The products and components that have been sold to an account or a consumer.
-   **Install base items:** Items that represent the instances that have been installed or provisioned for a customer.
-   **Installed products:** Provide information on the sold products and how they are deployed or installed. Use installed products to create an association between sold products and install base items.

## Procedure

-   You can import the following [[product-data|product data]] using guided setup.

    -   [[import-csm-product-models|Import product models with guided setup]]
    -   [[import-csm-sold-products|Import sold products with guided setup]]
    -   [[import-csm-install-base-items|Import install base items with guided setup]]
    -   [[import-csm-installed-products|Import installed products with guided setup]]
-   You can create new product data using the [[c_CustomerServiceManagement|Customer Service Management]] application.

    -   [[c_CreateAProductModel|Create a product model]]
    -   [[create-sold-item|Create sold products]]
    -   [[create-install-base-item|Create install base items]]
    -   [[create-deployed-sold-item|Create installed products]]
-   You can configure the following relationships and associations after importing or creating product data:

    -   Product models
        -   [[associate-service-offering-product|Associate service offerings to product models]]
        -   [[create-csm-product-model-items|Configure product model and catalog item relationships]]
    -   Sold products
        -   [[asssociate-service-offering-sold-prod|Associate service offerings with sold products]]
        -   [[add-sold-product-contract|Associate sold products with contracts]]

## Related

- [[import-csm-product-models|Import product models with guided setup]]
- [[import-csm-sold-products|Import sold products with guided setup]]
- [[import-csm-install-base-items|Import install base items with guided setup]]
- [[import-csm-installed-products|Import installed products with guided setup]]
- [[c_CreateAProductModel|Create a product model]]
- [[create-sold-item|Create a sold product]]
- [[create-install-base-item|Create an install base item]]
- [[create-deployed-sold-item|Create installed products]]
- [[associate-service-offering-product|Associate services with product models]]
- [[create-csm-product-model-items|Configure product model and catalog item relationships]]
- [[asssociate-service-offering-sold-prod|Associate service offerings with sold products]]
- [[add-sold-product-contract|Associate sold products with contracts]]
- [[product-models|Product models]]
- [[sold-product|Sold products]]
- [[install-base-item|Install base items]]
- [[installed-products|Installed products]]
- [[product-data|Product data]]
- [[c_CustomerServiceManagement|Customer Service Management]]
