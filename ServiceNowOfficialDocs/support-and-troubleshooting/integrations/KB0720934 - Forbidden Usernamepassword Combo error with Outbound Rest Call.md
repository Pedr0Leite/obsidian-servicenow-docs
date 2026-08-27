---
title: "Forbidden Username/password Combo error with Outbound Rest Call"
aliases:
  - KB0720934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720934
kb_number: KB0720934
last_modified: 2025-02-25
---

## Forbidden Username/password Combo error with Outbound Rest Call

  

### Issue

When trying to issue a REST outbound call from UI to an endpoint, you witness the error “Forbidden username/password combo” in the response message”

### Symptoms:

You will recognize this error when you go to the configured Outbound Rest call -> Select the http method (Get or Post) and then issue the Test command

The same error is visible from the Outbound HTTP requests as well

![../../image.png](/sys_attachment.do?sys_id=cd73997347b79a10f64de825126d43a8)

### Cause

Possible cause of the behavior is the “user agent” field value in the http header of the request is not liked by the endpoint leading to this access denied error message in the response

Actual Http Header Request from HTTP log on UI:  
{Accept=application/json, Content-Type=application/json, Authorization=Basic XXX, User-Agent=Jakarta Commons-HttpClient/3.1, Host=XXX}

Issue is identified when we were trying to issue CURL command from the App Physical host with the same header as the one passed to the endpoint from UI when you click on the est button in the Outbound REST call.

### Initial CURL Used with the default User Agent Value:

#### Failed

curl -v \\  
\> -H 'Accept: application/json' \\  
\> -H 'Content-Type: application/json' \\  
\> -H 'Authorization: Basic XXXXXX' \\  
\> -H 'User-Agent: Jakarta Commons-HttpClient/3.1' \\  
\> -H 'Host: XXXXXX' \\  
\> -X GET XXXXX

 User-agent changed to “ServiceNow” for testing and you see a success response

####   
Success:

 curl -v \\  
\> -H 'Accept: application/json' \\  
\> -H 'Content-Type: application/json' \\  
\> -H 'Authorization: Basic XXXXXX' \\  
\> -H 'User-Agent: servicenow' \\  
\> -H 'Host: XXXXXX' \\  
\> -X GET XXXXX

Similarly, when adding the user Agent value as "ServiceNow" in the Get/POST method Header of the REST call from UI, you see a successful response with the expected data 

![../../../Desktop/Screen%20Shot%202018-12-17%20at%209.21.25%20PM.png](/sys_attachment.do?sys_id=c973997347b79a10f64de825126d43ab)

### Resolution

The endpoint for some reasons doesn’t accept the value of the “User-Agent” field in the Header of the Outbound REST call. Changing this to "ServiceNow" in the outbound REST Header will resolve the error.
