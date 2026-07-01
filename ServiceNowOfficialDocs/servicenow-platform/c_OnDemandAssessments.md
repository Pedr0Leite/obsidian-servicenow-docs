---
title: On-demand assessments
description: On-demand assessments can be generated for metric types with the Schedule type field set to On demand.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/c\_OnDemandAssessments.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-concept
---

# On-demand assessments

On-demand assessments can be generated for metric types with the Schedule type field set to On demand.

For the system to properly generate on-demand assessments, the metric type must be active and published. The metric type must also be associated to at least one metric category. That metric category must be associated to one or more of each of the following items:

-   Assessable record
-   Metric

By default, an assessment administrator can generate an on-demand assessment for one assessable record or [[t_GenOnDemandAssessMultAssessRec|multiple assessable records]].

-   **[[t_OnDemandAssessment|Generate an on-demand assessment]]**  
Use on-demand assessments to familiarize yourself with the basic assessment process and test your questionnaires using minimal configuration.
-   **[[t_GenOnDemandAssessOneAssessRec|Generate an on-demand assessment for one assessable record]]**  
When you generate an on-demand assessment from the Assessable Record form, the resulting assessment contains questions from the categories associated to the assessable record.
-   **[Generate an on-demand assessment for multiple assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_GenOnDemandAssessMultAssessRec.md)**  
When you generate an on-demand assessment from the Assessment Metric Type form, the resulting assessment contains questions from all categories associated to any [[c_assessable-records|assessable records]] for the metric type.
-   **[[t_GenAssessmentOnDemandAPI|Generate an assessment with the on-demand API]]**  
The Assign Assessment buttons call an API to generate on-demand assessments.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

**Related topics**  


[[c_AssessmentGeneration|Assessment generation]]

[[c_ScheduledAssessments|Scheduled assessments]]

[Generate an on-demand assessment for multiple assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_GenOnDemandAssessMultAssessRec.md)

[[t_ViewAnAssessmentInstance|View an assessment instance]]

[[t_CleanUpAssessmentData|Clean up assessment data]]

## Related

- [[t_GenOnDemandAssessMultAssessRec|Generate an on-demand assessment for multiple assessable records]]
- [[t_OnDemandAssessment|Generate an on-demand assessment]]
- [[t_GenOnDemandAssessOneAssessRec|Generate an on-demand assessment for one assessable record]]
- [[t_GenAssessmentOnDemandAPI|Generate an assessment with the on-demand API]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[c_AssessmentGeneration|Assessment generation]]
- [[c_ScheduledAssessments|Scheduled assessments]]
- [[t_ViewAnAssessmentInstance|View an assessment instance]]
- [[t_CleanUpAssessmentData|Clean up assessment data]]
- [[c_assessable-records|Assessable records]]
