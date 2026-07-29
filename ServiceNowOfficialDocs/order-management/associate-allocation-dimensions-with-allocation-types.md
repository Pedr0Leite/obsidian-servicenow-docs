---
title: Associate allocation dimensions with allocation types
description: Associating allocation dimensions to allocation types enables consistent, transparent, multi‑dimensional roll‑ups for reporting and forecasting.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/associate-allocation-dimensions-with-allocation-types.html
release: australia
topic_type: task
last_updated: "2026-05-21"
reading_time_minutes: 1
breadcrumb: [Configure allocation types, Install and configure Opportunity Management, Lead and opportunity management apps, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Associate allocation dimensions with allocation types

Associating allocation dimensions to allocation types enables consistent, transparent, multi‑dimensional roll‑ups for reporting and forecasting.

## Before you begin

Role required: sn\_opty\_mgmt\_core.opportunity\_setup\_writer

## About this task

An allocation dimension defines the attributes \(for example, Territory, Product Offering Family\) used to group records for allocation. Use this task to create a dimension that determines how an Opportunity Allocation Type groups records and allocates amounts during allocation processing.

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Tables**.

2.  Select the **Opportunity Allocation Dimension** table.

3.  On the **Opportunity Allocation Dimension table** related links, select **Show List**.

4.  Select **New** to [[create-new-opportunity|create an opportunity]] allocation dimension record.

5.  On the form, fill in the [[fields|fields]].

    |Field|Description|
    |-----|-----------|
    |Allocation Type|Specifies the type of opportunity allocation.|
    |Name|Unique display name of the allocation dimension.|
    |Allocation Table|The table or entity the allocation type applies to \(Opportunity or Opportunity Line\).|
    |Allocation Table Field|The field from the source entity that is used as the basis for the allocation \(e.g., product family, territory\).|
    |Opportunity Allocation Table|The table used to store allocation records for opportunities.|
    |Opportunity Allocation Field|The field in the allocation table that references the allocation basis from the source record.|
    |Active|Indicates whether the allocation dimension is available for use.|

6.  Select **Submit**.


## Result

The opportunity allocation dimension is created and listed on the **Opportunity Allocation Dimensions** page.

## What to do next

-   [[manage-allocations|Manage allocations]]
-   [[add-or-edit-opportunity-allocations|Add or edit opportunity allocations]]
-   [[split-an-opportunity-allocation|Split opportunity allocation]]

**Related topics**  


[[opportunity-mgmt-using|Using Opportunity Management]]

[[opportunity-management|Opportunity Management]]

## Related

- [[manage-allocations|Manage allocations]]
- [[add-or-edit-opportunity-allocations|Add or edit opportunity allocations]]
- [[split-an-opportunity-allocation|Split opportunity allocation]]
- [[opportunity-mgmt-using|Using Opportunity Management]]
- [[opportunity-management|Opportunity Management]]
- [[create-new-opportunity|Create an opportunity]]
- [[fields|Fields]]
