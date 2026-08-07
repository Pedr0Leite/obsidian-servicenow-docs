---
title: "User Interface automatically changes to UI15"
aliases:
  - KB0749850
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749850
kb_number: KB0749850
last_modified: 2026-06-19
---

## User Interface automatically changes to UI15

  

### Issue

 On customer instances, the user interface automatically changes to UI15. 

### Release

Any Release

### Cause

The issue happens when a script include is using "sysparm\_device" parameter. When the script include is called from front-end and the value of "sysparm\_device" is passed, that is when the issue occurs.

"sysparm\_device" is an OOB parameter used to control page view.

### Resolution

It is suggested that instead of using "sysparm\_device", there are some other keywords used.

Since "sysparm\_device" is an internally used parameter, any other parameter that is not used by ServiceNow can be used to pass the required value in a script include.

### Related Links

This information is applicable to all versions of ServiceNow
