---
title: "Nutanix discovery script error in sensor cannot deserialize object"
aliases:
  - KB0779361
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779361
kb_number: KB0779361
last_modified: 2025-07-07
---

## Issue

Running a Nutanix discovery produces a script error in the sensor and fails to deserialize an object. The following pattern logs are observed when investigating this issue. 

**Pattern Log**

"message" : "2019-08-28 14:38:41: Pattern HTTP GET to https://<IP\_ADDRESS>:<PORT>/<DIR>/<DIR>/rest/v2.0/hosts?count=100&page=1",  
"severity" : "DEBUG"  
}, {  
"message" : "2019-08-28 14:38:41: Response has error. Status code is 401 . error code: 3 . error message: Method failed: (/<DIR>/<DIR>/rest/v2.0/hosts) with code: 401 - Invalid username/password combo",  
"severity" : "DEBUG"  
}, {  
"message" : "2019-08-28 14:38:41: HTTP response: <!doctype html><html lang=\\"en\\"><head><title>HTTP Status 401 � Unauthorized</title><style type=\\"text/css\\">h1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} h2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} h3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} body {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} b {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} p {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;} a {color:black;} a.name {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 401 � Unauthorized</h1><hr class=\\"line\\" /><p><b>Type</b> Status Report</p><p><b>Message</b> Bad credentials</p><p><b>Description</b> The request has not been applied because it lacks valid authentication credentials for the target resource.</p><hr class=\\"line\\" /><h3>Apache Tomcat/8.5.34</h3></body></html>",  
"severity" : "DEBUG"  
}, {  
"message" : "2019-08-28 14:38:41: Exception occurred while executing operation Nutanix API Query. Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: JSON.parse (script\_include:JSON; line 42). Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: JSON.parse (script\_include:JSON; line 42)",  
"severity" : "DEBUG"  
}

The pattern identified the latest Discovery and Service Mapping Patterns applications.System Applications > All Available 

Applications > Installed  
Search for "Discovery and Service Mapping Patterns"  
Currently installed: 1.0.49 L,M,N

**Agent Log**

Errors that concerns the default MID Server script include, NutanixApiQuery.

09/03/19 16:44:14 (665) Worker-Standard:HorizontalDiscoveryProbe-ccfeca231bab734019b7206ebd4bcb72 WARNING \*\*\* WARNING \*\*\* java.net.SocketTimeoutException: connect timed out when posting to https://<IP\_ADDRESS>:<PORT>/<DIR>/<DIR>/rest/v1/storage\_pools?count=100&amp;page=1  
09/03/19 16:44:18 (383) LogStatusMonitor.60 stats threads: 49, memory max: 3641.0mb, allocated: 3046.0mb, used: 1095.0mb, standard.queued: 0 probes, standard.processing: 1 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes  
09/03/19 16:44:24 (665) Worker-Standard:HorizontalDiscoveryProbe-ccfeca231bab734019b7206ebd4bcb72 WARNING \*\*\* WARNING \*\*\* java.net.SocketTimeoutException: connect timed out when posting to https://<IP\_ADDRESS>:<PORT>/<DIR>/<DIR>/rest/v1/storage\_pools?count=100&amp;page=1  
09/03/19 16:44:24 (665) Worker-Standard:HorizontalDiscoveryProbe-ccfeca231bab734019b7206ebd4bcb72 WARNING \*\*\* WARNING \*\*\* org.mozilla.javascript.EcmaError: Cannot read property "entities" from null  
Caused by error in MID Server script include 'NutanixApiQuery' at line 157  
  
154: tmp\_result = httpClient.invoke(CTX,url\_with\_page,method,null,null,ciType,null,"true");  
155: json\_response = JSON.parse(tmp\_result);  
156:  
\==&gt; 157: if(json\_response.entities.length != 0){  
158: result.add(tmp\_result);  
159: }  
160:  
  
09/03/19 16:44:24 (665) Worker-Standard:HorizontalDiscoveryProbe-ccfeca231bab734019b7206ebd4bcb72 WARNING \*\*\* WARNING \*\*\* org.mozilla.javascript.EcmaError: Cannot read property "entities" from null  
Caused by error in MID Server script include 'NutanixApiQuery' at line 40  
  
37: for (var i = 0 ; i &lt; element\_list.size(); i++){  
38: var element = element\_list.get(i);  
39: element\_url = url.replace("{prism\_element}", element);  
\==&gt; 40: var element\_tmp\_result = this.executeV1V2(element\_url, method, CTX, ciType);  
41: for (var j = 0 ; j &lt; element\_tmp\_result.size(); j++){  
42: var element\_page = parserHelper.addTagToResult("added\_sn\_prism\_element",element,element\_tmp\_result.get(j));  
43: result.add(element\_page);  
  
09/03/19 16:44:24 (665) Worker-Standard:HorizontalDiscoveryProbe-ccfeca231bab734019b7206ebd4bcb72 WARNING \*\*\* WARNING \*\*\* org.mozilla.javascript.EcmaError: Cannot read property "entities" from null  
Caused by error in Ad hoc script 'EvalClosure-Get Nutanix Pools' at line 9  
  
6: var ciType = CTX.getAttribute('pattern\_cit\_id');  
7:  
8: var nutaixQuery = new NutanixApiQuery();  
\==&gt; 9: rtrn = nutaixQuery.execute($url, $method, CTX, ciType, $response\_variable\_name, $body);

## Resolution

Apply the attached fix provided by the Pattern Team:

[MID Server Script Includes NutanixApiQuery](https://support.servicenow.com/sys_attachment.do?sys_id=75fc4b70dbc434d0471f9c41ba96191b&view=true)

ecc\_agent\_script\_include\_2dbbb321db2d730097db90c7db9619dc.xml

## Additional Information

Related to: PRB1362776
