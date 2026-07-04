---
title: "On call schedule isn't showing On-call shift correctly in on-call calendar."
aliases:
  - KB0725811
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725811
kb_number: KB0725811
last_modified: 2025-03-25
---

## On call schedule isn't showing On-call shift correctly in on-call calendar.

  

### Issue

Post London Upgrade, when a shift extends to next day and has to rotate between two people, the Calendar doesn't display the on-call resource correctly.

# Steps To Reproduce

* * *

1.  Navigate to On-Call Scheduling > Create New Schedule
2.  Fill in Mandatory Fields and click Next
3.  In Schedule Definition tab, fill No in 'Would you like to use an existing schedule?' and 'Is the shift for this schedule all day?'
4.  Fill in Start and End dates such that End Date is next day.Example : Schedule is defined from  21:00 hours present day to 0400 hours next day.
5.  Select 'Daily' for 'How often does 1 shift repeat?'
6.  Fill any remaining mandatory fields and click Next
7.  Fill in the member details and click Submit
8.  Check the On-Call Calendar for the group.
9.  USER A should be displayed present day  2100 hrs - 2359hr and on next day there should be another entry for user A from 0000hrs  - 0300hrs .
10.  However, USERA is being displayed from 2100 hrs - 2359hr on present day and USERB is being displayed for the rest of the shift on next day  feb instead of user A from 0000hrs - 0300 hrs  

### Release

Post London

### Cause

Introduction of a new system property from London. When a shift extends to next day and has to rotate between two people, the Calendar doesn't display the on-call resource correctly.

### Resolution

This issue was happening because of a new system property introduced in London - "_**com.snc.on\_call\_rotation.factor\_daily\_rotation\_interval\_all\_day**_".For rotation to happen , it should have value as false.

To fix this issue , follow below steps:

1.  Create a new user property - "com.snc.on\_call\_rotation.factor\_daily\_rotation\_interval\_all\_day"
2.  Set Type - boolean and Value  - false.
3.  Save the record.
4.  Clear cache.
5.  test 

### Related Links

**NOTE :** This property will not affect rotas/schedules created in past. It will only effect rota's which are created after setting this property to false which implies, rotas created in past will show wrong values post upgrade.To avoid this, we need to do a small update in rotas (like make a change , save the record again) .This property will then consider these rotas as well and will show correct result.
