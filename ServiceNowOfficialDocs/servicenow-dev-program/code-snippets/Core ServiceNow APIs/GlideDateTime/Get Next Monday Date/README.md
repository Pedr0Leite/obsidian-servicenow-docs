---
title: "Get Next Monday Date"
aliases:
  - Get Next Monday Date
tags:
  - servicenow-dev-program
  - code-snippet
  - get-next-monday-date
  - glidedatetime
---

# A Date Function to get the next upcoming Monday date.

This function uses a few Glide date and Glide Date Time API's 

1. First we get todays date with GlideDateTime()

2. Then we get the day of the month number with GlideDate().getDayOfMonthNoTZ();

3. Then we use the make a calculation to set the day to the next monday

4. Finally, we calcualtate the day using AddDays we return the New Date transforming it back with getDate()

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
