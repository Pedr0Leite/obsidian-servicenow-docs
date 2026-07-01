---
title: Enable a quiz retake
description: You can configure a quiz to allow recipients to resubmit their answers as many times as they like, until the quiz's due date.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_EnableAQuizRetake.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Quiz designer, Using Quizzes, Quizzes, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# Enable a quiz retake

You can [[t_ConfigureaQuiz|configure a quiz]] to allow recipients to resubmit their answers as many times as they like, until the quiz's due date.

## Before you begin

Role required: assessment\_admin or admin

## About this task

Results are not calculated until the quiz's configured duration has elapsed. The card in the user's queue remains visible until the quiz's due date and displays a button to allow retakes.

## Procedure

1.  Navigate to **All** &gt; **[[r_Assessments|Assessments]]** &gt; **Metric Definition** &gt; **Types**.

2.  Remove the **Evaluation method = Assessment** filter condition so you can see all the records in the list.

3.  Open the quiz.

4.  In the [[c_MetricTypesAndAssessableRecords|Assessment Metric Type]] form, select the **Allow retake** [[check-box|check box]] and save the record.


**Parent Topic:**[[c_QuizDesigner|Quiz designer]]

**Related topics**  


[Quiz designer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_QuizDesigner.md)

[[t_PublishaQuiz|Publish a quiz]]

## Related

- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[c_QuizDesigner|Quiz designer]]
- [[t_PublishaQuiz|Publish a quiz]]
- [[t_ConfigureaQuiz|Configure a quiz]]
- [[r_Assessments|Assessments]]
- [[check-box|Check box]]
