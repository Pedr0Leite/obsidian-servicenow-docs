---
title: "Approval History of a record is empty when approvals are created via workflow and gets approved."
aliases:
  - KB0714676
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714676
kb_number: KB0714676
last_modified: 2024-04-07
---

## Approval History of a record is empty when approvals are created via workflow and gets approved.

  

### Issue

# Symptoms

* * *

Approval History journal field of a record is empty when approvals are created via workflow and gets approved.

# Release

* * *

Jakarta,Kingston

# Cause

* * *

The property "glide.workflow.user\_approval\_history" is set to false.

# Resolution

* * *

The business rule:" Approval Events (Non-Task)"  and "Approval Events (Task)"  is looking for property "glide.workflow.user\_approval\_history" value.

If the value is set to "true" then approval history journal field is updated with the approver's name and approved time.

Note: This property updates approval history field only for approvals created via workflow
