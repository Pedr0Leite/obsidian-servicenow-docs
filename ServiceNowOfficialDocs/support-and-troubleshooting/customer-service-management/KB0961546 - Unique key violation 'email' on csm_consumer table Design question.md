---
title: "Unique key violation 'email' on csm_consumer table / Design question"
aliases:
  - KB0961546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961546
kb_number: KB0961546
last_modified: 2025-07-22
---

## Issue

After opening the "csm\_consumer.LIST" table and adding a consumer with a specified email address (i.e. abc@xyz.com), any further attempt to create a new consumer record setting the same email address used (abc@xyz.com) will throw the error:  
"Unique Key violation detected by database ((conn=128317) Duplicate entry 'abc@xyz.com' for key 'email')"

## Resolution

Different user records must have different email addresses.
