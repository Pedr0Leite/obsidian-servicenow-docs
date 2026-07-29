---
title: "Reserved for field is not shown on Receive Purchase Order page when Reserve toggle is enabled"
aliases:
  - KB2768094
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2768094
kb_number: KB2768094
last_modified: 2026-02-09
---

## Issue

● On the Receive Purchase Order page, users enable the Reserve toggle but the Reserved for field does not appear consistently

## Resolution

● This is expected behavior based on the Receive Purchase Order template logic  
● Validate the driving conditions for the PO line item  
↳ Confirm Reserve toggle is enabled  
↳ Confirm the item is hardware and not consumable  
↳ Confirm the model asset tracking strategy is not set to do\_not\_track  
↳ Confirm whether assets are already created for the PO line  
● If assets are pre created for the PO line  
↳ Reserved for will not be shown at the line level during receiving  
↳ Reservation handling is expected to be managed on the pre created asset records

● Additional expected behavior when Requested for is populated on the PO line  
↳ When Reserve toggle is enabled and item.requested\_for is present, the controller auto populates Reserved for using Requested for  
↳ If item.requested\_for is empty, Reserved for remains empty and can be selected when the field is visible
