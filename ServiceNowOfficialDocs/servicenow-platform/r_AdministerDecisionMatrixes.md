---
title: Decision matrixes
description: Assessment results obtained by questionnaires and scripted metrics can be mapped to decision matrixes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/r\_AdministerDecisionMatrixes.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Create a decision matrix, Assessment administrator tasks, Using assessments, Assessments, Assessments and Surveys, Exploring Service Administration, Service Administration, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Decision matrixes

[[r_AssessmentResults|Assessment results]] obtained by questionnaires and scripted metrics can be mapped to decision matrixes.

Assessment administrators can view and create these dynamically updated graphs, which make it possible to compare [[c_assessable-records|assessable records]] by category. Decision matrixes display data from a trailing twelve month \(TTM\) period.

**Note:** Assessment administrators can access decision matrixes through the Assessment application and vendor managers can access them through the  application.

## Decision matrix components

The decision matrix page has these components:

<table id="table_bkg_m2m_q4"><thead><tr><th>

Component

</th><th>

Description

</th></tr></thead><tbody><tr><td class="sub-head" colspan="2">

Options

</td></tr><tr><td>

Filter

</td><td>

Select the subset of assessable records you want to view. The filter options available vary by metric type, based on the **Filter** field and **Filter condition** field settings for each type.\[Omitted image "DecisionMatrixComponents.png"\] Alt text: Decision matrix components

 The maximum values in the filter are controlled by the **Maximum number of items to show for a decision matrix field filter** property **\(com.snc.assessment.decision\_matrix\_filter\_max\_entries\)**, which has a default value of 1000.

</td></tr><tr><td>

Scale

</td><td>

Select the scale for the decision matrix. The greater the scale, the larger the decision matrix appears.

</td></tr><tr><td class="sub-head" colspan="2">

Decision matrix

</td></tr><tr><td>

X- and Y-axes

</td><td>

Each axis represents one or more metric categories. If multiple categories are used for an axis, their respective[[c_AssessmentMetrics|weights]] determine the positioning of the plotted items.

</td></tr><tr><td>

Plotted items

</td><td>

The labeled points you see on a decision matrix, called plotted items, represent averages of [[r_CategoryResults|category result]] data for assessable records. Point to a plotted item [[label|label]] to view a rating summary for that assessable record. Click a plotted item label to view the [[t_ViewAnAssessmentScorecard|scorecard]] for the assessable record.\[Omitted image "VendorDecisionMatrix.png"\] Alt text: Vendor decision matrix

</td></tr></tbody>
</table>## Plotted item rating summaries

If you point to a plotted item label on a decision matrix, a rating summary appears. The summary displays the assessable record's [[r_AverageRatings|average ratings]] for each axis. If an axis represents one metric category, the ratings are calculated averages from results for that category. If an axis represents multiple categories, the ratings are calculated averages from weighted results for all of the categories.

The summary shows:

-   Current rating
-   Difference between the current rating and the rating from the previous year
-   Ratings from each previous year, going back three years

\[Omitted image "DecisionMatrixRatingSummary.png"\] Alt text:

**Parent Topic:**[[t_CreateADecisionMatrix|Create a decision matrix]]

## Related

- [[c_AssessmentMetrics|Assessment metrics]]
- [[r_CategoryResults|Category results]]
- [[t_ViewAnAssessmentScorecard|View an assessment scorecard]]
- [[t_CreateADecisionMatrix|Create a decision matrix]]
- [[r_AssessmentResults|Assessment results]]
- [[c_assessable-records|Assessable records]]
- [[label|Label]]
- [[r_AverageRatings|Average ratings]]
