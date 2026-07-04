---
title: "Rest Step in Flow Designer has unexpected results when compared to making the same call outside the Flow."
aliases:
  - KB0867608
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867608
kb_number: KB0867608
last_modified: 2023-11-11
---

## Rest Step in Flow Designer has unexpected results when compared to making the same call outside the Flow.

  

### Issue

When testing a Rest Step you may notice the response body is not showing the expected results when comparing to the response body when sent via a web services client such as Postman.

There may be different data in the body entirely.

### Release

Orlando Patch 7

### Cause

This is due to the way the Rest Step is designed to create the request, which breaks down the request into different fields and entires.

There is a "Resource Path" field where you will put the path to the API on the endpoint.  

Often times the query parameters will be added to the resource path as some will use the way they normally would write a request URI in this field.  

  

For example an incorrect Resource Path with query parameters in the path:

/api/now/table?sysparm\_limit=10

![](/sys_attachment.do?sys_id=63c5c23c1bc96810d2ccea89bd4bcbfc)

Example for how the Resource Path should display:

/api/now/table

### Resolution

You will need to remove the query parameters from the Resource Path and add it to the Query Parameters field.

The query parameters in the resource path will not be respected.
