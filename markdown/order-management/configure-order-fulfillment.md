---
title: Configure order fulfillment
description: Order fulfillment is the process for fulfilling customer orders by using Workflow Studio.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configure-order-fulfillment.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Order management, Configure, Sales Customer Relationship Management]
---

# Configure order fulfillment

[[reviewing-orchestration-plans-order-fulfillment|Order fulfillment]] is the process for fulfilling customer orders by using Workflow Studio.

Order fulfillment, also referred as [[order-orchestration|order orchestration]], defines how to coordinate the fulfillment of orders.

You can define the order fulfillment processes that you require and then configure them by performing the tasks in the following table.

|Task|Description|
|----|-----------|
|Configure subflows for order fulfillment|Subflows define the task flow for fulfillment agents to fulfill customer orders. You can copy a subflow from the base system and change your business needs. For more information on configuring subflows, see [Building Subflows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/subflows.md).|
|Configure decision tables for order fulfillment|Decision tables define the conditions for triggering the order fulfillment subflow. The Order Management for Telecommunications, Media, and Technology application uses the Order fulfillment Policy decision table. For more information on configuring decision tables, see [Decision tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/decision-table.md).|
|Configure order assignment [[rules_101|rules]] to route tasks to agents, based on their skill sets|For more information on assignment rules, see [Create an assignment rule](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_AssignmentModuleRule.md).|

-   **[[order-mgt-flow-actions-fulfillment-subflows|Flow actions for fulfillment subflow definition]]**  
If you define your own fulfillment subflows in Workflow Studio, you can use the standard flow actions that are available in the ServiceNow AI Platform. Each action deals with different aspects of the fulfillment or inventory maintenance that provides some consistency in retrieving and updating data.
-   **[[activate-fsm-csm-integration|Integrate with Field Service Management]]**  
Customer Service Management provides an integration with the Field Service Management application. This integration enables you to view work order and work order task information from a case.
-   **[[configure-customer-product-data-management|Configure customer product data management]]**  
Learn how to use the sn\_ind\_tmt\_orm.enable\_prod\_invt\_for\_order\_management system property to either create sold products or product inventory records after an order is completed and fulfilled.

**Parent Topic:**[[order-mgt-configuring|Configuring Order Management]]

**Related topics**  


[[explore-order-management|Order management]]

[[using-order-management|Using Order Management]]

## Related

- [[order-mgt-flow-actions-fulfillment-subflows|Flow actions for fulfillment subflow definition]]
- [[activate-fsm-csm-integration|Integrate with Field Service Management]]
- [[configure-customer-product-data-management|Configure customer product data management]]
- [[order-mgt-configuring|Configuring Order Management]]
- [[explore-order-management|Order management]]
- [[using-order-management|Using Order Management]]
- [[reviewing-orchestration-plans-order-fulfillment|Order fulfillment]]
- [[order-orchestration|Order orchestration]]
- [[rules_101|Rules]]
