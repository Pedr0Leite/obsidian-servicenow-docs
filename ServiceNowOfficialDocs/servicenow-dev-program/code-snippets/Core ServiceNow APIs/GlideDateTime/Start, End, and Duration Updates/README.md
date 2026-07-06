---
title: "Start, End, and Duration Updates"
aliases:
  - Start, End, and Duration Updates
tags:
  - servicenow-dev-program
  - code-snippet
  - start-end-and-duration-updates
  - glidedatetime
---

# Start, End, and Duration Updates
### Use this code to auto update associated GlideDateTime and Duration fields on a record.

This code assumes you're working on the sc_req_item and sc_task tables but can be modified to support other tables such as change.
1. Requires only a 2 of the 3 data points to work.  In this example, the start and duration variables are the required input.
2. Code checks for either a blank end time or if start or duration has changed. 
3. If start or duration has changed, it will calculate a new effective end date and duration accordingly.
4. If the end date is the one changing, it will calculate a new effective duration.
5. If all 3 data points change at the same time, only the start and duration fields will be accepted as input.  
6. It also includes a section to update an associated task if needed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
