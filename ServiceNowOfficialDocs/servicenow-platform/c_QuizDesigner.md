---
title: Quiz designer
description: The quiz designer provides a single interface that users with the assessment\_admin role can use to create, edit, and distribute quizzes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_QuizDesigner.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Using Quizzes, Quizzes, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Quiz designer

The quiz designer provides a single interface that users with the assessment\_admin role can use to create, edit, and distribute [[c_Quizzes|quizzes]].

You can also use it to edit existing quizzes and change scoring parameters.

Alternatively, you can use the modules of the [[r_Assessments|assessment engine]] to create and edit the records that make up a quiz. All quiz records are stored in assessment tables and displayed in Quiz views of those tables. For details, see [[c_CreateQuizzesWithForms|Create quizzes with forms]].

## Tools on the Quiz Designer

The quiz designer includes a design canvas, a header bar, and many controls that you can use to create quizzes.

To open the quiz designer, navigate to **Quizzes** &gt; **Quiz Designer**.

The designer contains the following elements:

-   **Controls** tab
-   **Questions** tab
-   **Categories** tab
-   **Header** bar
-   Design canvas

## Controls tab

Controls for the supported question data types are available in the Controls palette. Drag and drop a control onto the designer canvas to create a question of that type.

\[Omitted image "QuizDesignerControls.png"\] Alt text:

|Data type|Description|Scored|
|---------|-----------|------|
|Attachment|Question with a Manage Attachments icon that allows users to attach one or more files.|Y|
|Boolean|Question with a [[check-box|check box]] or a **[[yes-no|Yes/No]]** list for user responses.| |
|Choice|List of predefined options. For more information, see the definition for **Choices** [[t_CreateAQuizQuestion|Create quiz questions]]. Multiple correct answers are supported.|Y|
|Date|Date field.|N|
|Date/Time|Date and time field.|N|
|Number|Number field with predefined minimum and maximum values. The default is 1-10.|N|
|Percentage|Percentage field with a prescribed range.|N|
|Scale|Predefined Likert scale. Answer options appear as radio buttons. Multiple correct answers are supported.|Y|
|Numeric Scale|Selectable number scale. The default is 1-5. Answer options appear as radio buttons. Multiple correct answers are supported.|Y|
|Image Scale|Predefined set of images. Five emojis similar to the Likert scale \(very dissatisfied to very satisfied\) are provided. However, you can upload additional images in JPG, PNG, or GIF format. Multiple correct answers are supported.|Y|
|String|Single or multiline text field.|N|
|Template|Choice list of templates that provide a predefined scale of options. For details, see [[t_ConfigureATemplateQuestion|Configure a template question]]. Multiple correct answers are supported.|Y|
|Reference|Choice list of fields from a specified [[reference|reference]] table. This data type does not support reference qualifiers.| |

## Questions tab

This tab displays all metrics added to the question bank for quizzes. Use the **Filter** field to search for questions. Each metric is displayed with its name and type.

## Categories tab

This tab displays all metric categories added to the question bank for quizzes. All metrics in the question bank are group under the corresponding metric category. Use the **Filter** field to search for categories or questions.

## Header Bar

The header bar contains tabs that display different views and a menu of various functions.

Click one of the following tabs to change the view in the canvas:

-   **Design**: Add categories and questions, and configure the properties of each. This is the default view of the canvas when you open the designer.
-   **Configuration**: Create introductions and end notes for quizzes, and select a [[t_CreateAnAssessmentSignature|signature]].
-   **Availability**: Select the recipients for each category in the quiz.

Point to the menu icon \(\[Omitted image "Menu.png"\] Alt text: Menu icon\) in the in the upper right of the quiz designer to select the following options:

-   **Save**: Saves the current quiz.
-   **Preview**: Displays a preview of the quiz as it appears to the recipients.
-   **Publish**: Distributes the quiz to the selected recipients.
-   **Save and Publish**: Saves and distributes the quiz in one step.
-   **New Quiz**: Opens a fresh canvas for a new quiz.
-   **Load Quiz**: Opens a list of existing quizzes that you can select and edit.
-   **Copy Quiz**: Creates a copy of the quiz.

The availability of each option depends on the status of the quiz that is opened in the quiz designer.

## Design Canvas

New quizzes open in the **Design** view. The quiz **Name** field appears above first category in the canvas. A blank question field appears in the category container.

-   **[[t_CreateaQuiz|Create a quiz]]**  
When you create a quiz, you can create one or more categories and then add questions to each category.
-   **[[t_EditaQuiz|Edit a quiz]]**  
You can update a quiz after the quiz has been distributed.
-   **[[t_EnableAQuizRetake|Enable a quiz retake]]**  
You can [[t_ConfigureaQuiz|configure a quiz]] to allow recipients to resubmit their answers as many times as they like, until the quiz's due date.
-   **[[t_ViewAQuizResult|View a quiz result]]**  
You can view quiz results for each question and category, or view the quiz scorecard for a detailed breakdown.

**Parent Topic:**[[using-quizzes|Using Quizzes]]

**Related topics**  


[[t_ViewACategoryResult|View an assessment category result]]

[[t_ViewAQuizScorecard|View a quiz scorecard]]

[Create a quiz](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_CreateaQuiz.md)

[Edit a quiz](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_EditaQuiz.md)

## Related

- [[r_Assessments|Assessments]]
- [[c_CreateQuizzesWithForms|Create quizzes with forms]]
- [[t_CreateAQuizQuestion|Create quiz questions]]
- [[t_ConfigureATemplateQuestion|Configure a template question]]
- [[t_CreateAnAssessmentSignature|Create an assessment signature]]
- [[t_CreateaQuiz|Create a quiz]]
- [[t_EditaQuiz|Edit a quiz]]
- [[t_EnableAQuizRetake|Enable a quiz retake]]
- [[t_ViewAQuizResult|View a quiz result]]
- [[using-quizzes|Using Quizzes]]
- [[t_ViewACategoryResult|View an assessment category result]]
- [[t_ViewAQuizScorecard|View a quiz scorecard]]
- [[c_Quizzes|Quizzes]]
- [[check-box|Check box]]
- [[yes-no|Yes/No]]
- [[reference|Reference]]
- [[t_ConfigureaQuiz|Configure a quiz]]
