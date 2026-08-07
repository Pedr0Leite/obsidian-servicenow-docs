---
title: "Create AD Object activity fails when 'samaccountname' value starts with a number"
aliases:
  - KB0718104
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718104
kb_number: KB0718104
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

In Orchestration, Create AD Object activity fails.

# Release

* * *

All

# Cause

* * *

For the Create AD Object activity, the 'Object data' parameter in the ecc queue is corrupted. Once the activity is triggered, goto ecc queue and check the output record. The 'Object data' parameter will look something like this: n$\_$$\_$\_

# Resolution

* * *

1\. In the workflow, for Create AD Object activity, the 'Object data' parameter value is defined as '{"sAMAccountName":${workflow.scratchpad.database}}'.   
2\. This is causing issues during parsing the value in the activity definition.   
3\. To resolve this issue, set the JSON object in the scratchpad and then use the scratchpad variable in the workflow input.   
  
Define something like below in the 'Run Script' block:   
workflow.scratchpad.database={"sAMAccountName":"test123"};   
  
Use the variable in the activity input:   
Object data: ${workflow.scratchpad.database}.
