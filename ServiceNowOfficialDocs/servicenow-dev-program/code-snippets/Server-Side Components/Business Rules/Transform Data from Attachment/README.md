---
title: "Transform Data from Attachment"
aliases:
  - Transform Data from Attachment
tags:
  - servicenow-dev-program
  - code-snippet
  - transform-data-from-attachment
  - business-rules
---

Loading data into ServiceNow without needing admin privileges

This BR script enables any user to process data from an excel file by attaching that file to a record.

Pre-requisites:
A sys admin needs to create the following objects in SN first. The easiest way to do this is to load sample data using an excel file in the same format as the one that will be used by the user:
1. Importset table
2. Transform Map
3. Data Source
4. A table to house all the files that will be loaded

All the other explanations on the use of the code is in the script itself

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
