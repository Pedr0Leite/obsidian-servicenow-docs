---
title: "Unable to view added attachments"
aliases:
  - KB0815445
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815445
kb_number: KB0815445
last_modified: 2026-06-29
---

## Unable to view added attachments

  

### Issue

If an issue reported with few users unable to view the added attachment(s) after having same roles as other users who can view the attachments then issue is with the userID of the affected user

### Release

NA

### Cause

When a user adds an attachment to a record, an entry is created in sys\_attachment table and the 'Created By' field is updated with the user's userID. Since the 'Created By' field holds max\_length of 40 characters and if userID is more than 40 characters then 'Created By' trims till 40 characters and Read ACL on sys\_attachment unable to match the logged-in user ID with 'Created By'field and ACL fails. This ends up with attachment that doesn't show up to the user.

### Resolution

Always maintain the user ID field on 'sys\_user' table to be within 40 characters, this user ID is used as 'Created By' and 'Updated By' fields on all the tables of the instance
