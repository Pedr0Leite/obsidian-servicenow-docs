---
title: "CMP - Use MIDOverride Selection Filter "
aliases:
  - KB0749539
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749539
kb_number: KB0749539
last_modified: 2024-11-21
---

## CMP - Use MIDOverride Selection Filter

  

### Issue

This article shows how to configure the MID Selection Override filter for Cloud Operations to go through a specific MID server.

### MID Override

-   Impersonate with the user have Admin Privileges 
-   Make sure the Application is Cloud API 
-   Navigator >> System MID Server  >> MID selector Override 

https://<instancename>.service-now.com/mid\_selector\_override\_list.do 

-   MID selector Override  >> Create New or Modify the existing entry "Override by capability"
-   Note: The override feature allows multiple filter types but only one override filter for each filter type. The Override selector filter type overrides all other filters and takes complete control of the MID Server selection. If this type is active, it is the only filter applied.

![](sys_attachment.do?sys_id=18fbe8eadb42b450e515c223059619de)

### Example Scripts

### Example 1

context = JSON.parse(context);  
//Use a specific mid server for 'vSphere Compute API' Cloud API  
if(context\['capi\_impl\_name'\] == 'vSphere Compute API'){  
var midList = \[\];  
for(mid = 0; mid <= defaultSelectedMIDList.length; mid++){  
if(defaultSelectedMIDList\[mid\].name == 'MID NAME')  
midList.push(defaultSelectedMIDList\[mid\]);  
}  
return midList;  
}

### Example 2

context = JSON.parse(context);  
  
//Use a specific mid server for 'ListSubscriptions' operation   >>>>> Choose the Operation   
if(context\['capi\_method\_name'\] == 'ListSubscriptions'){        
var midList = \[\];  
for(mid = 0; mid <= defaultSelectedMIDList.length; mid++){  
if(defaultSelectedMIDList\[mid\].name == '<MID\_SERVER\_NAME>')  
midList.push(defaultSelectedMIDList\[mid\]);  
}  
return midList;  
}  
  
if (defaultSelectedMIDList.length > 0)  
return defaultSelectedMIDList;  
  
// Check if this is cloud capability - if not nothing to do  
if (!hasCloudCapability(requestedParameters.capabilities))  
return defaultSelectedMIDList;  
  
// get first non cloud capability (e.g AWS) - there should be only one more  
var capability = getNonCloudCapability(requestedParameters.capabilities);  
if (JSUtil.nil(capability)) {  
gs.warn("MID Selection filterOnCapability could not find a capablity for provider!");  
return defaultSelectedMIDList;  
}  
  
// Get mid with AWS capability  
var mids = getMidsWithCapability(capability);  
  
if (mids.length > 0)  
return mids;  
  
mids = getMidsWithCapability('Cloud Management');  
  
getMidsWithoutCapability(mids, capability);  
return mids;  
  
//  
// INNER FUNCTIONS  
//  
  
//  
// Do we have the Cloud capability in the list?  
//  
function hasCloudCapability(capabilities) {  
for(var j in capabilities) {  
if(capabilities\[j\].capability == 'Cloud Management');  
return true;  
}  
  
return false;  
}  
  
//  
// Get the first non cloud capability (e.g. AWS)  
//  
function getNonCloudCapability(capabilities) {  
for(var j in capabilities) {  
if(capabilities\[j\].capability != 'Cloud Management')  
return capabilities\[j\].capability;  
}  
  
return null;  
}  
  
//  
// Get the mids with this specific capability  
//  
function getMidsWithCapability(capability) {  
var selectedMids = \[\];  
for (var i in candidateMIDList) {  
//Get all capabilities assign to a MID server  
var capabilities = candidateMIDList\[i\].capabilities;  
  
for(var j in capabilities) {  
if('' + capabilities\[j\].capability == '' + capability &&  
JSUtil.nil(capabilities\[j\].value))  
selectedMids.push(candidateMIDList\[i\]);  
}  
}  
  
return selectedMids;  
}  
  
//  
// Filter out the mids with certain capability (Check name only, ignore value)  
//  
function getMidsWithoutCapability(mids, capability) {  
for (var i = 0; i < mids.length; i ++) {  
for (var j = 0; j < mids\[i\].capabilities.length; j ++) {  
if (mids\[i\].capabilities\[j\].capability + '' == capability + '') {  
mids.splice(i, 1);  
}  
}  
}  
}  
  

**Note:** Above mentioned scripts are only examples, users need to modify according to the requirement,  if any further questions or more information, please communicate with ServiceNow Technical support Team. 

### Related Links

[Override the MID Server selection filter](https://docs.servicenow.com/csh?version=latest&topicname=override_mid_server_selector.html "Override the MID Server selection filter")
