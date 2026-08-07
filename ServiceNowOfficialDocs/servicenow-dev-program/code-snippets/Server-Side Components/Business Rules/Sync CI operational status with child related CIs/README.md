---
title: "Sync CI operational status with child related CIs"
aliases:
  - Sync CI operational status with child related CIs
tags:
  - servicenow-dev-program
  - code-snippet
  - sync-ci-operational-status-with-child-related-cis
  - business-rules
---

# Sync CI operational status with child related CIs

**Use case** : Whenever any configuration item becomes operational or non-operational, then all the CIs which are related to the current CI as a child in cmdb_rel_ci table will also update their operational status

*info* : This method is to achieve the above use-case just with business rule

**Solution** : Create a `Async` business rule on `cmdb_ci` table with `update` checkbox checked. 

*condition* : operational status CHANGES

Follow the script present in [script.js](https://github.com/ServiceNowDevProgram/code-snippets/blob/patch-1/Business%20Rules/Sync%20CI%20operational%20status%20with%20child%20related%20CIs/script.js)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
