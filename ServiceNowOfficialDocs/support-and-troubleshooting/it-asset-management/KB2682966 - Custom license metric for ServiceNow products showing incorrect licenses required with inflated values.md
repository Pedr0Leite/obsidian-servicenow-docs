---
title: "Custom license metric for ServiceNow products showing incorrect licenses required with inflated values"
aliases:
  - KB2682966
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2682966
kb_number: KB2682966
last_modified: 2026-05-20
---

## Custom license metric for ServiceNow products showing incorrect licenses required with inflated values

  

### Issue

When using a custom license metric to license ServiceNow products, the licenses required value in the Software Asset Workspace may appear inflated or doubled compared to the actual units consumed.

For example, the Software Asset Management product may show 1,000 licenses required, while the related model shows only 500 units consumed.

### Symptoms

Symptoms

-   The `licenses_required` value in the `samp_license_required` table is double the expected amount.
-   The Software Asset Workspace shows an inflated licenses required count.
-   A custom license metric and resource values are configured on the instance.
-   A scheduled job updates `allocations_available` values in the entitlement.

To investigate, complete the following steps:

-   Review the licenses required and `units_consumed` values in the resource value table.
-   Review the custom license metric script to verify whether it returns double the `units_consumed` value.
-   Review the `allocations_available` value in the entitlement record.
-   Verify whether the same behavior occurs on a default instance to isolate whether the issue is caused by customizations.

### Release

All

### Cause

The issue is caused by a scheduled job on the instance that updates `allocations_available` values in the entitlement. The `allocations_available` value is used during SAMP reconciliation, and adding allocations for a custom license metric results in inflated licenses required values.

> Note: Custom license metrics do not support allocations.

### Resolution

Before making changes, back up relevant records.

1.  Disable the scheduled job that updates `allocations_available` values. To locate it, go to System Scheduler > Scheduled Jobs and search for the job by name.
2.  Reset the `allocations_available` value in the entitlement record to the correct value. To locate the entitlement, go to Software Asset > Entitlements and open the relevant record.
3.  Run SAMP reconciliation again to reflect the updated values. To do this, go to Software Asset > Administration > Run Software Reconciliation.
4.  Review all customizations related to the custom license metric and scheduled job to verify they align with supported configurations. Allocations are not supported for custom license metrics on resource values.

### Related Links

[Add a custom license metric](http://servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/task/add-custom-license-metric.html)  
[Custom license metric example script](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/reference/custom-license-example-script.html)  
[Software Asset Management properties](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/reference/sam-properties.html)
