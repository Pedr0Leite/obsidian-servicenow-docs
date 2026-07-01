---
title: Survey trigger conditions
description: Trigger conditions specify when to send a particular survey and the persons to send it to.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_TriggerConditions.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Survey trigger conditions

Trigger conditions specify when to send a particular survey and the persons to send it to.

Survey administrators can use trigger conditions to configure the system to generate a survey instance each time a specified action occurs on a specified table, for example, when an incident or change request closes. The system sends the survey to users that are related to the triggering record, for example, incident callers or change request assignees. You can choose to send a survey every time the condition is met, or you can set a probability for the system to send a survey at random when the condition is met.

Trigger conditions are ideal for sending transactional [[r_SurveyManagementLandingPage|surveys]]. Transactional surveys generally measure satisfaction with a recent experience, such as closing an incident or purchasing an item.

**Note:** Trigger conditions are comparable to survey conditions in legacy surveys. If you [[t_MigrateALegacySurvey|migrate a legacy survey]] that has survey conditions, ensure that the survey conditions are deactivated before you recreate them as trigger conditions.

-   **[[t_CreateATriggerCondition|Configure a trigger condition for a survey]]**  
Configure trigger conditions to specify when to send a particular survey and the persons to send it to.
-   **[[r_TriggerConditionExample|Trigger condition example]]**  
You can send out auto-triggered surveys when an incident is closed or resolved.

**Parent Topic:**[[r_SurveyAdminTasks|Survey administration]]

**Related topics**  


[View survey reports]()

[Survey designer]()

[View a survey instance]()

[Survey users and groups]()

[Copy a survey]()

[Publish a survey]()

[Customize the appearance of a survey]()

[Survey definitions]()

[Create a [[c_SurveyDesigner|survey designer]] template question]()

[Survey questions]()

[Survey distribution]()

[Outlook Actionable Messages]()

[Sentiment analysis for surveys]()

[Surveys in Service Portal and the Now Mobile app]()

[Surveys in ITSM Virtual Agent]()

[Legacy survey migration]()

## Related

- [[t_CreateATriggerCondition|Configure a trigger condition for a survey]]
- [[r_TriggerConditionExample|Trigger condition example]]
- [[r_SurveyAdminTasks|Survey administration]]
- [[r_SurveyManagementLandingPage|Surveys]]
- [[t_MigrateALegacySurvey|Migrate a legacy survey]]
- [[c_SurveyDesigner|Survey designer]]
