---
title: "Cases are getting the same image attachments multiple times from inbound emails"
aliases:
  - KB0781521
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781521
kb_number: KB0781521
last_modified: 2026-07-03
---

## Issue

Cases seem to get the same image attachments from email traffic multiple times for no apparent reason.

## Resolution

Look under System Mailboxes > Received, the raw emails may have the attachments inline, or the attachments may be at the top of the record, like they are for a Case.  
  
Retrieve the sys\_IDs of the emails from the sys\_attachment table.
