---
title: "Issue with unique key violation on database"
aliases:
  - KB0963803
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963803
kb_number: KB0963803
last_modified: 2026-04-24
---

## Issue with unique key violation on database

  

### Issue

Experiencing an issue with a unique key violation on the database.  
  
A compounding error message along the lines of this:  
  
Unique Key violation detected by database ((conn=224257) Duplicate entry '6816f79cc0a8016401c5a33be04be441-null-0b10223c57a313005baaaa65ef' for key 'agent')  
  
  
**Steps to Reproduce:**

1.  log in as admin.
2.  Navigate to Engagement Messenger > Module.
3.  The message typically appears here, otherwise, you can go into the **"NAB Trade Support"** list item and it should appear there.

### Release

NA

### Cause

-   Issues were caused by the browser cache.
-   The issue was only reproduced by the User.

### Resolution

-   We suggested User clear the browser cache and history verify the behavior.
-   After logging out/in and clearing the cache etc and the error message disappeared.
