---
title: Create stakeholders automatically
description: You can configure the system to create stakeholders automatically from all category users and assessable records associated with a category using the Create stakeholders check box on the Metric Category form.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_CreateAStakeholderAutomatically.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Category users and stakeholders, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Create stakeholders automatically

You can configure the system to create stakeholders automatically from all category users and [[c_assessable-records|assessable records]] associated with a category using the **Create stakeholders** [[check-box|check box]] on the [[metric-category-form|Metric Category form]].

## Before you begin

Role required: assessment\_admin or admin

## About this task

If you associate a user to the category, the system makes the resulting category user a stakeholder for all the assessable records associated to the category. Similarly, if you associate a new assessable record to the category, the system makes all category users stakeholders for that record if they are not already stakeholders.

**Note:** Use the **Create stakeholders** check box with caution. You can end up with more stakeholders than you want and a large amount of unnecessary assessment data. Automatic stakeholder creation is best suited to assessment implementations in which category users are knowledgeable about all or most of the assessable records associated to each category.

## Procedure

1.  Navigate to **All** &gt; **[[r_Assessments|Assessments]]** &gt; **Metric Definition** &gt; **Categories**.

2.  Select a category.

3.  Associate category users and assessable records to the category.

4.  Select the **Create stakeholders** check box.

5.  Click **Update**.

    All the category users are associated to all the assessable records as stakeholders.

6.  In the **Assessable Records** related list, click **Edit**.

7.  Using the slushbucket, associate an assessable record to the category.

8.  Click **Save**.

    The system makes all category users stakeholders for the new assessable record.

9.  Delete stakeholders as needed.


**Parent Topic:**[[r_CategoryUsersAndStakeholders|Category users and stakeholders]]

**Related topics**  


[Category users and stakeholders](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/r_CategoryUsersAndStakeholders.md)

[[t_CreateACategoryUser|Create a category user]]

[[t_AssocMultCatUsrsToMultAssessRecs|Associate multiple category users to multiple assessable records]]

[[t_AssocMultCatUsrsToOneAssessRec|Associate multiple category users to one assessable record]]

[[t_AssocOneCatUsrToOneAssessRec|Associate one category user to one assessable record]]

[[t_DelAStakeholderForMultAssessRecs|Delete a stakeholder for multiple assessable records]]

[[t_DelAStakeholderForOneAssessRec|Delete a stakeholder for one assessable record]]

## Related

- [[r_CategoryUsersAndStakeholders|Category users and stakeholders]]
- [[t_CreateACategoryUser|Create a category user]]
- [[t_AssocMultCatUsrsToMultAssessRecs|Associate multiple category users to multiple assessable records]]
- [[t_AssocMultCatUsrsToOneAssessRec|Associate multiple category users to one assessable record]]
- [[t_AssocOneCatUsrToOneAssessRec|Associate one category user to one assessable record]]
- [[t_DelAStakeholderForMultAssessRecs|Delete a stakeholder for multiple assessable records]]
- [[t_DelAStakeholderForOneAssessRec|Delete a stakeholder for one assessable record]]
- [[c_assessable-records|Assessable records]]
- [[check-box|Check box]]
- [[metric-category-form|Metric Category form]]
- [[r_Assessments|Assessments]]
