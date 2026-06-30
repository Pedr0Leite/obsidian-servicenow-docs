---
title: Legacy survey migration
description: Users with the survey\_admin role can migrate legacy survey data to create copies of legacy surveys and their related records in assessment tables. The Survey Management application, which is built on the assessment engine, is available as an alternative to legacy surveys.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_MigrateSurveys.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Legacy survey migration

Users with the survey\_admin role can migrate legacy survey data to create copies of legacy [[r_SurveyManagementLandingPage|surveys]] and their related records in assessment tables. The Survey Management application, which is built on the assessment engine, is available as an alternative to legacy surveys.

The following legacy survey components are migrated:

-   Survey masters
-   Supported [[c_SurveyQuestion|survey questions]] and question choices
-   Survey instances
-   Survey responses

Legacy survey conditions are not migrated and must be recreated as trigger conditions.

**Note:**

-   The **Legacy Surveys** and **Legacy Administration** modules are available on instances upgraded from a previous release but not available for new instances. Customers using legacy survey or survey wizard should plan to migrate to the Survey Management application to create modern and high quality surveys for their users.
-   The following legacy survey plugins are inactive by default, and are available upon request:
    -   Best Practice - Task Survey Management \(ID: com.snc.bestpractice.task\_survey\)
    -   Survey Management \(ID: com.glideapp.survey\)
    -   Assessment Components \(ID: com.snc.assessment\)
    -   Survey Wizard \(ID: com.glideapp.survey\_wizard\)
-   Survey wizards cannot be migrated.

-   **[[t_MigrateALegacySurvey|Migrate a legacy survey]]**  
Migrate a legacy survey and its related records to take advantage of a more powerful feature set.
-   **[[r_SurveyQuestionMigration|Survey question migration]]**  
Before you migrate a legacy survey, understand that some legacy survey questions cannot be migrated due to incompatible question types.
-   **[[r_MigratedComponents|Migrated components]]**  
When you migrate a survey, the system maps records from survey tables to assessment tables.
-   **[[r_ReviewMigratedQuestions|Migrated question review]]**  
To maintain accurate result calculations, you may need to make minor adjustments to some of the migrated survey records to ensure results are calculated correctly.

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

[Survey trigger conditions]()

[Survey distribution]()

[Outlook Actionable Messages]()

[Sentiment analysis for surveys]()

[Surveys in Service Portal and the Now Mobile app]()

[Surveys in ITSM Virtual Agent]()

## Related

- [[t_MigrateALegacySurvey|Migrate a legacy survey]]
- [[r_SurveyQuestionMigration|Survey question migration]]
- [[r_MigratedComponents|Migrated components]]
- [[r_ReviewMigratedQuestions|Migrated question review]]
- [[r_SurveyAdminTasks|Survey administration]]
- [[r_SurveyManagementLandingPage|Surveys]]
- [[c_SurveyQuestion|Survey questions]]
- [[c_SurveyDesigner|Survey designer]]
