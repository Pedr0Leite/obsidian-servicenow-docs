---
title: "Service Portal - Viewing which Client Scripts, UI Policies, and UI Actions are loaded on the page"
aliases:
  - KB0684010
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684010
kb_number: KB0684010
last_modified: 2025-01-03
---

## Service Portal - Viewing which Client Scripts, UI Policies, and UI Actions are loaded on the page

  

### Issue

If you've ever needed to know exactly which Client Scripts, UI Policies, and UI Actions are loading onto the page when you view a form or Service Catalog item in Service Portal, the information is readily available if your know where to look.

If you are using the out-of-box "SC Catalog Item" and "Form" widgets, you can find this information in the widget's scope.

To view the widget's scope, hold down the CTRL key and right-click anywhere in the widget. Choose "Log to console: $scope". Open your browser developer tools to the JavaScript console. Expand the "Object" that has been dumped to the console.

# "Form" widget

* * *

### Client Scripts are located at:

data.f.client\_script

### UI Policies are located at:

data.f.policy

### UI Actions are located at:

data.f.\_ui\_actions

![](sys_attachment.do?sys_id=962d6c62db82b450e515c2230596191c)

# "SC Catalog Item" widget

* * *

### Client Scripts are located at:

data.sc\_cat\_item.client\_script

### UI Policies are located at:

data.sc\_cat\_item.policy

![](sys_attachment.do?sys_id=5a2d6c62db82b450e515c22305961921)
