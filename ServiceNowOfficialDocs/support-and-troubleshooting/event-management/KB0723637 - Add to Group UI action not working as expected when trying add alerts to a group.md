---
title: "\"Add to Group\" UI action not working as expected when trying add alerts to a group"
aliases:
  - KB0723637
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723637
kb_number: KB0723637
last_modified: 2026-05-22
---

## "Add to Group" UI action not working as expected when trying add alerts to a group

  

### Issue

 

# Symptoms

* * *

1.When you click on "Add to Group" UI action on the alert form, it redirects to the same form instead of opening the alerts list.

2.Additionally we observe the below error in the system logs :

org.mozilla.javascript.EcmaError: "parent" is not defined.  
Caused by error in sys\_ui\_action.3440ff939f0022003cb39b0cc32e7084.script at line 1

\==> 1: gs.getSession().putClientData('em\_add\_parent\_id', parent.sys\_id);  
2: gs.getSession().putClientData('em\_add\_parent\_number', parent.number);  
3:  
4: action.setRedirectURL('/em\_alert\_list.do?sysparm\_view=add\_to\_group&sysparm\_fixed\_query=correlation\_group!=1^parent!=' + parent.sys\_id+"^ORparentISEMPTY^sys\_id!=" + parent.sys\_id + "^state!=Closed&sysparm\_query=maintenance=false");

# Release

* * *

Any

# Cause

* * *

From research, "glide.security.strict.actions" system property was causing the issue. This property is to: "Check conditions on UI actions before execution. Normally the conditions are only checked during form rendering.". So, its related to visibility of UI Actions. 

### Release

Any

### Resolution

# Resolution

* * *

1.Navigate to the sys\_properties table

2\. Search for the property "glide.security.strict.actions"

3\. Set the value for the property to true
