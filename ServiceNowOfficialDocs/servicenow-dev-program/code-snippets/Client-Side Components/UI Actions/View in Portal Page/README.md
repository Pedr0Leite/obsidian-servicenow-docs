---
title: "View in Portal Page"
aliases:
  - View in Portal Page
tags:
  - servicenow-dev-program
  - code-snippet
  - view-in-portal-page
  - ui-actions
---

code-snippet used in UI Action SCript to view the current record in Service Portal Page using a redirect

Example:
//to view a KB article in the Service Portal:

function goToPortal(){
	var url = 'sp?id=kb_article_view&sys_kb_id=' + g_form.getUniqueValue();
	g_navigation.openPopup(url);
	//g_navigation.open(url);
	return false;
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
