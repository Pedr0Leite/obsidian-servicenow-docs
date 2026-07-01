---
title: Survey question migration
description: Before you migrate a legacy survey, understand that some legacy survey questions cannot be migrated due to incompatible question types.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/r\_SurveyQuestionMigration.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Legacy survey migration, Survey administration, Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-reference
---

# Survey question migration

Before you [[t_MigrateALegacySurvey|migrate a legacy survey]], understand that some legacy [[c_SurveyQuestion|survey questions]] cannot be migrated due to incompatible question types.

Legacy survey questions are migrated from the Survey Question \[survey\_question\_new\] table to the Assessment Metric \[asmt\_metric\] table. In legacy [[r_SurveyManagementLandingPage|surveys]], the **Type** field on the Survey Question table determines how the question renders on the survey questionnaire. In assessment surveys, the **Data type** field on the Assessment Metric table serves a similar purpose. Certain legacy survey types are not supported in assessment surveys.

The following table shows the conversion path for each legacy survey question type to an assessment data type, if there is one.

|Legacy survey type|Assessment data type|
|------------------|--------------------|
|Break|Not available|
|CheckBox|Checkbox|
|Date|Date|
|Date/Time|Date/Time|
|HTML|Not available|
|Label|Not available|
|List Collector|Not available|
|Lookup Multiple Choice|Not available|
|Lookup Select Box|Not available|
|Macro|Not available|
|Macro with Label|Not available|
|Multi Line Text|String \(**String** option set to **Multiline**\)|
|Multiple Choice|Likert Scale|
|Numeric Scale|Number|
|Reference|Not available|
|Select Box|Choice|
|Single Line Text|String \(**String** option set to **Single line**\)|
|UI Page|Not available|
|Wide Single Line Text|String \(**String** option set to **Single line wide**\)|
|Yes / No|Yes/No|

**Parent Topic:**[[c_MigrateSurveys|Legacy survey migration]]

**Related topics**  


[Migrate a legacy survey]()

[Migrated components]()

[Migrated question review]()

## Related

- [[c_MigrateSurveys|Legacy survey migration]]
- [[t_MigrateALegacySurvey|Migrate a legacy survey]]
- [[c_SurveyQuestion|Survey questions]]
- [[r_SurveyManagementLandingPage|Surveys]]
