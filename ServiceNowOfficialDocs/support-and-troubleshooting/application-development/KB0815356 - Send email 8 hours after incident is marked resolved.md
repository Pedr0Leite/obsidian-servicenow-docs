---
title: "Send email 8 hours after incident is marked resolved"
aliases:
  - KB0815356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815356
kb_number: KB0815356
last_modified: 2024-12-05
---

## Send email 8 hours after incident is marked resolved

  

### Issue

We would like to send an email with a link eight hours after the incident has been marked resolved. How can something like this be accomplished best?

### Resolution

The easiest way to accomplish an email with a predefined delay is by creating a workflow that is fired when the condition for the start of the delay is reached. Within the workflow you will have a timer with a predefined delay and then a notification activity.  
  
Supporting documentation can be found here: [Getting started with Workflows](https://docs.servicenow.com/csh?topicname=getting-started-workflows.html&version=latest#getting-started-workflows "Getting started with Workflows")
