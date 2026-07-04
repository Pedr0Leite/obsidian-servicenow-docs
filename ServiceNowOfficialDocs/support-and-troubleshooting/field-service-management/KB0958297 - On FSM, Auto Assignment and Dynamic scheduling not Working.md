---
title: "On FSM, Auto Assignment and Dynamic scheduling not Working"
aliases:
  - KB0958297
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958297
kb_number: KB0958297
last_modified: 2026-04-11
---

## On FSM, Auto Assignment and Dynamic scheduling not Working

  

### Issue

Auto assignment suddenly stopped working and getting and error message as "Something went wrong. Please rerun".

### Release

NA

### Cause

This is because of customization.

### Resolution

When reproducing the issue there are system logs as below errors  
  
org.mozilla.javascript.EcmaError: "MatchingDimensionRejectedTechnicians" is not defined.  
Caused by error in sys\_script.658d666bdbf928508a705baed3961979.script at line 1  
  
\==> 1: (function processDimension(task, users, taskFieldValues, args) {  
2: var matchingDimensionRejectedTechnician = new MatchingDimensionRejectedTechnicians();  
3: return matchingDimensionRejectedTechnician.filterOutRejectedTechnician(task,users,taskFieldValues,args);  
4: })(task,j2js(users), j2js(taskFieldValues), j2js(args));  
  
So, the first thing that is checked is what is MatchingDimensionRejectedTechnicians and its a script include which is missing on your UAT instance and available on DEV instance.
