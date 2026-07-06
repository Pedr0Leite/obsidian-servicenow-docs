---
title: "How Fulfillment Count on Usage Data for Applications is calculated"
aliases:
  - KB0785203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785203
kb_number: KB0785203
last_modified: 2024-04-08
---

## Issue

The fulfiller count in the table Usage Data for Applications (ua\_app\_usage) is calculated from the columns (Insert Other's Request Count + Update Other's Request Count) from the same table.  
Insert Other's Request Count is calculated from the number of insert's on request records not owned by the user  
Update Other's Request Count is calculated from the number of updates on request records not owned by the user (Basically this means, if a fulfiller updates any record not owned by them it is counted as Update Other's Request Count).

![](/sys_attachment.do?sys_id=4fae444ddb4c7890dc2beeb5ca9619d4)
