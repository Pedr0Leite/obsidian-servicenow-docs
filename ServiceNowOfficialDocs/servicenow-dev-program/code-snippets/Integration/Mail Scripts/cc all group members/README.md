---
title: "cc all group members"
aliases:
  - cc all group members
tags:
  - servicenow-dev-program
  - code-snippet
  - cc-all-group-members
  - mail-scripts
---

This mail script can be used to CC all members of a group in the current record context. 

Use case: 
CC all members of the assignment group for the current record.

Solution: 
Create the mail script as mentioned in cc all group members.js file and then call the mail script in you email notification using ${mail_script: your mail script name} in the notification body

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
