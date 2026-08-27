---
title: "Fixed credentials for NodeAccess on ExecuteScript Operation(CMP)"
aliases:
  - KB0713665
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713665
kb_number: KB0713665
last_modified: 2025-01-07
---

## Issue

# Description

* * *

Cloud Management (CMP) node credentials associate credentials for a virtual server that Cloud Management stack provisions. The Cloud Management application automatically creates these credentials every time.

Currently the NodeAccess parameter on ExecuteScript Operation consumes NodeManagement credentials. The node management credentials records are getting created every time when VM creation happens.

We can use fixed credentials in the NodeAccess parameter and should not create Management credentials each and every time of VM creation. 

# Procedure

* * *

Modify the Node credential attribute to use fixed credentials 

1.  Login to the Instance 
2.  Navigate to the Discovery > Credentials or discovery\_credentials table 
3.  Create your own credential and **copy the sys\_id**.
4.  Navigate to Cloud Admin Portal > Design > Any preferred blueprint. 
5.  Click on the ExecuteScript operation. Node credential attribute will be there on the right-hand side.
6.  Replace the expression like $(Script:CustomScriptIncludeName.MethodName\[**arg=user created credential sys\_id**\])  
      
    (Example : $(Script:CMPProvideCAPIResolver.returnCAPIResolver\[arg=5a87909adb1b1300f32ed311ce9619e8\])  
      
    
7.  Navigate to System Definition > Script includes > Create NEW 
8.  Add a new script named **"CMPProvideCAPIResolver"** (Sample script include code as below)

var CMPProvideCAPIResolver = Class.create();  
CMPProvideCAPIResolver.prototype = {  
initialize: function() {  
},  
returnCAPIResolver : function(input){  
return '$(capiResolver.NodeCredentialResolver#nodeCredentialId=' + input + ')';  
},  
type: 'CMPProvideCAPIResolver'  
};
