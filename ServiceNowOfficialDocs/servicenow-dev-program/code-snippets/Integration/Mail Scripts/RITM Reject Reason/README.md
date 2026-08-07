---
title: "RITM Reject Reason"
aliases:
  - RITM Reject Reason
tags:
  - servicenow-dev-program
  - code-snippet
  - ritm-reject-reason
  - mail-scripts
---

After finding that reject reasons added from Employee Center for Requests do not get added to the Approval record but instead the RITM record, I made a change to the reject_reason email script to include the RITM reject reason (if found)
The changes calls the Script Include "RequestNotificationUtil" with an added function to call the RITM reject reason

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
