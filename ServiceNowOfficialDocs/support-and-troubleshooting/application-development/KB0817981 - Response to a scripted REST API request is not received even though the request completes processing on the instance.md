---
title: "Response to a scripted REST API request is not received even though the request completes processing on the instance"
aliases:
  - KB0817981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817981
kb_number: KB0817981
last_modified: 2026-04-29
---

## Response to a scripted REST API request is not received even though the request completes processing on the instance

  

### Issue

If a request is made to a scripted REST API, the logs on the instance may indicate that the request was processed successfully and the response was sent. However, the client that made the request still may keep loading, waiting for a response. 

### Release

### Cause

This may happen if the response\_status is **0** and not an expected response code like 200. This maybe because the scripted REST API doesn't explicitly set the response code to be sent.

Example log:

2020-03-15 13:55:32 (949) API\_INT-thread-4 SYSTEM txid=09d6c146dbab \*\*\* End #27207 /api/test/sitemap/snc\_knowledge, user: guest, total time: 0:00:01.525, processing time: 0:00:01.525, SQL time: 0:00:00.102 (count: 212), source: 199.91.136.61 , type:rest, method:GET, api\_name:test/sitemap, resource:test/sitemap/snc\_knowledge, version:Default, user\_id:5136503cc611227c0183e96598c4f706, response\_status:0

### Resolution

In the Scripted REST API script, make sure to set the response code.

For example, if the request was processed successfully, you may send a 200 response code like this:

response.setStatus(200);  
  
See [https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/add-schema-rest-api-response.html](https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/add-schema-rest-api-response.html) for more info on how to send http response.
