---
title: "Flows with REST/SOAP Step fail with error relating to \"Response size exceeds limit\""
aliases:
  - KB0852968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852968
kb_number: KB0852968
last_modified: 2026-04-30
---

## Flows with REST/SOAP Step fail with error relating to "Response size exceeds limit"

  

### Issue

For the latest information, see [https://docs.servicenow.com/csh?topicname=rest-request-action-designer&version=latest](https://docs.servicenow.com/csh?topicname=rest-request-action-designer&version=latest)

For a given response payload from a REST or SOAP step it is possible that it can exceed the default payload size.

The execution context would contain an error like the following:

..failed with error: com.snc.process\_flow.exception.OpException: Response size exceeds limit, allowed :xxxxx actual size: xxxxx

### Release

### Cause

By default, the allowed payload size for a REST or SOAP response is 5MB (5120KB).

### Resolution

To address that error message, add the respective properties to the \[sys\_properties\] table for the given step being used.  
  
REST:  
**glide.pf.rest.response\_payload\_max\_size**  
  
SOAP:  
**glide.pf.soap.response\_payload\_max\_size**  
  
**Note 1:** Please note that the value is in KB, so 10MB = 10240 (10 \* 1024KB).  
**Note 2:** If the respective flow is configured to use a MID Server, you would add the respective property to the MID Server properties table and not \[sys\_properties\].  
  
  
The maximum value that can be specified is: 10240  
  
If the response attachment is more than 10MB, then the Flow Action will need to utilise "Save As Attachment" (under "Response Handling").
