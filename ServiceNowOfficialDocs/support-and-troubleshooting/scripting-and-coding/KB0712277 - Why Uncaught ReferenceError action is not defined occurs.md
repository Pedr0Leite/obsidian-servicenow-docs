---
title: "Why \"Uncaught ReferenceError: action is not defined\" occurs?"
aliases:
  - KB0712277
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712277
kb_number: KB0712277
last_modified: 2024-11-21
---

## Why "Uncaught ReferenceError: action is not defined" occurs?

  

### Issue

While loading rm\_release.do form, observed below java script error on browser console,

Uncaught ReferenceError: action is not defined

Below screenshot of error shows the complete stack of exception,

![Error uncaught reference error on UI action in form view](sys_attachment.do?sys_id=7b907dcc93461ad0101833527cba1097 "Error uncaught reference error on UI action")

### Release

Any supported release. 

### Cause

Above described error occurs due to the reason that "Client" checkbox is ticked on an UI action, however "Onclick" function and client side code is not written on the UI Action script as shown in the below screenshot,

![UI Action with "Client" checked but onClick action is empty.](sys_attachment.do?sys_id=0ca07dcc93461ad0101833527cba1099 "client is selected but no onclick action defined")

Since there is no client side code defined, the server-side code is loaded on the on-load of the form and hence server side code breaks as the server side objects will not be available at client side.

### Resolution

Review the UI action, if "Client" checkbox is accidentally ticked, uncheck it.

OR

If client side code execution is needed, define onClick method and write client side code in script section, so that server-side code is only executed at server side upon client side code is successfully completed. 

### Related Links

[UI Actions](https://docs.servicenow.com/csh?topicname=c_UIActions.html&version=latest "UI Actions")

[Create a UI Action](https://www.servicenow.com/docs/csh?topicname=t_EditingAUIAction.html&version=latest "Create a UI Action")
