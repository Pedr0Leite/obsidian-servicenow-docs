---
title: Create a service definition
description: Create a service definition record in the Customer Service Management \(CSM\) application to establish connections between products, services, and case types.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/create-csm-service-definition.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Configuring service definitions, Service definitions, Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a service definition

Create a service definition record in the [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) application to establish connections between products, services, and case types.

## Before you begin

Role required: sn\_csm\_case\_types.service\_definition\_manager, sn\_csm\_case\_types.service\_definition\_admin, or admin

## About this task

A service definition record stores the details about a service that is provided to customers. You can create [[csm-service-definitions|service definitions]] for the types of services that are required to support your products and for cases, case types, and case tasks.

After creating a service definition, you can associate the service definition with a product. By associating one or more related services with a service definition, you can create parent-child relationships between the service definitions.

You can also [[configure-data-model-relationships|create relationships]] between the service definition and other related services. For example, you can create a service definition for a case and then create one or more service definitions for your case tasks. Afterward, you can establish a relationship between the case service definition and the case task service definitions.

## Procedure

1.  Navigate to **All** &gt; **Customer Service** &gt; **Administration** &gt; **Service Definitions**.

2.  Select **New**.

3.  In the **Name** field, enter a name for the service definition.

4.  If necessary, modify the information in the **ID** field.

    The system auto-populates the **ID** field with the name of the service definition and replaces the spaces with underscores. The ID can contain alphanumeric characters and underscores and can be up to 40 characters in length.

    **Note:** The value in this field must be unique.

5.  In the **Table** field, select the table that the service definition is available for.

    For example, if the service is available for the [[onboarding-case-type-overview|onboarding case type]], select the Onboarding Case \[sn\_onboarding\_case\] table.

6.  In the **Customer service type** field, select a service type for the service definition.

    A service type enables the system to show the following type of services based on the context:

    -   Pre-sale
    -   Post-sale
    -   General
7.  In the **Playbook record generator** field, select a playbook record generator.

    If a service definition has an associated playbook, the agent can use the playbook in a tab on the case record. For more information, see [[service-def-associate-playbook|Associate a playbook with a service definition]].

8.  In the **Image** field, select an image for the service definition.

    Service definitions appear in the [[csm-case-type-select-modals|case type selector]] in a card view. The image appears in the card for a service definition along with the name and description.

9.  In the **Default table field values** field, select one or more fields and values.

    Configure the default values for the fields in the target table for service definitions. When a record is created for this table, the system uses these values to automatically fill in the record fields. For more information, see [[service-def-default-field-values|Configure default field values for a service definition]].

10. In the **Order** field, add an order value for the service definition.

    This value determines the order in which the services are displayed in the case type selector or other workflows. Service definitions with the lowest order value are displayed first. The default value is 100.

    -   Service definitions with no order value appear after the ordered service definitions. These service definitions have the lowest priority.
    -   If one or more service definitions have the same order value, the system displays the service definitions in alphabetical order.
11. Enable the **Active** check box.

12. Enable the **Use service catalog item** check box.

    When this check box is enabled, the service definition can use catalog items and their associated record producers to create cases in [[csm-workspaces-configure|CSM Configurable Workspace]]. The Catalog Service Relationships related list stores the catalog items that are associated with the service definition. For more information, see [[csm-service-definition-catalog-items|service definition use service catalog items]].

13. In the **Description** field, add a description of the service definition.

    Service definitions appear in the case type selector in a card view. The card includes the name, description, and image for a service definition. Customer service agents can search for services by entering keywords found in the service definition name and description.

14. Select **Submit**.

    The service definition is added to the Service Definitions list.

    Upon save, the service definition record includes the following related [[migration-lists|lists]]:

    -   Product Service Relationships
    -   Catalog Service Relationships
    -   Service to Service Relationships
    -   Service Definition Category Relationships
    -   Reports

## Result

After creating a service definition, you can perform the following configuration tasks:

-   [[service-def-associate-products|Associate one or more products with a service definition]]
-   [[create-csm-service-def-category|Create a service definition category]]
-   [Associate a product with a service definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/service-def-associate-products.md)
-   [[service-def-associate-case-type|Associate a case type with a service definition]]
-   [Associate a playbook record generator with a service definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/service-def-associate-playbook.md)
-   [[service-def-category-associate-service|Associate a service definitions to a service definition category]]
-   [Configure default field values for a service definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/service-def-default-field-values.md)
-   [[service-def-config-catalog-items|Configure catalog items for a service definition]]
-   [[service-def-config-related-services|Configure related services for a service definition]].
-   [[associate-services-to-service-organization|Associate service organizations with a service]].
-   [[service-def-config-case-interceptor|Add a case type to the Case interceptor]].

## Related

- [[service-def-associate-playbook|Associate a playbook with a service definition]]
- [[service-def-default-field-values|Configure default field values for a service definition]]
- [[csm-service-definition-catalog-items|Service definitions with catalog items]]
- [[service-def-associate-products|Associate a product with a service definition]]
- [[create-csm-service-def-category|Create a service definition category]]
- [[service-def-associate-case-type|Associate a case type with a service definition]]
- [[service-def-category-associate-service|Associate a service definition with a service definition category]]
- [[service-def-config-catalog-items|Configure catalog items for a service definition]]
- [[service-def-config-related-services|Configure related services for a service definition]]
- [[associate-services-to-service-organization|Associate service organizations with a service]]
- [[service-def-config-case-interceptor|Add a case type to the Case interceptor]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[csm-service-definitions|Service definitions]]
- [[configure-data-model-relationships|Create relationships]]
- [[onboarding-case-type-overview|Onboarding case type]]
- [[csm-case-type-select-modals|Case type selector]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[migration-lists|Lists]]
