---
title: "Push Notifications have stopped sending"
aliases:
  - KB0791793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791793
kb_number: KB0791793
last_modified: 2024-04-08
---

## Push Notifications have stopped sending

  

### Issue

Push Notifications have stopped working. Since previous days, all of Push Notifications say "pending" in the System Logs for Push Notifications.

### Cause

The Job is stuck in Pending state next action is set to a past date and stuck in Running state and not claimed by any node.

### Resolution

Set the state to Error State . Change the date to today's date .

Save the record.

Set it to Ready again.
