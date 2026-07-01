---
title: Updating specification versions
description: Enterprises frequently create and update new versions of product and service specifications. When these changes occur, it's important to update the existing product specification in ServiceNow. Failure to update the product specifications can lead to difficulties with MACD \(Modify, Add, Change, Delete\) operation when orders enter fulfillment.OM content revamp - Check with Judy if this and sub-topics are covered in configuring product catalog.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/som-specification-version-update.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Specifications and product offerings, Configuring product offerings and catalogs, Lead-to-cash foundation apps, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Updating specification versions

Enterprises frequently create and update new versions of product and service specifications. When these changes occur, it's important to update the existing product specification in ServiceNow®. Failure to update the product specifications can lead to difficulties with MACD \([[Modify|Modify]], Add, Change, Delete\) operation when orders enter fulfillment.

Updating specification versions helps with:

-   Introducing new characteristics along with their options.
-   Adding new options to existing characteristics and removing existing characteristics or their options.
-   Renaming existing characteristics and options.
-   Incorporating new relationships and updating or removing existing relationships.
-   Adding compatibility [[rules_101|rules]].

## Specification version updates

The following list shows the types of specification version updates that can occur:

-   Characteristics
    -   New
    -   Changed - enumerations
    -   Removed
-   Child Relationships \(bundled/composed\)
    -   New
    -   Removed
    -   Change cardinality
-   Horizontal Relationships/Compatibility Rules
-   Attribute Mapping Rules

## Batch specification version update

A set of specification versions can be updated using the batch specification utility in [[order-mgt-overview|Sales Customer Relationship Management]]. The specification can also be scheduled.

**What to do next**

[[som-configure-specification-version-update|Configure update specification versions]]

-   **[Configure update specification versions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/som-configure-specification-version-update.md)**  
Configure specification version updates so that product specification versions can be updated to reflect changes and updates.
-   **[[som-configure-specification-version-update-silent-batch-utility|Batch update for product specification versions]]**  
Use the inventory batch update job to update product specifications when changes occur from one version to another.
-   **[[som-view-upgrade-inventory-job-status|View upgrade inventory job status]]**  
View the status of a specification upgrade job using the upgrade inventory Job status list form.

**Parent Topic:**[[order-mgt-product-catalog|Setting up specifications and product offerings]]

## Related

- [[som-configure-specification-version-update|Configure update specification versions]]
- [[som-configure-specification-version-update-silent-batch-utility|Batch update for product specification versions]]
- [[som-view-upgrade-inventory-job-status|View upgrade inventory job status]]
- [[order-mgt-product-catalog|Setting up specifications and product offerings]]
- [[Modify|Modify]]
- [[rules_101|Rules]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
