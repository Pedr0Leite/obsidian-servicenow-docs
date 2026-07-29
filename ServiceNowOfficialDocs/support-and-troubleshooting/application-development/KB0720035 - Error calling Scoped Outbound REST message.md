---
title: "Error calling Scoped Outbound REST message"
aliases:
  - KB0720035
tags:
  - servicenow
  - support-kb
  - REST
  - RESTMessageV2
  - scoped-applications
  - integration
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720035
kb_number: KB0720035
last_modified: 2025-08-11
---

## Error calling Scoped Outbound REST message

  

### Issue

If you need to access on Outbound REST message in another Scope. Assuming it is accessible, you may sometimes get the error:

**REST Msg Outbound - RESTMessageClient : Error constructing REST Message/Method: xxxxxxxxxxx \[HR Task\] HTTP Method (POST): com.glide.generators.InvalidGlideRecordException: Unable to find REST Message Record with Name: xxxxxxxxxxx: com.glide.rest.outbound.RESTMessageDAO.getRestMessageRecord(RESTMessageDAO.java:86)**  
com.glide.rest.outbound.RESTMessageDAO.<init>(RESTMessageDAO.java:71)  
com.glide.rest.outbound.RESTMessageDAO.newInstance(RESTMessageDAO.java:67)  
com.glide.rest.outbound.RESTMessageConfig.initNew(RESTMessageConfig.java:67)  
com.glide.rest.outbound.RESTMessageClient.<init>(RESTMessageClient.java:57)  
  
\[...\]  
  
java.lang.Thread.run(Thread.java:748)  
  
Evaluator: com.glide.communications.ProcessingException: Error constructing REST Message/Method:xxxxxxxxxxxr \[HR Task\] HTTP Method (POST)  
Caused by error in script at line 15  
  
13: gs.print(gr.function\_name);  
14: gs.print(gr.rest\_message.name);  
\==> 15: var sm = new sn\_ws.RESTMessageV2(gr.rest\_message.name, gr.function\_name);  
16: 

### Release

Apply to all releases

### Cause

To call any Scoped resources you need to explicitly specify the scope if you are not in that scope.

### Resolution

The Outbound REST message you are trying to call from within your Business Rule or Script Include is in another scope. But it is still accessible. You need to Prefix the REST message name with the scope name. This is referring to the first argument of the function below :

RESTMessageV2(**String** **name**, String methodName)

So if you know the name of the Outbound REST you can just add the prefix e.g.:

SCOPE = 'my\_scope'

REST Message= 'my\_rest'

The function call would look like :

var msg = new sn\_ws.RESTMessageV2('my\_scope.my\_rest', 'function\_name');

This solution applies even if the REST name is a variable e.g. :

SCOPE = 'my\_scope'

REST Message= gr.rest\_name

var msg = new sn\_ws.RESTMessageV2('my\_scope.'+gr.rest\_name, 'function\_name');

## Related

- [[KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
- [[KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[r_RESTMessageV2MIDServerExample]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance|Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance|Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724429 - glide_list reference field created through a REST API call stores the actual value instead of reference of the field|glide_list  reference field created through a REST API call stores the actual value instead of reference of the field]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0712001 - ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST|ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695169 - Changes to a scoped application are not being applied when the update is installed|Changes to a scoped application are not being applied when the update is installed]]
