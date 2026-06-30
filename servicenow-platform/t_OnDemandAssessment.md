---
title: Generate an on-demand assessment
description: Use on-demand assessments to familiarize yourself with the basic assessment process and test your questionnaires using minimal configuration.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_OnDemandAssessment.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [On-demand assessments, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Generate an on-demand assessment

Use on-demand assessments to familiarize yourself with the basic assessment process and test your questionnaires using minimal configuration.

## Before you begin

Role required: assessment\_admin or admin

## About this task

Select the [[c_assessable-records|assessable records]] to evaluate, create the categories and questions, and then assign an assessment to a user in the system. Pre-configured stakeholders are not used for on-demand assessments.

## Procedure

1.  Create a [[c_MetricTypesAndAssessableRecords|metric type]] and set the **Schedule type** to **On demand** to allow for testing of your assessment configuration.

2.  Generate the assessable records for the metric type you created.

3.  Create the [[c_AssessmentMetrics|metric categories]] required to evaluate the assessable records selected.

4.  Create one or more assessment questions, or [metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_AssessmentMetrics.md), for each category.

5.  [[t_PublishAMetricType|Publish the assessment]].

6.  Perform an [[c_OnDemandAssessments|on-demand assessment]] to test your categories and metrics.

7.  Analyze the assessment ratings in an [[t_ViewAnAssessmentScorecard|assessment scorecard]] or [[r_AdministerDecisionMatrixes|decision matrix]].


**Parent Topic:**[On-demand assessments](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_OnDemandAssessments.md)

**Related topics**  


[[r_Assessments|Assessments]]

## Related

- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[t_PublishAMetricType|Publish a metric type]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[t_ViewAnAssessmentScorecard|View an assessment scorecard]]
- [[r_AdministerDecisionMatrixes|Decision matrixes]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
