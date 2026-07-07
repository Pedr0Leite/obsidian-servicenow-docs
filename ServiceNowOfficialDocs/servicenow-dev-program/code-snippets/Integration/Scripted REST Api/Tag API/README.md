---
title: "Tag API"
aliases:
  - Tag API
tags:
  - servicenow-dev-program
  - code-snippet
  - tag-api
  - scripted-rest-api
---

This utility contains a scripted REST API which helps to insert tags in records with required parameters.

Below is the REST endpoint to access this SRAPI.

https://<<YOUR_INSTANCE_NAME>>>.service-now.com/api/gmi/insert_tags

Sample Code to call this SRAPI is below:

```r
var request = new sn_ws.RESTMessageV2();
request.setEndpoint('https://<<YOUR_INSTANCE_NAME>>>.service-now.com/api/gmi/insert_tags');
request.setHttpMethod('POST');

//Eg. UserName="admin", Password="admin" for this code sample.
var user = 'admin';
var password = 'admin';

request.setBasicAuth(user,password);
request.setRequestHeader("Accept","application/json");
request.setRequestHeader('Content-Type','application/json');
request.setRequestBody("{
    \"title\": \"my test7\",
     \"read\": \"yes\",
    \"table\" : \"cmdb_ci_computer\",
     \"table_key\" : \"aac0b1213784200044e0bfc8bcbe5de3\"
    

}");
var response = request.execute();
gs.log(response.getBody());

```

Sample Payload is below:

```r

{
    "title": "my test7",
     "read": "yes",
    "table" : "cmdb_ci_computer",
     "table_key" : "aac0b1213784200044e0bfc8bcbe5de3"
    

}

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
