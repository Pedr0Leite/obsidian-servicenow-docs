---
title: "Unable to set Assignment Group in Create task by SysID (sys_id)"
aliases:
  - KB0745499
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745499
kb_number: KB0745499
last_modified: 2024-04-07
---

## Unable to set Assignment Group in Create task by SysID (sys\_id)

  

### Issue

# Symptoms

In Flow Designer, the assignment Group reference field cannot accept a value with type SysID (sys\_id)

When you drag a field with type SysID (sys\_id), the assignment group field is not accepting it

# Release

London

# Cause

Flow Designer allows  a reference, documentID, and string type in the Assignment group field

# Resolution

1\. Before the action with the Assignment Group field, add an OOB action from ServiceNow Core "Lookup Record" with the Conditions field having a Sys ID filter (this will take in a sys\_id pill type).   
2. Now in the Create Task action for the Assignment group field, you should now be able to drag in the record from the output of the previous action.
