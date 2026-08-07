---
title: "Deletion Option Not Available for Asset Contacts Table"
aliases:
  - KB1736483
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1736483
kb_number: KB1736483
last_modified: 2024-12-25
---

## Issue

User cannot delete multiple Asset Contacts \[sn\_customerservice\_m2m\_asset\_contact\] from the list view.

Reproduced Steps

1.  Open alm\_asset.LIST and click data.
2.  Check the data in Asset Contacts \[sn\_customerservice\_m2m\_asset\_contact\] tab
3.  Select pull down menu in "Action on selected rows..."
4.  "Delete" is not listed.  
    ![](/sys_attachment.do?sys_id=cb4c81e9936e56105736b25d6cba104b "KB-001.png")

## Resolution

To resolve this issue, follow these steps:  
  
1\. Click "I" icon to open the data in the Asset Contacts \[sn\_customerservice\_m2m\_asset\_contact\].  
![](/sys_attachment.do?sys_id=747cc5e9936e56105736b25d6cba1055 "KB-002.png")  
2\. Click delete button.  
![](/sys_attachment.do?sys_id=ad9c0de9936e56105736b25d6cba1096 "KB-003.png")  
  
Note: It is no longer possible to delete multiple Asset Contacts records at once from the list view. Each record must be deleted individually.
