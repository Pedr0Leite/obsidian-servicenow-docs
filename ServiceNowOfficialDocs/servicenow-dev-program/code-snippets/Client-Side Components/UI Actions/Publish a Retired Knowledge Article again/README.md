---
title: "Publish a Retired Knowledge Article again"
aliases:
  - Publish a Retired Knowledge Article again
tags:
  - servicenow-dev-program
  - code-snippet
  - publish-a-retired-knowledge-article-again
  - ui-actions
---

**UI Action**: 
Publish a Retired Knowledge Article again after it is already retired.

**How it works:**
1. The code finds existing articles in the Knowledge base that share the same Article ID but are not the current article and are 'retired'.
2. It updates the workflow state of these found articles to 'outdated'.
3. For the current article, it sets the workflow_state to 'pubblished', records the current date and updates the 'published' field with the date.
4. It also removes the pre-existing 'retired' date from the 'retired' field.
5. It redirects the user to the updated current record.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
