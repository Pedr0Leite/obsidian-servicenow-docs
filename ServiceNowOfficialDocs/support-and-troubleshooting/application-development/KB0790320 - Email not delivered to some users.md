---
title: "Email not delivered to some users"
aliases:
  - KB0790320
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790320
kb_number: KB0790320
last_modified: 2024-04-30
---

## Email not delivered to some users

  

### Issue

Some  times we can see the emails are not delivered to certain users even though it is showing sent in the email table of service now instance

### Release

All

### Cause

At Service now side if the email status is sent, there is a possibility of failure at destination mail server issue.

### Resolution

We need to check with the destination mail admin team by sharing the message-id of the email. You can find a message-id from the email header at Service now side.
