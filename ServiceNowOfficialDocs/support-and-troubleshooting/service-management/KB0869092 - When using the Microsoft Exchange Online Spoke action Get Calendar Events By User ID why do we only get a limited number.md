---
title: "When using the Microsoft Exchange Online Spoke action \"Get Calendar Events By User ID\" why do we only get a limited number of calendar events from Microsoft"
aliases:
  - KB0869092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869092
kb_number: KB0869092
last_modified: 2023-11-23
---

## When using the Microsoft Exchange Online Spoke action "Get Calendar Events By User ID" why do we only get a limited number of calendar events from Microsoft

  

### Issue

When using the Microsoft Exchange Online Spoke action "Get Calendar Events By User ID" getting only limited number of calendar events even though there are more number if events for particular user

### Release

All

### Cause

Need to send the query parameter to query more number of events from calendar otherwise it will default from 5 to 13 events

### Resolution

\* According to the Microsoft documentation there is a query parameter we need to send when a request is made to graph API  
\* That query parameter is top and then we can give the value  
\* Max allowed value if 999, but please make sure you are giving only less value to avoid timeout and cancellation of flow  
\* You can also use the data stream to get this kind of data.  
\* take a look at the below screen shot on how you can add that query parameter

![](sys_attachment.do?sys_id=7691210ddb19a410679499ead396199a)

\* Here is the Microsoft documentation which explains about all query parameters which we can use when making the API call to graph API

[https://docs.microsoft.com/en-us/graph/query-parameters](https://docs.microsoft.com/en-us/graph/query-parameters)
