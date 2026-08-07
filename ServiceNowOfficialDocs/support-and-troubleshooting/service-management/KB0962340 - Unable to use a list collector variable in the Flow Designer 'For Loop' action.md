---
title: "Unable to use a list collector variable in the Flow Designer 'For Loop' action"
aliases:
  - KB0962340
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962340
kb_number: KB0962340
last_modified: 2025-07-15
---

## Unable to use a list collector variable in the Flow Designer 'For Loop' action

  

### Issue

In Flow Designer, after retrieving a list collector variable from the Get Catalog Variables action, you cannot use it as the array in a For Loop action.

### Release

### Cause

The Get Catalog Variables action returns a list collector as a comma separated string rather than an array. Because of this, we cannot iterate through the values from the string list.

### Resolution

Create a flow with below approach:

\==============  
Trigger - Service Catalog

Action 1 - Get Catalog Variables from \[Request Item\] (pulls in List Collector field)

Action 2 - Look Up \[Account\] Records where Sys ID = \[List Collector Field (from Action 1)\] 

Action 3 - For Each \[Account Record\] (from Action 2)  
\==============
