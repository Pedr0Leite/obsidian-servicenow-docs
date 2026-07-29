---
title: View an assessment metric category
description: View assessment metric categories that are used with assessment metric types and assessment metrics in generating the bubble charts on the Demand Workbench. The bubble charts help the demand managers to assess the demands visually.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_CreateAnAssessmentCategory.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# View an assessment metric category

View assessment metric categories that are used with assessment metric types and [[c_AssessmentMetrics|assessment metrics]] in generating the bubble charts on the Demand Workbench. The bubble charts help the demand managers to assess the demands visually.

## Before you begin

Role required: it\_pps\_admin

## About this task

The Demand Management application comes with an assessment metric type named **Demand**, five default assessment metric categories, and assessment metrics.

## Procedure

1.  Navigate to **All** &gt; **Project Administration** &gt; **Settings** &gt; **[[r_Assessments|Assessments]] Metric Categories**.

2.  Open an assessment metric category to review it.

    The following default assessment metric categories are available with the Demand Management.

    |Assessment metric category|Data source|Description|
    |--------------------------|-----------|-----------|
    |**Size**|**T-Shirt size** field on the [Demand](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/t_CreatingDemands.md) form.|Assesses demand size relative to the size of other demands.|
    |**Strategic Alignment**|[[t_ViewACategoryResult|View an assessment category result]] field in the assessment category result for the Strategic Alignment metric category.|Assesses how closely the demand aligns with strategic goals of the organization compared to other demands.|
    |**Risk**|**Rating** field in the assessment category result for the Risk metric category.|Assesses demand risks compared to other demands.|
    |**ROI**|**Impact** and **Financial return** fields on the Demand form.|Assesses demand return on investment compared to other demands.|
    |**Cost**|**Labor costs**, **Capital expense**, and **Operating expense** fields on the Demand form.|Assesses demand cost compared to other demands.|


-   **[[c_AssessmentMetricCategories|Assessment metric categories]]**  
In the Assessments application, a metric category represents a theme for evaluating [[c_assessable-records|assessable records]] in a given metric type.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[t_ViewACategoryResult|View an assessment category result]]
- [[c_AssessmentMetricCategories|Assessment metric categories]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
