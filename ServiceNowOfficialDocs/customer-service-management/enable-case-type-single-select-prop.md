---
title: Enable the case type single select property
description: Enable the case type single select property so that customer service agents can use the case type single select version of the case type selector and create cases of a specific type with one click.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/enable-case-type-single-select-prop.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring customer service case types, Customer service case types, Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Enable the case type single select property

Enable the case type single select property so that customer service agents can use the case type single select version of the [[csm-case-type-select-modals|case type selector]] and create cases of a specific type with one click.

## Before you begin

Role required: admin

## About this task

In [[csm-workspaces-configure|CSM Configurable Workspace]], there are three versions of the case type selector available to agents when creating cases of a specific type.

-   With the multi-select version, the agent selects a case type and optionally selects a category and subtype to narrow the available choices before creating a case. This is the default functionality.
-   With the single-select version, the agent selects a case type and creates a case. The system populates some of the fields on the [[r_CustomerServiceCaseForm|Case form]] with values that have been predefined in the selection configuration.
-   With the Product Service Select version, the agent selects a product and a service to create a case. For more information, see [[csm-case-type-select-modals-product-service|Product Service select version of the case type selector]].

To use the single-select version, enable the **sn\_csm\_case\_types.case\_type\_single\_field\_select** property. You must also [[create-case-type-single-selection|create a configuration]].

## Procedure

1.  Navigate to **sys\_properties.list**.

2.  Click the **sn\_csm\_case\_types.case\_type\_single\_field\_select** property in the **Name** field.

3.  Set the **Value** to true.

4.  Click **Update**.

## Related

- [[csm-case-type-select-modals-product-service|Product Service select version of the case type selector]]
- [[create-case-type-single-selection|Create a configuration for case type single-select]]
- [[csm-case-type-select-modals|Case type selector]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[r_CustomerServiceCaseForm|Case form]]
