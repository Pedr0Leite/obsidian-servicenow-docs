---
title: Use update sets for surveys and assessments
description: Use an update set to capture changes to surveys and assessments.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_UseUpdateSetsForSurveyAssess.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Share surveys, Survey distribution, Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# Use update sets for surveys and assessments

Use an update set to capture changes to [[r_SurveyManagementLandingPage|surveys]] and [[r_Assessments|assessments]].

## Before you begin

Role required: admin or survey\_admin

## Procedure

1.  Create an update set and use it to make changes on a development instance.

    **Note:** For more information, see [System update sets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/system-update-sets.md).

    When developing surveys and assessments, use an update set to capture the changes and move them from a development instance to a production instance. Once an update set is created and marked current, all of the updates to the following tables are recorded in the update set.

    The following tables are now update set enabled and also extend the application file:

    -   Assessment [[r_MetricTemplates|Metric Templates]] \[asmt\_template\]
    -   Assessment metric type \[asmt\_metric\_type\]
    -   Assessment Template Definitions \[asmt\_template\_definition\]
    -   Assessment Metric Definitions \[asmt\_metric\_definition\]: survey question answer options
    -   Schedule \[sys\_trigger\]: scheduled jobs associated with the survey
    -   [[c_AssessmentMetricCategories|Assessment Metric Categories]] \[asmt\_metric\_category\]: [[c_SurveyCategory|survey categories]]
    -   [[c_AssessmentMetrics|Assessment Metrics]] \[asmt\_metric\]: [[c_SurveyQuestion|survey questions]]
    -   Assessment Category Users \[asmt\_m2m\_category\_user\]: survey users
    -   Trigger Conditions \[asmt\_condition\]

**Parent Topic:**[[c_SurveyInportAndExport|Sharing surveys]]

**Parent Topic:**[[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]

## Related

- [[c_SurveyInportAndExport|Sharing surveys]]
- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[r_SurveyManagementLandingPage|Surveys]]
- [[r_Assessments|Assessments]]
- [[r_MetricTemplates|Metric templates]]
- [[c_AssessmentMetricCategories|Assessment metric categories]]
- [[c_SurveyCategory|Survey categories]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[c_SurveyQuestion|Survey questions]]
