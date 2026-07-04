---
title: "The 'Subscription Consumption' tab is missing in the Software Asset Workspace for a specific integration profiles."
aliases:
  - KB2611216
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2611216
kb_number: KB2611216
last_modified: 2025-11-11
---

## The 'Subscription Consumption' tab is missing in the Software Asset Workspace for a specific integration profiles.

  

## Table of Contents

-   [Symptoms](#mcetoc_1j9evup162c)
-   [Cause](#mcetoc_1j9evup162d)
-   [Resolution](#mcetoc_1j9evup162e)
-   [Additional Information](#mcetoc_1j9f019hk9a)

## Symptoms

The Subscription Consumption tab is missing in the Software Asset Workspace for Salesforce integration profiles.

Consumption data exists in the sam\_saas\_consumption\_summary\_list table and the consumption job has runs successfully.

## Cause

The OOB views do not include the related list for Subscription Consumption Summary by default.

This is expected behavior because ServiceNow allows you to change OOB (customizable) views; the tab is not automatically added to these views.

## Resolution

1.  The workspace shows the related list records as tab on a Workspace.
2.  To display the Subscription Consumption tab, you can add a related list record to the view
    1.  Navigate to the form view for the integration profile.
    2.  Open the hamburger menu on the top left of the window
    3.  Configure > Related list
        1.  https://<instance>.service-now.com/slushbucket.do?sysparm\_view=<specific view>&sysparm\_list=samp\_sw\_subscription\_profile
    4.  Move Subscription Consumption Summary – Subscription profile to the right bucket.
3.  Save changes and verify the tab appears in the Software Asset Workspace.

## Additional Information

This is not a defect; it is expected behavior due to customizable views and ability to add or remove tabs from a workspace

If you would like to add this tab included by default, you can submit an enhancement request via our Idea portal [https://support.servicenow.com/ideas](/ideas).
