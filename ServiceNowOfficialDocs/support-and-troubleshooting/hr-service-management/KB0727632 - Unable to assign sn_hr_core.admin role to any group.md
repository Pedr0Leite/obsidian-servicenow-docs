---
title: "Unable to assign sn_hr_core.admin role to any group"
aliases:
  - KB0727632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727632
kb_number: KB0727632
last_modified: 2024-04-07
---

## Unable to assign sn\_hr\_core.admin role to any group

  

### Issue

# Symptoms

* * *

Unable to assign sn\_hr\_core.admin role to any group

# Release

* * *

London Patch 4 Hot Fix 2

# Cause

* * *

In order to add groups to the role record you should have admin,user\_admin and sn\_hr\_core.admin role. Specifically 'sn\_hr\_core.admin' should be provided by user who already has 'sn\_hr\_core.admin' role in order to make this work.   
  

# Resolution

* * *

Execute normal change on production to remove and re-add 'sn\_hr\_core.admin' role to your user as Maint.
