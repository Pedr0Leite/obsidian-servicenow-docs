---
title: "Restrict the web service user (REST) to read only specific tables"
aliases:
  - KB0793194
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793194
kb_number: KB0793194
last_modified: 2024-04-08
---

## Restrict the web service user (REST) to read only specific tables

  

### Issue

Restrict the web service user (REST) to read-only specific tables.

### Resolution

You may be able to do this by creating a new ACL.  
Type: REST\_Endpoint  
Operation: Execute  
Name: Name of rest end point  
  

### Related Links

[https://docs.servicenow.com/csh?topicname=c\_CustomWebServices.html&version=latest](https://docs.servicenow.com/csh?topicname=c_CustomWebServices.html&version=latest)
