---
title: "User (sys_user) fields are syncing to what is populated on associated HR Profile (sn_hr_core_profile)."
aliases:
  - KB0721979
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721979
kb_number: KB0721979
last_modified: 2025-03-11
---

## User (sys\_user) fields are syncing to what is populated on associated HR Profile (sn\_hr\_core\_profile).

  

### Issue

# Symptoms

* * *

User (sys\_user) fields are syncing to what is populated on associated HR Profile (sn\_hr\_core\_profile).

# Release

* * *

Kingston

# Resolution

* * *

This is working as designed.

This is occurring because (Synchronize fields to sys\_user/Synchronize fields to sn\_hr\_core\_profile) business rules are designed to run upon updating a (sn\_hr\_core\_profile) record:  
_https://<instance-name>.service-now.com/sys\_script\_list.do?sysparm\_query=nameSTARTSWITHSynchronize%20fields%20to_

These business rules were designed to keep the (sn\_hr\_core\_profile) & (sys\_user) record in sync as HR users do not usually have access to update the sys\_user table.

The Script include function (hr\_Utils().syncProfileFields) in these BR's call the hr\_Utls Script Include below:

**https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=f65370019f22120047a2d126c42e7000**

Adding the fields you desire to no longer be synced to the (profileExclusionList) of this script include will ensure that these fields are no longer synced when updating an HR profile
