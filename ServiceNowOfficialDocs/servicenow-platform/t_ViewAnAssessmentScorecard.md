---
title: View an assessment scorecard
description: The Assessments application prepares printable scorecards. A scorecard displays easy-to-interpret assessment results, in which the current calculated ratings for an assessable record are compared to previous ratings or to the ratings of other records.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/t\_ViewAnAssessmentScorecard.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - type-task
---

# View an assessment scorecard

The [[r_Assessments|Assessments]] application prepares printable scorecards. A scorecard displays easy-to-interpret [[r_AssessmentResults|assessment results]], in which the current calculated ratings for an assessable record are compared to previous ratings or to the ratings of other records.

## Before you begin

Role required: assessment\_admin or admin

## About this task

Users can examine ratings over time, compare ratings for one assessable record with all [[c_assessable-records|assessable records]] in a table, or compare the ratings of two assessable records. All ratings are averages for the time range selected. The system dynamically updates a scorecard each time you view it, so the ratings reflect recently completed assessments and scripted metrics.

Administrators can display a scorecard for any table by creating a **Related Link** on assessable records. The system provides this link on the Company form by default when Vendor Performance is active.

The Vendor Performance application provides an enhanced scorecard view for vendors.

See Vendor Performance in . [Project Portfolio Suite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/c_ProjectPortfolioSuite.md).

## Procedure

1.  Navigate to **All** &gt; **Assessments** &gt; **Assessable Records**.

2.  Open a record.

3.  Under **Related Links**, click **View Scorecard**.


-   **[[t_CreateALinkToAScorecard|Create a link to a scorecard]]**  
Users with the admin role can create UI actions that allow users to view scorecards from tables.
-   **[[r_Averages|Assessment scorecard averages]]**  
The Averages view compares the current ratings for an assessable record in each metric category with the average, minimum, and maximum values from all assessable records in the filter. All ratings are from assessments generated over the trailing twelve months \(TTM\).
-   **[[r_Categories|Assessment scorecard categories]]**  
The Categories view displays a bar chart showing the [[r_AverageRatings|average ratings]] for each category in the selected time interval.
-   **[[r_CategoryMetrics|Assessment scorecard category metrics]]**  
The Category Metrics view displays the weighted average results for each metric within a category. Use this view to learn how individual metrics affect the overall rating for the category.
-   **[[r_HeadToHeadCompare|Assessment scorecard head-to-head compare view]]**  
The Head to Head Compare view allows you to compare the ratings of two assessable records of the same type. Select an assessable record from the choice list to compare against the current record's trailing twelve month \(TTM\) ratings.
-   **[[r_History|Assessment scorecard history]]**  
The History view compares the current ratings for each category with ratings from the previous three years or four quarters.
-   **[[r_LiveFeed|Live feed view of assessable records]]**  
The Live Feed view displays Live Feed conversations that apply to the assessable record. Users can view the group feed, including tagged comments, and add comments of their own.
-   **[[r_Ratings|Assessment scorecard ratings]]**  
The scorecard ratings section displays various ratings for the assessable record.

**Parent Topic:**[[c_AssessmentProcess|Assessment administrator tasks]]

## Related

- [[t_CreateALinkToAScorecard|Create a link to a scorecard]]
- [[r_Averages|Assessment scorecard averages]]
- [[r_Categories|Assessment scorecard categories]]
- [[r_CategoryMetrics|Assessment scorecard category metrics]]
- [[r_HeadToHeadCompare|Assessment scorecard head-to-head compare view]]
- [[r_History|Assessment scorecard history]]
- [[r_LiveFeed|Live feed view of assessable records]]
- [[r_Ratings|Assessment scorecard ratings]]
- [[c_AssessmentProcess|Assessment administrator tasks]]
- [[r_Assessments|Assessments]]
- [[r_AssessmentResults|Assessment results]]
- [[c_assessable-records|Assessable records]]
- [[r_AverageRatings|Average ratings]]
