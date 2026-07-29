---
title: Configuring service definitions
description: Create service definitions for the types of services required to support your products. Associate different features such as case types, playbooks, and record producers with service definitions so that customers can request the services they need and agents can create cases of the right type to support those services.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-service-definitions-configure.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Service definitions, Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Configuring service definitions

Create [[csm-service-definitions|service definitions]] for the types of services required to support your products. Associate different features such as case types, playbooks, and record producers with service definitions so that customers can request the services they need and agents can create cases of the right type to support those services.

System administrators can use the service definitions feature to define the services that are offered to customers and connect those services to products, case types, playbooks, and catalog items.

<table id="table_u5g_1p3_fwb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-csm-service-definition|Create a service definition]]

</td><td>

Create a definition for a service that's offered to support a product.

</td></tr><tr><td>

[[service-def-associate-products|Associate a product with a service definition]]

</td><td>

Configure the relationship between a product and service.

</td></tr><tr><td>

[[service-def-associate-case-type|Associate a case type with a service definition]]

</td><td>

A case type defines the case resolution process for a service definition.

</td></tr><tr><td>

[[service-def-associate-playbook|Associate a playbook with a service definition]]

</td><td>

A playbook provides step-by-step guidance for resolving a specific type of case. Defining a playbook record generator view enables case creation for a requested service.

</td></tr><tr><td>

[[configure-user-criteria-for-a-service-definition|Configure user criteria for a service definition]]

</td><td>

Configure user criteria for a service definition that restricts access to the service. Associate user-specific criteria such as role, assignment group, or specific user with a service definition to determine which users can access and use that service to create a case.

</td></tr><tr><td>

[[configure-customer-criteria-for-a-service-definition|Configure customer criteria for a service definition]]

</td><td>

Configure customer criteria for a service definition that restricts access to the service. Associate customer-specific criteria such as location, customer level, or verified status with a service definition to determine which customers are eligible for that service.

</td></tr><tr><td>

[[service-def-default-field-values|Configure default field values for a service definition]]

</td><td>

Configure default values for fields in a service definition's target table. When a record is created for this table, the system uses these values to auto populate record fields.

</td></tr><tr><td>

[[service-def-config-catalog-items|Configure catalog items for a service definition]]

</td><td>

End users can select a catalog item from the service portal and use the record producer to create the service request.

</td></tr><tr><td>

[[service-def-config-related-services|Configure related services for a service definition]]

</td><td>

Associate one or more related services with a service definition to create parent-child relationships between service definitions. For example, you can create service definitions for case tasks and associate them with a service definition for a case type.

</td></tr><tr><td>

[[associate-services-to-service-organization|Associate service organizations with a service]]

</td><td>

After creating a service definition, you can associate organizations offering service with a service organization.

</td></tr><tr><td>

[[create-csm-service-def-category|Create a service definition category]]

</td><td>

Create a category for service definitions. You can use these categories to create logical groupings of service definitions.

</td></tr><tr><td>

[[service-def-category-associate-service|Associate service definitions with a category]]

</td><td>

Add service definitions to a category. A category can have one or more associated service definitions and a service definition can belong to multiple categories.

</td></tr><tr><td>

[[service-def-config-case-interceptor|Add a case type to the Case interceptor]]

</td><td>

In the Core UI, the Case interceptor [[migration-lists|lists]] the types of customer service cases that an agent can create. If you create a case type and you want that case type to appear in the Case interceptor, you need to add it to the Case interceptor configuration.

</td></tr></tbody>
</table>

## Related

- [[create-csm-service-definition|Create a service definition]]
- [[service-def-associate-products|Associate a product with a service definition]]
- [[service-def-associate-case-type|Associate a case type with a service definition]]
- [[service-def-associate-playbook|Associate a playbook with a service definition]]
- [[configure-user-criteria-for-a-service-definition|Configure user criteria for a service definition]]
- [[configure-customer-criteria-for-a-service-definition|Configure customer criteria for a service definition]]
- [[service-def-default-field-values|Configure default field values for a service definition]]
- [[service-def-config-catalog-items|Configure catalog items for a service definition]]
- [[service-def-config-related-services|Configure related services for a service definition]]
- [[associate-services-to-service-organization|Associate service organizations with a service]]
- [[create-csm-service-def-category|Create a service definition category]]
- [[service-def-category-associate-service|Associate a service definition with a service definition category]]
- [[service-def-config-case-interceptor|Add a case type to the Case interceptor]]
- [[csm-service-definitions|Service definitions]]
- [[migration-lists|Lists]]
