---
title: "Templates are missing when Facilities Request are being created through Order Guide"
aliases:
  - KB0783549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783549
kb_number: KB0783549
last_modified: 2024-04-08
---

## Templates are missing when Facilities Request are being created through Order Guide

  

### Issue

Template is not taken into consideration/loaded when we create a FCR (Facilities Request) through an order guide. As well as any specific work flows associated with it.

### Release

London Patch 10

### Cause

\> If you're creating a Facilities request through catalog it does not add a template. Please check the [Document](https://docs.servicenow.com/csh?topicname=t_CreateAReqThroughFacCatalog.html&version=latest "Document").

### Resolution

\> In that particular record producer, you need to add a line in beginning of the script.

current.template = "value"; \\\\You need to add the value as Sys\_ID template model here in the script.
