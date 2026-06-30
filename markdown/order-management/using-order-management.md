---
title: Using Order Management
description: ServiceNow Order Management provides a centralized platform to create and manage customer and service orders throughout their entire life cycle. It automates the complex process from order capture and enrichment through to fulfillment and closure, promoting seamless coordination between sales, operations, and technical teams.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/using-order-management.html
release: australia
topic_type: concept
last_updated: "2025-09-02"
reading_time_minutes: 6
keywords: [use]
breadcrumb: [Use, Sales Customer Relationship Management]
---

# Using Order Management

ServiceNow [[explore-order-management|Order Management]] provides a centralized platform to create and manage customer and service orders throughout their entire life cycle. It automates the complex process from order capture and enrichment through to fulfillment and closure, promoting seamless coordination between sales, operations, and technical teams.

## Overview of the order life cycle

Access the Order Management capabilities from the CSM/FSM Configurable Workspace to capture and manage orders. A typical order life cycle is a structured, multiphase process that guides a customer's request from initial submission to final delivery and fulfillment.

1.  [[som-create-product-order|Creating orders]]

    The order life cycle begins when a customer's request is submitted. This could be from a salesperson creating a quote that's then converted to an order, a sales agent directly capturing an order through the workspace, a customer placing an order online through the Business Portal, or an order being created via an API from another system. This phase focuses on getting all the customer-facing details, including what was ordered, pricing, and customer information, into the system.

2.  [[order-enrichment|Enriching orders]]

    If order enrichment subflow is configured for a product offering, then order enrichment tasks are created. The fulfillment agent captures additional details required to fulfill the order. This phase prevents errors from propagating further into the process. Not all orders need enrichment.

3.  [[approving-rejecting-orders-som|Approving or rejecting orders]]

    The fulfillment manager reviews the order, order lines, and pricing details and approves or rejects the order.

4.  \[System\] [[order-mgt-order-decomposition|Order decomposition]]

    This is a critical step for businesses selling complex products or services. The single, high-level order is automatically broken down into smaller, actionable service orders or fulfillment tasks based on how the process admin has configured order decomposition. For example, a customer's order for a telecom bundle would be decomposed into separate tasks for IT provisioning, a field technician, and the billing department. This process translates the customer's request into a detailed operational plan.

    View product, service, or resource orders for tracking the fulfillment process, verifying that all required tasks and suborders are created correctly, and confirming that the order progresses through its life cycle as expected. For more information, see [[view-domain-orders|View domain orders]].

5.  \[System\] [[order-orchestration|Order orchestration]]

    The system orchestrates the fulfillment of each individual product, service, and resource orders. Tasks are automatically created and assigned to the correct teams and systems, and the application tracks their progress.

    Work orders are created if you have an integration with Field Service Management.

6.  \(Optional\) [[inflight-order-change-mgt-overview|Inflight order changes]]

    Inflight order changes come into the picture after an order has been submitted and is actively being processed, but before it has been completely fulfilled and closed. These changes are a form of MACD orders \([[Modify|Modify]], Adds, Changes, and Deletes\) that occur during the fulfillment life cycle.

7.  [[reviewing-orchestration-plans-order-fulfillment|Order fulfillment]]

    Fulfillment agents complete order tasks assigned to them. Fulfillment managers monitor the fulfillment process and manage issues using features such as [[jeopardy-management|Jeopardy Management]] to alert teams about potential delays and Fallout Management to handle errors.

    As each fulfillment task is completed, the service or product is activated or delivered to the customer. This can involve anything from a physical delivery to the electronic provisioning of a digital service. Once all products and services are activated and delivered, the order is officially closed. The system updates the order status to reflect completion and updates creates sold product records.

8.  [[fallout-management-overview|Managing order fallouts]]

    Manage failures that may take place during order fulfillment due to errors and exceptions. These exceptions include incorrect data, connectivity problems, inadequate inventory supply, or other unforeseen issues.

9.  [[monitoring-jeopardy-management|Monitoring order jeopardy]]

    Proactively monitor and mitigate order delivery delays, dynamically track task progression to predict potential order fulfillment delays, and alert service delivery teams when fulfillment plans exceed or are expected to exceed committed completion times by monitoring the jeopardy status.

10. [[managing-orders|Managing post-fulfillment order changes]]

    Order agents can make the following post-sale changes to the orders after an initial order has been placed and fulfilled:

    -   Change
    -   Disconnect
    -   [[Suspend|Suspend]]
    -   [[Resume|Resume]]

**Related topics**  


[[order-mgt-configuring|Configuring Order Management]]

[[som-order-types|Order types in Sales Customer Relationship Management]]

[[order-mgt-customer-order-types|Action types for customer and service orders]]

[[order-lifecycle-states|Order life cycle states]]

[[order-capture-methods-som|Methods of creating orders in Sales Customer Relationship Management]]

[[reviewing-customer-accounts|Reviewing customer or partner accounts]]

[[now-assist-order-management|Now Assist for Order Management]]

[[order-mgt-reference|Order Management reference]]

## Related

- [[som-create-product-order|Create an order in Order Management]]
- [[order-enrichment|Enriching orders in Order Management]]
- [[approving-rejecting-orders-som|Approving or rejecting orders]]
- [[order-mgt-order-decomposition|Order decomposition]]
- [[view-domain-orders|View domain orders]]
- [[order-orchestration|Order orchestration]]
- [[inflight-order-change-mgt-overview|Managing inflight order changes and cancellation requests]]
- [[reviewing-orchestration-plans-order-fulfillment|Order fulfillment]]
- [[fallout-management-overview|Managing order fallout]]
- [[monitoring-jeopardy-management|Monitoring order jeopardy]]
- [[managing-orders|Managing post-fulfillment order changes]]
- [[order-mgt-configuring|Configuring Order Management]]
- [[som-order-types|Order types in Sales Customer Relationship Management]]
- [[order-mgt-customer-order-types|Action types for customer and service orders]]
- [[order-lifecycle-states|Order life cycle states]]
- [[order-capture-methods-som|Methods of creating orders in Sales Customer Relationship Management]]
- [[reviewing-customer-accounts|Reviewing customer or partner accounts]]
- [[now-assist-order-management|Now Assist for Order Management]]
- [[order-mgt-reference|Order Management reference]]
- [[explore-order-management|Order management]]
- [[Modify|Modify]]
- [[jeopardy-management|Jeopardy Management]]
- [[Suspend|Suspend]]
- [[Resume|Resume]]
