---
title: "No condition defined against sn_hr_core_case table 'New' UI Action results in button still showing when 'Omit new button' is checked against List Control"
aliases:
  - KB0727809
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727809
kb_number: KB0727809
last_modified: 2024-04-07
---

## No condition defined against sn\_hr\_core\_case table 'New' UI Action results in button still showing when 'Omit new button' is checked against List Control

  

### Issue

# Symptoms

* * *

When checking the 'Omit new button' field against the sn\_hr\_core\_case table list control it was found to be still visible in the UI.

The sn\_hr\_core\_case table is part of the 'Human Resources Scoped App: Core' (com.sn\_hr\_core) plugin.

# Release

* * *

This behaviour has been verified to be present in Kingston onwards, but could also be present in prior releases too.

# Cause

* * *

The 'New' UI Action defined against the sn\_hr\_core\_case table has no '!RP.getListControl().isOmitNewButton()' condition defined against it.

This results in the button being displayed in the List UI even when the 'Omit new button' field is checked against the List Control.

# Resolution

* * *

PRB1328620 has been raised to have this addressed in a later release.

As a workaround, the !RP.getListControl().isOmitNewButton() condition can be added to the 'New' UI Action.
