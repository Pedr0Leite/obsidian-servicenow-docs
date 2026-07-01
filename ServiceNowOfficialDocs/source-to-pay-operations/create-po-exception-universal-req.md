---
title: Create purchase order exception from Universal Request
description: Operational buyers can convert universal requests into purchase order exceptions during triage, cutting down on manual effort and ensuring that purchase order related issues are tracked and resolved more efficiently.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/create-po-exception-universal-req.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
tags:
  - source-to-pay-operations
  - type-task
---

# Create purchase order exception from Universal Request

Operational buyers can convert universal requests into [[purchase-order-table|purchase order]] exceptions during triage, cutting down on manual effort and ensuring that purchase order related issues are tracked and resolved more efficiently.

## Before you begin

Role required: Operational buyer

-   You must have the following plugin installed: [[universal-request|Universal Request]] for [[source-to-pay-operations-overview|Source-to-Pay Operations]] Plugin \[sn\_fsc\_ur\_common\].
-   You must enable the Universal Request functionality.
-   You must maintain users in the [[purchase-order-mgmt-landing-page|Purchase Order Management]] Universal Request Group associated with the universal request service set.

## Procedure

1.  Navigate to **All** &gt; **[[purch-order-mgmt-ws|Source-to-Pay workspace]]**.

2.  Select the list icon.

3.  Navigate to **Universal request** &gt; **All**.

4.  Select a Universal Request.

5.  Select **Create [[purchase-order-exception-table|purchase order exception]]**.

6.  In the Create New Purchase Order Exception form, fill in the details.

    For a description of the field values, see [[create-new-poe-form|Create new purchase order exception form]].

    The universal request number from which the purchase order exception is created appears in the **Universal Request** field on the [[purch-order-exception-form|purchase order exception form]].

7.  Select **Save**.


## Result

A purchase order exception record is created, which links to the original universal request.

**Parent Topic:**[[use-purch-order-mgmt|Use Purchase Order Management]]

**Related topics**  


[Reporting delivery plan issues]()

[Resolving purchase order exceptions]()

## Related

- [[create-new-poe-form|Create new purchase order exception form]]
- [[use-purch-order-mgmt|Use Purchase Order Management]]
- [[purchase-order-table|Purchase order]]
- [[universal-request|Universal Request]]
- [[source-to-pay-operations-overview|Source-to-Pay Operations]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[purch-order-exception-form|Purchase order exception form]]
