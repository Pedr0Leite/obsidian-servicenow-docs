---
title: "SAM - Troubleshooting Data Population Issues on Software Asset Analytics Dashboard"
aliases:
  - KB1996885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1996885
kb_number: KB1996885
last_modified: 2025-03-25
---

## Issue

The SaaS Overview Dashboard on the Software Asset Analytics page is displaying incorrect data across its widgets. The discrepancies may be due to inconsistencies in data processing logic, misconfigured data sources, or errors in aggregation and filtering criteria.

This article provides a detailed breakdown of the data logic behind the numbers displayed on the Software Asset Analytics widgets, including how data is collected, processed, and presented, to help diagnose and resolve discrepancies effectively.

## Resolution

### 1\. Snapshot of Last Meaningful Activity

-   Widget Indicator: `Assigned Subscriptions Monthly`
-   Data Source: `Software Subscriptions` (`samp_sw_subscription`)
-   Filtering Conditions:
    -   `Active = true`
    -   `Product.Subscription software = true`
    -   `Product.Product type = Licensable`
    -   `Licensable software model.License under management = true`
-   Logic: Counts the number of active software subscriptions that meet the defined criteria.

View date here = https://instance.service-now.com/samp\_sw\_subscription\_list.do?sysparm\_query=active%3Dtrue%5Eproduct.subscription\_software%3Dtrue%5Eproduct.product\_type%3Dlicensable%5Elicensable\_software\_model.license\_under\_management%3Dtrue&sysparm\_view=

### 2\. Stale Subscriptions by Instance

-   Widget Indicator: `Stale Subscription by Instance`
-   Data Source: `SAM Reclaimed Candidates Monthly` (`samp_sw_reclamation_candidate`)
-   Filtering Conditions:
    -   `User subscription.Stale license = true`
-   Logic: Counts the total number of records where `Stale license = true`. If no records match the criteria, it returns an empty result.

View Date here = https://instance.service-now.com/samp\_sw\_reclamation\_candidate\_list.do?sysparm\_query=user\_subscription.stale\_license%3Dtrue&sysparm\_view=

### 3\. Potential Savings by Instance

-   Widget Indicator: `Potential Software Subscription Savings`
-   Data Source: `SAM Reclaimed Candidates Monthly` (`samp_sw_reclamation_candidate`)
-   Filtering Conditions:
    -   `User subscription.Stale license = true`
    -   `Active = true`
-   Logic: Finds all matching records, extracts the `potential_savings` field, and calculates the total sum.

View Date here = https://instance.service-now.com/samp\_sw\_reclamation\_candidate\_list.do?sysparm\_query=user\_subscription.stale\_license%3Dtrue%5Eactive%3Dtrue&sysparm\_view=

### 4\. User Summary - Subscription Assigned

-   Data Source: `data.sam__user_summary_1.output.1.count`
-   Data Broker Server Script: `"SAM - User Summary"`
    -   [View Script](https://instance.service-now.com/nav_to.do?uri=sys_ux_data_broker_transform.do?sys_id=fd603231532011107f77ddeeff7b1223)
-   Logic:
    -   The script retrieves user summary data.
    -   The metric `SAMWorkspaceCommUtil.USER_SUBSCRIPTION_LICENSE_METRIC` is used to filter results.
    -   It identifies user subscription licenses linked to entitlements associated with a software model.

View Date here = https://instance.service-now.com/samp\_sw\_subscription\_list.do?sysparm\_query=product.subscription\_software%3Dtrue%5Esoftware\_model.sw\_product\_type%3Dlicensable%5Elicensable\_software\_model.license\_under\_management%3Dtrue%5Elicense\_metric\_result.license\_metric%3D48c5d8d293200300544814f1b47ffb45&sysparm\_view=

For more details on data logic and visualization, refer to the official [ServiceNow SaaS Dashboard Documentation](https://www.servicenow.com/docs/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/reference/saas-dashboard-workspace.html).
