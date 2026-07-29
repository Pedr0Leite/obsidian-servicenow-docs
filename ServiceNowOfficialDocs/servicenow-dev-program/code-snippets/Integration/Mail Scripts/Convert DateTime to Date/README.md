---
title: "Convert DateTime to Date"
aliases:
  - Convert DateTime to Date
tags:
  - servicenow-dev-program
  - code-snippet
  - convert-datetime-to-date
  - mail-scripts
---

Use this mail script to extract the date from GlideDateTime objects and use it in your email notification.
example: 2024:10:29 18:18:52 to 2024:10:29

Use case:
Print just the date in email body from the GlideDateTime object.

Solution:
Create a mail script as shown in script.js and then call this mail script in email body using ${mail_script: your mail script name}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
