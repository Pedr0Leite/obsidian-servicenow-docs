---
title: Setting up products and available services at a business location
description: By setting up the relationships between organizations and users in the Customer Service Management \(CSM\) application, your organization can associate the products and services with the service organization \(SO\). The SO staff can address the customer queries about the products and services at a business location and even raise a case on the behalf of their customers.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/products-services-at-bus-loc.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Service Model Foundation, Data models, Set up your environment, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Setting up products and available services at a business location

By setting up the relationships between organizations and users in the [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) application, your organization can associate the products and services with the service organization \(SO\). The SO staff can address the customer queries about the products and services at a business location and even raise a case on the behalf of their customers.

<table id="table_wlp_2jn_byb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-csm-service-definition|Create a service definition]]

</td><td>

Create a service definition record.

</td></tr><tr><td>

[[service-definition-form-fields|Service Definition form]]

</td><td>

Specify how a service organization provides its services by configuring the **Organizations offering Service** field in the sn\_case\_type\_selection table.

</td></tr><tr><td>

[[service-def-associate-products|Associate a product with a service definition]]

</td><td>

Associate one or more products with a service definition.

</td></tr><tr><td>

[[associate-services-to-service-organization|Associate service organizations with a service]]

</td><td>

Establish an association between products and available services to service organizations. This association can be done by defining the organization criteria.

</td></tr></tbody>
</table>**Note:** The service-related capabilities are available only after activating the [[customer-service-case-types|Customer Service Case Types]] \(sn\_csm\_case\_types\) plugin. The plugin is optional and must be enabled if you want to use these capabilities with business locations.

## Related

- [[create-csm-service-definition|Create a service definition]]
- [[service-definition-form-fields|Service Definition form]]
- [[service-def-associate-products|Associate a product with a service definition]]
- [[associate-services-to-service-organization|Associate service organizations with a service]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[customer-service-case-types|Customer service case types]]
