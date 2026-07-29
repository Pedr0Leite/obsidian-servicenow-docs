---
title: Configuring Service Exchange Order Management for Providers
description: Configure the Service Exchange Order Management for Providers application, which enables providers to use Order Management to create and fulfill product orders over Service Exchange. Providers publish the product offerings and service specifications as remote catalog items so that consumers can order from the Service Catalog on their own instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-sb-om.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Order Management for providers with Service Exchange, Integrate, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Configuring Service Exchange Order Management for Providers

Configure the Service Exchange [[explore-order-management|Order Management]] for Providers application, which enables providers to use Order Management to create and fulfill product orders over Service Exchange. Providers publish the product offerings and service specifications as remote catalog items so that consumers can order from the Service Catalog on their own instance.

## Configuration overview

Follow these tasks to set up the Service Exchange Order Management for Providers application, which uses Order Management to [[som-create-product-offering|create product offerings]] and service specification and publish them ServiceNow in your provider instance as remote record producers. Service Exchange admins can then activate these remote record producers to make the products and services available from the Service Catalog on consumer instances.

<table id="table_n2l_dcy_qxb"><thead><tr><th>

Configuration step

</th><th>

Description

</th><th>

Role

</th></tr></thead><tbody><tr><td>

[Install Service Exchange for Providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/install-service-bridge-v2-provider.md)

</td><td>

Install the Service Exchange for Providers application from the ServiceNow Store. For more information on configuring this application, see [Configure Service Exchange for Providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-configure-provider.md).

</td><td>

Admin

</td></tr><tr><td>

[Install Service Exchange for Consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/install-service-bridge-v2-customer.md)

</td><td>

Install the Service Exchange for Consumers application from theServiceNow Store. For details on configuring this application, see [Configure Service Exchange for Consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-install.md).

</td><td>

Admin

</td></tr><tr><td>

[[install-service-bridge-om-providers|Install Service Exchange Order Management for Providers]]

</td><td>

Install the Service Exchange Order Management for Providers application from the ServiceNow Store.

</td><td>

Admin

</td></tr><tr><td>

[[create-sb-product-offerings|Create a product offering for a remote catalog item]]

</td><td>

In the provider instance, create the product offerings to be added as remote catalog item to the service catalog for your consumers.

</td><td>

Product catalog admin or manager

</td></tr><tr><td>

[[create-sb-service-specs|Create a service specification for a remote catalog item]]

</td><td>

In the provider instance, create the service specification for a service to be added as a remote catalog item to the service catalog for your consumers.

</td><td>

Product catalog admin or manager

</td></tr><tr><td>

[[associate-criteria-remote-catalog|Associate consumer criteria to a remote record producer]]

</td><td>

In the provider instance, review the remote record producer and associate the customer criteria that entitles the catalog item for eligible Service Bridge consumers.

</td><td>

Service Exchange provider admin

</td></tr><tr><td>

Associate consumer criteria to the remote record producer for managing inventory.

</td><td>

Review the remote record producer for managing inventory and associate the customer criteria.

</td><td>

 

</td></tr><tr><td>

[[activate-entitlements-sb-consumer|Activate the remote record producer]]

</td><td>

In the consumer instance, activate entitlements for the remote record producers.

</td><td>

Service Exchange consumer admin

</td></tr><tr><td>

[[retire-product-offer|Retire a remote catalog item]]

</td><td>

Retire a product offering or service specification used in a remote catalog, which automatically retires the corresponding remote record producer and removes the item from the service catalog on the consumer instance.

</td><td>

Product catalog admin or manager

</td></tr></tbody>
</table>

## Related

- [[install-service-bridge-om-providers|Install Service Exchange Order Management for Providers]]
- [[create-sb-product-offerings|Create a product offering for a remote catalog item]]
- [[create-sb-service-specs|Create a service specification for a remote catalog item]]
- [[associate-criteria-remote-catalog|Associate consumer criteria to a remote record producer]]
- [[activate-entitlements-sb-consumer|Activate the remote record producer]]
- [[retire-product-offer|Retire a remote catalog item]]
- [[explore-order-management|Order management]]
- [[som-create-product-offering|Create product offerings]]
