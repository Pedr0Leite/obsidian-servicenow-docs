---
title: "Connect Support requires support team members to have the \"live_feed_admin\" or \"admin\" role to close cases to prevent publishing public messages to the Live Feed"
aliases:
  - KB0598883
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598883
kb_number: KB0598883
last_modified: 2024-04-07
---

## Connect Support requires support team members to have the "live\_feed\_admin" or "admin" role to close cases to prevent publishing public messages to the Live Feed

  

### Issue

When using the Connect Support plugin, a user will start a support chat session that will then be accepted by the support agent.

While all conversations between user and agent will remain private within a conversation, when the support agent closes the case, a public message is created and is accessible on the Live Feed within the Company Feed.

-   if the agent closes the case before the user, a message "<Agent-name> has left the support session" is published
-   if the agent closes the case after the user has ended the session, a message "<Agent-name> has closed the support session" is published

The Live Feed and Connect Support use the same table (live\_message) to store messages, so the public message for closing the case from the Connect Support session is immediately visible on the Company Feed. All other messages in the conversation remain in the private group feeds.

To ensure the closing of the case in Connect Support remains a part of the user-agent conversation and is a private message, ensure the agents are given the role "live\_feed\_admin" or "admin".
