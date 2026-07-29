---
title: "LicensedUserCount"
aliases:
  - LicensedUserCount
tags:
  - servicenow-dev-program
  - code-snippet
  - licensedusercount
  - glideaggregate
---

# Licensed User Count by Role Using GlideAggregate

# Overview
This script counts how many **licensed users** hold specific ServiceNow roles using the `GlideAggregate` API.  
It’s useful for **license compliance**, **role audits**, and **access management reporting**.

The licensed roles analyzed:
- sys_approver  
- itil  
- business_stakeholder  
- admin  

# Objective
To provide a simple, fast, and accurate way to count licensed users per role directly at the database level using `GlideAggregate`.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
