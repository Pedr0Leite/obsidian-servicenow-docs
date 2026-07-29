---
title: "On-Call Schedule  updating shifts does not reflect without manual Refresh"
aliases:
  - KB0964479
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964479
kb_number: KB0964479
last_modified: 2026-06-24
---

## On-Call Schedule updating shifts does not reflect without manual Refresh

  

### Issue

  
Customer reported an issue updating a roster.  
Users will update on-call schedules within form view, as it opens into a separate browser window, and when going back to platform, there is no refresh option to bring in new updates. Clicking Save does not update unless a change is made from within the Platform view.  
  
This is confusing the end users as the change in not reflected unless they refresh.

**Steps to Reproduce:**   
Navigate to On-Call Scheduling > On-Call Schedules > All On Call  
Select a group Icon  
In the Workbench, select the Shifts tab,  
From the Menu (3 dots), select 'Edit Shift' - this opens the shift record in a separate browser page  
Select the Roster and in Members Related List , remove a member and save  
  
In the Workbench, (which is still open in another browser tab) the update is not reflected.  
  
  

### Release

All

### Cause

This is the Platform behavior. This behavior is also seen OOB.

### Resolution

  
  
  
The behavior is the Platform behavior.  
  
Our Documentation also suggests to make such changes via the Platform, see below for your reference

https://docs.servicenow.com/bundle/quebec-it-service-management/page/administer/on-call-scheduling/task/remove-member-from-roster-oncall.html  
Remove a member from a roster  
Delete shift member record  
  
From the on-call roster:  
Navigate to On-Call Scheduling > My Group Schedules.
