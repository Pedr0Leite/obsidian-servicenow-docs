---
title: "How to schedule a script/report Mondays to Friday every hour between 11am and 5pm"
aliases:
  - KB0786496
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786496
kb_number: KB0786496
last_modified: 2025-01-03
---

## How to schedule a script/report Mondays to Friday every hour between 11am and 5pm

  

### Summary

Out of the box, you can schedule your script executing Periodically at a defined repeat interval. But when you have a requirement like scheduling a script/report Mondays to Friday every hour between 11am and 5pm then it is little tricky. We can achieve this requirement by adding a conditional script.

Please use below script as a reference and modify this further as per your business need.

### Release

Applicable to all releases

### Instructions

```
doIt();function doIt() {    var gdt = new GlideDateTime(); //setup date time object    var hourInUTC = gdt.getTime().getHourOfDayUTC(); //Gets Hours    var dayOfWeek = gdt.getDayOfWeekUTC();    var startingHour = 11; //Adjust to correct UTC offset    var endingHour = 17; //Adjust to correct UTC offset    if (dayOfWeek < 6) {        if (hourInUTC >= startingHour && hourInUTC < endingHour) {            gs.log('Condition True: ' + gdt, 'doIt');            return true;        } else {            gs.log('Condition False: ' + gdt, 'doIt');            return false;        }    }}
```
