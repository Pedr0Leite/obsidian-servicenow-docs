---
title: "How to end a Connect Chat conversation initiated by the \"Connect with board members\" feature on a Visual Task Board"
aliases:
  - KB0656743
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656743
kb_number: KB0656743
last_modified: 2024-04-07
---

## How to end a Connect Chat conversation initiated by the "Connect with board members" feature on a Visual Task Board

  

### Issue

# How to end a Connect Chat conversation initiated by the "Connect with board members" feature on a Visual Task Board

If you enable **Connect Chat** in your instance, it will also enable Chat in the Visual Task Boards (**VTB**).

When you create a conversation from a task board, **all the board members automatically join the conversation**. All these logged in user events are synchronized between the task board and the conversation. 

With the current feature, a **user cannot end a connect conversation initiated within Visual Task Board**. Due to the existing code implications, security access is not granted to end the conversation. Deactivating Connect only on the VTB is also not possible on the current releases.

However, a user can click the **close icon in the chat window**, so to hide the window, even though the chat events handler is still active in the background, and the user is still logged in the chat session. 

In case this issue is relevant to your users, please create a new Enhancement Request from the Self-Service portal on HI.
