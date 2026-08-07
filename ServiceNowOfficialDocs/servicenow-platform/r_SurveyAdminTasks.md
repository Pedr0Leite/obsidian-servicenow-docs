---
title: Survey administration
description: Survey administrators—users with the survey\_admin role—create and maintain surveys and configure how they are distributed and published. Surveys on Service Portal are also supported.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/r\_SurveyAdminTasks.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-reference
---

# Survey administration

Survey administrators—users with the survey\_admin role—create and maintain [[r_SurveyManagementLandingPage|surveys]] and configure how they are distributed and published. Surveys on Service Portal are also supported.

Survey administration includes the following procedures.

-   Create, customize, and publish surveys.
-   Write and maintain survey questions.
-   Define trigger conditions for when surveys are sent to users, such as when an incident closes.
-   Maintain surveys and survey questions as the organization's needs change.

To set up surveys in [Service Portal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_ServicePortal.md), you must first install Service Portal and then [Create and edit a page using the Service Portal Designer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_ConfigureAPage.md) on the page. The base system includes the Survey widget.

-   **[[view-survey-overview|View survey reports]]**  
Use the [[survey-overview-module|Survey Overview dashboard]] to view various survey reports, such as Surveys by Metric Type and State.
-   **[[c_SurveyDesigner|Survey designer]]**  
Users with the survey\_admin role can use the survey designer. The survey designer lets you create [[c_SurveyCategory|survey categories]] and questions, configure the details, and publish the survey to specific users or groups.
-   **[[t_ViewSurveyInstance|View a survey instance]]**  
A survey instance represents one questionnaire assigned to one user. You view an instance to verify that survey instances were created, to check the state of a survey instance, or to reassign a survey instance.
-   **[[c_SurveyUsersAndGroups|Survey users and groups]]**  
Survey users and survey user groups help survey administrators control who can [[t_TakeASurvey|take a survey]].
-   **[[copy-survey|Copy a survey]]**  
Create a copy of a survey with at least one category to reduce the effort of creating another survey with similar data.
-   **[[t_PublishASurvey|Publish a survey]]**  
You must publish a survey to enable people to receive and complete survey instances.
-   **[[t_CustomizingAppearance|Customize the appearance of a survey]]**  
As an assessment and survey administrator, set properties to customize the color of various elements on the questionnaires.
-   **[[c_SurveyDefinitions|Survey definitions]]**  
A survey definition is the root record upon which a survey is built.
-   **[[t_CreateASurveyDesignerTemplateQ|Create a survey designer template question]]**  
You can create a question that uses choice lists from a template.
-   **[[c_SurveyQuestion|Survey questions]]**  
Survey questions appear on [[c_SurveyQuestionnairesForUsers|survey questionnaires]] for the associated survey definition.
-   **[[c_TriggerConditions|Survey trigger conditions]]**  
Trigger conditions specify when to send a particular survey and the persons to send it to.
-   **[[c_SurveyDistribution|Survey distribution]]**  
There are several ways for survey administrators to distribute surveys to users.
-   **[[outlook-actionable-messages|Outlook Actionable Messages]]**  
Outlook actionable messages plugin enables users to respond to the survey from within the Microsoft Outlook application.
-   **[[sentiment-analysis|Sentiment analysis for surveys]]**  
You can use sentiment analysis to determine whether user responses for a survey are considered positive, negative, or neutral.
-   **[[c_SurveyServicePortal|Surveys in Service Portal and the Now Mobile app]]**  
If you've installed Service Portal, you can use the My [[assessments-surveys-landing-page|Assessments and Surveys]] widget in Service Portal. Users can view surveys in Service Portal. Service Portal also supports surveys for users on mobile devices that have the Now Mobile app installed. The My Assessments and Surveys widget is available by default on the Service Portal home page.
-   **[[survey-virtual-agent|Surveys in ITSM Virtual Agent]]**  
You can use surveys in ITSM Virtual Agent to collect survey responses from users through conversational questionnaires \(pre-chat and post-chat surveys\) in the chat client.
-   **[[c_MigrateSurveys|Legacy survey migration]]**  
Users with the survey\_admin role can migrate legacy survey data to create copies of legacy surveys and their related records in assessment tables. The Survey Management application, which is built on the assessment engine, is available as an alternative to legacy surveys.

**Parent Topic:**[[using-surveys|Using surveys]]

## Related

- [[view-survey-overview|View survey reports]]
- [[c_SurveyDesigner|Survey designer]]
- [[t_ViewSurveyInstance|View a survey instance]]
- [[c_SurveyUsersAndGroups|Survey users and groups]]
- [[copy-survey|Copy a survey]]
- [[t_PublishASurvey|Publish a survey]]
- [[t_CustomizingAppearance|Customize the appearance of a survey]]
- [[c_SurveyDefinitions|Survey definitions]]
- [[t_CreateASurveyDesignerTemplateQ|Create a survey designer template question]]
- [[c_SurveyQuestion|Survey questions]]
- [[c_TriggerConditions|Survey trigger conditions]]
- [[c_SurveyDistribution|Survey distribution]]
- [[outlook-actionable-messages|Outlook Actionable Messages]]
- [[sentiment-analysis|Sentiment analysis for surveys]]
- [[c_SurveyServicePortal|Surveys in Service Portal and the Now Mobile app]]
- [[survey-virtual-agent|Surveys in ITSM Virtual Agent]]
- [[c_MigrateSurveys|Legacy survey migration]]
- [[using-surveys|Using surveys]]
- [[r_SurveyManagementLandingPage|Surveys]]
- [[survey-overview-module|Survey Overview dashboard]]
- [[c_SurveyCategory|Survey categories]]
- [[t_TakeASurvey|Take a survey]]
- [[c_SurveyQuestionnairesForUsers|Survey questionnaires]]
- [[assessments-surveys-landing-page|Assessments and Surveys]]
