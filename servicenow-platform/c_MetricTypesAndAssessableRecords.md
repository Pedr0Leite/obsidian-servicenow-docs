---
title: Metric types and assessable records
description: In the Assessments application, assessment administrators create and administer metric types and assessable records.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_MetricTypesAndAssessableRecords.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Create an assessment metric for a category, Assessment metrics, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Metric types and assessable records

In the [[r_Assessments|Assessments]] application, assessment administrators create and administer metric types and assessable records.

A metric type defines a set of records an organization wants to evaluate, such as vendors, projects, or employees. For each type, the system generates unique assessable records that link the type to records that need to be evaluated, such as the individual records for the vendors Amazon and Intel. There may be multiple assessable records for the same source record if the source record meets the criteria for more than one type. For example, you might want to evaluate a record on the Company table, such as Intel, as a vendor and as a manufacturer, with different [[r_CategoryMetrics|categories]] and [[c_AssessmentMetrics|metrics]].

For configuration suggestions, see [[c_AssessmentProcess|Assessment administrator tasks]].

## Assessable records

An assessable record links a source record you want to evaluate, such as the company record for Amazon or the user record for a sales representative, to a metric type, such as vendors or employees.

You use assessments to evaluate the assessable record. The system generates assessable records from the source records that match the table and conditions set on the Assessment Metric Type form. You evaluate the assessable records with metric categories and metrics, which define traits and values to assess. For metric types with the **On demand** schedule type, you can [[t_GenOnDemandAssessOneAssessRec|generate on-demand assessments]] from the Assessable Record form. This method of [[c_AssessmentGeneration|assessment generation]] makes it easy to create and preview short questionnaires or to quickly obtain [[r_AssessmentResults|assessment results]] for specific assessable records.

You can set up an assessment description that includes information from multiple fields on an assessable record and is displayed on multiple lines. This set up provides the user who is taking the assessment with a more detailed and understandable description of the information being requested on the assessment questionnaire. Create a multi-line description using table titles, which can be defined to use one or more fields from the selected table.

-   **[[t_CreatMetricTypesAndGenAssessRecs|Create metric types and generate assessable records]]**  
Create a metric type, which sets a table and filter conditions that define a set of records to evaluate.
-   **[[t_DeleteAMetricType|Delete a metric type]]**  
Deleting a metric type entails deleting many related records.
-   **[[t_ExportAssessment|Export an assessment]]**  
You can share assessments between ServiceNow instances by exporting an assessment and then importing the assessment on another instance.
-   **[[t_ImportAssessment|Import an assessment]]**  
Share assessments between ServiceNow instances by importing a previously exported assessment.
-   **[[t_UseUpdateSetsForSurveyAssess|Use update sets for surveys and assessments]]**  
Use an update set to capture changes to [[r_SurveyManagementLandingPage|surveys]] and assessments.
-   **[[t_CreateAnAssessmentSignature|Create an assessment signature]]**  
A signature on an assessment questionnaire contains assertions that can communicate directions, a legal statement, or any text that you want the recipient to consider.
-   **[[c_assessable-records|Assessable records]]**  
An assessable record links a source record you want to evaluate, such as the company record for Amazon or the user record for a sales representative, to a metric type, such as vendors or employees.
-   **[[t_DeleteAssessableRecord|Delete an assessable record]]**  
When you delete an assessable record, the system deletes any stakeholders for the record.
-   **[[t_ViewAnAssessableRecord|View an assessable record]]**  
View the Assessable Record form to edit preferences and perform various actions.

**Parent Topic:**[[t_CreateAMetric|Create an assessment metric for a category]]

**Parent Topic:**[[using-assessments|Using assessments]]

**Related topics**  


[Use update sets for surveys and assessments](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_UseUpdateSetsForSurveyAssess.md)

[Metric types and assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_MetricTypesAndAssessableRecords.md)

[View an assessable record](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_ViewAnAssessableRecord.md)

## Related

- [[r_CategoryMetrics|Assessment scorecard category metrics]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[t_GenOnDemandAssessOneAssessRec|Generate an on-demand assessment for one assessable record]]
- [[t_CreatMetricTypesAndGenAssessRecs|Create metric types and generate assessable records]]
- [[t_DeleteAMetricType|Delete a metric type]]
- [[t_ExportAssessment|Export an assessment]]
- [[t_ImportAssessment|Import an assessment]]
- [[t_UseUpdateSetsForSurveyAssess|Use update sets for surveys and assessments]]
- [[t_CreateAnAssessmentSignature|Create an assessment signature]]
- [[c_assessable-records|Assessable records]]
- [[t_DeleteAssessableRecord|Delete an assessable record]]
- [[t_ViewAnAssessableRecord|View an assessable record]]
- [[t_CreateAMetric|Create an assessment metric for a category]]
- [[using-assessments|Using assessments]]
- [[r_Assessments|Assessments]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[r_AssessmentResults|Assessment results]]
- [[r_SurveyManagementLandingPage|Surveys]]
