---
title: "Approvals being approved (skipped) unexpectedly. Why? (Hint: Approval workflow activity can't resolve parameters to pull a group/user to approve)"
aliases:
  - KB0786264
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786264
kb_number: KB0786264
last_modified: 2024-09-20
---

## Approvals being approved (skipped) unexpectedly. Why? (Hint: Approval workflow activity can't resolve parameters to pull a group/user to approve)

  

### Issue

The user is facing an issue with their Workflow "General Software Request" where the Approval activities inside of the workflow were unexpectedly approved (hint: they have an activity.result of "skipped"). The user wanted to know why this is happening.

### Resolution

It was found that the Approval activities in question could not resolve the parameters that had been set in them. Hence, when they tried to pull approvers and no approvers were returned from the search, the Approval activities were skipped (i.e. took the "Approved" path which has a condition of "activity.result == 'approved' | activity.result == 'skipped'").

Below are the failed parameters:

-   -   `${u_requested_for.manager}`
    -   `6a3a9eeb22393a00b94222131f9619ad   `

With regard to the first parameter `${u_requested_for.manager}`, when navigating to the RITM record where the workflow is attached and viewing the XML for that record, the field "u\_requested\_for" was found to be empty. Hence, the workflow says, "As I am not able to find any value of any user in the 'u\_requested\_for' field, I cannot dot-walk to pull a non-existant user's manager. So, let's skip this" (i.e. take the "activity.result == 'skipped'" path).  
  
This first parameter is on both approval activities, so it fails for both of them.  
  
The second approval activity also contained a possible group (sys\_user\_group) to populate. In this case, the group which this sys\_id is pointing to does not exist in the reported affected instance - hence, the approval activity cannot resolve this parameter either:

-   -   -   /sys\_user\_group\_list.do?sysparm\_query=sys\_id%3D6a3a9eeb22393a00b94222131f9619ad
