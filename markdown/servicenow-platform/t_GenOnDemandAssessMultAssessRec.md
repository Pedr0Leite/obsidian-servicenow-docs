---
title: Generate an on-demand assessment for multiple assessable records
description: When you generate an on-demand assessment from the Assessment Metric Type form, the resulting assessment contains questions from all categories associated to any assessable records for the metric type.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_GenOnDemandAssessMultAssessRec.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [On-demand assessments, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Generate an on-demand assessment for multiple assessable records

When you [[t_OnDemandAssessment|generate an on-demand assessment]] from the Assessment Metric Type form, the resulting assessment contains questions from all categories associated to any [[c_assessable-records|assessable records]] for the metric type.

## Before you begin

Role required: assessment\_admin or admin

Publish the assessment.

## About this task

For example, if there are 15 assessable records associated to at least one category with [[c_AssessmentMetrics|assessment metrics]], the assessment contains questions for all 15 assessable records.

## Procedure

1.  Navigate to **All** &gt; **[[r_Assessments|Assessments]]** &gt; **Metric Definition** &gt; **Types**.

2.  Open a metric type that has the **On demand** schedule type.

3.  To assign the assessment to users configured in the **Assessors** tab of the assessment, and other specified users, perform these steps.

    1.  On the Assessment Metric Type form, click **Assign Assessment**.

    2.  Select a user from the Recent Assessors list or select a different user.

    3.  Click **OK**.

4.  To assign the assessment to users configured in the **Assessors** tab of the assessment, click **Assign to Assessors**.


## Result

The system generates an assessment instance assigned to the selected users.

**Parent Topic:**[[c_OnDemandAssessments|On-demand assessments]]

**Related topics**  


[[c_AssessmentGeneration|Assessment generation]]

[[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]]

[[c_AssessmentGroups|Assessment groups]]

[[t_CleanUpAssessmentData|Clean up assessment data]]

## Related

- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]]
- [[c_AssessmentGroups|Assessment groups]]
- [[t_CleanUpAssessmentData|Clean up assessment data]]
- [[t_OnDemandAssessment|Generate an on-demand assessment]]
- [[c_assessable-records|Assessable records]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[r_Assessments|Assessments]]
