---
title: "HR Tasks are not being generated for Lifecycle Event cases"
aliases:
  - KB0788929
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788929
kb_number: KB0788929
last_modified: 2024-04-08
---

## Issue

HR Tasks are not being generated for Lifecycle Event cases.

## Resolution

In order to prevent this from occurring in the future, it is advisable to validate that the "Restricted Caller Access" records associated with the source/target 'Script Include: hr\_ActivitySet' are not modified once changes are made to the Script Include.  
  

To solve this issue, set the RCA record(s) to 'Allowed' state.
