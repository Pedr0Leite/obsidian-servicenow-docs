---
title: "Auto-Generate Knowledge Article for Resolved Incidents"
aliases:
  - Auto-Generate Knowledge Article for Resolved Incidents
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-generate-knowledge-article-for-resolved-incidents
  - business-rules
---

## Overview
This ServiceNow Business Rule automatically creates a Knowledge Article when an Incident is resolved and includes detailed resolution notes.  
It helps promote knowledge sharing, reduce repeated issues, and improve ITSM efficiency.


## Features
- Automatically creates a Knowledge Article in the **Draft** state.
- Extracts content from the Incident's **Resolution Notes**.
- Prevents duplicate Knowledge Articles by checking for similar issue titles.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
