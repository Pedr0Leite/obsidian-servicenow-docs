---
title: Enable manager notifications
description: Users with the assessment\_admin role can enable the Notify manager assessment is overdue email notification.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_EnablingManagerNotifications.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Enable manager notifications

Users with the assessment\_admin role can enable the [[notify-landing-page|Notify]] manager assessment is overdue [[email|email]] notification.

## Before you begin

Role required: assessment\_admin or admin

## About this task

This notification sends emails to assessors' managers when assessors do not complete their assigned [[r_Assessments|assessments]] on time. For more information, see the table of assessment notifications. You must enable or disable this email notification separately for each metric type.

## Procedure

1.  Navigate to **All** &gt; **Assessments** &gt; **Metric Definition** &gt; **Types**.

2.  Open a metric type.

3.  Select the **Notify if overdue** [[check-box|check box]].

    \[Omitted image "NotifyIfOverdue.png"\] Alt text: The Notify if overdue option

    To disable manager notifications, clear the check box.

4.  Save the record.

    **Note:** The assessor's user record must have a manager specified in the **Manager** field to use this notification. You might need to configure the form to use this field.


-   **[[r_AssessmentNotifications|Assessment notifications]]**  
You can configure the system to send email notifications for assessments.
-   **[[r_AssessmentNotificationWorkflow|Assessment notification workflow]]**  
The system sends assessment notifications according to the Notify assessment user workflow. Users with the workflow\_admin, workflow\_creator, or workflow\_publisher roles can view workflows.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[r_AssessmentNotifications|Assessment notifications]]
- [[r_AssessmentNotificationWorkflow|Assessment notification workflow]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[notify-landing-page|Notify]]
- [[email|Email]]
- [[r_Assessments|Assessments]]
- [[check-box|Check box]]
