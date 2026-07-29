---
title: Create a needs-based product offering recommendation
description: Set the product offering to be used as a product recommendation for a needs template.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/create-product-recommendations.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring needs analysis, Configuring product offerings and catalogs, Lead-to-cash foundation apps, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Create a needs-based product offering recommendation

Set the product offering to be used as a product recommendation for a needs template.

## Before you begin

Product offerings must be defined and published before they can be set as a product recommendation.

Role required: sn\_prd\_pm.product\_catalog\_manager, sn\_prd\_pm.product\_catalog\_admin, admin

## Procedure

1.  In the CSM Configurable Workspace, select the **List** \[Omitted image "list-outline-24.svg"\] Alt text: view.

2.  Navigate to **Needs** &gt; **Needs Based Offering Recommendation** and select **New**.

    On the form, fill in the [[fields|fields]]:

    |Field|Description|
    |-----|-----------|
    |Name|Name of the recommended offering displayed to the agent. For example: Recommend Flex or Recommend Quad Play service bundle.|
    |Description|Brief description of the recommendation. For example: Recommending flex offers based on customer needs.|
    |Product Offering|Product offering to be recommended.|

3.  Select **Save**.

    The selected product offering is available as a product offering recommendation and can be selected as a guidance node in a needs decision tree.


## What to do next

[[configure-needs-decision-tree|Create a decision tree for a needs template]].

**Related topics**  


[[using-product-catalog|Using product catalogs]]

[[product-catalog-managment|Product Catalog Management]]

## Related

- [[configure-needs-decision-tree|Create a decision tree for a needs template]]
- [[using-product-catalog|Using product catalogs]]
- [[product-catalog-managment|Product Catalog Management]]
- [[fields|Fields]]
