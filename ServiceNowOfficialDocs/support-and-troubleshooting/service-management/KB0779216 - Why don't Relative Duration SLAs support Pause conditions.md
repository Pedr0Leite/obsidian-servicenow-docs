---
title: "Why don't Relative Duration SLAs support Pause conditions"
aliases:
  - KB0779216
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779216
kb_number: KB0779216
last_modified: 2024-12-19
---

## Why don't Relative Duration SLAs support Pause conditions

  

### Issue

The user wanted to know why Relative Durations are listed as not supporting Pause conditions (per the [documentation](https://docs.servicenow.com/csh?topicname=t_UseARelativeDuration.html&version=latest "documentation")).

### Resolution

The SLA Product Owners came back and shared that the reason behind why Pause conditions are not supported with Relative Duration is strictly historical. The functionality was never added based on the use cases at the time. For example, what does a user do with a "Next business day at 17:00" when they pause? All of a sudden that duration doesn't hold true.  
  
The SLA Product Owners recommended that an Enhancement Request be created for this behavior to be added into the Platform. Here is the Enhancement Request: FTASK46800.
