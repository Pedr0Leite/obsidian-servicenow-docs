---
title: "Scripted planned maintenance schedule"
aliases:
  - KB0818061
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818061
kb_number: KB0818061
last_modified: 2024-10-09
---

## Issue

How to create maintenance schedules for 12 different monthly schedules? The tasks should generate on the first day of the month and due on the last day of the month. 

## Resolution

A suggested way to model the maintenance plan is to create a maintenance plan which has 12 annual schedules associated to it. Annual schedules will let you pick the specific month and day for the due date and then the lead times need to be adjusted as per the number of days in the month.  
  
For example, for January, the customer would create a annual schedule which is due on Jan 31 with a 30 day lead time. For February, the customer would create an annual schedule which is due on Feb 28 with a 27 day lead time; March would be similar to Jan and then April would have a due date of Apr 30 and a lead time of 29 days. This way the work orders/tasks can be generated on the first day of the month and due on the last day of the month. Please let me know if you have any further questions.

See attached screenshot for an example of how to structure the plan
