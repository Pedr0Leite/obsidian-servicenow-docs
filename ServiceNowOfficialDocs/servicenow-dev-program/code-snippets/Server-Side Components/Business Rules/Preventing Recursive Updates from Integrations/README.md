---
title: "Preventing Recursive Updates from Integrations"
aliases:
  - Preventing Recursive Updates from Integrations
tags:
  - servicenow-dev-program
  - code-snippet
  - preventing-recursive-updates-from-integrations
  - business-rules
---

**Business Rule** 

Table : Any Custom Table or (Incident,Problem , Change)...
Active : true
When : before 
Update : true
order : 100 

condition : gs.getUser().getUserName() == 'integration.user/Web services User'

The rule must only run when the update is coming from the dedicated integration user to avoid impacting manual user updates, Can Update Fields to check as Required 

This business rule is designed to prevent unnecessary and redundant updates to records that are synchronized with external systems (e.g., Jira, Azure DevOps, or a custom application) via integration / E bonding 

This rule executes a check to ensure that the fields critical to the integration (Work Notes, Comments, State) have genuinely changed before allowing the update to process.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
