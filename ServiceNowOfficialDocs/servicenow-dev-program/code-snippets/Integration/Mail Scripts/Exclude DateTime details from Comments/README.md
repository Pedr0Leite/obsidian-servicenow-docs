---
title: "Exclude DateTime details from Comments"
aliases:
  - Exclude DateTime details from Comments
tags:
  - servicenow-dev-program
  - code-snippet
  - exclude-datetime-details-from-comments
  - mail-scripts
---

//Retrieves the most recent comment (journal entry) from the comments field of the current record.
//We can call this notification email script in notifications to get the comments only excluding the name, date/time details.

current.comments.getJournalEntry(1)
//Extracting the Comment's Content (Removing Username/Date/Time):

.match(/\n.*/gm)
//Matches all text after the first newline (\n). In ServiceNow, journal entries typically start with a username, date, and time stamp followed by the comment text. This regex targets everything after the first line, effectively bypassing the username and timestamp.


.join('')
//Joins the matched lines back into a single string. The empty string ('') is used to remove any newlines in the matched parts.


.replace(/^\s*\n/gm, "")
//This removes any leading empty lines (^\s*\n) or unnecessary whitespace that may remain after removing the username/timestamp, ensuring the comment starts cleanly with actual content.


Result: The final output is the content of the most recent comment without the username, date, or time. This is useful for including clean, user-entered content in an email notification, without system-generated metadata like when the comment was added or who added it.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
