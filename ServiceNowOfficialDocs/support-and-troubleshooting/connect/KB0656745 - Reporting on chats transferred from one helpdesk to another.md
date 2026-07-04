---
title: "Reporting on chats transferred from one helpdesk to another"
aliases:
  - KB0656745
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656745
kb_number: KB0656745
last_modified: 2024-04-07
---

## Reporting on chats transferred from one helpdesk to another

  

### Issue

Reporting on chats transferred from one helpdesk to another

  
  

# Overview

* * *

The chat\_queue\_entry\_transfer table holds transfer only between agents. When you transfer a chat queue conversation to another queue, the platform updates the chat\_queue\_entry record for the current queue to have a status of **Closed Escalated**. You can therefore see how many transfers occurred for a conversation by searching the chat\_queue\_entry table where the state is **Closed Escalated** and then group by the **Group** field.

# How to Report on Transfers

* * *

1.  Type "chat\_queue\_entry.list" in the filter navigator to access the Chat Queue entries.
    
2.  Sort the entries by queue name.
    
    All the chat entries for that specific queue are listed.
    
3.  Filter the result by status (in this case, Closed Escalated) and then group by agent.
    
    The count will be displayed next to the list.
