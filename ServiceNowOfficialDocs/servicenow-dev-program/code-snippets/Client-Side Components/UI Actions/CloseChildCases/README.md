---
title: "CloseChildCases"
aliases:
  - CloseChildCases
tags:
  - servicenow-dev-program
  - code-snippet
  - closechildcases
  - ui-actions
---

Name: Close all Child Case
Table:sn_customerservice_case
Condition: (gs.hasRole('sn_customerservice_agent') || gs.hasRole('admin') ) && (new GlideRecord('sn_customerservice_case').addQuery('parent', current.sys_id).query().hasNext())

Use Case: 
Provide UI action button to close all the associated child cases from the parent Case.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
