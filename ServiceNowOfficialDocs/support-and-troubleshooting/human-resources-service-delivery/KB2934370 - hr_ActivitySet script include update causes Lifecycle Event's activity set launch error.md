---
title: " hr_ActivitySet script include update causes Lifecycle Event's activity set launch error"
aliases:
  - KB2934370
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2934370
kb_number: KB2934370
last_modified: 2026-04-02
---

## Issue

HR tasks are not created for HR Cases with HR Service=Onboarding.

Errors are observed in Activity Set Execution logs, such as

```
Error thrown when registering activity set context: Error: ErrorMethodName: _createActivitySetContext->skipActivitySet ## undefined is not a function. Source: sys_script_include.088df2fe534a22003066a5f4a11c08de.script lineNumber: 1711
```

The issue was traced to a recent update of the hr\_ActivitySet script include.   
  

## Resolution

1.  Review the list of invalidated Restricted Caller Access (RCA) records with source = 'Script Include: hr\_ActivitySet' and status!=Allowed
2.  Allow the specific RCA record (sys\_id: 071518a053532300e167ddeeff7b12d9) that prevents hr\_ActivitySet from accessing the sn\_cd.cd\_Audience script include.
3.  Verify that the RCA is updated to 'Allowed' status to restore access and resolve the error.
