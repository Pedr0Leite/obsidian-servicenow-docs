---
title: Assessment generation
description: In the Assessments application, administrators or assessment administrators can trigger the system to generate scheduled assessments or on-demand assessments when all the prerequisite steps are completed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_AssessmentGeneration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Assessment generation

In the [[r_Assessments|Assessments]] application, administrators or assessment administrators can trigger the system to generate [[c_ScheduledAssessments|scheduled assessments]] or [[c_OnDemandAssessments|on-demand assessments]] when all the prerequisite steps are completed.

An assessment administrator must publish the metric type to enable assessment generation.

The system performs these tasks when it generates assessments:

-   Creates [[c_AssessmentQuestionnaires|assessment questionnaires]] from non-scripted metrics and assigns the questionnaires to users. When users complete their assigned questionnaires, the system uses their responses to calculate assessment results.
-   Runs scripted metrics from each category to query the database and calculate assessment results.

Each time the system generates assessments, it creates some or all of the following components. Consider having an administrator set a schedule for recurring data cleanup, as the system can potentially generate a considerable amount of assessment data.

-   [[c_AssessmentGroups|Assessment group]]
-   [[c_AssessmentInstances|Assessment instances]]
-   [[r_AssessmentResults|Assessment results]]

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[c_AssessmentGroups|Assessment groups]]
- [[c_AssessmentInstances|Assessment instances]]
- [[r_AssessmentResults|Assessment results]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[r_Assessments|Assessments]]
- [[c_ScheduledAssessments|Scheduled assessments]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_AssessmentQuestionnaires|Assessment questionnaires]]
