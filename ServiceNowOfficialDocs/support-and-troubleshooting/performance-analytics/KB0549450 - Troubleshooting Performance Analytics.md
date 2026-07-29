---
title: "Troubleshooting Performance Analytics"
aliases:
  - KB0549450
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549450
kb_number: KB0549450
last_modified: 2026-03-27
---

## Issue

This article contains information about troubleshooting issues in Performance Analytics, a ServiceNow performance management tool that enables you to align resources, systems, and employees to objectives and priorities.

### No data shown for a particular indicator

**Question**: I do not see any data on the scorecard/dashboard for a particular indicator, though I am sure there is data in the system.

**Answer**: The most likely causes are:

-   The indicator is not included in any job.  
    1.  Navigate to **Performance Analytics > Data Collector > Jobs**. You need the _pa\_admin_ or _pa\_data\_collector_ role for this.
    2.  Scroll down to the bottom of the form and check if the indicator is included in the **Indicators** related list.
    3.  If not, click **Edit** and add the indicator.
    4.  **Save**.
    5.  You can also view the Job Logs and see if there are any errors or warnings for this indicator.
-   One of the restraints in the Performance Analytics Data Collector properties may have prevented the data for the indicator to be collected.  
    1.  Navigate to **Performance Analytics > System > Properties**
    2.  Check the settings in the **Performance Analytics Data Collector** section.

### No data shown for a particular breakdown

**Question**: I do not see any data on the scorecard/dashboard for a particular breakdown, though I am sure there is data in the system.

**Answer**: The most likely causes are:

-   The indicator that the breakdown is part of is not included in any job. See the previous question.
-   There are too many breakdown elements to be included in a data collection, or the maximum number of elements produced by combining two breakdowns to be included in data collection has been exceeded. Check **Performance Analytics > System > Properties**.
-   The breakdown is excluded in the **Breakdown matrix exclusions** list.  
    1.  Navigate to **Performance Analytics > Indicators > Automated Indicators**.
    2.  Open the indicator that does not show any scores.
    3.  Scroll down to the bottom of the indicator form.
    4.  Click the **Breakdown matrix exclusions** tab.
    5.  Check if the breakdown is in the exclusions list.
    6.  Remove the breakdown from the exclusions list.
    7.  **Update**.
