---
title: Configure an assessment
description: You can create a new assessment on a selected assessable records to evaluate, score, and rank records from any table in the system. Then create a metric category and assessment metrics for the assessment, publish the assessment, and assign it to the selected users.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/configure-assessment.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Configure an assessment

You can create a new assessment on a selected [[c_assessable-records|assessable records]] to evaluate, score, and rank records from any table in the system. Then create a metric category and [[c_AssessmentMetrics|assessment metrics]] for the assessment, publish the assessment, and assign it to the selected users.

## Before you begin

Role required: admin, survey\_creator, or assessment\_admin

## Procedure

1.  Navigate to **All** &gt; **[[r_Assessments|Assessments]]** &gt; **Metric Definition** &gt; **Types**.

2.  Click **New**.

3.  On the Assessment Metric form, fill in the fields.

    For a description of the field values, see [[assessment-metric-form|Assessment Metric form]].

4.  Create a new assessment and assign it to the assessors.

    Do the following in the Assessment Metric form.

    1.  Add a condition: In the **Condition** tab, add a condition to define the assessable records on which the assessment is created.
    2.  Add decision matrix fields: In the **Decision Matrix** tab, add the required filter field to identify filter menu choices on decision matrices and scorecard averages for this type. For more information, see [[r_AdministerDecisionMatrixes|Decision matrixes]] .
    3.  Select the Assessors: In the **Assessors** tab, select the users to whom the assessment will be assigned.
    4.  Generate Assessable records: When you save the assessment and click **Generate Assessable Records**, an assessable record is created for each unique user of the user field.

        **Note:**

        -   You must generate the assessable records, each time you update the condition.
        -   You can generate the assessable records only after updating the condition.
        A new assessment is created. You must now create metric category and add assessment metrics to each metric category. Then publish the assessment and assign the assessment to the selected users.

    5.  Create a metric category: To create a metric category, do the following:
        1.  Open the assessment you just created and click **New** in the **Metric Categories** tab. Fill the form.

            For more information about form fields, see [[metric-category-form|Metric Category form]]form.

            **Tip:** To know how to create metric category alternatively, see [[t_CreateACategoryAR|Create a category for assessable records]].

        2.  Open a metric category, add a condition, and click **Assessable records** tab. The assessable records appear based on the selection made in the metric category form.
        3.  Open a metric category, click **Assessment Metric** tab to add the questions. Click **New**.

            For more information about form fields, see [[assessment-metric-category-form|Assessment Metric form for a category]].

            **Tip:** To know how to create assessment metric category alternatively, see [[t_CreateAMetric|Create an assessment metric for a category]].

    6.  Click **Publish**, to publish the assessment. For more information, see [[t_PublishAMetricType|Publish a metric type]].
    7.  Assign the Assessment to the required users. Do the following:
        1.  For an [[c_OnDemandAssessments|on-demand Assessments]], click either the **Assign Assessment** or **Assign to Assessors** link to assign the assessment. For more information, see [[t_GenOnDemandAssessMultAssessRec|Generate an on-demand assessment for multiple assessable records]].
        2.  For a scheduled Assessment, click the **Generate Assessments ** link to trigger the scheduled job immediately. For more information, see [[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]].

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[assessment-metric-form|Assessment Metric form]]
- [[r_AdministerDecisionMatrixes|Decision matrixes]]
- [[metric-category-form|Metric Category form]]
- [[t_CreateACategoryAR|Create a category for assessable records]]
- [[assessment-metric-category-form|Assessment Metric form for a category]]
- [[t_CreateAMetric|Create an assessment metric for a category]]
- [[t_PublishAMetricType|Publish a metric type]]
- [[t_GenOnDemandAssessMultAssessRec|Generate an on-demand assessment for multiple assessable records]]
- [[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[c_assessable-records|Assessable records]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[r_Assessments|Assessments]]
- [[c_OnDemandAssessments|On-demand assessments]]
