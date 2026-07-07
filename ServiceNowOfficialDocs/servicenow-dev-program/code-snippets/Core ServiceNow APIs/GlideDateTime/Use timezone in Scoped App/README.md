---
title: "Use timezone in Scoped App"
aliases:
  - Use timezone in Scoped App
tags:
  - servicenow-dev-program
  - code-snippet
  - use-timezone-in-scoped-app
  - glidedatetime
---

The normal APIs for using Timezones modifications doesn't work in scoped app. For this you can use a undocumented API called "GlideScheduleDateTime". Meaning you can set the time to be e.g. 23 June 2023 15.00.00. And then you want that time to be in IST time, then you use this api to make set this and then you can save it in a normal glideDatetime and get the correct time saved in the field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
