---
title: Scheduled assessments
description: The system generates a unique scheduled job for each metric type with the Schedule type field set to Scheduled.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_ScheduledAssessments.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Scheduled assessments

The system generates a unique scheduled job for each metric type with the **Schedule type** field set to **Scheduled**.

The system generates a unique scheduled job for each metric type with the **Schedule type** field set to **Scheduled**. Each scheduled job generates assessment components for the related metric type. By default, the scheduled job runs when an administrator executes it manually, but administrators can set a schedule to generate [[r_Assessments|assessments]] automatically on a recurring basis.

For the system to properly generate scheduled assessments, the metric type must be active and [[t_PublishAMetricType|published]]. The metric type must also be associated to at least one metric category. That metric category must be associated to one or more of each of the following items:

-   [[r_ManageAssessablRecordAssociation|Assessable record]]
-   [[r_CategoryUsersAndStakeholders|Stakeholder]] associated to one of the [[c_assessable-records|assessable records]]
-   [[c_AssessmentMetrics|Metric]]

-   **[[t_ScheduledAssessment|Schedule an assessment]]**  
After you have evaluated your questionnaires using [[c_OnDemandAssessments|on-demand assessments]], edit your categories and metrics as needed, reset your metric type record, and select the users who are qualified to evaluate the assessable records.
-   **[[c_ScheduleTypes|Schedule types]]**  
You can schedule assessments for preconfigured users or send them to any user on demand.
-   **[[t_SetAssesstGenerationSchedule|Set an assessment generation schedule]]**  
You can set [[c_AssessmentGeneration|assessment generation]] schedules. You must set a schedule for each metric type individually.
-   **[Publish a metric type](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_PublishAMetricType.md)**  
Before it is possible to generate assessments, an assessment administrator must publish the associated metric type.
-   **[[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]]**  
Administrators can generate scheduled assessments manually.
-   **[[t_GenAVendorTypeAssmtManually|Generate a vendor type assessment manually]]**  
The Vendor Performance feature provides a direct method of generating assessments for the Vendor metric type.
-   **[[t_CleanUpAssessmentData|Clean up assessment data]]**  
The assessment process generates a considerable amount of data, some of which is not useful after a short time.
-   **[[c_AssessmentInstances|Assessment instances]]**  
An assessment instance represents one occurrence of a questionnaire assigned to one user.
-   **[[t_ViewAnAssessmentInstance|View an assessment instance]]**  
An assessment instance represents one occurrence of a questionnaire assigned to one user.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

**Related topics**  


[Assessment metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_AssessmentMetrics.md)

## Related

- [[t_PublishAMetricType|Publish a metric type]]
- [[r_ManageAssessablRecordAssociation|Assessable record associations]]
- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
- [[c_AssessmentMetrics|Assessment metrics]]
- [[t_ScheduledAssessment|Schedule an assessment]]
- [[c_ScheduleTypes|Schedule types]]
- [[t_SetAssesstGenerationSchedule|Set an assessment generation schedule]]
- [[t_GenSchedAssessmentManually|Generate a scheduled assessment manually]]
- [[t_GenAVendorTypeAssmtManually|Generate a vendor type assessment manually]]
- [[t_CleanUpAssessmentData|Clean up assessment data]]
- [[c_AssessmentInstances|Assessment instances]]
- [[t_ViewAnAssessmentInstance|View an assessment instance]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_AssessmentGeneration|Assessment generation]]
