---
title: "Fetch Table(Incident) fields in UI Page"
aliases:
  - Fetch Table(Incident) fields in UI Page
tags:
  - servicenow-dev-program
  - code-snippet
  - fetch-tableincident-fields-in-ui-page
  - ui-pages
---

Fetch Incident fields(or any table fields) in a UI page via UI Action trigger

Steps
1) Create a UI action and create a function.
2) Add the UI action script provided in the Script section.
3) This code helps to render a pop up window of 600x600 dimentions for the UI page and passes the current sys id to UI page.
4) Make sure to add the code in the UI Page : <g:evaluate var="jvar_sysId" expression="RP.getWindowProperties().get('sysparm_sys_id')" />
5) Create a UI Page and add the HTML Code provided.
6) Trigger the UI Action from the Incident form and it should render the ui page with the incident fields data.
7) Add additional static or dynamic data as per the requirement.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Add Multiple Items to Order Guide/README|Add Multiple Items to Order Guide]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/BulkUpdate Worknotes/Readme|BulkUpdate Worknotes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Custom Alert using UI Page/README|Custom Alert using UI Page]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Dynamic program status overview/README|Dynamic program status overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/EDM DocUnifiedSearch/README|EDM DocUnifiedSearch]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Edit Last WorkNotes/README|Edit Last WorkNotes]]
