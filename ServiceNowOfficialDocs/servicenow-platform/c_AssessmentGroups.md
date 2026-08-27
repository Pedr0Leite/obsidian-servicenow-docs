---
title: Assessment groups
description: An assessment group is a container for assessment instances and assessment results generated in a single occurrence.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_AssessmentGroups.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# Assessment groups

An assessment group is a container for [[c_AssessmentInstances|assessment instances]] and [[r_AssessmentResults|assessment results]] generated in a single occurrence.

The system generates an assessment group every time the scheduled job runs or the API is called, when there is at least one assessable record associated to a category in the type. You can find assessment group records in **[[r_Assessments|Assessments]]** &gt; **Assessment Groups**.

The Assessment Group form displays the group **Number**, the associated **Metric type**, and these related lists:

-   **Assessment Instances**: Lists all assessment instances within this group. There may be no records in this related list. The system does not generate assessment instances if there are only scripted metrics for the type.
-   **Metric Results**: Lists all [[t_ViewAMetricResult|metric results]] for this group. There may be no records in this related list initially. The system generates metric results immediately for scripted metrics, but not for non-scripted metrics, which appear as questions on assessments and require user response. The system dynamically updates the records in this list as users complete [[c_AssessmentQuestionnaires|assessment questionnaires]].
-   **Assessment [[r_CategoryResults|Category Results]]**: Lists all [[t_ViewACategoryResult|category results]] for this group. There may be no records in this related list initially. The system generates category results immediately if there are only scripted metrics in a category. Otherwise, the system does not calculate category results until a user completes an assessment questionnaire that contains questions from the category.

**Note:** To prevent the loss of important assessment data, you cannot delete an assessment group if it contains any assessment instances, metric results, or category results.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[t_ViewAMetricResult|View a metric result]]
- [[t_ViewACategoryResult|View an assessment category result]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[c_AssessmentInstances|Assessment instances]]
- [[r_AssessmentResults|Assessment results]]
- [[r_Assessments|Assessments]]
- [[c_AssessmentQuestionnaires|Assessment questionnaires]]
- [[r_CategoryResults|Category results]]
