---
title: Setting up the Customer Contracts and Entitlements application
description: Configure the features and components of Customer Contracts and Entitlements to enable a seamless, end-to-end service experience including after sales services for your customers.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/set-up-post-sales-support.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Customer Contracts and Entitlements, Product data, Set up your environment, Configure, Customer Service Management]
---

# Setting up the Customer Contracts and Entitlements application

Configure the features and components of Customer Contracts and Entitlements to enable a seamless, end-to-end service experience including after sales services for your customers.

As a user with the admin role, you can set up the Customer Contracts and Entitlements application to enable users to create entitlements and customer contracts for users.

<table id="table_pxs_xwx_gyb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-entitlement-template-characteristic|Create a characteristic]]

</td><td>

Create a characteristic to add to an entitlement. A characteristic refers to the specific attributes or properties that define the entitlement.

</td></tr><tr><td>

[Create a user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateAUser.md)

</td><td>

Add a user to your instance to enable them to log in and use designated application features. After adding the user, you make them approver to review customer contracts.

</td></tr><tr><td>

[Assign a role to a user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_AssignARoleToAUser.md)

</td><td>

[[configure-data-model-roles|Assign roles]] to users. Use this feature to grant the sn\_customerservice\_manager \(CSM manager\) role to a newly added user and authorize them to make an informed judgment to review a customer contract.

</td></tr><tr><td>

[[import-create-csm-accounts|Create customer accounts]]**Note:** On the Accounts form, to view the customer contracts, remove the contract-related [[migration-lists|lists]] and configure the customer contracts related list.

</td><td>

Create an account and associate it to a customer contract.

</td></tr><tr><td>

[[create-a-consumer-record|Create a consumer record]]

</td><td>

Create a consumer record in [[c_CustomerServiceManagement|Customer Service Management]]. A consumer can be associated with a customer contract in the Customer Contracts and Entitlements application.

</td></tr><tr><td>

[[create-sold-item|Create a sold product]]

</td><td>

Create a record for a product that is sold to an account or a consumer. A sold product can be associated with multiple contracts.

</td></tr><tr><td>

[[create-install-base-item|Create an install base item]]

</td><td>

Create a record for an install base item that is sold to an account or a consumer. An install base item can be associated with multiple contracts.

</td></tr></tbody>
</table>

## Related

- [[create-entitlement-template-characteristic|Create a characteristic]]
- [[import-create-csm-accounts|Create customer accounts]]
- [[create-a-consumer-record|Create a consumer record]]
- [[create-sold-item|Create a sold product]]
- [[create-install-base-item|Create an install base item]]
- [[configure-data-model-roles|Assign roles]]
- [[migration-lists|Lists]]
- [[c_CustomerServiceManagement|Customer Service Management]]
