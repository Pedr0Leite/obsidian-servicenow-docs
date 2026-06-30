---
title: Create quizzes with forms
description: As an alternative to the Quiz Designer, you can create a complete quiz using records in the Assessment application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_CreateQuizzesWithForms.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using Quizzes, Quizzes, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Create quizzes with forms

As an alternative to the [[c_QuizDesigner|Quiz Designer]], you can create a complete quiz using records in the Assessment application.

All the elements of a quiz, the categories, questions, and answers, are stored in tables used by the assessment engine and are displayed in **quiz views** of these tables. Users creating [[c_Quizzes|quizzes]] in the Assessment application must have the assessment\_admin role.

Create a quiz using assessment forms by following the procedures in the order shown here:

-   Create the quiz.
-   Set up the categories.
-   Create the questions for the quiz.
-   Create the answers for the questions.
-   Distribute the quizzes to recipients.

**Note:** The recommended method of creating and editing quizzes is to use the quiz designer, which provides a single, intuitive interface for creating and editing quizzes quickly. If you determine that you need to add specific features to your quiz not offered through the quiz designer, you can do so by using some of the specific procedures described here.

-   **[[t_SetUpACategory|Set up a category]]**  
A category represents a theme for evaluating a specific element of the quiz topic and contains questions pertaining to that theme.
-   **[[t_SelectAUserForACategory|Select a user for a category]]**  
Category users are the recipients of the questions for each category.
-   **[[t_CreateAQuestion|Create questions]]**  
[[t_CreateAQuizQuestion|Create quiz questions]]. A category can have multiple questions associated with it.
-   **[[t_CreateAnAnswerForAQuestion|Create answers for questions]]**  
Create answer options for questions with the Choice or Likert Scale data type.
-   **[[t_DistributeAQuiz|Distribute a quiz]]**  
When you finish configuring the answers for the quiz questions, you are ready to distribute the quiz.
-   **[[t_ModifyAPublishedQuiz|Modify a published quiz]]**  
Post changes to existing questions immediately. Make new questions available to users who have not started the quiz.

**Parent Topic:**[[using-quizzes|Using Quizzes]]

**Related topics**  


[[t_CreateaQuiz|Create a quiz]]

[[t_CreateACategoryAR|Create a category for assessable records]]

## Related

- [[t_SetUpACategory|Set up a category]]
- [[t_SelectAUserForACategory|Select a user for a category]]
- [[t_CreateAQuestion|Create questions]]
- [[t_CreateAnAnswerForAQuestion|Create answers for questions]]
- [[t_DistributeAQuiz|Distribute a quiz]]
- [[t_ModifyAPublishedQuiz|Modify a published quiz]]
- [[using-quizzes|Using Quizzes]]
- [[t_CreateaQuiz|Create a quiz]]
- [[t_CreateACategoryAR|Create a category for assessable records]]
- [[c_QuizDesigner|Quiz designer]]
- [[c_Quizzes|Quizzes]]
- [[t_CreateAQuizQuestion|Create quiz questions]]
