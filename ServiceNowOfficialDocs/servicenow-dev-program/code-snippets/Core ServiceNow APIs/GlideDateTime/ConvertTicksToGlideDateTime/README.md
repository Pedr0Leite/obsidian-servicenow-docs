---
title: "ConvertTicksToGlideDateTime"
aliases:
  - ConvertTicksToGlideDateTime
tags:
  - servicenow-dev-program
  - code-snippet
  - converttickstoglidedatetime
  - glidedatetime
---

# .Net Ticks to GlideDateTime

An utility function to convert .Net ticks to GlideDateTime.

A tick is 1/10000 of a milli second (1 Milli second = 10,000 ticks)

This is more useful when you are bringing the Date Time data from Microsoft tools such as Active Directory, which will provide date time values in ticks. By using this utility function we can convert it to ServiceNow native GlideDateTime object.

### Example

`var gdt = convertTicksToGlideDateTime(5954484981710000)`

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
