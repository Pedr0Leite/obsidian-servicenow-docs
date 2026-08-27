---
title: "Approval - Group activities are getting skipped in workflow. Why?"
aliases:
  - KB0779284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779284
kb_number: KB0779284
last_modified: 2024-09-20
---

## Approval - Group activities are getting skipped in workflow. Why?

  

### Issue

In the user's Standard CHG workflow, they were seeing that their Approval Coordinator activity had an activity.result of "skipped", but they could not figure out why.

### Resolution

After attempting to reproduce the above-reported issue, it was found that the failure really occurs upon clicking the "Request Approval" UI Action, and not at a later time as the user supposed.  
  
The issue is seen when the "Avengers Facility: Security Upgrade Request" Standard Change template is chosen. The reason the workflow is skipping approvals for this specific template is that the conditions for both Approval - Group activities within the Approval Coordinator fail. Note that the first approval group for "Lawn-care group" requires that the category be "Lawn-care" and the subcategory be "Hedge trimming". This is not the case with the "Avengers Facility: Security Upgrade Request" template. The category with this Standard Change template is "Facility" and the subcategory is "Security".  
  
Next, the "Lawn-care Review" Approval - Group activity says that the "u\_lawncare\_approval\_groups" field must not be empty. Yet, it is when approval is requested. Hence, this also fails.  
  
Finally, the entire Approval Coordinator requires that _**all**_ child activities must be approved. Because both requirements to evaluate this activity fail, the workflow progresses with a result of "skipped".  
  
When Out of Box (OOB) Business Rule "Restrict fields from Standard Change" is disabled, allowing values to be entered via script, the Category and Sub-category can be hard-coded to meet the "Lawn-care group" activity, and some group can also be set inside of the custom field "u\_lawncare\_approval\_groups" to satisfy the "Lawn-care Review" Approval - Group activity. When this is done, the workflow works per expectation.  
  
Therefore, the real issue is that the user just needs to meet the right requirements for the Approval Coordinator to evaluate. Otherwise, it will skip. This is the natural behavior of the Platform, and is expected.
