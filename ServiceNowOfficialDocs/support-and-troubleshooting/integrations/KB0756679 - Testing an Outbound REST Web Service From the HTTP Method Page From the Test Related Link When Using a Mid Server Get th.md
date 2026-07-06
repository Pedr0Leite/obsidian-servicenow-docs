---
title: "Testing an Outbound REST Web Service From the HTTP Method Page From the \"Test\" Related Link When Using a Mid Server Get the Error: No response for ECC message request with sysid=xxxx after waiting for 60 seconds in ECC Queue"
aliases:
  - KB0756679
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756679
kb_number: KB0756679
last_modified: 2023-09-27
---

## Testing an Outbound REST Web Service From the HTTP Method Page From the "Test" Related Link When Using a Mid Server Get the Error: No response for ECC message request with sysid=xxxx after waiting for 60 seconds in ECC Queue

  

### Issue

Testing an Outbound REST Web Service From the HTTP Method Page From the "Test" Related Link When Using a Mid Server Get the Error: No response for ECC message request with sysid=xxxx after waiting for 60 seconds in ECC Queue

### Cause

ScriptableRESTMessageTestUIAction.java is hard coded to only wait 60 seconds for a response (response.waitForResponse(60)) when a Mid Server is Used for the web service call when the "Test" Related Link is used.

### Resolution

If the response takes longer than 60 seconds do not use the "Test" Related Link, instead script the REST call into a Script Include or Business Rule.
