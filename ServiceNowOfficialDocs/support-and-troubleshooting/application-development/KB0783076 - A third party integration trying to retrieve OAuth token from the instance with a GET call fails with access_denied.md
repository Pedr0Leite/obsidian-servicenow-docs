---
title: "A third party integration trying to retrieve OAuth token from the instance with a GET call fails with \"access_denied\""
aliases:
  - KB0783076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783076
kb_number: KB0783076
last_modified: 2024-04-26
---

## A third party integration trying to retrieve OAuth token from the instance with a GET call fails with "access\_denied"

  

### Issue

A third party integration trying to retrieve OAuth token from the instance with a GET call fails with "access\_denied"

### Cause

To retrieve the token from the instance you can only make a POST call and not a GET call since you are passing data to the call like clientID, Client secret, grant type etc.

### Resolution

Make a POST call instead of GET

### Related Links

Sending sensitive information over URI query parameters may lead to sensitive information disclosure by clients, the server, or any host between the requests.
