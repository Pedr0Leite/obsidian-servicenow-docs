---
title: "Sync Fields for two tables"
aliases:
  - Sync Fields for two tables
tags:
  - servicenow-dev-program
  - code-snippet
  - sync-fields-for-two-tables
  - business-rules
---

**Scenario**: Synchronize fields between two different tables.

**Example**: Any changes made to the fields on the New Hire HR Case for a user, where the same field also exists on the HR Profile, will automatically be updated on the HR Profile when the field is modified on the case.
Fields on the case that are derived from the HR Profile are excluded from this synchronization.

**Script Logic**: An after-update business rule that checks the updated fields in the current table (HR case) exist in the other table (HR Profile) and updates them accordingly.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
