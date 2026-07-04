---
title: "Email inbound email not able to locate the Facilities Request"
aliases:
  - KB0793388
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793388
kb_number: KB0793388
last_modified: 2024-04-08
---

## Email inbound email not able to locate the Facilities Request

  

### Issue

-   The activity log for the Facilities Request is not logging all emails.
-   It logs the outbound email, but when a response is received (Inbound), it is not logged in the request. 

### Release

Any

### Cause

This is to do with the configuration setting in the Facilities Management

The configuration "Create or update requests by Inbound Email" is not enabled to get an update on the Request for an inbound email.

### Resolution

Enable this ""Create or update requests by Inbound Email" inbound action , so the inbound email will get attached to the target request.  
  
  

### Related Links

Reminder: Always test in Sub-Production before implementing in Production.

Also see attached screen shot
