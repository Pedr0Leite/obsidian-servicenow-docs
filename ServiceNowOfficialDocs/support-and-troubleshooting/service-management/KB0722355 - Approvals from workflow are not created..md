---
title: "Approvals from workflow are not created."
aliases:
  - KB0722355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722355
kb_number: KB0722355
last_modified: 2024-04-07
---

## Approvals from workflow are not created.

  

### Issue

# Symptoms

* * *

1) No Approvals from workflow are created.

2) Workflow shows the approval activity as skipped.

# Release

* * *

Kingston, London

# Cause

* * *

The business rule "approval\_query" is active on instance.

If the business rules "approval\_query" is active on instance and the user do not have "approval\_admin" role, the query for approvals results "0" records which is making the workflow to skip the approval activity as there are "0" records.

# Resolution

* * *

The business rule "approval\_query" is not active OOB, Please deactivate the business rules "approval\_query" Which will create approvals from workflow.
