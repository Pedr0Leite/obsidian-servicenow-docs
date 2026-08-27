---
title: "No events from PRTG eventhough the connector is up and Active"
aliases:
  - KB0759382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759382
kb_number: KB0759382
last_modified: 2024-04-07
---

## No events from PRTG eventhough the connector is up and Active

  

### Issue

There are no events from PRTG into ServiceNow instance. The connector is up. PRTG monitoring tool is up and running. The username and password configured correct in connector instance.

### Release

All Versions.

### Cause

The below connector definition is used to pull events from PRTG

Connector Definitions: 

https://<Instance\_Name>.service-now.com/nav\_to.do?uri=em\_connector\_definition.do?sys\_id=676f941d0ffc030046354cace1050e71

JavaScript Script that would run to fetch the events:

https://<Instance\_Name>.service-now.com/nav\_to.do?uri=ecc\_agent\_script\_include.do?sys\_id=9a6b185d0ffc030046354cace1050eab

`if(type == "GET"){   response = request.get();   body = this.parseJSON(response);   }`

You can add the below statement in the JavaScript to check how we are getting the response from the PRTG. 

ms.log("INT4343174: BODY: stringify " + JSON.stringify(body));

The above log statement will write the events that we are fetching from PRTG in raw format.

Sample Message:

{"prtg-version":"19.2.50.2842","treesize":1000000,"messages":\[{"parent":"PRTG Servers","name":"ELBMCPV03.EXXARO.COM","type":"Device","type\_raw":"device","objid":2054,"tags":"","message":"&lt;div class=\\\\\\"logmessage\\\\\\"&gt;Device Auto-Discovery Finished: 0 sensors found. Device Templates found: Default Server Template&lt;div class=\\\\\\"moreicon\\\\\\"&gt;&lt;/div&gt;&lt;/div&gt;","message\_raw":"Device Auto-Discovery Finished: 0 sensors found. Device Templates found: Default Server Template","status":"Auto-Discovery: Device template(s) applied","status\_raw":805,"priority":"1","datetime":"2019/08/20 04:48:51","datetime\_raw":43697.1172573611,"actions":"&lt;div class=\\\\\\"tablebuttonbox\\\\\\"&gt;&lt;span class=\\\\\\"icon ui-icon ui-icon-pencil\\\\\\"&gt;&lt;/span&gt;&lt;a class=\\\\\\"actionbutton\\\\\\" href=\\\\\\"#\\\\\\"&gt;Edit&lt;/a&gt;&lt;a class=\\\\\\"actionbutton\\\\\\" href=\\\\\\"#\\\\\\"&gt;&lt;span class=\\\\\\"icon ui-icon ui-icon-pause\\\\\\"&gt;&lt;/span&gt;Pause&lt;/a&gt; &lt;a href=\\\\\\"#\\\\\\"&gt;Menu&lt;/a&gt;&lt;/div&gt;","actions\_raw":"","baselink":2054,"baselink\_raw":2054,"basetype":"device","modifiedby":"","modifiedby\_raw":"","Not found":"\_raw"},{"parent":"ELBMCPV02.EXXARO.COM","name":"Memory","type":"WMI Memory","type\_raw":"wmimemory","objid":2014,"tags":"memorysensor wmimemorysensor","message":"&lt;div class=\\\\\\"logmessage\\\\\\"&gt;68 %&lt;div class=\\\\\\"moreicon\\\\\\"&gt;&lt;/div&gt;&lt;/div&gt;","message\_raw":"68 %","status":"Up","status\_raw":607,"priority":"0","datetime":"2019/08/14 06:24:28","datetime\_raw":43691.1836669907,"actions":"","actions\_raw":"","baselink":2014,"baselink\_raw":2014,"basetype":"sensor","modifiedby":"","modifiedby\_raw":"","Not found":"\_raw"}\]}

Please use any JSON Formatter online to parse the message and see how each field is being retrieved from PRTG:

{   
"prtg-version":"19.2.50.2842",   
"treesize":1000000,   
"messages":\[   
{   
"parent":"PRTG Servers",   
"name":"ELBMCPV03.EXXARO.COM",   
"type":"Device",   
"type\_raw":"device",   
"objid":2054,   
"tags":"",   
"message":"&lt;div class=\\\\\\"logmessage\\\\\\"&gt;Device Auto-Discovery Finished: 0 sensors found. Device Templates found: Default Server Template&lt;div class=\\\\\\"moreicon\\\\\\"&gt;&lt;/div&gt;&lt;/div&gt;",   
"message\_raw":"Device Auto-Discovery Finished: 0 sensors found. Device Templates found: Default Server Template",   
`"status":"Auto-Discovery: Device template(s) applied",`   
"status\_raw":805,   
"priority":"1",   
"datetime":"2019/08/20 04:48:51",   
"datetime\_raw":43697.1172573611,   
"actions":"&lt;div class=\\\\\\"tablebuttonbox\\\\\\"&gt;&lt;span class=\\\\\\"icon ui-icon ui-icon-pencil\\\\\\"&gt;&lt;/span&gt;&lt;a class=\\\\\\"actionbutton\\\\\\" href=\\\\\\"#\\\\\\"&gt;Edit&lt;/a&gt;&lt;a class=\\\\\\"actionbutton\\\\\\" href=\\\\\\"#\\\\\\"&gt;&lt;span class=\\\\\\"icon ui-icon ui-icon-pause\\\\\\"&gt;&lt;/span&gt;Pause&lt;/a&gt; &lt;a href=\\\\\\"#\\\\\\"&gt;Menu&lt;/a&gt;&lt;/div&gt;",   
"actions\_raw":"",   
"baselink":2054,   
"baselink\_raw":2054,   
"basetype":"device",   
"modifiedby":"",   
"modifiedby\_raw":"",   
"Not found":"\_raw"   
},   
{   
"parent":"ELBMCPV02.EXXARO.COM",   
"name":"Memory",   
"type":"WMI Memory",   
"type\_raw":"wmimemory",   
"objid":2014,   
"tags":"memorysensor wmimemorysensor",   
"message":"&lt;div class=\\\\\\"logmessage\\\\\\"&gt;68 %&lt;div class=\\\\\\"moreicon\\\\\\"&gt;&lt;/div&gt;&lt;/div&gt;",   
"message\_raw":"68 %",   
"status":"Up",   
"status\_raw":607,   
"priority":"0",   
"datetime":"2019/08/14 06:24:28",   
"datetime\_raw":43691.1836669907,   
"actions":"",   
"actions\_raw":"",   
"baselink":2014,   
"baselink\_raw":2014,   
"basetype":"sensor",   
"modifiedby":"",   
"modifiedby\_raw":"",   
"Not found":"\_raw"   
}   
\]   
} 

Once we get the events from PRTG, we will check the below condition to see if the events are valid.

if(snSeverity == null || basetype != "sensor") // Condition should be false to valid events.

 **snSeverity** is obtained from the events' "status" field and **basetype** is from the raw event. If any of the above condition is met then we will ignore the event and will move on to next event.

  

Also, we use the status field to map to Event Severity. The below values are expected for the status field from PRTG and mapping is done accordingly.

  
"Up": 5,  
"DownAcknowledged": 5,  
"Active": 5,  
"Paused (License Limit)": 4,  
"Paused": 4,  
"Resuming": 5,  
"Collecting": 5,  
"PausedbyDependency": 4,  
"PausedbySchedule": 4,  
"PausedbyLicense": 4,  
"PausedUntil": 4,  
"PausedbyUser": 4,  
"NoProbe": 4,  
"Unknown": 4,  
"Warning": 4,  
"Unusual": 4,  
"DownPartial": 2,  
"Down": 1

  

### Resolution

If the incoming events are not valid, please check with PRTG team on why valid events are not being sent.

We use the below query to pull events from PRTG:

https://<PRTG\_Server\_IP>/api/table.json?filter\_dstart=<Start\_Date>&amp;content=messages&amp;columns=parent,name,type,objid,tags,message,status,priority,datetime,actions,baselink,basetype,modifiedby,false&amp;count=50000&amp;username=ServiceNow&amp;passhash=1224854257

<Start\_Date> will be in below format 2019-08-14-06-24-28

Also, the query URL can be obtained from the script by adding ms.log statement after the below line:

url = encodeURI(url);

The logging statement should look like below:

ms.log("Encoded URI: " + url);
