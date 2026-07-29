---
title: "Why would Events with the same message key result in generating alerts with the same message key and associate each alert to a separate event?"
aliases:
  - KB0696148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696148
kb_number: KB0696148
last_modified: 2024-04-07
---

## Why would Events with the same message key result in generating alerts with the same message key and associate each alert to a separate event?

  

### Issue

## Description

Why would Events with the same message key result in generating alerts with the same message key and associate each alert to a separate event?

## Cause:

If there are incoming Events with the same message key. The following matching logic with the alerts should apply : 

The first event will result in generating an alert with the same message key and Alert.category = default if there is no logic in between manipulated the event of the alert message key.

\> This manipulation may be achieved by Event Rules or by using the Event Management Advanced script postTransformHandler or Before Insert/Update Business Rule on em\_alert table. 

The next events with the same message key should be associated with the same created alert if the message\_key and category of the existing alert are not manipulated. As SNOW relies on the alerts' message\_key and category fields to match the new incoming events with the existing alerts.

For example, If the category field of the existing alert is modified, This modification will impact SNOW matching logic and it will result in creating many alerts with the same message key.
