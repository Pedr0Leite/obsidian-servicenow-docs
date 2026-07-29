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

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0712001 - ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST|ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance|Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance|Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0726269 - Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutExc|Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutException: connect timed out]]
