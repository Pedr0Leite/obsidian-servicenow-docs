---
title: "Finding missing email in an instance"
aliases:
  - KB0563560
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563560
kb_number: KB0563560
last_modified: 2025-09-10
---

## Issue

This article explains how ServiceNow administrators can verify if an email has been received by an instance.

## Resolution

### Finding the message-id of the email

The first step is to find the message-id of the email in question ([https://en.wikipedia.org/wiki/Message-ID](https://en.wikipedia.org/wiki/Message-ID)). If you do not know how to find a message ID, search for "how to view email source in (email client name here)." After you have the source open, copy the line that starts with "**Message-ID:**".

### Validating that ServiceNow received the email 

If applicable, provide the message-id of that email to your email server administrator. The email server administrator should be able to give you confirmation that the ServiceNow email infrastructure received the message successfully. Ask for a log message showing an SMTP reply code of 250 indicating that the server transmitted the message successfully.

### Searching the email table for message-ID

Using an indexed query, an administrator can search the entire sys\_email table for the message-id. The query must include the field's message-id and type. For example:

message\_id=<D2C7E4EE.43578%joe.smith@servicenow.com>^type=received^ORtype=received-ignored

This is an indexed search that returns quickly and shows if an email with the message-id was ever received.

### Filing an incident with ServiceNow Technical support

If you have validated that the message was transmitted to ServiceNow successfully, but you are still unable to find the message in the sys\_email table using **message-id** and **type=received or type=received-ignored**, open case with ServiceNow support and provide these details in the incident. This will decrease the time it takes for the ServiceNow customer support team to find the missing email and to resolve the root cause.
