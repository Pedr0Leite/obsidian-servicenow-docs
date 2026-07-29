---
title: "EnhanceIncidentWithProblem"
aliases:
  - EnhanceIncidentWithProblem
tags:
  - servicenow-dev-program
  - code-snippet
  - enhanceincidentwithproblem
  - business-rules
---

# Enhance Incident Description with Linked Problem Statement

## Overview
This ServiceNow Business Rule enhances Incident records by automatically appending the short description of a linked Problem record. It improves visibility and context for support teams working on related incidents.

## Features
- Triggered when a Problem ID is newly linked or changed on an Incident.
- Fetches the Problem's short description and number.
- Appends the Problem Statement to both the Incident's short description and description fields.
- Includes general error handling to ensure stability.

## Business Rule Configuration
- Table: `incident`
- When to Run: `before insert` and `before update`
- Condition: 
  ```javascript
  current.problem_id.changes() || !previous

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
