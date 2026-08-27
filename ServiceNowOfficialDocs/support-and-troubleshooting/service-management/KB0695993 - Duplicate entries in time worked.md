---
title: "Duplicate entries in time worked"
aliases:
  - KB0695993
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695993
kb_number: KB0695993
last_modified: 2024-04-07
---

## Duplicate entries in time worked

  

### Issue

# Symptoms

* * *

Duplicate entries in "Time Worked" related list are seen

# Release

* * *

Jakarta Patch 8a

# Cause

* * *

The CHG record's state field is being updated twice, causing the double entry in Time Worked related list.

# Resolution

* * *

After reviewing both Business Rules and Client Scripts on the change\_request table, it was found that neither of those was responsible for the experienced behavior.  
  
In the user's instance, there was a custom UI Action "Next Step" where the user was updating the state of the CHG via this code:  
  

```
action.setRedirectURL(current);current.state = parseInt(current.state) + 1;current.update();
```

  
This is the update which should move the CHG from a state of "Draft" to a state of "Assess".  
  
The issue happens when, somewhere within the user's custom CHG workflow "CHG - General" or it's subflow "CHG - Approval", there is a second state update. This is causing the double stamp under the "Time Worked" related list.  
  
For certain, the root cause of the second state change is in the user's custom workflow(s).  
  
Finding out where within the workflow(s) this second update is happening, and what specific workflow activity is causing it, is something that the user and their development team would handle internally.
