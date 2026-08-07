---
title: "When initiating a chat conversation the first message sent by the End User to the queue is missing also, after closing a chat session all messages disappear"
aliases:
  - KB0647536
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647536
kb_number: KB0647536
last_modified: 2024-04-07
---

## When initiating a chat conversation the first message sent by the End User to the queue is missing also, after closing a chat session all messages disappear

  

### Issue

# Symptoms

* * *

-   Within Connect Chat, the initial message from the caller user does not reach the agent user, however subsequent messages go through successfully. When an end user initiates a conversation, the responding agent user accepts the chat, but does not receive the first message. 
-   Usually the chat window header will reflect the initial message of end user, hence customer could work-around the issue via using the chat window header for referring the initial message. However, when the message is longer than 160 characters, the chat window will truncate the text starting at the 161st character. This is due to the Short Description field being set OOB to 160 characters length. Trying to increase the Short Description length is not an allowed option, so users can not rely on the chat window short description for longer texts.
-   Also once the chat is end by end chat UI action by the agent or the user then on the refresh of the page the chat conversation is lost. The conversation is lost on both the sides of the agent and the customer and it wont be visible anymore.

# Release

* * *

Kingston, Jakarta, Istanbul 

# Cause

* * *

The Live Feed permission logic is set on the Comments field type on the main Task table. OOB, this is of type 'Journal Input'. If the Comments field type is set to anything different from 'Journal Input', the Live Feed permissions fail and cause the initial message from the user to not to reach the agent.

# Resolution

* * *

Do not alter the field type of \[task\].\[comments\] or revert it back to the out of the box definition as 'Journal Input'.
