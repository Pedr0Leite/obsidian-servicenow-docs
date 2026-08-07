---
title: "Check domain of record against user session"
aliases:
  - Check domain of record against user session
tags:
  - servicenow-dev-program
  - code-snippet
  - check-domain-of-record-against-user-session
  - business-rules
---

Type: Business Rule
When: onDisplay
example Table: sys_script

This script gets the domain of the user session, and the domain of the record that you call it from, such as an onLoad Client Script.
Help to prevent accidental inserts of scripts in the wrong domain
eg:
Table: sys_script

function onLoad() {
	var currentUserDomain = g_scratchpad.currentDomain;
	var currentRecordDomain = g_scratchpad.recordDomain;
	
	if (currentUserDomain == 'Global') {
		g_form.addErrorMessage('You are currently in the Global domain. Editing this record won\'t create another record');
	} else if (currentUserDomain == currentRecordDomain) {
		g_form.addErrorMessage('You are currently in the same domain as the record you are about to edit: ' +currentUserDomain);
	} else {
		g_form.addErrorMessage('Your current domain is: ' +g_scratchpad.currentDomain +', and the record you are editing is in the ' +g_scratchpad.recordDomain +' domain. If you save any edits, the action will create a new record in your current domain');
	}
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
