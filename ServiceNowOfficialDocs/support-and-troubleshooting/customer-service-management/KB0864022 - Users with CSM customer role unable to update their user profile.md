---
title: "Users with CSM customer role unable to update their user profile"
aliases:
  - KB0864022
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864022
kb_number: KB0864022
last_modified: 2023-10-11
---

## Users with CSM customer role unable to update their user profile

  

### Issue

From the /csm portal, user with the sn\_customerservice.customer role are unable to update their own user profile.

### Cause

A before query business rule on the sys\_user or customer\_contact table is preventing users from seeing the own records.

### Resolution

Modify the before query business rule to ensure customers have visibility to their own records on the customer\_contact table.
