---
title: Survey responses and results
description: There is a metric result record for each user response to each question on every survey instance. Survey results for each question and category are calculated automatically based on the metric result records.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_SurveyResults.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Use surveys, Surveys, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Survey responses and results

There is a metric result record for each user response to each question on every survey instance. Survey results for each question and category are calculated automatically based on the metric result records.

If you use survey result calculations for results and scorecards, ensure that the [[t_CreateQuestSurveyDesigr|positive indicator]] field for the question is set appropriately, based on the answer options. To have any results, a category must contain scored questions.

## Survey responses

Survey responses are stored in the Metric Result \[asmt\_metric\_result\] table and display the recipients' answers to each question in a category. To view general results, navigate to **Survey** &gt; **Survey Responses**. To view results for a particular criterion, use a filter on the Metric Result \[asmt\_metric\_result\] table. For example, to view results based on the assignment group, apply a filter condition for assignment group.

\[Omitted image "SurveyDesignerResults.png"\] Alt text: Survey metric results

## Category results

[[r_CategoryResults|Category results]] are stored in the Assessment Category Result \[asmt\_category\_result\] table and display the overall ratings for each category based on the weighted value for each scored question. To view these results, navigate to **[[r_Assessments|Assessments]]** &gt; **Results** &gt; **Category results** and filter the results using the **\[Type.Evaluation method\] \[is\] \[Survey\]** condition.

\[Omitted image "SurveyDesignerCategoryResultsList.png"\] Alt text: Assessment category results

## Survey scorecards

A scorecard provides a visual breakdown of survey responses, based on the way questions were answered, by category. To access a scorecard, see [[t_ViewAScorecard|View a survey scorecard]].

-   **[[t_ViewResultsForAllSurveys|View results for all surveys]]**  
You can view the survey responses that are stored on the Metric Result \[asmt\_metric\_result\] table.
-   **[[t_ViewResultsForASpecificSurvey|View the results for a survey]]**  
You can view the responses for one survey definition. Survey results are stored on the Metric Result \[asmt\_metric\_result\] table.
-   **[View a survey scorecard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_ViewAScorecard.md)**  
A survey scorecard provides a visual breakdown of survey responses by category, based on the way questions were answered.
-   **[[t_ExportAQuizScorecard|Export a quiz scorecard as an image]]**  
You can export scorecards as images.
-   **[[request-translations-for-surveys|Request translations for surveys]]**  
Request translations for surveys to localize them into one or more languages. Localization requested items that are created for the selected [[r_SurveyManagementLandingPage|surveys]] in all the selected languages.
-   **[[edit-translations-for-surveys|Edit translations for surveys]]**  
Edit the translations for surveys, and after you make the changes, you can publish the translation.
-   **[[survey-result-database-view|Survey responses in a database view]]**  
You can view survey responses in a database view for reporting purposes. For each survey instance, you can view the instance as a single row and the answers to each survey question \(metric\) in the corresponding columns. Analyze the responses easily and, if you want, export the survey responses.

**Parent Topic:**[[using-surveys|Using surveys]]

**Related topics**  


[View a survey scorecard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_ViewAScorecard.md)

[[c_SurveyDesignerElements|Survey designer elements]]

[[t_ConfigCatWeightsForSurvey|Configure category weights for a survey]]

## Related

- [[t_CreateQuestSurveyDesigr|Create a question in the survey designer]]
- [[t_ViewAScorecard|View a survey scorecard]]
- [[t_ViewResultsForAllSurveys|View results for all surveys]]
- [[t_ViewResultsForASpecificSurvey|View the results for a survey]]
- [[t_ExportAQuizScorecard|Export a quiz scorecard as an image]]
- [[request-translations-for-surveys|Request translations for surveys]]
- [[edit-translations-for-surveys|Edit translations for surveys]]
- [[survey-result-database-view|Survey responses in a database view]]
- [[using-surveys|Using surveys]]
- [[c_SurveyDesignerElements|Survey designer elements]]
- [[t_ConfigCatWeightsForSurvey|Configure category weights for a survey]]
- [[r_CategoryResults|Category results]]
- [[r_Assessments|Assessments]]
- [[r_SurveyManagementLandingPage|Surveys]]
