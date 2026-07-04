---
title: "Approvals Being Requested for Inactive Users"
aliases:
  - KB0693290
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693290
kb_number: KB0693290
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Approvals are requested for inactive users

# Release

* * *

I,J,K - latest Patch

# Cause

* * *

The current OOB functionality is that even though the user is inactive, an approval  will be added for that user. However we have a workaround to change this functionality

  

# Resolution

* * *

At present the OOB is that a user who is inactive will still have approvals created.  I verified that there is an enhancement request to change this functionality.

  

 However, we have a workaround, if you want to change this functionality you will need to modify the activity definition "Approval - User". 

  

STEPS:

1\. Type in "wf\_activity\_definition.list" in the filter navigator

2\. Search for "Approval - User" in the Name column and open the record.

3\. Under script section, on line 195, we can find the function \_buildApprovals,

  

Remove lines 195 to 201 and replace with the code below,

  

\_buildApprovals: function(userIds, state, approvalOrder) { 

var approvalIds = \[\]; 

var user = new GlideRecord('sys\_user'); 

for (var id in userIds){ 

user.get(id); 

if (user.active == true){ 

approvalIds.push(this.\_createApproval(id, state, approvalOrder)); 

} 

} 

return approvalIds; 

}, 

  

4\. Save the record.

5\. Type "cache.do" in the filter navigator.

  

Now the approval will not be created for those users who are inactive.
