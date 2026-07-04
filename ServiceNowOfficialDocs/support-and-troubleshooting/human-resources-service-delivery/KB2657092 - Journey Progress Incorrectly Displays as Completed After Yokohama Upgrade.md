---
title: " Journey Progress Incorrectly Displays as Completed After Yokohama Upgrade"
aliases:
  - KB2657092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657092
kb_number: KB2657092
last_modified: 2026-01-02
---

## Journey Progress Incorrectly Displays as Completed After Yokohama Upgrade

  

### Issue

After upgrading to Yokohama, the HR portal’s journey list view incorrectly shows all journeys as completed, even when open tasks remain. This affects accurate progress and state representation for journeys and impacts multiple environments.

### Release

Yokohama

### Cause

A defect (PRB1928897) in the journey progress calculation logic after the Yokohama upgrade causes incorrect progress display when tasks are updated by users other than the assigned/subject/mentor.

### Resolution

To resolve the issue:

-   Override the \_buildJourneyObject method in the jny\_JourneyService script include.
-   Update the method to use:

JavaScript

new sn\_jny.jny\_JourneyProgressUtils(journeyRecord).updateJourneyLeProgress(true);

Show more lines

-   Optionally, update the getAllJourneyInfo method in jny\_JourneyPortalDetails similarly.
-   Validate the fix in a lower environment before applying to production.
-   Monitor PRB1928897 for updates on the permanent fix from ServiceNow.
