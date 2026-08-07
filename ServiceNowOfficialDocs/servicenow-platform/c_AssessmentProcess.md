---
title: Assessment administrator tasks
description: Before you create assessments, assign the assessment\_admin role to the appropriate users in your organization and determine your objectives for the assessment.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_AssessmentProcess.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 8
breadcrumb: [Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Assessment administrator tasks

Before you create [[r_Assessments|assessments]], assign the assessment\_admin role to the appropriate users in your organization and determine your objectives for the assessment.

Decide which sets of records in the system to assess, which themes you are interested in, and which traits to measure. Consider your organization's options for obtaining the data to compare. If you intend to use [[c_AssessmentQuestionnaires|assessment questionnaires]], consider which people can answer the questions.

## Assessment terminology

Assessment admins use several terms when working with assessments.

<table id="table_eg1_3yr_np"><thead><tr><th>

Term

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Metric type

</td><td>

A metric type defines a set of records to evaluate, such as vendors, projects, or employees.

</td></tr><tr><td>

Assessable record

</td><td>

An assessable record links a record to evaluate, such as the company record for Amazon or the user record for a sales representative, to a metric type, such as vendors or employees. You define sets of [[c_assessable-records|assessable records]] when you create metric types.

</td></tr><tr><td>

Metric category

</td><td>

A metric category represents a theme for evaluating assessable records. Categories contain one or more individual metrics, which define specific traits or values that comprise the theme. Examples of categories include overall vendor performance or quality of delivery services. You can also set filter conditions that control which assessable records to evaluate for the metrics in a category.

</td></tr><tr><td>

Metric

</td><td>

A metric is a trait or value used to evaluate assessable records. A metric can measure subjective values in an assessment questionnaire, or gather objective values in a database query run by a script. Examples of metrics include perceived courtesy of sales representatives or number of incidents per vendor.

</td></tr><tr><td>

Category user

</td><td>

A category user is a person who knows about a specific category. One person can be a category user for multiple categories. Examples of category users include a vendor manager who oversees all purchasing operations or a supervisor of a sales team.

</td></tr><tr><td>

Stakeholder

</td><td>

A stakeholder is a category user who knows about a specific assessable record. Examples of stakeholders include a vendor manager who coordinates purchases from Amazon or a supervisor of a sales team who manages a specific employee.

</td></tr><tr><td>

Assessment instance

</td><td>

An assessment instance represents one assessment questionnaire assigned to one user. The system generates a new assessment instance for each assigned user when:-   The assessment generation scheduled job runs.
-   An assessment administrator creates an on-demand assessment.

</td></tr><tr><td>

Scorecard

</td><td>

A scorecard provides a visual illustration of an assessable record's performance, based on [[r_AssessmentResults|assessment results]]. Use scorecards to view a variety of data summaries for one assessable record and to compare the ratings with other assessable records.

</td></tr><tr><td>

Decision matrix

</td><td>

A decision matrix is a graph with two axes that plots the assessment results for multiple assessable records. Use [[r_AdministerDecisionMatrixes|decision matrixes]] to determine the relative standing of assessable records in selected categories.

</td></tr><tr><td>

Bubble chart

</td><td>

A bubble chart is a graph with three axes that plots the assessment results for multiple assessable records. Use bubble charts to determine the relative standing of assessable records in selected categories, with an emphasis on one category.

</td></tr></tbody>
</table>## Assessment roles

The Assessments application requires certain roles to perform assessment tasks. No role is required to take assessment questionnaires that are assigned to you.

<table id="table_ivw_1zk_v4"><thead><tr><th>

Role Title

</th><th>

Role Name

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Assessment administrator

</td><td>

assessment\_admin

</td><td>

Assessment administrators set up assessments. They know which records to evaluate, the criteria on which to evaluate the records, and who to assign assessments to.**Note:** By default, users with the assessment\_admin role have limited system rights and might not have access to all source records to assess. When planning assessments, grant additional roles to assessment administrators as needed. For example, to create and manage vendor assessments, the assessment administrator must also have the vendor\_manager role, which grants access to the Company table and other relevant tables.

</td></tr><tr><td>

ITIL user

</td><td>

[Base system roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_BaseSystemRoles.md)

</td><td>

ITIL users perform basic technician operations in the system. In the Assessments application, they have read access to the Assessable Record table.

</td></tr><tr><td>

Administrator

</td><td>

[Base system roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_BaseSystemRoles.md)

</td><td>

Administrators have access to all aspects of the assessment process. Only administrators can set up assessment schedules.

</td></tr></tbody>
</table>## Assessment methods

The available methods are **Assessment**, for non-scripted metrics, and **Script**, for scripted metrics. Each method serves a different function and can be used with certain data types.

Use the **Method** field to specify how to use the metric.

## Assessment method

Metrics with the Method set to Assessment are called non-scripted metrics. Use each non-scripted metric to define a question for assessment questionnaires. Non-scripted metrics are useful if you want to obtain subjective data like personal opinions.

You can use the Assessment method with these **Data type** values:

-   [[attachment|Attachment]]
-   Checkbox
-   Choice
-   Date
-   Date/Time
-   Likert Scale
-   Number
-   Percentage
-   String
-   Template
-   [[yes-no|Yes/No]]

## Script method

Metrics with the Method set to Script are called scripted metrics. Use each scripted metric to define a custom script for database queries. Scripted metrics are useful if your system contains reliable data for the traits you want to evaluate.

You can use the Script method with these **Data type** values:

-   Duration
-   Number
-   Percentage

Use the Script field to write JavaScript code. By default, the field contains information about available variables and an example, which you can use as the basis of your script or replace entirely:\[Omitted image "asmt\_metric\_form\_script.png"\] Alt text: metric form script field

You must use the following variables in your script:

-   *primary*: Input variable used to access the sys\_id of the record being assessed.
-   *string\_result*: Output variable that contains the display string value for this metric
-   *actual\_result*: Output variable that contains the actual value for this metric. The system uses this variable to populate the Actual value field on the [[r_MetricResultFieldNames|Metric Result form]]. For each *actual\_result,* you must specify a corresponding **scaled\_result** value.
-   *scaled\_result*: Output variable that contains a numerical scaled value to represent an actual value. The system uses this variable to populate the **Scaled value** field on the **Metric Result** form. Ensure the scaled values you specify are between or equal to the **Min** and **Max** values for the metric. The **Scale definition** field determines how the system uses the scaled value. A scale definition of **Low** means smaller numbers are better, such as for a metric that measures the number of incidents for a vendor. **High** means larger numbers are better, such as for a metric that measures user satisfaction on a scale of one to five.

## Script example

The metric Number of active devices uses the script pictured below. The *primary* variable is used to find CIs that are associated to the vendor record being assessed. The script retrieves the actual\_result, the number of CIs associated to the vendor, then calculates the correct scaled\_result. The script uses a series of scaled values, from the **Min** to the **Max** value, to represent actual values. Because the **Scale definition** is set to **High**, the greatest scaled values are best, meaning a vendor associated to the most CIs scores highest. The system stores the actual and scaled values in a metric result record for the vendor.

\[Omitted image "ScriptedMetricExample.png"\] Alt text: Scripted metric example

-   **[[configure-assessment|Configure an assessment]]**  
You can create a new assessment on a selected assessable records to evaluate, score, and rank records from any table in the system. Then create a metric category and assessment metrics for the assessment, publish the assessment, and assign it to the selected users.
-   **[[c_AssessmentGeneration|Assessment generation]]**  
In the Assessments application, administrators or assessment administrators can trigger the system to generate scheduled assessments or on-demand assessments when all the prerequisite steps are completed.
-   **[[c_AssessmentGroups|Assessment groups]]**  
An assessment group is a container for [[c_AssessmentInstances|assessment instances]] and assessment results generated in a single occurrence.
-   **[[t_CreateAnAssessmentCategory|View an assessment metric category]]**  
View [[c_AssessmentMetricCategories|assessment metric categories]] that are used with assessment metric types and assessment metrics in generating the bubble charts on the Demand Workbench. The bubble charts help the demand managers to assess the demands visually.
-   **[[c_AssessmentMetrics|Assessment metrics]]**  
In the Assessments application, a metric is a trait or value used to evaluate assessable records.
-   **[[add-questionbank-assessment|Add a metric category and metric in the question bank for assessments]]**  
Reuse the question categories \(metric categories\) and questions \(metrics\) added in the question bank for assessments. You can add metric categories or metrics from the question bank to an assessment, or from the assessment to a question bank.
-   **[[copy-assessment|Copy an assessment]]**  
Create a copy of an assessment with at least one category to reduce the effort of creating another assessment with similar data.
-   **[[t_CreateAMetricTemplate|Create a metric template]]**  
Create a metric template to define reusable rating scales for evaluating non-scripted metrics.
-   **[[r_CategoryUsersAndStakeholders|Category users and stakeholders]]**  
Users who take assessments are individuals in your organization who have specific knowledge of the assessment categories and the records being assessed.
-   **[[c_OnDemandAssessments|On-demand assessments]]**  
On-demand assessments can be generated for metric types with the Schedule type field set to On demand.
-   **[[c_ScheduledAssessments|Scheduled assessments]]**  
The system generates a unique scheduled job for each metric type with the **Schedule type** field set to **Scheduled**.
-   **[[t_CreateTriggerAssessment|Configure trigger conditions for an assessment]]**  
Trigger conditions specify when to send a particular assessment and who to send the assessment to.
-   **[[t_EnablingManagerNotifications|Enable manager notifications]]**  
Users with the assessment\_admin role can enable the [[notify-landing-page|Notify]] manager assessment is overdue [[email|email]] notification.
-   **[[t_ViewAMetricResult|View a metric result]]**  
Metric results contain values that represent an evaluated record's performance for a specific metric, based on a single evaluation from one user or from the execution of a script. Metric results contain actual values as well as calculated values. The system uses values from metric results to calculate [[r_CategoryResults|category results]].
-   **[[t_ViewAnAssessmentScorecard|View an assessment scorecard]]**  
The Assessments application prepares printable scorecards. A scorecard displays easy-to-interpret assessment results, in which the current calculated ratings for an assessable record are compared to previous ratings or to the ratings of other records.
-   **[[t_CreateADecisionMatrix|Create a decision matrix]]**  
The name and labels on a decision matrix are closely linked to the categories you choose for the axes. For that reason, first select the metric type and define the X and Y axes before you fill in other fields on the Decision Matrix form.

**Parent Topic:**[[using-assessments|Using assessments]]

**Related topics**  


[Assessment metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_AssessmentMetrics.md)

[[t_CreateAMetric|Create an assessment metric for a category]]

[[t_CreateAMetricDefinition|Create an assessment metric definition]]

[[t_UpdAMetrMinMaxValToMatchATmplate|Update a metric minimum and maximum value to match a template]]

## Related

- [[configure-assessment|Configure an assessment]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[c_AssessmentGroups|Assessment groups]]
- [[t_CreateAnAssessmentCategory|View an assessment metric category]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[add-questionbank-assessment|Add a metric category and metric in the question bank for assessments]]
- [[copy-assessment|Copy an assessment]]
- [[t_CreateAMetricTemplate|Create a metric template]]
- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_ScheduledAssessments|Scheduled assessments]]
- [[t_CreateTriggerAssessment|Configure trigger conditions for an assessment]]
- [[t_EnablingManagerNotifications|Enable manager notifications]]
- [[t_ViewAMetricResult|View a metric result]]
- [[t_ViewAnAssessmentScorecard|View an assessment scorecard]]
- [[t_CreateADecisionMatrix|Create a decision matrix]]
- [[using-assessments|Using assessments]]
- [[t_CreateAMetric|Create an assessment metric for a category]]
- [[t_CreateAMetricDefinition|Create an assessment metric definition]]
- [[t_UpdAMetrMinMaxValToMatchATmplate|Update a metric minimum and maximum value to match a template]]
- [[r_Assessments|Assessments]]
- [[c_AssessmentQuestionnaires|Assessment questionnaires]]
- [[c_assessable-records|Assessable records]]
- [[r_AssessmentResults|Assessment results]]
- [[r_AdministerDecisionMatrixes|Decision matrixes]]
- [[attachment|Attachment]]
- [[yes-no|Yes/No]]
- [[r_MetricResultFieldNames|Metric Result form]]
- [[c_AssessmentInstances|Assessment instances]]
- [[c_AssessmentMetricCategories|Assessment metric categories]]
- [[notify-landing-page|Notify]]
- [[email|Email]]
- [[r_CategoryResults|Category results]]
