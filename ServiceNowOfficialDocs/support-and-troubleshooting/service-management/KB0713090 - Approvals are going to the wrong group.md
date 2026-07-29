---
title: "Approvals are going to the wrong group"
aliases:
  - KB0713090
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713090
kb_number: KB0713090
last_modified: 2024-04-07
---

## Approvals are going to the wrong group

  

### Issue

# Symptoms

* * *

-   Approvals are going to an unexpected (incorrect) group

# Release

* * *

Kingston Patch 6, Hot Fix 3

# Cause

* * *

Approvals are going to the correct group (see continued explanation below...) 

# Resolution

* * *

The root cause of the issue is that the user is dot-walking the approval group's value. In other words, if the user navigates to any RITM where they are seeing this issue, they can go down to the Approvers related list, click the personalization cog icon, and they will see that the Assignment Group is a dot-walked value.  
  
The dot-walked value is "Approval for.Assignment Group".  
  
This means that whatever value is in the "Assignment Group" field near the top of the form is going to be copied down into the Approvers related list "Assignment Group" field value.  
  
The user can test and confirm this by changing the value in "Assignment Group" near the top of the record, saving the record, and they will see the change reflected in the value in the Approvers related list per their change.
