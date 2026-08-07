---
title: "How to update the agent's name displayed on Connect Chat without updating the sys_user record"
aliases:
  - KB0656237
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656237
kb_number: KB0656237
last_modified: 2024-04-20
---

## How to update the agent's name displayed on Connect Chat without updating the sys\_user record

  

### Issue

This article describes how to update the agent's name displayed on Connect Chat without updating the sys\_user record.

### Resolution

This article describes how to update the agent's name displayed on Connect Chat without updating the sys\_user record.

The display name on Chat is the user's live\_profile record name value. When a user logs in for the first time, a live\_profile record is created for them, and the Name field is automatically populated with the first/last name of the user record. This record can be modified, which means you can change the Chat name.

1.  Go to /nav\_to.do?uri=/live\_profile\_list.do.
2.  Filter the list with the username for the user for whom you wanted to update the username displayed on Connect Chat.
3.  Open the live\_profile record of that user and update the name field of the record to the desired value.
