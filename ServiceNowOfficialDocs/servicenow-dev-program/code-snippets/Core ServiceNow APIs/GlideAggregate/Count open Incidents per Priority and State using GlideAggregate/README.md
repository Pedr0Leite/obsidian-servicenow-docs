---
title: "Count open Incidents per Priority and State using GlideAggregate"
aliases:
  - Count open Incidents per Priority and State using GlideAggregate
tags:
  - servicenow-dev-program
  - code-snippet
  - count-open-incidents-per-priority-and-state-using-glideaggregate
  - glideaggregate
---

# Count open Incidents per Priority and State using GlideAggregate

## Overview
This script will dynamically calculate the **number of open incidents** for each priority level and also give you a total for what 
current state the Incident is in using **server-side scripting**
Priority levels typically include:  
+ 1 – Critical  
+ 2 – High  
+ 3 – Moderate  
+ 4 – Low

Incident State typically include:
+ New
+ In Progress
+ On Hold
+ Resolved
+ Closed
+ Canceled

The scripting solution leverages **GlideAggregate** to efficiently count records grouped by priority and state. This scripts approach
is useful for:
+ Dashboards
+ Business Rules
+ SLA monitoring and reporting
 
--
## Table and Fields
+ **Table:** Task
+ **Fields:** Priority, State

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Get Incident Count by Priority/README|Get Incident Count by Priority]]
