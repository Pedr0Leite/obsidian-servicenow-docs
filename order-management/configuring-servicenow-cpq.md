---
title: Configuring CPQ Configurator
description: Plan and configure your implementation of the CPQ Configurator. Product catalog admins and agents run CPQ Configurator in the CSM Configurable Workspace, while users using self-service features use it in the Business Portal.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-servicenow-cpq.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [configure]
breadcrumb: [Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Configuring CPQ Configurator

Plan and configure your implementation of [[understand-the-commerce-logic-engine|the CPQ Configurator]]. Product catalog admins and agents run [[explore-servicenowcpq|CPQ Configurator]] in the CSM Configurable Workspace, while users using self-service features use it in the Business Portal.

## Configuration overview

1.  Install the following applications using the Application Manager:

    -   [[explore-order-management|Order Management]] v15.3.0
    -   Product configurator v1.0.1
    -   CPQ Integration v2.1.0
    -   CPQ Configurator v1.2.5
    -   [[quote-management|Quote Management]] v9.1.0
    -   Customer Life Cycle Management Workflows v5.1.1
    -   Product and Pricing [[rules_101|Rules]] v9.0.0
    -   [[opportunity-management|Opportunity Management]] v8.0.0
    -   Sales Cart v2.1.0
    **Note:** Other applications, such as [[product-catalog-managment|Product Catalog Management]] Core v17.1.0, and [[pricing-management|Pricing Management]] v15.0.0 are installed automatically with the preceding applications.

2.  [[cpq-integration-create-certificates|Set up a ServiceNow instance for CPQ integration]].
3.  [[set-up-logik-instance|Provision a Logik.ai instance]]
4.  [[connect-sn-instance-logik|Set up a ServiceNow instance connection with a Logik.ai instance]].
5.  [[set-up-external-connection-logik|Set up an external connection in CPQ]].
6.  [[enable-advanced-configurator|Enable the CPQ Configurator]].

    If you're currently using the [[order-mgt-overview|Sales Customer Relationship Management]] product configurator and want to use the CPQ Configurator, use the **enable\_advanced\_configuration** system property to enable the CPQ Configurator.

## Related

- [[cpq-integration-create-certificates|Set up a ServiceNow instance for CPQ integration]]
- [[set-up-logik-instance|Provision a Logik.ai instance]]
- [[connect-sn-instance-logik|Set up a ServiceNow instance connection with a Logik.ai instance]]
- [[set-up-external-connection-logik|Set up an external connection in CPQ]]
- [[enable-advanced-configurator|Enable the CPQ Configurator]]
- [[understand-the-commerce-logic-engine|The CPQ Configurator]]
- [[explore-servicenowcpq|CPQ Configurator]]
- [[explore-order-management|Order management]]
- [[quote-management|Quote Management]]
- [[rules_101|Rules]]
- [[opportunity-management|Opportunity Management]]
- [[product-catalog-managment|Product Catalog Management]]
- [[pricing-management|Pricing Management]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
