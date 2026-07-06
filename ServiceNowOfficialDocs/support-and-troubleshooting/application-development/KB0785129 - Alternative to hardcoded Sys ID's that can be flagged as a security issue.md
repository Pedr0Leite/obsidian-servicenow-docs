---
title: "Alternative to hardcoded Sys ID's that can be flagged as a security issue"
aliases:
  - KB0785129
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785129
kb_number: KB0785129
last_modified: 2023-09-04
---

## Alternative to hardcoded Sys ID's that can be flagged as a security issue

  

### Issue

ServiceNow occasionally performs health scans on user instances. One practice that will be flagged as a security issue is when hardcoded Sys IDs from objects in the instance are used within scripts.

A workaround to this issue is to create system properties that contain the Sys IDs and then retrieve them from when needed.

### Release

All

### Resolution

Note that in the following script, the "encodedquery" string contains the sys\_id's for a manufacturer, location and company.  This code would be flagged during a health scan as a security issue.  

var ciName = new GlideRecord('cmdb\_ci');  
var encodedquery = 'sys\_class\_name=cmdb\_ci\_computer^manufacturer=b7e9e843c0a80169009a5a485bb2a2b5^location=f90735e70a0a0b9100de208fbc63907d^company=31bea3d53790200044e0bfc8bcbe5dec';  
  
ciName.addEncodedQuery(encodedquery);  
ciName.query();  
  
while (ciName.next()) {  
gs.print('cmdb\_ci.name ' + ciName.name);  
}

This issue can be addressed by creating a system property record for each of these Sys IDs and retrieving these values with gs.getProperty().  In this example, the system properties, "acme\_corp", "loc\_santa\_ana" and "acme\_ne" were created with the following values:

acme\_corp = b7e9e843c0a80169009a5a485bb2a2b5  
location = f90735e70a0a0b9100de208fbc63907d  
company = 31bea3d53790200044e0bfc8bcbe5dec

The script then was modified to retrieve these values and then incorporated into the encoded query string.

var acme\_corp\_SysID = gs.getProperty("acme\_corp");  
var location\_SysID = gs.getProperty("loc\_santa\_ana");  
var company\_SysID = gs.getProperty("acme\_ne");  
  
var ciName = new GlideRecord('cmdb\_ci');  
var encodedquery = 'sys\_class\_name=cmdb\_ci\_computer^manufacturer=' + acme\_corp\_SysID.toString() +'^location=' + location\_SysID.toString() + '^company=' + company\_SysID.toString();  
  
ciName.addEncodedQuery(encodedquery);  
ciName.query();  
  
while (ciName.next()) {  
gs.print('cmdb\_ci.name ' + ciName.name);  
}

This information can also be found in an answered question by Chuck Tomasi in the Community:

[https://community.servicenow.com/community?id=community\_question&sys\_id=0ed187a9db98dbc01dcaf3231f961934&view\_source=searchResult](https://community.servicenow.com/community?id=community_question&sys_id=0ed187a9db98dbc01dcaf3231f961934&view_source=searchResult)

This does have the ServiceNow suggested method of resolving the issue of retrieving items from the sys\_properties table using the **getProperty** method.
