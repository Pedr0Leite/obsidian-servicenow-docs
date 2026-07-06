---
title: "Calculate Due date using user defined schedules"
aliases:
  - Calculate Due date using user defined schedules
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-due-date-using-user-defined-schedules
  - glidedatetime
---

**Description:**
This  Script Include  calculates a future due date by adding a specified number of business days to a given start date, based on a defined schedule.
This can be used anywhere within the server side scripts like fix scripts, background scripts, UI Action (server script).

**Pre-requisite:**
A schedule record with valid schedule entries should be created in the cmn_schedule table
A business hours value per day need to be configured
In this sample, the business hours per day is configured as 8 hours i.e 9AM - 5PM.

**Sample:**
var daysToAdd = 4; // No of days need to be added
var script = new CaclculateDueDate().calculateDueDate(new GlideDateTime(),daysToAdd); // Passing the current date and daysToAdd value to script include
gs.print(script);

**Output:**
*** Script: 2025-10-13 13:56:07

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/ConvertTicksToGlideDateTime/README|ConvertTicksToGlideDateTime]]
