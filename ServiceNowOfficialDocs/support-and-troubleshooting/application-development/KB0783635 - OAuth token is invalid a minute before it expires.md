---
title: "OAuth token is invalid a minute before it expires"
aliases:
  - KB0783635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783635
kb_number: KB0783635
last_modified: 2024-04-26
---

## OAuth token is invalid a minute before it expires

  

### Issue

OAuth token (used to make an outbound call from ServiceNow to 3rd party end point) expires 60 seconds before the actual expiration time of the token.

### Cause

The default threshold for OAuth token expiration is 60 seconds.(the amount of time at which the system considers a token to be effectively expired. Default is one minute)

### Resolution

If lower threshold is required ,for example 30 seconds, create a new system property and set it's value as below:

Name: glide.rest.outbound.oauth\_token\_expired\_threshold

Type: integer

Value: 30
