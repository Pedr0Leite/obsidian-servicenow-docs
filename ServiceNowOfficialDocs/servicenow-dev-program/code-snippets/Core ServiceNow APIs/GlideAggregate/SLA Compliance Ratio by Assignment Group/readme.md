---
title: "SLA Compliance Ratio by Assignment Group"
aliases:
  - SLA Compliance Ratio by Assignment Group
tags:
  - servicenow-dev-program
  - code-snippet
  - sla-compliance-ratio-by-assignment-group
  - glideaggregate
---

Overview

This script calculates the SLA breach percentage for each assignment group based on closed incidents in ServiceNow.
It leverages GlideAggregate to count both total SLAs and breached SLAs efficiently, providing key SLA performance insights.

Useful for:
	•	SLA dashboards
	•	Support performance tracking
	•	Service improvement reports

Objective

To determine, for each assignment group:
	•	How many SLAs were closed
	•	How many of those breached
	•	The resulting SLA compliance percentage

Script Logic
	1.	Query the task_sla table.
	2.	Filter for closed SLAs linked to incidents.
	3.	Aggregate total SLAs (COUNT) and breached SLAs (COUNT, 'breach', 'true').
	4.	Group results by assignment group.
	5.	Calculate breach percentage.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
