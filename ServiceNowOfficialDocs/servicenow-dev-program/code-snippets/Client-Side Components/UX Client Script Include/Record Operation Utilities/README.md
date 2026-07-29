---
title: "Record Operation Utilities"
aliases:
  - Record Operation Utilities
tags:
  - servicenow-dev-program
  - code-snippet
  - record-operation-utilities
  - ux-client-script-include
---

#Record Operations Utilities which can be in imported in any UIB client script (Make sure to make the client script include accessible in all scopes)
1. createRecord - Function to execute create record data broker with necessary arguments
2. updateRecord - Function to execute update record data broker with necessary arguments
3. deleteRecord - Function to execute delete record data broker with necessary arguments

/*Sample script to show how to import client script include can be included :-
function handler({api, event, helpers, imports}) {
  const { createRecord, updateRecord, deleteRecord } = imports['global.Record Operation Utilities']();
}
*/

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UX Client Script Include/Access global object from page scripts/README|Access global object from page scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UX Client Script Include/Reusable Debounce/README|Reusable Debounce]]
