---
title: Delete a metric type
description: Deleting a metric type entails deleting many related records.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_DeleteAMetricType.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Metric types and assessable records, Create an assessment metric for a category, Assessment metrics, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Delete a metric type

Deleting a metric type entails deleting many related records.

## Before you begin

Role required: assessment\_admin or admin

## About this task

You must delete some of these records manually before deleting the type, while the system deletes others automatically with the type.

## Procedure

1.  Delete the records associated with the type to delete:

    -   [[r_AssessmentResults|Assessment results]] \(metric and [[r_CategoryResults|category results]]\)
    -   [[c_AssessmentInstances|Assessment instance]] \(questions and assessment instances, in that order\)
    -   [[c_AssessmentGroups|Assessment groups]]
2.  Delete the type.

    A confirmation dialog box appears and alerts you that certain records associated with the type will also be deleted.

3.  Click **OK** to delete the type and these related records:

    -   Scheduled job for [[c_AssessmentGeneration|assessment generation]]
    -   Business rule for assessable record generation
    -   [[c_assessable-records|Assessable records]]
    -   Metric categories
    -   Category users
    -   Stakeholders
    -   Metrics
    -   Metric definitions
    -   [[r_AdministerDecisionMatrixes|Decision matrixes]]

**Parent Topic:**[[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]

**Related topics**  


[Metric types and assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_MetricTypesAndAssessableRecords.md)

## Related

- [[r_AssessmentResults|Assessment results]]
- [[c_AssessmentInstances|Assessment instances]]
- [[c_AssessmentGroups|Assessment groups]]
- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[r_CategoryResults|Category results]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[c_assessable-records|Assessable records]]
- [[r_AdministerDecisionMatrixes|Decision matrixes]]
