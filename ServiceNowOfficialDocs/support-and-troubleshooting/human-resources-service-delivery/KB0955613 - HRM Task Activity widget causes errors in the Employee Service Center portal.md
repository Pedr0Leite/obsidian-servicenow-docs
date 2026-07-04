---
title: "HRM Task Activity widget causes errors in the Employee Service Center portal"
aliases:
  - KB0955613
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955613
kb_number: KB0955613
last_modified: 2025-10-02
---

## HRM Task Activity widget causes errors in the Employee Service Center portal

  

### Issue

After an upgrade, when viewing tasks on the ESC portal, the 'HRM Task Activity' widget is displaying an error to the screen:  Cannot find function getStateLabel in object \[object Object\]

### Release

Quebec and higher

### Cause

This can occur if the **todoPageUtils** Script Include (sys\_id=) was customized.

[https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=fb5a924473b7130030f331d7caf6a764](https://instance_name.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=fb5a924473b7130030f331d7caf6a764)

### Resolution

This can be resolved by reverting Script Include **todoPageUtils** to its OOB version.
