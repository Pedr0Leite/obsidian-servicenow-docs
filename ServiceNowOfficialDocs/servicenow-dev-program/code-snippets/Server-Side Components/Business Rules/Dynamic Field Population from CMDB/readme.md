---
title: "Dynamic Field Population from CMDB"
aliases:
  - Dynamic Field Population from CMDB
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamic-field-population-from-cmdb
  - business-rules
---

Project Description

Dynamic Field Population from CMDB is a reusable ServiceNow solution that automatically fills key fields on incidents, tasks, or change requests based on the selected Configuration Item (CI). By fetching data such as Owner, Assignment Group, Location, Department, and Business Service directly from the CMDB, this project reduces manual effort, ensures data consistency, and improves ITSM efficiency.

It leverages a Business Rule that triggers on record insert or update, combined with a Script Include that handles dynamic mapping of CI fields to target fields. The solution can be extended for multiple tables, integrated with the Service Portal via GlideAjax, and configured using a JSON or mapping table for maximum flexibility.

Key Benefits:

Saves time for agents by auto-filling fields.

Reduces errors and ensures standardized data.

Reusable across multiple tables (Incident, Change, Problem).

Easily configurable for different CI-to-field mappings.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
