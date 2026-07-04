---
title: "How to insert a message into a Connect Chat or Support conversation by clicking on a connect action"
aliases:
  - KB0623467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623467
kb_number: KB0623467
last_modified: 2024-04-07
---

## How to insert a message into a Connect Chat or Support conversation by clicking on a connect action

  

### Issue

This article explains how to insert a message into a Connect Chat or Connect Support conversation using Connect Action.

There might be business requirements where predefined messages need to be inserted in the chat by clicking a connect action. 

### Release

Any release supporting Connect Support plugin

### Cause

The suggested script below can be added into a Connect Action and it will result in the message displaying in the Connect conversation both for the Agent and End User

var id = sn\_connect.Conversation.get(conversation.sys\_id);  
id.sendMessage({body:"MESSAGE HERE",field:'comments'});

### Related Links

For more details, refer to the below API

[https://developer.servicenow.com/app.do#!/api\_doc?v=london&id=conversation-sendMessage\_String\_String](https://developer.servicenow.com/app.do#!/api_doc?v=london&id=conversation-sendMessage_String_String)
