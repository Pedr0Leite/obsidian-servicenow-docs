---
title: Roles required for B2B2C data models
description: With the B2B2C model, organizations across industries can easily configure multi-level customer relationships and support business customers who, in turn, support their end consumers.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/rolesforb2b2c.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Customer Service Management]
---

# Roles required for B2B2C data models

With the B2B2C model, organizations across industries can easily configure multi-level customer relationships and support business customers who, in turn, support their end consumers.

[[customer-data-model-b2b2c|Customer data models for B2B2C]] require different roles, depending on the tasks you perform.

<table id="table_nkn_3tg_4qb"><thead><tr><th>

Role

</th><th>

Tasks

</th></tr></thead><tbody><tr><td>

sn\_customerservice\_agent \(customer service agent\)

</td><td>

Create a case for an account consumer from platform or [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) workspaces to track issues. See [[t_CreateACaseFromCustServApp|Create cases for an account consumer]].

</td></tr><tr><td>

awa\_agent and sn\_customerservice\_agent

</td><td>

Accept a chat request on CSM workspaces and create a case from the chat interaction.

</td></tr><tr><td>

sn\_customerservice\_manager \(customer service manager\)

</td><td>

Associate consumers to an account to identify the end consumers who are using products or services.Associate install base items/sold products with account consumers to track the end consumer issues.

</td></tr><tr><td>

sn\_acct\_consumer.consumer \(account consumer\)

</td><td>

View sold products/install bases items to track the instances provisioned for your account and the products or services sold to your account.Create a case for [[install-base-item|install base items]] or [[sold-product|sold products]] issues from the CSM portal. You get email notifications when a case is created, commented, resolved, or closed. See [[t_CreateACaseFromCustPortal|Create a case from the CSM portal]].

</td></tr><tr><td>

sn\_customerservice.customer \(account contact\)

</td><td>

View sold products/install bases items to track end consumer issues. See[[view-install-base-info|View install base information from the Customer Service Portal]] and [[view-product-info-csp|View products information from the Customer Service Portal]].Create a case for an account consumer to track consumer issues. See [Create cases for an account consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/t_CreateACaseFromCustPortal.md).

</td></tr></tbody>
</table>

## Related

- [[t_CreateACaseFromCustServApp|Create a customer service case]]
- [[t_CreateACaseFromCustPortal|Create a product case from the Customer Service Portal]]
- [[view-install-base-info|View install base information from the Customer Service Portal]]
- [[view-product-info-csp|View product information from the Customer Service Portal]]
- [[customer-data-model-b2b2c|Customer data models for B2B2C]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[install-base-item|Install base items]]
- [[sold-product|Sold products]]
