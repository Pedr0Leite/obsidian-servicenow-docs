---
title: "Software Asset Workspace - \"Create entitlement\" form is stuck in loading"
aliases:
  - KB1351941
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1351941
kb_number: KB1351941
last_modified: 2026-05-29
---

## Software Asset Workspace - "Create entitlement" form is stuck in loading

  

### Issue

1\. Open Software Asset Workspace  
2\. Click "Create entitlement" Ui Action.  
3\. Click next, we can see it is stuck in loading.

![](/sys_attachment.do?sys_id=cdc9703f47c3e9d0b8a4aa25126d4335)

4\. Expected Behaviour, it should load the create Entitlement form

![](/sys_attachment.do?sys_id=0d0a747f47c3e9d0b8a4aa25126d436c)

### Release

Any

### Cause

From Browser Inspect, we can find below logs

```
8now_x.js:1 Uncaught (in promise) DOMException: Failed to execute 'put' on 'Cache': Unexpected internal error.
record/alm_license/-1:1 Uncaught (in promise) DOMException: Failed to execute 'add' on 'Cache': Unexpected internal error.
3now_x.js:1 Uncaught (in promise) DOMException: Failed to execute 'put' on 'Cache': Unexpected internal error.
index.js:105 Error while trying to saving history
```

  
This is related to the browser cache issue.

### Resolution

Please try clearing the browser cache / Open the instance in Incognito mode.
