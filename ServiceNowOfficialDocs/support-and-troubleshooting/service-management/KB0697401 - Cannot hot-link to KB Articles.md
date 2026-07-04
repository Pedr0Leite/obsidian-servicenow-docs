---
title: "Cannot hot-link to KB Articles"
aliases:
  - KB0697401
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697401
kb_number: KB0697401
last_modified: 2024-04-07
---

## Cannot hot-link to KB Articles

  

### Issue

When accessing a KB article without logging into the instance, it is throwing an error as 'Article not found'.

When a service catalog item is accessed without logging in, it would redirect to the login page asking for credentials.

### Release

NewYork +

### Cause

Public access is enabled on kb\_article portal page.

### Resolution

By default, public access is enabled on the kb\_article page.

When this was disabled, the behavior is the same as that of a catalog item.
