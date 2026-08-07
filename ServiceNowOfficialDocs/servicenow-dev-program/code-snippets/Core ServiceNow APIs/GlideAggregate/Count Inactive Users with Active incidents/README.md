---
title: "Count Inactive Users with Active incidents"
aliases:
  - Count Inactive Users with Active incidents
tags:
  - servicenow-dev-program
  - code-snippet
  - count-inactive-users-with-active-incidents
  - glideaggregate
---

Count Active Incidents Assigned to Inactive Users 

This script uses GlideAggregate to efficiently count the number of active incidents assigned to inactive users. 

This is a crucial task for maintaining data hygiene and preventing incidents from being stalled due to inactive assignees. 

Overview The script performs the following actions: Initializes GlideAggregate: Creates an aggregate query on the incident table. 

Filters Records: Uses addQuery() to restrict the search to incidents that are both active (true) and assigned to a user whose active status is false.

This filter uses a "dot-walk" on the assigned_to field to check the user's active status directly within the query.

Aggregates by Count: Uses addAggregate() to count the number of incidents, grouping the results by assigned_to user.

Executes and Logs: Runs the query, then loops through the results. 

For each inactive user found, it logs their name and the number of active incidents assigned to them. Use case This script is essential for regular cleanup and maintenance. 

It can be used in: Scheduled Job: Automatically run the script daily or weekly to monitor for and report on incidents assigned to inactive users. 

Installation As a Scheduled Job Navigate to System Definition > Scheduled Jobs.


Click New and select Automatically run a script of your choosing. Name the job (e.g., Find Incidents Assigned to Inactive Users).


Set your desired frequency and time. Paste the script into the Run this script field. Save and activate the job. As a Fix Script Navigate to System Definition > Fix Scripts.

Click New. Name it (e.g., Find Active Incidents with Inactive Assignee).


Paste the script into the Script field. Run the script to see the results in the System Log. 


Customization Targeted tables: Change the table name from incident to task or any other table with an assigned_to field to check for active records assigned to inactive users.


Automated reassignment: Extend the script to automatically reassign the incidents to a group or another user. This is a common practice to ensure that tickets do not get stuck in the queue. Email notification: Instead of logging the information, modify the script to send an email notification to the group manager or another stakeholder with the list of incidents needing attention.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Get Incident Count by Priority/README|Get Incident Count by Priority]]
