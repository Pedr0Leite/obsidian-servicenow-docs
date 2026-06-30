---
title: Associate multiple category users to multiple assessable records
description: The stakeholder list helper in the create stakeholders module is the most efficient way to associate multiple category users to multiple assessable records in a single interface.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_AssocMultCatUsrsToMultAssessRecs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Category users and stakeholders, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Associate multiple category users to multiple assessable records

The stakeholder list helper in the create stakeholders module is the most efficient way to associate multiple category users to multiple assessable records in a single interface.

## Before you begin

Role required: assessment\_admin or admin

## About this task

You can select category users from one category at a time.

**Note:** You cannot edit or delete stakeholders using the list helper.

## Procedure

1.  Navigate to **All** &gt; **[[r_Assessments|Assessments]]** &gt; **Advanced** &gt; **Create Stakeholders**.

    The stakeholder list helper appears.

2.  Select a metric type from the list of available types.

    **Note:** Only metric types for [[c_ScheduledAssessments|scheduled assessments]] are available. [[c_OnDemandAssessments|On-demand assessments]] do not use category users or stakeholders.

3.  Select a category from the list of available categories.

    **Note:** Only categories within the selected metric type are available.

    The system populates the **Category User** and **[[c_assessable-records|Assessable Records]]** lists with category users and assessable records associated to the selected category.

4.  Select one or more category users from the **Category Users** list.

5.  Select one or more assessable records from the **Assessable Records** list.

6.  Click the **Associate** arrow between the lists to complete the association.

    A message above the list helper advises you that the selected category users are now stakeholders for the selected assessable records.


-   **[[t_DelAStakeholderForMultAssessRecs|Delete a stakeholder for multiple assessable records]]**  
You can delete stakeholders for multiple assessable records.

**Parent Topic:**[[r_CategoryUsersAndStakeholders|Category users and stakeholders]]

**Related topics**  


[Category users and stakeholders](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/r_CategoryUsersAndStakeholders.md)

[[t_CreateACategoryUser|Create a category user]]

[[t_AssocMultCatUsrsToOneAssessRec|Associate multiple category users to one assessable record]]

[[t_AssocOneCatUsrToOneAssessRec|Associate one category user to one assessable record]]

[Delete a stakeholder for multiple assessable records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_DelAStakeholderForMultAssessRecs.md)

[[t_DelAStakeholderForOneAssessRec|Delete a stakeholder for one assessable record]]

## Related

- [[t_DelAStakeholderForMultAssessRecs|Delete a stakeholder for multiple assessable records]]
- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
- [[t_CreateACategoryUser|Create a category user]]
- [[t_AssocMultCatUsrsToOneAssessRec|Associate multiple category users to one assessable record]]
- [[t_AssocOneCatUsrToOneAssessRec|Associate one category user to one assessable record]]
- [[t_DelAStakeholderForOneAssessRec|Delete a stakeholder for one assessable record]]
- [[r_Assessments|Assessments]]
- [[c_ScheduledAssessments|Scheduled assessments]]
- [[c_OnDemandAssessments|On-demand assessments]]
- [[c_assessable-records|Assessable records]]
