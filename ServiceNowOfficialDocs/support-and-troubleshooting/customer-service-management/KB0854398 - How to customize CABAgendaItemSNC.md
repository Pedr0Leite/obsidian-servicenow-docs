---
title: "How to customize CABAgendaItemSNC "
aliases:
  - KB0854398
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854398
kb_number: KB0854398
last_modified: 2025-01-02
---

## How to customize CABAgendaItemSNC

  

### Summary

The OOB script include "CABAgendaItemSNC" has a protection policy and we are not able to edit the mentioned script include.

How do I customize the behaviour captured in that script include.

### Instructions

1.  Log in
2.  Go to the list of script includes
3.  open 'CABAgendaItemSNC
4.  Switch to the Change Management - CAB Workbench application
5.  Observe that you do not have permissions to edit this file.

  
**Most Probable Cause:**  
  
This is ootb behaviour. This particular item is read-only based on its protection policy.  
  
**Solution Proposed:**  
  
In this case, what we advise is that you edit the CABAgendaItem script include.  
This object extends the CABAgendaItemSNC. That means that if you define a function here, it will take precedence over the one defined in the other script include.  
  
It is designed this way so that the CABAgendaItemSNC will continue to get updates and it will be easier for you to maintain any customizations by comparing them to the updated version. It will also easily allow you to revert to ootb should you choose to do so.
