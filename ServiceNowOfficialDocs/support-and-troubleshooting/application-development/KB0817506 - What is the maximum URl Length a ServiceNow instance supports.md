---
title: "What is the maximum URl Length a ServiceNow instance supports?"
aliases:
  - KB0817506
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817506
kb_number: KB0817506
last_modified: 2026-06-29
---

## What is the maximum URl Length a ServiceNow instance supports?

  

### Issue

When calling ServiceNow Inbound Web Service APIs with a long URI, it fails with **HTTP 400 Bad Request Error** with below screenshot and it raises a question asking what is the maximum URl Length the service now instance supports.

![](sys_attachment.do?sys_id=bfabd55947394fd43542f24c736d4325)

### Release

All

### Cause

This is important to understand that this limit is not set by ServiceNow platform/application. The limit is dependent on both the server and the client used (and if applicable, also the proxy the server or the client is using).

Most web servers have a limit of 8192 bytes (8 KB), which is usually configurable somewhere in the web server configuration. Same is the case with ServiceNow Web Servers which accept/process the incoming HTTP requests and are further linked with Application Servers where ServiceNow applications are hosted.

As long as the HTTP GET request URL size is below 8 KB (including request headers plus other metadata if there is any), the server accepts the request, ask for authentication URLs and process it successfully.

### Resolution

You cannot increase this size limit as it is configured at Web Servers which is part of ServiceNow cloud infrastructure.

As a best practice, we suggest you to pull the data in smaller chunks by making multiple API calls which is far better than pulling the huge amount of data in one single API call. Following this best practice will automatically maintain your API URL size limit.

For pulling data in small chunks, please consider using [Supported request parameters](https://docs.servicenow.com/csh?topicname=c_TableAPI.html&version=latest#d81750e444 "Supported request parameters") as explained in ServiceNow docs.
