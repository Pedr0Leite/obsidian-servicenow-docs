---
title: "BulkUpdate Worknotes"
aliases:
  - BulkUpdate Worknotes
tags:
  - servicenow-dev-program
  - code-snippet
  - bulkupdate-worknotes
  - ui-pages
---

Bulk Update Worknotes

Script Type: UI Action, Table: incident, List banner button: True, Client: True, Show update: True, OnClick: functionName()

Script Type: UI Page Category: General

Goal: To update the worknotes for multiple tickets in a single view 

Walk through of code: So in the incident List view we do have a list banner button called "Bulk Updates" so that was the UI Action configured with the script which has used the GlideModel API to call the UI page which is responsible to get the multiple tickets and worknotes value and then update to the respective ticket and store in the worknotes in journal entry. For this the HTML part in the UI page is configured with two fields, one for the multiple list of tickets, and then the worknotes field, and one submit button to save that into the table.
And the Processing Script is used to get each ticket number and then check the valid tickets and query the respective table, and then update the worknotes of each respective ticket if it is valid. Otherwise, it won't update.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Add Multiple Items to Order Guide/README|Add Multiple Items to Order Guide]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Custom Alert using UI Page/README|Custom Alert using UI Page]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Dynamic program status overview/README|Dynamic program status overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/EDM DocUnifiedSearch/README|EDM DocUnifiedSearch]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Edit Last WorkNotes/README|Edit Last WorkNotes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Export UI pages to word docx/README|Export UI pages to word docx]]
