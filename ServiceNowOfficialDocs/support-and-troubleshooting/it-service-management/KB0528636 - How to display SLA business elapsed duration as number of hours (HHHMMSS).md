---
title: "How to display SLA business elapsed duration as number of hours (HHH:MM:SS)"
aliases:
  - KB0528636
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528636
kb_number: KB0528636
last_modified: 2026-06-03
---

## How to display SLA business elapsed duration as number of hours (HHH:MM:SS)

  

### Issue

This article aims to help avoiding confusion in SLA reporting when using business\_duration fields. The duration of 1 day is always calculated as 24 hours, whether using a schedule or not. Therefore, when reporting against a duration field using a schedule, it will always result in the calculated number if days (DD:HH:MM:SS). This solution will allow to change the Business Elapsed \[business\_duration\] to show in hours instead of days.

Use case configuration example:

\- Business elapsed duration is being calculated using the schedule 7-6 M-F

\- The business elapsed time is 1 day 8 hours 5 minutes (32 hours total)

\- An incident was opened late on Wednesday at 4:50pm and closed on Monday at 3:56pm

\- 1 day = 24 hours

\- The calculated time span will be:

Wednesday – 1hr 10min left

Thursday – 11 hours

Friday – 11 hours

Saturday – Not counted

Sunday – Not counted

Monday – 8hrs 56min

\- Total will be 32:05:00

\- The Business Duration shows as 1 day 8 hours 5 minutes

### Resolution

To display the business\_duration field on the Task SLA table in hours (as 32:05:00 in the example above) instead of days:

1.  Open the Dictionary
2.  Select the Task SLA table
3.  Find the business\_duration field
4.   Personalize the dictionary by adding the following Attribute:

     **max\_unit=hours**

The business\_duration will now display as HHH:MM:SS.
