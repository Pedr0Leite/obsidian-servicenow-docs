---
title: "Flow Designer UI - jumbled/messy connecting lines between actions"
aliases:
  - KB0952631
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952631
kb_number: KB0952631
last_modified: 2024-02-26
---

## Flow Designer UI - jumbled/messy connecting lines between actions

  

### Issue

![](sys_attachment.do?sys_id=aefe4736dbca68d0679499ead39619ef)

  

The connecting lines between Flow actions are displaying incorrectly, in a jumbled and messy manner. Please see screenshot. 

  

### Cause

Duplicate records in Flow Designer tables

### Resolution

Suggested workaround:  
  
The issue seems to be related to duplicated records in a couple of the Flow Designer tables. Deleting these duplicates returns the flow to the expected state. 

1.  Go to the \`sys\_hub\_flow\_logic\` table and filter for the flow you're working with and check for any duplicate records. Duplicate here means they have the same UI Identifier. Delete any duplicates.  
    
2.  Go to the \`sys\_hub\_actioin\_instance\` table and filter for your flow and check for and delete any duplicates here. Duplicate here means the same UI Identifier too, but they could have different orders. If they do, delete the record with an invalid order like "3.1.1.1.0" which is invalid because orders should not end in a "0".  
    
3.  Go to your flow and refresh if you had it open already. The extra lines should disappear, but the flow might be out of order. Re-order the instances in the correct order
