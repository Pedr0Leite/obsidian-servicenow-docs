---
title: Filter data visualizations with the condition builder
description: Use the condition builder to help you create a custom filter for a visualization based on table data. You can save filters as predefined conditions for other visualizations based on the same table.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/filter-dv-condition-builder.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, Data visualizations, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-task
---

# Filter data visualizations with the condition builder

Use the condition builder to help you create a custom filter for a visualization based on table data. You can save filters as predefined conditions for other visualizations based on the same table.

## Before you begin

Role required: Anyone with access to data can create a visualization of that data on any dashboard that they can edit. Users with the itil, report\_user, admin, or viz\_creator role can create a visualization in the Visualization Designer. When you create a visualization in the Visualization Designer, it is saved to the Library. For more information on access, see [Report\_view access control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/reporting/report-view-access-control.md) and [[platform-analytics-roles|Platform Analytics roles]].

## Procedure

1.  Navigate to **All** &gt; **[[c_performanceAnalyticsAndReporting|Platform Analytics]]** &gt; **Library** &gt; **Data Visualizations**, or open an inline dashboard and select **Edit**.

2.  Select **Create data visualization**.

3.  Choose the visualization type that you want to create.

4.  Select **Add data source** and choose a table.

5.  Select a predefined condition.

6.  Expand **+ Add a custom filter**.

7.  On the Conditions tab, create a condition with a field, an operator, and a value on the table data source.

    -   The Field is any available field in the source table.
    -   Available operators are based on the field. For example, **Assigned to** is a string field and the operators refer to strings: is, is not, contains, starts with, for example. The operators for Date fields, such as Assigned and Created, refer to dates: before, after, and relative, for example.
    -   The Value options are dependent on the field and the operator. For example **Assigned to** might be a single user \(operator=`is`, operator=`is (dynamic)` when the Value=`Me`\) or several \(operator=`begins with` or operator=`is (dynamic)` when value =`One of My Approvals`\).
8.  Add more conditions with the **or** and **and** logical operators.

9.  On the Related list conditions tab, include a relationship with another table filter.

    1.  Select an operator and a value.

        The operator and value determine a number of records on the related table that should apply to the original filter.

    2.  Select the table that the operator and value apply to.

    3.  Select the other field and operator.

10. Select **Run** to see the list of records from the table that match the conditions you specified.

11. Select **Save as predefined condition**.

    Predefined conditions are available filters for other visualizations based on the same table.

12. Select **Add this source** to use the filtered source for your visualization.


-   **[[create-dynamic-js-filter-pae|Add a dynamic JavaScript filter]]**  
Add a dynamic JavaScript statement for evaluation as part of a report visualization's filter criteria.
-   **[[filter-dv-condition-builder-rel-list|Related list conditions example]]**  
Related list conditions enable you to include a relationship with another table in the filter.

**Parent Topic:**[[configure-data-visualizations|Configure data visualizations]]

## Related

- [[platform-analytics-roles|Platform Analytics roles]]
- [[create-dynamic-js-filter-pae|Add a dynamic JavaScript filter]]
- [[filter-dv-condition-builder-rel-list|Related list conditions example]]
- [[configure-data-visualizations|Configure data visualizations]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
