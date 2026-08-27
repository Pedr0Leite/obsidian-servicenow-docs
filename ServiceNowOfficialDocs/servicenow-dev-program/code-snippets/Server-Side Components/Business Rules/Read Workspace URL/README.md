---
title: "Read Workspace URL"
aliases:
  - Read Workspace URL
tags:
  - servicenow-dev-program
  - code-snippet
  - read-workspace-url
  - business-rules
---

Display BR that reads the caller_id parameter from the Workspace URL (agent or sow) for creating a new record/interaction and seearches 
for the corresponding user to set it in the g_scratchpad to be used as default value in the new Interaction form. 
eg url https://instance-name.service-now.com/now/sow/record/interaction/-1_uid_1/params/query/active%3Dtrue%5Ecaller_id=<email>

The scratchpad can be used in an onLoad client script like so:
   if (g_form.isNewRecord())
		g_form.setValue('opened_for', g_scratchpad.caller_id);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
