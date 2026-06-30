---
title: Update a purchase order to revise supplier suggested changes
description: After a purchase order exception is assigned to you, update the impacted purchase order by proposing changes that differ from the supplier’s suggestions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/update-po-revise-supp-changes.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [Address exception, Resolve purchase order exception, Update purchase order, Edit order]
breadcrumb: [Resolving purchase order exceptions, Use, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
---

# Update a purchase order to revise supplier suggested changes

After a [[purchase-order-exception-table|purchase order exception]] is assigned to you, update the impacted [[purchase-order-table|purchase order]] by proposing changes that differ from the [[supplier|supplier]]’s suggestions.

## Before you begin

Role required: sn\_poem\_core.operational\_buyer

## Procedure

1.  Navigate to **Workspaces** &gt; **[[purch-order-mgmt-ws|Source-to-Pay Workspace]]**.

2.  Select the **[[purchase-order-mgmt-landing-page|Purchase order management]]** tab.

3.  Select an open exception that you want to work on.

4.  From the **Address exception** list, select **Update impacted order**.

    \[Omitted image "pom-update-impacted-order.png"\] Alt text: Update an impacted purchase order to address the exception

5.  Select **Edit order**.

    \[Omitted image "pom-update-order-edits.png"\] Alt text: Edit the order to revise the supplier's changes

6.  In the Quick edit window, update the purchased quantity or requested delivery date, or both.

    \[Omitted image "pom-update-order-quickedits.png"\] Alt text: Revise the quantity or delivery date or both

7.  Select **Save edit**.

    .

8.  To update more fields, select **Edit full record**.


## Result

A [[purchase-requisition|purchase requisition]] of type Revision is created with your updates and is assigned to a reviewer for further action.

**Parent Topic:**[[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]

## Related

- [[resolving-purchase-order-exceptions|Resolving purchase order exceptions]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[purchase-order-table|Purchase order]]
- [[supplier|Supplier]]
- [[purch-order-mgmt-ws|Source-to-Pay Workspace]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-requisition|Purchase requisition]]
