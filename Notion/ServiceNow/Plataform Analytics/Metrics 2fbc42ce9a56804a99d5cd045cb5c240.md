---
aliases:
  - "Plataform Analytics – Metrics"
tags:
  - performance-analytics
  - metrics
  - business-rules
  - non-task-tables
  - kpi
---

# Metrics

# **Unlock Powerful Metrics for Non-Task Tables with ServiceNow**

# **Introduction**

In the dynamic world of ServiceNow, metrics play a crucial role in monitoring and improving system performance, usage, and business processes. Traditionally, these metrics are limited to task-extended tables. However, in this article, we will explore how to extend these powerful capabilities to non-task tables, unlocking new potentials for your ServiceNow environment. This guide is designed for ServiceNow developers and advocates who seek to enhance their platform's functionality through advanced metric tracking.

# **Understanding Metrics in ServiceNow**

Metrics in ServiceNow are measures of specific aspects of system performance, usage, or business processes. They help in:

- Tracking and analyzing data over time
- Identifying trends
- Monitoring Key Performance Indicators (KPIs)
- Driving process improvements

For example, you might want to track the response time of incidents or the duration of a change request. These metrics are typically applied to task-extended tables, such as incidents, problems, or changes. But what if you need to track metrics on non-task tables? Let's dive into how you can achieve this.

[https://youtu.be/bwIQUkU3Dgo](https://youtu.be/bwIQUkU3Dgo)

# **Extending Metrics to Non-Task Tables**

### **Use Case: Tracking State Changes in a Sales Approval Table**

Consider a scenario where you want to track state changes in a sales approval table. Here’s a step-by-step guide to extend metric capabilities to this non-task table.

### **Step 1: Define a Metric**

**1. Navigate to Metric Definitions:**

- Go to Metrics > Metric Definitions in ServiceNow.
- Create a new metric definition for your non-task table, in this case, the `approval` table.

**2. Configure the Metric:**

- Name the metric appropriately (e.g., `Approval State Change`).
- Select the field you want to track (e.g., `State`).
- Set the metric type to `Field Duration` to measure the time it takes for the state to change.

### **Step 2: Create and Test the Metric Instance**

1. Create a Metric Instance:

- Open any record from the `approval` table.
- Change the state of the record to simulate the workflow (e.g., from `Requested` to `Approved`, then to `Cancelled`).

2. Verify the Metric:

- Navigate to Metrics > Metric Instances.
- Search for the metric you created and verify if it captured the state change

### **Step 3: Modify the Business Rule**

1. Identify the Limitation:

- The default metric calculation is limited to task tables due to the existing business rule configuration.

2. Create a New Business Rule:

- Go to System Definition > Business Rules.
- Clone the existing `Metric Events` business rule.
- Modify the new business rule to apply to your non-task table.

3. Configure the New Business Rule:

- Set the table to your non-task table (e.g., `approval`).
- Ensure the business rule triggers on the appropriate events (e.g., `Insert`, `Update`).

# **Best Practices for Implementing Metrics**

- Avoid Direct Modifications: Do not change out-of-the-box definitions. Always create custom configurations to maintain system integrity.
- Consistent Naming Conventions: Use clear and consistent names for your metrics and business rules to avoid confusion.
- Regular Monitoring: Periodically check your metric instances to ensure they are capturing data correctly.
- Documentation: Keep detailed documentation of your custom metrics and business rules for future reference and troubleshooting.

# **Conclusion**

Extending metrics to non-task tables in ServiceNow opens up new possibilities for tracking and improving your business processes. By following the steps outlined in this article, you can effectively monitor state changes and other critical data points in non-task tables, leveraging the full power of ServiceNow's metrics. Implement these practices to enhance your platform’s functionality and drive better decision-making.

## Related

- [[Plataform Analytics]]
- [[Knowledge Base Articles – Metrics]]
- [[SLA]]