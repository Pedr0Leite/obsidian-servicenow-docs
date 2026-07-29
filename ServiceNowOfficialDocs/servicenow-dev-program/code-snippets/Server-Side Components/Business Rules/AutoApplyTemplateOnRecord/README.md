---
title: "AutoApplyTemplateOnRecord"
aliases:
  - AutoApplyTemplateOnRecord
tags:
  - servicenow-dev-program
  - code-snippet
  - autoapplytemplateonrecord
  - business-rules
---

//Used to automate the application of template when additional fields are required for a process. ex. incident, change etc.

//Template
// Navigate to System Definition > Templates and create new template
// Fill Name, Table, short description, and Template fields.

//Business Rule
// Navigate to System Definition > Business Rule and create a new rule
// Configure the trigger condition and when to run to meet your business need.
// Advanced table: Input script and replace place holder variable values.
// var templateName = "Your Template Name"; //replace template name
// current.applyTemplate(templateName);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
