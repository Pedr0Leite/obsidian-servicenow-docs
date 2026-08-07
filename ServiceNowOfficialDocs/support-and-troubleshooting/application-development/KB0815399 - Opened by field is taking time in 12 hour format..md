---
title: "\"Opened by\" field is taking time in 12 hour format."
aliases:
  - KB0815399
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815399
kb_number: KB0815399
last_modified: 2024-04-08
---

## "Opened by" field is taking time in 12 hour format.

  

### Issue

"Opened by" field is taking time in 12 hour format. "yyyy-MM-dd _hh_:mm:ss"

### Release

All environments.

### Cause

The time format is chosen as hh(12-hour) instead of (24-hour) HH, which has caused the issue

### Resolution

In the transform map : https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_transform\_map.do?sys\_id=xxxx

Field "opened\_at" is mapped to sys\_created\_on. sys\_created\_on is pointing to 12-hour format. "yyyy-MM-dd _hh_:mm:ss" , for 24 hours it has to be " yyyy-MM-dd **HH**:mm:ss"
