---
title: Add a metric category and metric in the question bank for surveys
description: Reuse the question categories \(metric categories\) and questions \(metrics\) added in the question bank for surveys. You can add metric categories or metrics from the question bank to a survey, or from the survey to a question bank.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/add-questionbank-for-survey.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Survey questions, Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# Add a metric category and metric in the question bank for surveys

Reuse the question categories \(metric categories\) and questions \(metrics\) added in the question bank for [[r_SurveyManagementLandingPage|surveys]]. You can add metric categories or metrics from the question bank to a survey, or from the survey to a question bank.

## Before you begin

Role required: admin or survey\_admin

Activate the Survey Question Bank Sample Data plugin \(com.snc.question\_bank\_data\) to access the demo data for the question bank.

## Procedure

1.  Navigate to **All** &gt; **Survey** &gt; **Question Bank**.

2.  Click **New**.

3.  On the [[metric-category-form|Metric Category form]], fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Name|Name of the metric category.|
    |Description|Description of the metric category.|
    |Total metrics|Total number of metrics in the metric category. This number is automatically updated when you add or delete metrics from the category.|

4.  Right-click on the title bar and click **Save**.

5.  In the [[c_AssessmentMetrics|Assessment Metrics]] related list, click **New**.

6.  In the [[survey-question-form|Survey Question form]], fill the fields.

    For information on these fields, see [[t_CreateOrModifySurveyQuestions|Create or modify survey questions]].

7.  Click **Submit**.


-   **[[configure-questionbank-survey|Configure metric categories or metrics for a survey using the question bank]]**  
Reuse question categories \(metric categories\) and questions \(metrics\) from the **Question Bank** module while creating or updating a survey.

**Parent Topic:**[[c_SurveyQuestion|Survey questions]]

**Related topics**  


[Create or modify survey questions]()

[Survey question data types]()

[Survey question template]()

[Create or modify answer options]()

[Change the order of survey questions]()

## Related

- [[t_CreateOrModifySurveyQuestions|Create or modify survey questions]]
- [[configure-questionbank-survey|Configure metric categories or metrics for a survey using the question bank]]
- [[c_SurveyQuestion|Survey questions]]
- [[r_SurveyManagementLandingPage|Surveys]]
- [[metric-category-form|Metric Category form]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[survey-question-form|Survey Question form]]
