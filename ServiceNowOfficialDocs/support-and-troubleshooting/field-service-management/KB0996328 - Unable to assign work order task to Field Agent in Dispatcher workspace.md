---
title: "Unable to assign work order task to Field Agent in Dispatcher workspace"
aliases:
  - KB0996328
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996328
kb_number: KB0996328
last_modified: 2026-04-19
---

## Unable to assign work order task to Field Agent in Dispatcher workspace

  

### Issue

Dispatcher Workspace is a configurable scheduling application.  
As a dispatcher, you can efficiently route work to field service agents and monitor their performance.  
The issue is unable to assign an agent to the work order task.

Steps to reproduce:  
1.Impersonate the affected user.  
2.Open the dispatcher workspace from filter navigator.  
3.Now check the dispatcher icon and we can find that the work order task is not yet assigned.  
4.Now try to drag the task and drop in the calendar of the user but still we can find that the task is not assigned.

### Release

Every

### Cause

The script include AgentScheduleUtil is customized which is causing the issue.  
The getEventSpan() method is missing in the script include.

### Resolution

Reverting the script include to OOB will resolved the issue as the getEventSpan() method will be present.  
Adding the method "getEventSpan()" would also resolve the issue.

### Related Links

Check the below mentioned scripts id's as well if they are customized.  
1\. Assigned - 5fb15e351b53200050fdfbcd2c071332  
2\. Assigned - 7340f6d3df03110068c383f36bf26372
