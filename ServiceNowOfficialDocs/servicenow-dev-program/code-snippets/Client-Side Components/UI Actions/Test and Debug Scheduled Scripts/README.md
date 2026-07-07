---
title: "Test and Debug Scheduled Scripts"
aliases:
  - Test and Debug Scheduled Scripts
tags:
  - servicenow-dev-program
  - code-snippet
  - test-and-debug-scheduled-scripts
  - ui-actions
---

<h4>Test and Debug Scheduled Scripts using the Script Debugger</h4>

This UI Action will run the script in the current session, so that it can be run and debugged in the script debugger.

<h4>Steps to Add:</h4>
1. Create a new UI Action in Global scope.<br>
2. Name = Test and Debug (Modify this as per your preference).<br>
3. Table = "Scheduled Script Execution [sysauto_script]"<br>
4. Form Button = selected<br>
5. Add the given script.<br>
6. New UI Action will be available on Scheduled Scripts in Studio.<br>
7. Use break points in script to debug.

<h3><span style='color: red;'>WARNING</span></h3>
This will run the script. So use it wisely.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
