---
title: "Mark Records Inactive - List Action"
aliases:
  - Mark Records Inactive - List Action
tags:
  - servicenow-dev-program
  - code-snippet
  - mark-records-inactive---list-action
  - ui-actions
---

Above two scripts will help you to select records in list view and mark them inactive. You can create your UI action(list action) on any table and then you should be able to
mark the records as inactive by calling the reusable script include. Process is pretty simple as shown below:
1. Create a List action - list banner button or list choice.
2. Check the client checkbox. Use the script and do any necessary modifications.
3. Keep your script include ready with the function to make records inactive and done.

You can even modify the scrip include to change other fields too based on your requirements. And you do not need to pass any table name also. This is complete generic.

**UPDATE:**
_Replaced standard Javascript Window method 'alert' with GlideModal as per issue #745. This completes the task 'Mark Records Inactive UI Action'_

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
