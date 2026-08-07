---
title: "Licensed User Access Job"
aliases:
  - Licensed User Access Job
tags:
  - servicenow-dev-program
  - code-snippet
  - licensed-user-access-job
  - scheduled-jobs
---

# Weekly Licensed User Access Review (90-Day Inactivity)

# Overview
This scheduled job runs weekly and automatically revokes access for licensed users who have been inactive/last login for more than 90 days.  
It ensures license compliance, cost control, and adherence to security policies.

# Objective
To identify active users holding licensed roles who have not logged into ServiceNow within the past 90 days and revoke their access by removing them from their respective groups.

# Configuration Summary
1. Threshold - 90 days since last login
2. Frequency - Weekly
3. Licensed Roles Checked - 'itil', 'sys_approver', 'admin', 'business_stakeholder'
4. Groups Managed - ITIL Group, Approver Group, Admin Group, Business Stakeholder Group

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
