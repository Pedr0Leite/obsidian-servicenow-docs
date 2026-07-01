---
title: Surveys
description: 
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/r\_SurveyManagementLandingPage.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-reference
---

# Surveys

Two versions of the application are supported, Surveys, which is the latest version, and Legacy Surveys. Survey improves the user interface and extends the capabilities of the Legacy Surveys application.

## Configuring surveys

There are many options for advanced configuration in Surveys:

-   Create a survey, add questions, and choose recipients, all in one interface.
-   Create conditional questions, which appear only when users answer other questions a certain way.
-   Restrict a survey so only specific survey users can take it, and send invitations to those users simultaneously. Alternatively, make the survey a public survey so that any user can take the survey, even anonymous users \(users who have not logged in to the ServiceNow system\).

    **Tip:** The assessment\_take2 [[ui-page|UI page]] should be public for public surveys. If that page is not public, anonymous users do not have access to the page and public surveys do not work.

-   Set a schedule to automatically assign a survey to users and to limit how often the same user can [[t_TakeASurvey|take a survey]].
-   Customize the look and feel of [[c_SurveyQuestionnairesForUsers|survey questionnaires]].
-   Save anonymous survey responses.
-   Convert survey responses to numerical scores and view them on scorecards.
-   Deactivate a survey for maintenance or to retire it without deleting it.

**Note:** Because surveys use the same tables and other back-end components as [[r_Assessments|assessments]], you may see assessment elements such as table and field names in certain places throughout the survey feature.

## Legacy Surveys

Survey administrators can continue to use legacy survey functionality and data, however, it is recommended that you migrate legacy surveys to the Surveys application. Concurrent use of both survey applications can cause confusion and redundancy.

Survey wizards are not impacted and cannot be migrated.

**Note:** The Legacy Surveys application is not described in the documentation that you are viewing. It is documented on the ServiceNow wiki.

|Capability|Surveys|Legacy Surveys|
|----------|-------|--------------|
|Surveys in Service Portal.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Save new survey responses each time a user takes the same survey.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Create question templates to reuse sets of answer options.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Categorize [[c_SurveyQuestion|survey questions]] and report on [[r_CategoryResults|category results]].|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Deactivate a survey without deleting it.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Create conditional questions.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Send surveys automatically based on a schedule.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Customize survey questionnaire color scheme.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Save anonymous survey responses for logged-in users.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|View survey responses on graphical scorecards.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Save surveys in a draft state until they are ready to publish.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Create and send surveys from one page.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Allow only specific users to access a survey.|\[Omitted image "Tick.png"\] Alt text: check mark| |
|Send surveys based on conditions.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Send survey [[email|email]] notifications.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Limit how often a user can take the same survey.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Add introduction and end note text.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Create survey modules.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Public survey: Allow persons to take a survey without logging in.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|
|Use update sets to track changes.|\[Omitted image "Tick.png"\] Alt text: check mark|\[Omitted image "Tick.png"\] Alt text: check mark|

-   **[[using-surveys|Using surveys]]**  
Survey administrators—users with the survey\_admin role—create and maintain surveys and configure how they are distributed and published. Surveys on Service Portal are also supported.
-   **[[survey-reference|Surveys reference]]**  
[[reference|Reference]] topics provide additional information about the forms, fields, and properties you use while working with surveys.

**Parent Topic:**[[assessments-surveys-landing-page|Assessments and Surveys]]

**Related topics**  


[[c_MigrateSurveys|Legacy survey migration]]

[[c_SurveyDesigner|Survey designer]]

[[r_SurveyManagementRoles|Survey roles]]

[[c_SurveyServicePortal|Surveys in Service Portal and the Now Mobile app]]

[Service Portal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_ServicePortal.md)

## Related

- [[using-surveys|Using surveys]]
- [[survey-reference|Surveys reference]]
- [[assessments-surveys-landing-page|Assessments and Surveys]]
- [[c_MigrateSurveys|Legacy survey migration]]
- [[c_SurveyDesigner|Survey designer]]
- [[r_SurveyManagementRoles|Survey roles]]
- [[c_SurveyServicePortal|Surveys in Service Portal and the Now Mobile app]]
- [[ui-page|UI page]]
- [[t_TakeASurvey|Take a survey]]
- [[c_SurveyQuestionnairesForUsers|Survey questionnaires]]
- [[r_Assessments|Assessments]]
- [[c_SurveyQuestion|Survey questions]]
- [[r_CategoryResults|Category results]]
- [[email|Email]]
- [[reference|Reference]]
