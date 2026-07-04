---
title: "Requested Item (RITM) workflows are being automatically approved when assigned to a certain user"
aliases:
  - KB0814948
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814948
kb_number: KB0814948
last_modified: 2024-09-20
---

## Requested Item (RITM) workflows are being automatically approved when assigned to a certain user

  

### Issue

When RITMs are being assigned to a certain user, the associated workflow's approvals are being automatically approved.

### Resolution

It was found that there were two custom _before_ query Business Rules (BRs) which were causing the issue.  
  
Upon disabling the two custom BRs, the user was able to correctly see the group approval records, and the system could then resolve the approvals and not skip them.  
  
The root of the problem, then, is that the custom query BRs were blocking the user from seeing group approval records.  
  
Hence, when the user tried to update the record and critical workflow BRs ran and tried to talk to the workflow, at that time the system tried to resolve the group approval records but could not due to the user's inability to see them per the query BRs. Therefore, the system broadcasts to the workflow "I can't resolve (find) these - so let's skip them".  
  
This is why the "activity.result" on the approval - group activity is not "approved", but is "skipped" (the condition path to exit the "Always" condition is activity.result == 'approved' OR activity.result == 'skipped').
