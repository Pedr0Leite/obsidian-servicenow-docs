---
title: Schedule an assessment
description: After you have evaluated your questionnaires using on-demand assessments, edit your categories and metrics as needed, reset your metric type record, and select the users who are qualified to evaluate the assessable records.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_ScheduledAssessment.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Scheduled assessments, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# Schedule an assessment

After you have evaluated your questionnaires using [[c_OnDemandAssessments|on-demand assessments]], edit your categories and metrics as needed, reset your metric type record, and select the users who are qualified to evaluate the [[c_assessable-records|assessable records]].

## Before you begin

Role required: assessment\_admin or admin

## Procedure

1.  Open the metric type you created for the [[t_OnDemandAssessment|on-demand assessment]] and set the **Schedule type** to **Scheduled**.

2.  Make sure the categories and metrics you created for the on-demand assessment are correct.

3.  Create [[r_CategoryUsersAndStakeholders|category users]] who have special knowledge of your categories.

4.  Create [stakeholders](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/r_CategoryUsersAndStakeholders.md) by associating category users to specific assessable records.

5.  [[t_SetAssesstGenerationSchedule|Set a schedule]] for automatic [[c_AssessmentGeneration|assessment generation]] or [[t_GenAVendorTypeAssmtManually|generate the assessment manually]].

    **Note:** This procedure must be done by a system administrator.

6.  Configure [[r_AssessmentNotifications|email notifications]] to remind users of their assigned assessments and to report to managers when an employee misses an assessment deadline.

7.  Analyze the assessment ratings in an assessment scorecard or decision matrix.


**Parent Topic:**[[c_ScheduledAssessments|Scheduled assessments]]

**Related topics**  


[[r_Assessments|Assessments]]

## Related

- [[t_OnDemandAssessment|Generate an on-demand assessment]]
- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
- [[t_SetAssesstGenerationSchedule|Set an assessment generation schedule]]
- [[t_GenAVendorTypeAssmtManually|Generate a vendor type assessment manually]]
- [[r_AssessmentNotifications|Assessment notifications]]
- [[c_ScheduledAssessments|Scheduled assessments]]
- [[r_Assessments|Assessments]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_assessable-records|Assessable records]]
- [[c_AssessmentGeneration|Assessment generation]]
