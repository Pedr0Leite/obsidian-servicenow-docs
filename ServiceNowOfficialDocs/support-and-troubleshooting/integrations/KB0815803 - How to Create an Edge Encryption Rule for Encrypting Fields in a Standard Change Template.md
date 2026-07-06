---
title: "How to Create an Edge Encryption Rule for Encrypting Fields in a Standard Change Template"
aliases:
  - KB0815803
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815803
kb_number: KB0815803
last_modified: 2024-04-08
---

## How to Create an Edge Encryption Rule for Encrypting Fields in a Standard Change Template

  

### Issue

You have the "Change Management - Standard Change Catalog" plugin active and need to encrypt fields from a Standard Change Template.  

In order to do this you need to define a custom Edge Encryption Rule.

This article describes how this can be done.

### Release

Applies to any release that uses the Standard Change Catalog and Edge Encryption.

### Resolution

(1) In this example, you have active edge encryption configurations on these two columns:

change\_request.backout\_plan  
change\_request.implementation\_plan

(2) Set the dictionary Attribute "Edge Encrypted Data Allowed" on these two columns:

(a) Go to Tables  
(b) Open table name = sys\_template  
(c) Open table column name = template  
(d) Select the Attributes tab and select New  
(e) In Attribute magnifying glass search for Label = Edge Encrypted Data Allowed - if this attribute is not visible SN support may need to add this attribute  
(f) Set Value = true  
(g) Submit  
(h) Go back to Tables  
(i) Open table name = std\_change\_proposal  
(j) Open table column name = template\_value  
(k) Select the Attributes tab and select New  
(l) In Attribute magnifying glass search for Label = Edge Encrypted Data Allowed - if this attribute is not visible SN support may need to add this attribute  
(m) Set Value = true  
(n) Submit

(3) From the edge encryption proxy URL -> Go to Change -> Standard Change -> All Templates -> for this example choose Template name = Clear BGP sessions on a Cisco router -> under Related Links select "Create Edge Encryption Rule" -> two rules will be created:

RP\_ClearBGPsessionsonaCiscorouterJson  
and  
RP\_ClearBGPsessionsonaCiscorouter

(4) Edit rule RP\_ClearBGPsessionsonaCiscorouterJson:

Fill out the Condition section as follows:

function RP\_ClearBGPsessionsonaCiscorouterJsonCondition(request) {  
if (endsWith(request.path, '/service\_catalog.do') &&  
request.postParams.sysparm\_action == 'execute\_producer' &&  
request.postParams.sysparm\_id == '32b19f3b9fb002002920bde8132e7024')  
return true;  
else if (endsWith(request.path, '/std\_change\_record\_producer.do') &&  
request.postParams.sys\_action == '66148b12bf3021000ba9dc2ecf0739cc')  
return true;  
return false;  
}

Fill out the Action section as follows:

function RP\_ClearBGPsessionsonaCiscorouterJsonAction(request) {  
// Some fields are set in script, additional parameter lines may need to be added  
// current.std\_change\_producer\_version is accessed via script from "16c2273c47010200e90d87e8dee49006";  
// current.type is accessed via script from "standard";  
request.postParams\['IO:0fb19f3b9fb002002920bde8132e7029'\].encodedQueryFor('change\_request');  
request.postParams\['sys\_template.template'\].encodedQueryFor('change\_request');  
}

Note that the sys\_id and the variable value are just place holders for now:

request.postParams.sysparm\_id == '32b19f3b9fb002002920bde8132e7024')  
request.postParams.sys\_action == '66148b12bf3021000ba9dc2ecf0739cc')  
request.postParams\['IO:0fb19f3b9fb002002920bde8132e7029'\].encodedQueryFor('change\_request');

(5) To find the sys\_id for this line in the Condition section do the following:

request.postParams.sysparm\_id == '32b19f3b9fb002002920bde8132e7024')

(a) Go to Change -> Standard Change -> All Templates -> select template "Clear BGP sessions on a Cisco router"  
(b) From Related Links select -> Modify Template  
(c) Enter a "Template description"  
(d) From the browser start Developer tools and go to the Network tab  
(e) Save the template  
(f) From the Developer Tools Network tab find the POST to service\_catalog.do and find the sysparm\_id as in this screen shot:

![](sys_attachment.do?sys_id=37aa28c9db48b8d066e0a345ca961939)

This will be the line in the Rule Condition:

request.postParams.sysparm\_id == '32b19f3b9fb002002920bde8132e7024')

(g) For the saved template select to "Request Approval" then have one of the Approvers approve the changed template.

(6) To find the sys\_id for this line in the Condition section do the following:

request.postParams.sys\_action == '66148b12bf3021000ba9dc2ecf0739cc')

(a) Go to Change -> Standard Change -> All Templates -> select template "Clear BGP sessions on a Cisco router"  
(b) Edit the "Template description" to any new value  
(c) From the browser start Developer tools and go to the Network tab  
(d) Save the template  
(e) From the Developer Tools Network tab find the POST to std\_change\_record\_producer.do and find the sys\_action as in this screen shot:

![](sys_attachment.do?sys_id=bbaa28c9db48b8d066e0a345ca96193a)

This will be the line in the Rule Condition:

request.postParams.sys\_action == '66148b12bf3021000ba9dc2ecf0739cc')

(7) To find the variable value in the Action section do the following:

request.postParams\['IO:0fb19f3b9fb002002920bde8132e7029'\].encodedQueryFor('change\_request');

(a) Go to Change -> Standard Change -> All Templates -> select template "Clear BGP sessions on a Cisco router"  
(b) From Related Links select -> Modify Template  
(c) Enter a "Template description"  
(d) From the browser start Developer tools and go to the Network tab  
(e) Save the template  
(f) From the Developer Tools Network tab find the POST to service\_catalog.do and find the IO:xxxx as in this screen shot:

![](sys_attachment.do?sys_id=b3aa28c9db48b8d066e0a345ca96193c)

This will be the line in the Rule Condition:

request.postParams\['IO:0fb19f3b9fb002002920bde8132e7029'\].encodedQueryFor('change\_request');

(8) Go back to the Rule RP\_ClearBGPsessionsonaCiscorouterJson and make sure the Condition and Action sections have the correct values, set it to Active and save it, in this example this is the Rule:

Fill out the Condition section as follows:

function RP\_ClearBGPsessionsonaCiscorouterJsonCondition(request) {  
if (endsWith(request.path, '/service\_catalog.do') &&  
request.postParams.sysparm\_action == 'execute\_producer' &&  
request.postParams.sysparm\_id == '32b19f3b9fb002002920bde8132e7024')  
return true;  
else if (endsWith(request.path, '/std\_change\_record\_producer.do') &&  
request.postParams.sys\_action == '66148b12bf3021000ba9dc2ecf0739cc')  
return true;  
return false;  
}

Fill out the Action section as follows:

function RP\_ClearBGPsessionsonaCiscorouterJsonAction(request) {  
// Some fields are set in script, additional parameter lines may need to be added  
// current.std\_change\_producer\_version is accessed via script from "16c2273c47010200e90d87e8dee49006";  
// current.type is accessed via script from "standard";  
request.postParams\['IO:0fb19f3b9fb002002920bde8132e7029'\].encodedQueryFor('change\_request');  
request.postParams\['sys\_template.template'\].encodedQueryFor('change\_request');  
}

(9) Go to the Standard Change Catalog and test that the implementation and backout plans are encrypted as expected for the template used.
