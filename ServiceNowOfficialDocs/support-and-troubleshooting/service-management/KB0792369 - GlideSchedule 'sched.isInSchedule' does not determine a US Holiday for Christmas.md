---
title: "GlideSchedule 'sched.isInSchedule' does not determine a US Holiday for Christmas"
aliases:
  - KB0792369
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792369
kb_number: KB0792369
last_modified: 2026-06-08
---

## GlideSchedule 'sched.isInSchedule' does not determine a US Holiday for Christmas

  

### Issue

Calling the method isInSchedule, which is available inside the GlideSchedule class, does not provide the expected result if you are trying to determine if Christmas is in the US Holiday schedule.

This is documented in the developer portal in [GlideScheduleScopedAPI](https://developer.servicenow.com/app.do#!/api_doc?v=newyork&id=c_GlideScheduleScopedAPI "GlideScheduleScopedAPI")

However, the result of the script below says Christmas is not in the US Holiday schedule. 

Script:

var g = new GlideRecord('cmn\_schedule');  
g.addQuery('name', 'U.S. Holidays');  
g.query();  
  
//gs.debug('g ' + g.getRowCount())  
if (g.next()) {  
  var sched = new GlideSchedule(g.sys\_id);  
  var d = new GlideDateTime();  
  d.setDisplayValue("2019-12-25 12:00:00");  
  if (sched.isInSchedule(d))  
    gs.debug("Is in the schedule");  
  else  
    gs.debug("Is NOT in the schedule");  
}

### Cause

This is working as expected.

Each schedule has span which is either of _exclude_ or _include_ type. _Exclude_ time spans contain what are meant to be excluded from the schedule definition when we create a timeline with all the schedules' spans. For example, when we create a schedule with one span as **Dec 20, 2019 to Dec 31, 2019 2-3pm** (**include**) and another span with **Dec 25, 2019** (**exclude**) and call the **IsInSchedule** with Dec 25, it will not be in the schedule as it is an _exclude_. Dec 21 will, however, return **true**.

"U.S Holidays" contains only the exclude spans. It is meant to be used as child schedule, like in "8-5 weekdays excluding holidays", so that when an overall time line is created those days would be excluded.

### Resolution

This is expected behavior; instead of checking on U.S Holidays directly, it is better to create a schedule on which days the script has to be run.
