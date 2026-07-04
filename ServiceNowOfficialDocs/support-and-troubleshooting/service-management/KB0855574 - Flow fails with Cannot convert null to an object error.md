---
title: "Flow fails with \"Cannot convert null to an object\" error"
aliases:
  - KB0855574
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855574
kb_number: KB0855574
last_modified: 2025-08-06
---

## Flow fails with "Cannot convert null to an object" error

  

### Summary

A flow with a custom action executes without any issues when run as 'User who initiates the session' but not by 'Run by System User'. The flow fails showing "Error: "Cannot convert null to an object" 

The custom action tries to access records but when trying to access the records outside the flow, it cannot find them. 

### Release

Any supported release

### Instructions

The issue is caused by Before Query Business Rules. These rules prevent the flow from accessing the necessary records when running as 'Run by System User'.

To resolve this, deactivate the Before Query Business Rules. After deactivation, the flow can access the records and execute without errors.
