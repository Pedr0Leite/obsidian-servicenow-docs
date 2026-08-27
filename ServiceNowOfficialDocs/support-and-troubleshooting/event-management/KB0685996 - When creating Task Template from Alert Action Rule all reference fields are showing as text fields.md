---
title: "When creating Task Template from Alert Action Rule all reference fields are showing as text fields"
aliases:
  - KB0685996
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685996
kb_number: KB0685996
last_modified: 2025-01-03
---

## When creating Task Template from Alert Action Rule all reference fields are showing as text fields

  

### Issue

# Symptoms

* * *

When creating Task Template from Alert Action Rule, all reference field are showing as text field 

# Release

* * *

Any

# Cause

* * *

This is expected behavior when open another popup window from a popup window.

However, for fields that are defined as reference, limited lookup functionality do exists in popup windows.

When user starts typing in such field, a drop down list is displayed allowing the user to select relevant item - see attached screenshot below.

![](sys_attachment.do?sys_id=82292caedb02b450e515c22305961976)

# Resolution

* * *

Create create a Task Template via: 

  
Event Management > Settings > Task templates > New   
  
Then the Service field is showing as reference correctly. 

Once task template is created, select it in the Alert Action Rule.
