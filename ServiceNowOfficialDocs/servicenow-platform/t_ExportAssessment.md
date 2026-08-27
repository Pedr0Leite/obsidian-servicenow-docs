---
title: Export an assessment
description: You can share assessments between ServiceNow instances by exporting an assessment and then importing the assessment on another instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_ExportAssessment.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Metric types and assessable records, Create an assessment metric for a category, Assessment metrics, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# Export an assessment

You can share [[r_Assessments|assessments]] between ServiceNow instances by exporting an assessment and then importing the assessment on another instance.

## Before you begin

Role required: assessment\_admin or admin

**Note:** Update sets are available in the Helsinki release and should be used to move data from one instance to another. For information about update sets, see [System update sets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/system-update-sets.md).

## About this task

**Note:** The system exports a single XML file that does not contain result data.

The XML file contains a metric type `[asmt_metric_type]` and the following records that are associated with the type:

-   [[c_assessable-records|Assessable records]] `[asmt_assessable_record]`
-   Metric categories `[asmt_metric_category]`
-   Metrics `[asmt_metric]`
-   Metric definitions `[asmt_metric_definition]`
-   Category users `[asmt_m2m_category_user]`
-   Stakeholders `[asmt_m2m_stakeholder]`
-   [[r_AdministerDecisionMatrixes|Decision matrixes]] `[asmt_decision_matrix]`, `[asmt_m2m_xcategory_matrix]`, and `[asmt_m2m_ycategory_matrix]`

## Procedure

1.  Navigate to **All** &gt; **Assessments** &gt; **Metric Definition** &gt; **Types**.

2.  Right-click the record and select **Export Assessment**.

3.  Save the XML file.


**Parent Topic:**[[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]

**Related topics**  


[[t_ImportAssessment|Import an assessment]]

[Metric types and assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_MetricTypesAndAssessableRecords.md)

## Related

- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[t_ImportAssessment|Import an assessment]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
- [[r_AdministerDecisionMatrixes|Decision matrixes]]
