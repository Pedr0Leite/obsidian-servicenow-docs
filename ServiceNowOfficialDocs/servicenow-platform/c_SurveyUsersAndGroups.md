---
title: Survey users and groups
description: Survey users and survey user groups help survey administrators control who can take a survey.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_SurveyUsersAndGroups.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Survey users and groups

Survey users and survey user groups help survey administrators control who can [[t_TakeASurvey|take a survey]].

Survey administrators can restrict a survey so that only specified users can access it unless a survey administrator manually assigns the survey to a different user. Survey user groups provide a way to quickly designate multiple survey users.

## Administering survey users

The list of survey users for a survey is visible on the Survey Definition and Survey Category forms. You can add or remove users from the list of survey users at any point. Note that designating a survey user does not automatically generate a survey instance for that user unless both of the following conditions are true:

-   The survey definition **Schedule** period is set to **Daily**, **Weekly**, **Monthly**, or **Yearly**. In this case the system assigns a new survey instance to each survey user at the beginning of each schedule period.
-   The user has no instances of the survey that are incomplete or that have not yet reached their expiration date.

You can designate survey users from the [[c_SurveyDesigner|Survey Designer]], the Survey Definition form, or the Survey Category form.

**Note:** If there are trigger conditions for a survey, do not create survey users. Instead, use the Trigger Conditions form to assign users.

-   **[[t_CreatingSurveyUserGroups|Create a survey user group]]**  
Survey user groups are groups that have the **Type** field set to survey and display only the information most relevant to [[r_SurveyManagementLandingPage|surveys]]. You can assign survey groups or any user group to surveys.
-   **[[t_SelRecipsForASurveyInDesigner|Select recipients for a survey in the Survey Designer]]**  
You can assign survey users while designing or modifying the survey.
-   **[[t_SurveyDefinitionForm|Designate a survey user]]**  
You can designate one survey user at a time from the Survey Definition form.
-   **[[t_SurveyCategoryForm|Designate or remove multiple survey users at one time]]**  
Use the Survey Category form to designate or remove multiple survey users at a time.
-   **[[t_AllowRecipientsToRetakeASurvey|Allow recipients to retake a survey]]**  
You can configure a survey to allow recipients to resubmit their answers as many times as they like, up to the survey's due date.

**Parent Topic:**[[r_SurveyAdminTasks|Survey administration]]

**Related topics**  


[View survey reports]()

[Survey designer]()

[View a survey instance]()

[Copy a survey]()

[Publish a survey]()

[Customize the appearance of a survey]()

[Survey definitions]()

[Create a survey designer template question]()

[Survey questions]()

[Survey trigger conditions]()

[Survey distribution]()

[Outlook Actionable Messages]()

[Sentiment analysis for surveys]()

[Surveys in Service Portal and the Now Mobile app]()

[Surveys in ITSM Virtual Agent]()

[Legacy survey migration]()

[[t_SendSurveyInvitationsToUsers|Send survey invitations to users]]

[[c_TriggerConditions|Survey trigger conditions]]

[[c_SurveyCategory|Survey categories]]

[[c_SurveyDefinitions|Survey definitions]]

## Related

- [[t_CreatingSurveyUserGroups|Create a survey user group]]
- [[t_SelRecipsForASurveyInDesigner|Select recipients for a survey in the Survey Designer]]
- [[t_SurveyDefinitionForm|Designate a survey user]]
- [[t_SurveyCategoryForm|Designate or remove multiple survey users at one time]]
- [[t_AllowRecipientsToRetakeASurvey|Allow recipients to retake a survey]]
- [[r_SurveyAdminTasks|Survey administration]]
- [[t_SendSurveyInvitationsToUsers|Send survey invitations to users]]
- [[c_TriggerConditions|Survey trigger conditions]]
- [[c_SurveyCategory|Survey categories]]
- [[c_SurveyDefinitions|Survey definitions]]
- [[t_TakeASurvey|Take a survey]]
- [[c_SurveyDesigner|Survey designer]]
- [[r_SurveyManagementLandingPage|Surveys]]
