---
title: Assessable records
description: An assessable record links a source record you want to evaluate, such as the company record for Amazon or the user record for a sales representative, to a metric type, such as vendors or employees.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_assessable-records.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Metric types and assessable records, Create an assessment metric for a category, Assessment metrics, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Assessable records

An assessable record links a source record you want to evaluate, such as the company record for Amazon or the user record for a sales representative, to a metric type, such as vendors or employees.

You use [[r_Assessments|assessments]] to evaluate the assessable record. The system generates assessable records from the source records that match the table and conditions set on the Assessment Metric Type form. You evaluate the assessable records with metric categories and metrics, which define traits and values to assess. For metric types with the **On demand** schedule type, you can [[t_GenOnDemandAssessOneAssessRec|generate on-demand assessments]] from the Assessable Record form. This method of [[c_AssessmentGeneration|assessment generation]] makes it easy to create and preview short questionnaires or to quickly obtain [[r_AssessmentResults|assessment results]] for specific assessable records.

You can set up an assessment description that includes information from multiple fields on an assessable record and is displayed on multiple lines. This provides the user who is taking the assessment with a more detailed and understandable description of the information being requested on the assessment questionnaire. Create a multi-line description using table titles, which can be defined to use one or more fields from the selected table.

-   **[[t_ViewAnAssessableRecord|View an assessable record]]**  
View the Assessable Record form to edit preferences and perform various actions.
-   **[[t_EnforceACondition|Enforce a condition to delete an assessable record]]**  
By default, the system does not delete assessable records, even if you change the table or conditions for the type and the existing assessable records no longer match.
-   **[[t_DeleteAssessableRecord|Delete an assessable record]]**  
When you delete an assessable record, the system deletes any stakeholders for the record.

**Parent Topic:**[[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]

**Related topics**  


[Metric types and assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_MetricTypesAndAssessableRecords.md)

[View an assessable record](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_ViewAnAssessableRecord.md)

## Related

- [[t_GenOnDemandAssessOneAssessRec|Generate an on-demand assessment for one assessable record]]
- [[t_ViewAnAssessableRecord|View an assessable record]]
- [[t_EnforceACondition|Enforce a condition to delete an assessable record]]
- [[t_DeleteAssessableRecord|Delete an assessable record]]
- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[r_Assessments|Assessments]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[r_AssessmentResults|Assessment results]]
