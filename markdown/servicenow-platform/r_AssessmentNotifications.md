---
title: Assessment notifications
description: You can configure the system to send email notifications for assessments.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/r\_AssessmentNotifications.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Enable manager notifications, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Assessment notifications

You can configure the system to send [[email|email]] notifications for [[r_Assessments|assessments]].

You can configure any of the following types of notification during the process of generating [[c_assessable-records|assessable records]]:

-   [[notify-landing-page|Notify]] assessment user: This messages notifies you of an assigned an assessment and includes the [[c_MetricTypesAndAssessableRecords|type]], the due date, and basic instructions. The message also contains a link to the record where you take the assessment.

    **Note:** If a user has a pending assessment, then the system will not generate another instance of the same assessment.

-   Remind assessment user: This message reminds you of the due date if half the time passes and you have not completed the assessment. The message content is the same as the first notification.
-   Notify manager assessment is overdue: If you do not complete an assessment by the due date, the system may send a notification to your manager, depending on configuration.

**Note:** By default, the system runs a script every 30 days to cancel expired assessment and survey instances that are in the **Work in progress** or **Ready to take** states.

**Parent Topic:**[[t_EnablingManagerNotifications|Enable manager notifications]]

**Related topics**  


[[t_CreatMetricTypesAndGenAssessRecs|Create metric types and generate assessable records]]

[Event scheduling](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ScheduleEvents.md)

## Related

- [[c_MetricTypesAndAssessableRecords|Metric types and assessable records]]
- [[t_EnablingManagerNotifications|Enable manager notifications]]
- [[t_CreatMetricTypesAndGenAssessRecs|Create metric types and generate assessable records]]
- [[email|Email]]
- [[r_Assessments|Assessments]]
- [[c_assessable-records|Assessable records]]
- [[notify-landing-page|Notify]]
