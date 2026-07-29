---
title: "Event Management - Alert fields getting wiped out with re-open alerts"
aliases:
  - KB0692588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692588
kb_number: KB0692588
last_modified: 2024-04-07
---

## Event Management - Alert fields getting wiped out with re-open alerts

  

### Issue

# Symptoms

* * *

Alerts custom fields are being cleared out when the Alert is reopened

# Release

* * *

All releases

# Cause

* * *

1.   When you click ‘New’ button, Designer loads all fields (non-system) on Alert table and place them under Transform and Compose Alert Output tab.
2.  The Custom fields are left blank by default and so are some of the OOB fields.
3.   Onload, all fields are marked as not dirty (not modified) on client side.
4.   When user save the rule, backend logic loops over all form elements and check to see if they are dirty (modified). An em\_compose\_field record is created for each ‘dirty’ element.
5.   If a field has data and then blanked out, then an em\_compose\_field record will be created, mapping the value for that field to a blank value. Similarly, if a field has no value and a value is entered and and then removed. The field is still marked as dirty and an em\_compose\_field record with blank value mapping is created as well.

Note:  If the Alert is reopened, the value of those fields will be blanked, due to this mapping.

# Resolution

* * *

Remove the record from the em\_compose\_field which has a mapping to those blank fields.
