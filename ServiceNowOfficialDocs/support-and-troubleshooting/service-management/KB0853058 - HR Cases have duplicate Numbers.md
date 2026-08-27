---
title: "HR Cases have duplicate Numbers"
aliases:
  - KB0853058
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853058
kb_number: KB0853058
last_modified: 2024-04-08
---

## HR Cases have duplicate Numbers

  

### Issue

The user was seeing that many of their HR Case numbers were being duplicated, and they wanted to know what the cause was.

### Cause

The user had a custom UI Action with a "current.update()" in it which was presumed to have caused the issue.

### Resolution

After reviewing the syslog\_transaction record where the action was performed by the user just at the time of the duplication, and cross-checking with the corresponding localhost logs, a _Duplicate entry for key PRIMARY_ error was found.  
  
Immediately following the error, a small stack-trace displayed with only two references provided within it - both of which pointed to the user's custom UI Action where a custom script containing "current.update()" was fired.   
  
This is the most common cause of the _Duplicate entry for key PRIMARY_ error (improperly using "current.update()"), and proved to be the cause in this user's case as well.
