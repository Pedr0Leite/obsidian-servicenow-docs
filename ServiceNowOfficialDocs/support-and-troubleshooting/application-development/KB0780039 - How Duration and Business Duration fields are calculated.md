---
title: "How Duration and Business Duration fields are calculated"
aliases:
  - KB0780039
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780039
kb_number: KB0780039
last_modified: 2026-06-04
---

## How Duration and Business Duration fields are calculated

  

### Issue

Learn how the Duration and Business Duration fields are calculated on task records, including the business rules and calendar settings that control these calculations.

The Duration and Business Duration fields are legacy fields from the pre-2010 SLA engine. While newer methods exist for tracking time-based metrics, these fields remain in use on many task tables.

### Business rules that calculate duration

Several business rules calculate the Duration and Business Duration fields on task tables. The following table lists these business rules by table:

| 
Table

 | 

Business rule

 | 

Trigger

 |
| --- | --- | --- |
| 

Incident \[incident\]

 | 

mark\_resolved

 | 

Incident state changes to Resolved

/nav\_to.do?uri=sys\_script.do?sys\_id=d3b21f640a0a3c7400f6acab7de3f5f8

 |
| 

Incident \[incident\]

 | 

mark\_closed

 | 

Incident state changes to Closed (if not already set by mark\_resolved)

  
/nav\_to.do?uri=sys\_script.do?sys\_id=bf3f8917c0a8016400a867dc0794e8ad

 |
| 

Catalog Task \[sc\_task\]

 | 

Close Ticket

 | 

Task is closed

/nav\_to.do?uri=sys\_script.do?sys\_id=74d38bd0c611227d0151ca6b62ae87e6

 |
| 

Change Task \[change\_task\]

 | 

Close Ticket

 | 

Task is closed

/nav\_to.do?uri=sys\_script.do?sys\_id=9023ada50a0a0b01004228007704cf66

 |
| 

Problem \[problem\]

 | 

mark\_closed

 | 

Problem is closed

/nav\_to.do?uri=sys\_script.do?sys\_id=12a53c4fc6112275000bc7c04a87cfb6

 |
| 

Change Request \[change\_request\]

 | 

mark\_closed

 | 

Change request is closed

/nav\_to.do?uri=sys\_script.do?sys\_id=6e20e124c611228e00e44dd37ad1b842

 |

### The calDateDiff function

Most duration business rules (except mark\_closed on change\_request) use the GlideSystem function calDateDiff:

current.business\_duration = gs.calDateDiff(current.opened\_at.getDisplayValue(), current.closed\_at.getDisplayValue(), false);

Key points about calDateDiff:

-   Calculates duration based on closed time, not resolved time. 
-   Uses a calendar (System Policy > Calendars), not a schedule
-   Uses the default calendar, which is the first record in the sys\_calendar table arbitrarily returned by the database
-   If multiple calendars exist, the function uses the first one found

**Important:** If you have multiple calendars, modify your primary calendar to reflect your business hours rather than relying on the arbitrary selection behavior.

### How business duration is calculated

The mark\_resolved and mark\_closed business rules use the legacy API calDateDiff. The calDateDiff function calculates duration using:

-   The first calendar from the sys\_calendar table
-   The session time zone of the user who resolves or closes the record

**Important:** Because the calculation uses the resolver's time zone, results may appear incorrect when viewed from a different time zone. To verify calculations, impersonate the user who resolved or closed the record.

#### **Calculation examples**

The following examples demonstrate how business duration is calculated based on the resolver's time zone and the calendar business hours.

#### **Example 1: Incident opened and resolved outside business hours**

| 
Field

 | 

Value

 |
| --- | --- |
| 

Opened at

 | 

2022-11-09 08:36:30 (London)

 |
| 

Resolved at

 | 

2022-11-09 08:39:38 (London)

 |
| 

Resolved by time zone

 | 

Europe/London

 |
| 

Calendar business hours

 | 

Wednesday 5 PM – 1 AM (London)

 |
| 

Business duration result

 | 

0

 |

Explanation: The incident was opened and resolved between 8:36 AM and 8:39 AM London time, which is outside the calendar business hours of 5 PM to 1 AM. Therefore, the business duration is 0.

#### **Example 2: Incident spans business hours**

| 
Field

 | 

Value

 |
| --- | --- |
| 

Opened at

 | 

2022-11-08 08:49:47 (London)

 |
| 

Resolved at

 | 

2022-11-09 08:50:14 (London)

 |
| 

Resolved by time zone

 | 

Europe/London

 |
| 

Calendar business hours

 | 

Tuesday 5 PM – 1 AM (London)

 |
| 

Business duration result

 | 

8 hours

 |

Calculation breakdown:

-   From 2022-11-08 08:49:47 AM to 2022-11-08 05:00:00 PM = 0 hours (outside business hours)
-   From 2022-11-08 05:00:00 PM to 2022-11-09 01:00:00 AM = 8 hours (within business hours)
-   From 2022-11-09 01:00:00 AM to 2022-11-09 08:50:14 AM = 0 hours (outside business hours)
-   Total: 0 + 8 + 0 = 8 hours

#### **Example 3: Different time zone**

| 
Field

 | 

Value

 |
| --- | --- |
| 

Opened at

 | 

2022-11-07 16:41:27 (Madrid)

 |
| 

Resolved at

 | 

2022-11-07 16:43:58 (Madrid)

 |
| 

Resolved by time zone

 | 

Europe/Madrid

 |
| 

Calendar business hours

 | 

Wednesday 6 PM – 2 AM (Madrid)

 |
| 

Business duration result

 | 

0

 |

### Verify business duration calculations

Use the following script to verify business duration calculations for specific opened and resolved date/times.

**Before you begin:** Change your user time zone to match the time zone of the user who resolved or closed the record.

var opened = new GlideDateTime('2022-11-07 15:41:27'); gs.info(opened.getDisplayValue());

var resolved = new GlideDateTime('2022-11-07 15:43:58'); gs.info(resolved.getDisplayValue());

gs.info(gs.calDateDiff(opened.getDisplayValue(), resolved.getDisplayValue(), false));

**Note:** Replace the date/time values with the opened\_at and resolved\_at values from the record you want to verify.

### Calculate business duration using a schedule

To calculate business duration based on a schedule instead of a calendar, replace the calDateDiff function in the mark\_closed and mark\_resolved business rules with schedule-based logic.

1.  Create a schedule or identify an existing base system schedule to use.
2.  Select a time zone for the schedule that is appropriate for your environment. For example, defining US/Pacific ensures that the duration is calculated according to the schedule spans applied in the US/Pacific time zone.
3.  Copy the sys\_id of the chosen schedule.
4.  Modify the mark\_closed and mark\_resolved business rules to use the following script:

// Default Workday 8-5 Floating schedule. Replace with sys\_id of the schedule to be used   
var schedule = new GlideSchedule("38f8b6d2c0a801640075da0e39d47696");   
   
// Use closed\_at for "mark\_closed" business rule and resolved\_at for "mark\_resolved" business rule   
var duration = schedule.duration(current.opened\_at.getGlideObject(), current.closed\_at.getGlideObject());   
   
// Stores value as a GlideDuration   
current.business\_duration = duration; 

   
// Stores value in seconds. The numeric value function returns a value in milliseconds, hence divide by 1000   
current.business\_stc = duration.getNumericValue() / 1000; 

### Release

All supported releases

### Resolution
