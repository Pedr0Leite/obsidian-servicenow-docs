---
title: "Count All Open Incidents Per Priority"
aliases:
  - Count All Open Incidents Per Priority
tags:
  - servicenow-dev-program
  - code-snippet
  - count-all-open-incidents-per-priority
  - glideaggregate
---

# Count Open Incidents per Priority Using GlideAggregate

## Overview
This script dynamically calculates the **number of open incidents** for each priority level using **server-side scripting** in ServiceNow.  
Priority levels typically include:  
+ 1 – Critical  
+ 2 – High  
+ 3 – Moderate  
+ 4 – Low  

The solution leverages **GlideAggregate** to efficiently count records grouped by priority. This approach is useful for:  
+ Dashboards  
+ Automated scripts  
+ Business rules  
+ SLA monitoring and reporting  

---

## Table and Fields
+ **Table:** `incident`  
+ **Fields:** `priority`, `state`  

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Get Incident Count by Priority/README|Get Incident Count by Priority]]
