---
title: Making self-service order and invoice case management available on the Business Portal
description: Install the necessary applications based on the self-service order and invoice case management options that you want to offer customers on the Business Portal.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/activating-self-service-order-case-management-business-portal.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Business Portal, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Making self-service order and invoice case management available on the Business Portal

Install the necessary applications based on the self-service order and invoice case management options that you want to offer customers on the Business Portal.

**Note:** For information about activating the Business Portal itself, see [[order-management-enable-business-portal|Enable the Business Portal]]

## Case management applications

The following apps must be installed from the ServiceNow Store to enable your customers to create and view order cases from the Business Portal:

-   Order Case Self Service \[sn\_ord\_case\_ss\]
-   Order Case Playbook \[sn\_ord\_case\_pb\]

These plugins have the following dependencies:

-   Customer Service Portal \[com.snc.customer\_service\_portal\]
-   [[order-operations-landing|Order Operations]] Case Management \[sn\_order\_case\]
-   Playbooks for Customer Service Management \[sn\_csm\_playbook\]

If your customers need to only view order cases in the Business Portal, you don't need to install the Order Case Playbook \[sn\_ord\_case\_pb\] and Playbooks for Customer Service Management \[sn\_csm\_playbook\] plugins.

## Invoice and invoice case management applications

The following apps must be installed from the ServiceNow Store to enable your customers to manage invoices and invoice cases from the Business Portal:

-   Invoice Self-Service \[sn\_invoice\_ss\]
-   Invoice Case Self-Service \[sn\_invoice\_case\_ss\]
-   Invoice Case Playbook \[sn\_inv\_case\_pb\]

These plugins have the following dependencies:

-   Customer Service Portal \[com.snc.customer\_service\_portal\]
-   Invoice Operations Case Management \[sn\_csm\_invoice\]
-   Playbooks for Customer Service Management \[sn\_csm\_playbook\]

If your customers only need to view invoice cases in the Business Portal, you don’t need to install the Invoice Case Playbook \[com.sn\_inv\_case\_pb\] and the Playbooks for Customer Service Management \[sn\_csm\_playbook\] plugins.

**Related topics**  


[[som-self-service-business-portal|Customer self-service for Sales Customer Relationship Management]]

[[order-mgt-business-portal|Customer self-service using the Business Portal]]

## Related

- [[order-management-enable-business-portal|Enable the Business Portal]]
- [[som-self-service-business-portal|Customer self-service for Sales Customer Relationship Management]]
- [[order-mgt-business-portal|Customer self-service using the Business Portal]]
- [[order-operations-landing|Order operations]]
