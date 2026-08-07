---
title: "Auto-complete does a 'starts with' search instead of 'contains' when the system property 'glide.ui.goto_use_contains' is set to true for reference fields."
aliases:
  - KB0727722
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727722
kb_number: KB0727722
last_modified: 2024-04-07
---

## Auto-complete does a 'starts with' search instead of 'contains' when the system property 'glide.ui.goto\_use\_contains' is set to true for reference fields.

  

### Issue

# Symptoms

* * *

For a reference field on a form, searching for a value and clicking on reference lookup, the search takes 'Starts With' instead of 'Contains'.

(Eg : For assignment group field on incident record, on entering fo, two valid results are shown. Clicking on reference lookup shows Name starts with 'fo' and not Name contains 'fo'). 

![](sys_attachment.do?sys_id=eda9a062db42b450e515c2230596190b)

# ![](sys_attachment.do?sys_id=a1a9a062db42b450e515c22305961911)

# Release

* * *

Any supported release

# Cause

* * *

The system property 'glide.ui.goto\_use\_contains' controls the search in the list view and not reference lookup.

# Resolution

* * *

A system level user preference with the format <table\_name>.autocomplete.contains with value true has to be created for contains search to work on reference fields.

For assignment group field, User Preference with below details has to be created:

Name :sys\_user\_group.autocomplete.contains

Type : true|false

Value : true

System : true

Once the user preference is created, make sure to clear the instance cache (by doing cache.do) and login back to the instance.
