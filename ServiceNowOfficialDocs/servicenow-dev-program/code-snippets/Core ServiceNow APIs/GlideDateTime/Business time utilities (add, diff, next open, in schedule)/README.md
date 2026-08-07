---
title: "Business time utilities (add, diff, next open, in schedule)"
aliases:
  - Business time utilities (add, diff, next open, in schedule)
tags:
  - servicenow-dev-program
  - code-snippet
  - business-time-utilities-add-diff-next-open-in-schedule
  - glidedatetime
---

# Business time utilities (add, diff, next open, in schedule)

## What this solves
Teams repeatedly reimplement the same business-time maths. This utility wraps `GlideSchedule` with four practical helpers so you can:
- Add N working hours to a start date
- Calculate working minutes between two dates
- Find the next open time inside a schedule
- Check if a specific time is inside the schedule window

All functions return simple objects that are easy to log, test, and consume in Flows or Rules.

## Where to use
- Script Include in global or scoped app
- Call from Business Rules, Flow Actions, or Background Scripts

## Functions
- `addWorkingHours(scheduleSysId, hoursToAdd, startGdt, tz)`
- `workingMinutesBetween(scheduleSysId, startGdt, endGdt, tz)`
- `nextOpen(scheduleSysId, fromGdt, tz)`
- `isInSchedule(scheduleSysId, whenGdt, tz)`

## Notes
- The schedule determines both business hours and holidays.
- `tz` is optional; if omitted, the schedule’s TZ or instance default applies.
- All inputs accept either `GlideDateTime` or ISO strings (UTC-safe).

## References
- GlideSchedule API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideSchedule/concept/c_GlideScheduleAPI.html
- GlideDateTime API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideDateTime/concept/c_GlideDateTimeAPI.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/ConvertTicksToGlideDateTime/README|ConvertTicksToGlideDateTime]]
