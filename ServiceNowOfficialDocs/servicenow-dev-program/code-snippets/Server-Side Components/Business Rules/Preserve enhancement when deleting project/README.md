---
title: "Preserve enhancement when deleting project"
aliases:
  - Preserve enhancement when deleting project
tags:
  - servicenow-dev-program
  - code-snippet
  - preserve-enhancement-when-deleting-project
  - business-rules
---

Stops the related enhancement records being cascade deleted from a project record when they also belong to a demand (i.e. we're deleting the project, but want to re-evaluate the original demand with it's associated enhancements). IF you want all enhancements to be preserved then just adjust the filter conditions to suit.

Table: pm_project

When: before

Delete: true

Filter: Demand is not empty AND Demand is not ""

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
