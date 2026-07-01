---
title: Assessment metric categories
description: In the Assessments application, a metric category represents a theme for evaluating assessable records in a given metric type.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_AssessmentMetricCategories.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [View an assessment metric category, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Assessment metric categories

In the [[r_Assessments|Assessments]] application, a metric category represents a theme for evaluating [[c_assessable-records|assessable records]] in a given metric type.

Each category has a numeric weight value to indicate its importance relative to other categories. Within a category, records called metrics are the traits or values used to evaluate assessable records. For example, there are many categories within the **Vendor** metric type, including Support Rating, which contains metrics that measure the quality of vendors' customer support services. Assessable records must be associated to categories to be eligible for evaluation. Assessment administrators create categories and manage which assessable records each category is associated to.

## Weight categories and metrics

When you create a metric category or metric, you must specify a weight, a numeric value that indicates the importance of the category or metric relative to other categories and metrics.

The greater the weight value, the more important the item is. The system uses weight values in [[r_AssessmentResults|assessment result]] calculations. Consider these recommendations when choosing weight values.

-   Determine a weighting scale and use it consistently. In general, use a scale with a small numeric range. A standard 1-10 scale is usually appropriate, where 1 is least and 10 most important. Understand that increasing the maximum value of a weighting scale impacts all related result calculations.
-   Use the same weighting scale for metric categories and metrics. Though there is no limitation, consider using the same or very similar weighting scales for both categories and metrics to make it easier to remember which values to use. A scale of 1-10 is an effective and simple weighting system, but may not be suitable for all organizations.

**Note:** If you do not want to use weighting, set the same weight value for all categories and metrics. The default weight value is 10.

-   **[[t_CreateACategoryAR|Create a category for assessable records]]**  
After you create a metric type and generate assessable records, create categories for the themes you are interested in using to evaluate the assessable records.
-   **[[r_ManageAssessablRecordAssociation|Assessable record associations]]**  
Only the assessable records associated to a category can be evaluated using metrics in that category. Manage which assessable records you evaluate for each category by creating and removing the associations.
-   **[[t_DeleteACategory|Delete a category]]**  
When you delete a category, the system also deletes the associated [[r_CategoryUsersAndStakeholders|category users and stakeholders]].

**Parent Topic:**[[t_CreateAnAssessmentCategory|View an assessment metric category]]

**Related topics**  


[[c_AssessmentMetrics|Assessment metrics]]

[[t_CreateAMetric|Create an assessment metric for a category]]

[[t_CreateAMetricDefinition|Create an assessment metric definition]]

[[r_MetricTemplates|Metric templates]]

[[t_UpdAMetrMinMaxValToMatchATmplate|Update a metric minimum and maximum value to match a template]]

## Related

- [[r_AssessmentResults|Assessment results]]
- [[t_CreateACategoryAR|Create a category for assessable records]]
- [[r_ManageAssessablRecordAssociation|Assessable record associations]]
- [[t_DeleteACategory|Delete a category]]
- [[t_CreateAnAssessmentCategory|View an assessment metric category]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[t_CreateAMetric|Create an assessment metric for a category]]
- [[t_CreateAMetricDefinition|Create an assessment metric definition]]
- [[r_MetricTemplates|Metric templates]]
- [[t_UpdAMetrMinMaxValToMatchATmplate|Update a metric minimum and maximum value to match a template]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
