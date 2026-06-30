---
title: Application plugin installation sequence in Purchase Order Management
description: View the consolidated list of plugins, high-level description of each plugin, and the dependencies that are required before installing each plugin in Purchase Order Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/app-plugin-install-seq-purch-ord-mgmt.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [app installation sequence, Purchase order management installation, plugins]
breadcrumb: [Install Purchase Order Management, Configure, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
---

# Application plugin installation sequence in Purchase Order Management

View the consolidated list of plugins, high-level description of each plugin, and the dependencies that are required before installing each plugin in [[purchase-order-mgmt-landing-page|Purchase Order Management]].

## Application plugin list

<table id="table_ep1_c32_q2c"><thead><tr><th>

Plugin name

</th><th>

Description

</th><th>

Dependencies

</th></tr></thead><tbody><tr><td>

[[purchase-experience-workflow|Sourcing and Purchasing Automation]] \(com.snc.sn\_pr\)

</td><td>

Provides workflows and automation for sourcing requests, [[negotiations|negotiations]], and purchase requisitions.

</td><td>

-   Source-to-Pay Common Architecture \(com.snc.sn\_shop\)
-   [[supplier-common|Supplier Common Architecture]] \(com.snc.sn\_slm\)

</td></tr><tr><td>

Purchase Order Management \(com.snc.sn\_poem\_core\)

</td><td>

Enables operational buyers and suppliers to flag [[purchase-order-table|purchase order]] issues and resolve them efficiently.

</td><td>

Sourcing and Purchasing Automation \(com.snc.sn\_pr\)

</td></tr><tr><td>

[[awa-spo|Advanced Work Assignment for Source-to-Pay Operations]] \(snc.sn\_spend\_awa\)

</td><td>

Provides configurations to support automatic routing, queuing, and assignment of finance cases and emails.

</td><td>

[[advanced-work-assignment|Advanced Work Assignment]] \(glide.awa\)

</td></tr></tbody>
</table>**Parent Topic:**[[install-purch-order-mgmt|Install Purchase Order Management]]

## Related

- [[install-purch-order-mgmt|Install Purchase Order Management]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-experience-workflow|Sourcing and Purchasing Automation]]
- [[negotiations|Negotiations]]
- [[supplier-common|Supplier Common Architecture]]
- [[purchase-order-table|Purchase order]]
- [[awa-spo|Advanced Work Assignment for Source-to-Pay Operations]]
- [[advanced-work-assignment|advanced work assignment]]
