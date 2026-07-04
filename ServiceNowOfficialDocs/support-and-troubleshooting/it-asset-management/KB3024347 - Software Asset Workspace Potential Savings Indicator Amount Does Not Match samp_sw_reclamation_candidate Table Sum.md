---
title: "Software Asset Workspace: Potential Savings Indicator Amount Does Not Match samp_sw_reclamation_candidate Table Sum"
aliases:
  - KB3024347
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3024347
kb_number: KB3024347
last_modified: 2026-05-17
---

## Software Asset Workspace: Potential Savings Indicator Amount Does Not Match samp\_sw\_reclamation\_candidate Table Sum

  

### Issue

 

The Potential Savings amount displayed in the Software Asset Workspace (Software Asset Overview) does not match the sum of the `potential_savings` field when queried directly on the `samp_sw_reclamation_candidate` table.

### Symptoms

 

-   The Potential Savings indicator value shown in **Software Asset Workspace > Software Asset Overview** differs from the total calculated by summing records directly on the `samp_sw_reclamation_candidate` table.
-   The discrepancy may appear as a higher or lower value than expected when compared against a manual query or list view aggregate.

### Facts

 

-   The Potential Savings value in the Software Asset Overview is populated by the Performance Analytics (PA) Indicator: _SAM Potential Savings from Removal Candidates_.
    -   Indicator sys\_id: `f33f5b8d08e26010f877a5cec59e9751`
    -   Measurement: Daily, unit = USD ($)
    -   Data Source: _SAM Potential Savings from Removal Candidates_
    -   Source Table: `samp_sw_reclamation_candidate`
    -   Filter Applied: `Active = true`
-   The indicator score is collected by the scheduled job _SAM - Daily Job_.
    -   Job sys\_id: `ffc55a94dbfb22003fc57bfdae9619d9`
    -   Collection Window: 1 Day ago to 1 Day ago (relative)
    -   Timezone: US/Eastern (as configured in the _Run as tz_ field)
    -   Indicator Source Used: _SAM Active Removal Candidates Daily_
    -   Source Table: `samp_sw_reclamation_candidate`
    -   Filter Applied: `Active = true`

### Release

All Releases

### Cause

 

The Potential Savings value in the Software Asset Overview reflects a PA indicator score collected during the previous day's scheduled job run, not a real-time sum of the current `samp_sw_reclamation_candidate` table. The displayed value may differ from a live table query due to one or more of the following:

-   **Data staleness** — The indicator is collected once daily. Any changes to reclamation candidates (additions, removals, or active flag updates) after the last job run will not be reflected until the next execution of _SAM - Daily Job_.
-   **Timezone offset** — The job collects scores based on the US/Eastern timezone. If the instance or user is in a different timezone, the collection window may not align with expectations.
-   **Active filter timing** — Records deactivated or activated between job runs will affect the live table sum but will not impact the stored indicator score until the next collection cycle.

### Resolution

 

Step 1: Confirm the PA Indicator Configuration

1.  Navigate to **Performance Analytics > Indicators > All Indicators**.
2.  Search for and open the indicator: _SAM Potential Savings from Removal Candidates_ (sys\_id: `f33f5b8d08e26010f877a5cec59e9751`).
3.  Verify the data source points to `samp_sw_reclamation_candidate` with the filter `Active = true`.

Step 2: Review the SAM Daily Job Last Run Time

1.  Navigate to **System Scheduler > Scheduled Jobs** and open the _SAM - Daily Job_ record (sys\_id: `ffc55a94dbfb22003fc57bfdae9619d9`).
2.  Confirm the Last run time and verify the job executed successfully.
3.  Check the **Run as tz** field and confirm the US/Eastern timezone is correctly configured for the environment.

Step 3: Manually Trigger the Scheduled Job (If Needed)

1.  From the _SAM - Daily Job_ record, click **Execute Now** to force an immediate score collection.
2.  After execution completes, refresh **Software Asset Workspace > Software Asset Overview** and verify the Potential Savings value updates.

Step 4: Validate the Live Table Sum

1.  Navigate to `samp_sw_reclamation_candidate.list` in a browser tab.
2.  Apply the filter: `Active = true`.
3.  Use the list view aggregate or a background script to sum the `potential_savings` field.
4.  Compare this value against the PA indicator score collected during the last job run — a difference is expected if records have changed since the last collection window.

Step 5: Assess Ongoing Discrepancy

-   If the discrepancy persists after the job runs successfully, review whether any business rules, data policies, or transforms are modifying the `potential_savings` field on reclamation candidate records outside of the standard SAM reclamation process.
-   If the timezone configuration does not match the instance's primary operating region, consider adjusting the **Run as tz** field on the _SAM - Daily Job_ to align collection timing with business expectations.

### Related Links

 

-   [Software reclamation candidates](https://docs.servicenow.com/bundle/latest/page/product/software-asset-management2/concept/sam-reclamation-candidates.html)
-   [Performance Analytics overview](https://docs.servicenow.com/bundle/latest/page/product/performance-analytics/concept/c_PerformanceAnalytics.html)
