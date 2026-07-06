---
title: "Rest API Explorer is escaping the special characters like single quote in the xml payload content."
aliases:
  - KB0748767
  - Rest API Explorer is escaping the special characters like single quote in the xml payload content
tags:
  - servicenow
  - support-kb
  - rest-api-explorer
  - rest-api
  - xml
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748767
kb_number: KB0748767
last_modified: 2024-04-07
---

## Rest API Explorer is escaping the special characters like single quote in the xml payload content.

  

### Issue

# Overview

Rest API Explorer is escaping the special characters like single quote in the xml payload content leading to insertion of incorrect data into the tables

# Subject

We use Rest API Explorer from the platform to insert the data into tables using REST calls. The issue is that when we introduce special characters like 'apostrophe' in any of the fields on the input payload, they are escaped in the payload and incorrect or irrelevant data is inserted into the target tables when the REST call is executed from REST Explorer. 

# Example

In Rest API Explorer, try to send a rest request with below data. Make sure request format is application/xml. Observed that data is escaped.

Data:  
table = incident  
short\_description = rama'krishna

output = rama\\'krishna

So the value of short description on the target incident record is inserted as rama\\'krishna which is incorrect.

**Another example in the below screenshot:**

![](/sys_attachment.do?sys_id=a28a20a6db42b450e515c22305961925)

# Work Around

This issue is identified as a bug in REST API Explorer and is targeted to fix in New York release. Problem ticket is PRB1333220. 

The workaround is to use the response builder in REST API Explorer , then copy/paste whatever you want into the "Raw" builder and remove the extra escape backslashes.

## Related

- [[KB0747638 - Attachment limit for Inbound Integration with base64 encoding]]
- [[use-REST-API-Explorer|Use REST API Explorer]]
