---
title: "User Activity Log Tracking"
aliases:
  - User Activity Log Tracking
tags:
  - servicenow-dev-program
  - code-snippet
  - user-activity-log-tracking
  - business-rules
---

# Overview
This script logs specific user actions (e.g: record updates and approvals) in ServiceNow into a custom table `u_user_activity_log`. 

This provides audit capabilities and allowing developers to track user actions for compliance or analytics.

# How It Works
The script is triggered by a Business Rule on record updates and checks for changes in specified critical fields (e.g., `state`, `approval`). When a change occurs, it logs relevant details in the `u_user_activity_log` table, including:
- `u_user`: User ID
- `u_action`: Type of action performed
- `u_record_id`: ID of the updated record
- `u_record_table`: Name of the table where the change occurred
- `u_description`: Brief description of the action

# Implementation
- Create Custom Table: Ensure `u_user_activity_log` table exists with fields like `u_user`, `u_action`, `u_record_id`, `u_record_table`, `u_description`, etc.
- Configure Business Rule: Set the Business Rule to run on update and add conditions for monitoring fields (`state`, `approval`).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
