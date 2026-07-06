---
title: "UI Page Auto Populate Assigned to based on Assignment group"
aliases:
  - UI Page Auto Populate Assigned to based on Assignment group
tags:
  - servicenow-dev-program
  - code-snippet
  - ui-page-auto-populate-assigned-to-based-on-assignment-group
  - ui-pages
---

This project adds functionality to dynamically filter the "Assigned To" field based on the selected "Assignment Group" on a UI page. When a group is selected, only users from that group will be displayed in the "Assigned To" reference field.

Overview
The UI page includes two reference fields:

Assignment Group: A reference to the sys_user_group table where users can select an active group.
Assigned To: A reference to the sys_user table that should display users belonging to the selected "Assignment Group."
Solution Approach
UI Page Setup: The "Assignment Group" field is configured to trigger a function when a group is selected. The "Assigned To" field is updated based on the selected group.

Client-Side Script:

The onAssignmentGroupChange() function is triggered when the "Assignment Group" field is changed. It retrieves the selected group's internal ID.
A GlideAjax call is made to send the selected group ID to the server-side Script Include.
Upon receiving a response, the script processes the data and updates the lookup filter of the "Assigned To" field to display only the users from the selected group.
Server-Side Script (Script Include):

A client-callable Script Include queries the sys_user_grmember table to retrieve user IDs of members in the selected group.
The user IDs are returned to the client as a comma-separated string, which is used to update the "Assigned To" field's query.
Key Steps
onChange Trigger:

The client script triggers whenever the "Assignment Group" field is updated by the user.
GlideAjax Call:

The onAssignmentGroupChange() function uses GlideAjax to send the selected group ID to the server-side Script Include.
Retrieve Group Members:

The Script Include queries the sys_user_grmember table to fetch user IDs for users in the selected group.
Update the Lookup Field:

The client script dynamically modifies the "Assigned To" field's lookup to filter users based on the selected "Assignment Group."
Additional Notes
Ensure that the Script Include is client-callable for it to be accessible via GlideAjax.
This solution enhances user experience by restricting the "Assigned To" lookup field to relevant users from the selected "Assignment Group," improving data accuracy.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Add Multiple Items to Order Guide/README|Add Multiple Items to Order Guide]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/BulkUpdate Worknotes/Readme|BulkUpdate Worknotes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Custom Alert using UI Page/README|Custom Alert using UI Page]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Dynamic program status overview/README|Dynamic program status overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/EDM DocUnifiedSearch/README|EDM DocUnifiedSearch]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Pages/Edit Last WorkNotes/README|Edit Last WorkNotes]]
