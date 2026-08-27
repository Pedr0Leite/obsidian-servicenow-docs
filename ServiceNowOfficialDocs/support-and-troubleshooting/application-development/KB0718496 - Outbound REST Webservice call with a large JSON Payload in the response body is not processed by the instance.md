---
title: "Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance"
aliases:
  - KB0718496
tags:
  - servicenow
  - support-kb
  - REST
  - JSON
  - scripting
  - RESTMessageV2
  - integration
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718496
kb_number: KB0718496
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

The instance makes an outbound REST web service call and it comes back with a successful HTTP-200 response code with no errors in the logfiles at all, but attempting to process the JSON response body via scripting does not process any of the returned data.

Consider a large response body in the area of 18MB+ as viewed in the "Response length" in the "Outbound HTTP Logs" in the instance UI.

When the response body is smaller it gets processed by the scripting without issue.

# Release

* * *

This applies to any release.

# Cause

* * *

The scripting uses the JSONParser() and  parse() methods to parse the JSON response body:

var parser = new JSONParser();

var parsed = parser.parse(responseBody);

Using these methods are not intended for use with large payloads. 

# Resolution

* * *

Replace JSONParser() and parse() methods with the following constructions:

var parser = new JSON();

var parsed = parser.decode(responseBody); 

This is an example of what the script would look like:

try {  
var r = new sn\_ws.RESTMessageV2('REST Webservice', 'Default GET');

var response = r.execute();

var httpStatus = response.getStatusCode();  
var requestBody = response.getRequestBody();  
var responseHeaders = response.getHeaders();  
var responseBody = response.getBody();

if (httpStatus == "200") {  
var parser = new JSON();  
var parsed = parser.decode(responseBody);

<Code to process the response here>

}  
}  
catch(ex) {  
var message = ex.getMessage();  
}

## Related

- [[KB0720035 - Error calling Scoped Outbound REST message]]
- [[KB0724429 - glide_list reference field created through a REST API call stores the actual value instead of reference of the field]]
- [[r_ScriptingOutboundSOAP]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance|Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724429 - glide_list reference field created through a REST API call stores the actual value instead of reference of the field|glide_list  reference field created through a REST API call stores the actual value instead of reference of the field]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()|Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
