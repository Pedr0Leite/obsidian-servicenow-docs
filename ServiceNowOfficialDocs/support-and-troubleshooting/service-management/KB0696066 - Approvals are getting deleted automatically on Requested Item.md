---
title: "Approvals are getting deleted automatically on Requested Item"
aliases:
  - KB0696066
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696066
kb_number: KB0696066
last_modified: 2025-05-19
---

## Approvals are getting deleted automatically on Requested Item

  

### Issue

# Symptoms

* * *

Approvals are getting deleted automatically on Requested Item.

# Release

* * *

Kingston and earlier

# Cause

* * *

No approval records are returned when the workflow hits the approval coordinator the second time, so all the approval records are deleted.

# Resolution

* * *

The second time the workflow hits the approval coordinator, the script inside the "Approval - group activity" returns no approvers. 

So when the there are no approvers returned for the second time, the workflow engine would assume that there should not be any approvers and so it goes and deletes all the approvers. This issue occurs since the same approval coordinator activity is being hit by the workflow for the second time.

The behavior is present in Jakarta as well. 

This is an expected behavior. When we are hitting the same approval coordinator twice, and when we add the same approval group the second time, then the approval records will not be deleted and the workflow engine would know that approvers have already been approved and it would move to the next activity. 

But in our case, we are adding no approvers the second time, so the workflow engine would assume that there should not be any approval records and so all the approval records will be deleted.
