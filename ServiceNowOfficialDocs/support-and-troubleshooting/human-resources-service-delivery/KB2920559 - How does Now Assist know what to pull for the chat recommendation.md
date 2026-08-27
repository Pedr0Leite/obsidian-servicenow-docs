---
title: "How does Now Assist know what to pull for the chat recommendation"
aliases:
  - KB2920559
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2920559
kb_number: KB2920559
last_modified: 2026-03-27
---

## How does Now Assist know what to pull for the chat recommendation

  

### Summary

When enabling Chat reply recommendation for Now Assist in HRSD.

Reply recommendations are generated based on KB articles, similar chats, and the context of the conversation.

**How does Now Assist know what to pull for the chat recommendation?**

The skill uses real-time conversation history, related case metadata, and knowledge available at the time of the interaction and passes this information to the LLM for reply generation. Displays a draft suggestion that the agent can review, refine, and send.

  
We can check in now assist skill kit. Please find the link below for the same.  
https://<instancename>.service-now.com/now/now-assist-skillkit/skill/9c0665d5a352061075d1d78446fcdaca/params/prompt-id/7ee409653b0b0210c20ad02c95e45a9a/config-id/d9ae10e337f202103f02ee4174924b36/tab-id/id%3Dclw545zce03rw3b8fsw37gk6h

Link to product documentation: [https://www.servicenow.com/docs/bundle/xanadu-intelligent-experiences/page/administer/now-assist-platform/concept/now-assist-chat-recommendation.html](https://www.servicenow.com/docs/bundle/xanadu-intelligent-experiences/page/administer/now-assist-platform/concept/now-assist-chat-recommendation.html)

### Release

Xanadu
