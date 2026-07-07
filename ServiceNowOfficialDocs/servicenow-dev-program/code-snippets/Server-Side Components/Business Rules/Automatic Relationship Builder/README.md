---
title: "Automatic Relationship Builder"
aliases:
  - Automatic Relationship Builder
tags:
  - servicenow-dev-program
  - code-snippet
  - automatic-relationship-builder
  - business-rules
---

# ServiceNow Automatic Relationship Builder  
**Auto-create CMDB relationships dynamically on CI insert or update**

---

## Overview

The **Automatic Relationship Builder** ensures that your CMDB stays complete and accurate by automatically creating parent–child relationships between Configuration Items (CIs) whenever they are inserted or updated.  

Instead of manually linking servers, applications, and databases, this Business Rule dynamically establishes **"Runs on"**, **"Depends on"**, or **"Connected to"** relationships based on CI attributes.

---

## Key Highlights

Builds CMDB relationships automatically  
Eliminates manual linking of dependent CIs  

---

## Use Case

When a new **Application CI** is created or discovered and its **host CI (server)** is known,  
the script automatically builds a relationship of type **“Runs on::Runs”** between the two.

This keeps your CMDB up-to-date without human intervention.

---

## Table and Trigger

| Item | Value |
|------|-------|
| **Table** | `cmdb_ci_appl` |
| **Trigger** | After Insert / After Update |
| **Condition** | `u_host` field is populated |
| **Purpose** | Create a “Runs on” relationship between host and application |

---

## Script — Business Rule


Business Rule: Auto Relationship Builder
Table: cmdb_ci_appl
When: after insert / after update

## Example Input (New CI Record)
| Field  | Value                        |
| ------ | ---------------------------- |
| Name   | Payroll Application          |
| Class  | Application (`cmdb_ci_appl`) |
| u_Host | APP-SERVER-01                |
| Owner  | IT Operations                |

## Example Output (Created Relationship)

| Field  | Value               |
| ------ | ------------------- |
| Parent | APP-SERVER-01       |
| Child  | Payroll Application |
| Type   | Runs on :: Runs     |
| Table  | cmdb_rel_ci         |
Relationship automatically visible in CI Relationship Viewer.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
