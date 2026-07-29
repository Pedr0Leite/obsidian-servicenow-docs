---
title: "Updating an end date on a project task does not update the end date on the project"
aliases:
  - KB0696643
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696643
kb_number: KB0696643
last_modified: 2024-04-07
---

## Updating an end date on a project task does not update the end date on the project

  

### Issue

# Symptoms

* * *

When updating an end date on a project task does not update the end date on the project. Errors are also seen in the logs

# Release

* * *

Jakarta patch 8b

# Cause

* * *

The Original End Date on the project is blank

# Resolution

* * *

From the investigation, we kept seeing this error:

     com.snc.planned\_task.core.PlannedTaskAPI: PPM Unable to Recalculate Task : 47375a9a13ee03005dcff4b2e144b0fa null: no thrown error

From there error, it was seen that the Original End Date on the Project was blank. Therefore, this was causing it to not be updated. After putting in a value into the field by turning off the "Read Only" attribute on the sys\_dictionary entry for Original End Date, it was seen that the project was rolling up correctly after that.
