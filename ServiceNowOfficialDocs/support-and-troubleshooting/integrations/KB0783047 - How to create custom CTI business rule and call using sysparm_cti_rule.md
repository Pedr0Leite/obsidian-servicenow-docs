---
title: "How to create  custom CTI business rule and call using sysparm_cti_rule"
aliases:
  - KB0783047
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783047
kb_number: KB0783047
last_modified: 2026-01-23
---

## How to create custom CTI business rule and call using sysparm\_cti\_rule

  

### Summary

1) Create a new business rule :

a)application:global 

b) table:global

c) and client\_callable =true

2) In the script create a custom function . For example : cti\_custom , with the below sample code

\-------------------------

function cti\_custom() {  
var url = null;  
var name = sysparm\_caller\_name;  
eid = sysparm\_caller\_id;  
var phone = sysparm\_caller\_phone;  
var taskID = sysparm\_task\_id;  
var fQuery = sysparm\_query;  
if (fQuery == null)  
fQuery = '';  
var view = sysparm\_view;  
if (view == null || view == '')  
view = "itil";

var userID = null;  
if (eid != null && eid != '') {  
userID = UserGetSysId("employee\_number",eid);  
}  
if (userID == null && name != null && name != '') {  
userID = UserGetSysId("name", name);  
}  
if (userID == null && phone != null && phone != '') {  
userID = UserGetSysId("phone", phone);  
}  
if (userID != null) {  
var gr = new GlideRecord("incident");  
gr.addQuery("active", "true");  
gr.addQuery("caller\_id", userID);  
gr.setWorkflow(false);  
gr.query();  
if (gr.next())  
// url = "sys\_user.do?sys\_id=" + userID + "&sysparm\_view=" + view;  
url=null;  
} else {  
if (taskID != null && taskID != '') {  
url = "task.do?sys\_id=" + taskID + "&sysparm\_view=" + view;  
}  
}  
if (userID != null) {  
if (fQuery.length > 0)  
fQuery += "^";  
fQuery += "caller\_id=" + userID;  
}  
if (url == null) {  
url = "incident.do?sys\_id=-1";  
if (fQuery != null)  
url += "&sysparm\_query=" + fQuery;  
}  
answer = url;  
return url;  
}

function UserGetSysId(field, value) {  
var user = new GlideRecord("sys\_user");  
user.addQuery(field, value);  
user.query();  
if (user.next())  
return user.sys\_id;  
else  
return null;  
}

\--------------------------------------

3) Test and make sure that the new function can be invoked with sysparm\_cti\_rule

(sysparm\_cti\_rule=name where 'name' is the name of a function to be invoked for CTI processing rather than using the default script)

[https://<instance\_name>.service-now.com/cti.do?sysparm\_cti\_rule=cti\_custom&sysparm\_caller\_name=Abel%20Tuter](https://empukemburu02.service-now.com/cti.do?sysparm_cti_rule=cti_custom&sysparm_caller_name=Abel%20Tuter)

### Release

All
