---
title: "Why are External users with \"sn_customerservice.customer\" role able to access Cases LIST view on platform UI."
aliases:
  - KB0755254
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755254
kb_number: KB0755254
last_modified: 2024-04-07
---

## Issue

Ideally, users with "sn\_customerservice.customer" don't have the required roles to see the Module "Cases.  
But these users are able to access "sn\_customerservice\_case\_list.do"  LIST view on platform UI.

## Resolution

This is expected behavior and working as per the current design.

If you do not want to see this behavior, you need to modify the OOB ACLs on the table: "sn\_customerservice\_case" as per the business need.
