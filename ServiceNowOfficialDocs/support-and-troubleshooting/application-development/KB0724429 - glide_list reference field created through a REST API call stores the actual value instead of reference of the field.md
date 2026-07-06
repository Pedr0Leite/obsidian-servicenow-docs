---
title: "glide_list  reference field created through a REST API call stores the actual value instead of reference of the field"
aliases:
  - KB0724429
tags:
  - servicenow
  - support-kb
  - REST
  - glide_list
  - Table-API
  - integration
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724429
kb_number: KB0724429
last_modified: 2024-04-07
---

## glide\_list reference field created through a REST API call stores the actual value instead of reference of the field

  

### Issue

# Symptoms

* * *

A glide\_list reference field created through a REST API call does not store the reference of the field . Instead it saves the actual value. Similar call using SOAP creates glide\_list reference field with the actual reference .

# Cause

* * *

Query parameter sysparm\_input\_display\_value=true  is not passed .

# Resolution

* * *

Query parameter  'sysparm\_input\_display\_value' in the request URL should be set to true {sysparm\_input\_display\_value = true}.

Passing the parameter makes the REST call behave similar to SOAP .

## Related

- [[KB0717382 - An empty or blank box appears inside List collector in Service Portal]]
- [[KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
