---
title: "How to stop creating alerts for CI's that are currently in Un-Installed  Non-Operational status"
aliases:
  - KB0692596
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692596
kb_number: KB0692596
last_modified: 2025-01-03
---

## How to stop creating alerts for CI's that are currently in Un-Installed Non-Operational status

  

### Issue

# Description

* * *

How to stop creating alerts for CI's in non-operational or un-installed status?

# Procedure

* * *

There is a Out of the box script include called EvtMgmtCustom\_PostBind\_Create, this is after we bind the CI but before we create an alert.

This script include is  not active out of the box but you can define your logic in this script include to ignore the creation of the alert based on Operational status. 

 For example, You can use this  piece of code which will ignore any CI with operational status (4,2,3). you will have to define these numbers based on the choice list and your requirements. You can add more logic around this code. If returned false, it will skip creation of alert. 

**\*\*\*\*\*Sample code to ignore creating alerts if the CI is in operational status (4,2,3)\*\*\*\*\*\***  
  
  
(function postBindCreate(event, alert, origEventSysId){   
gs.log('PostBind\_Create custom script is active');   
  
var ignore\_statuses = \['4','2','3'\]; //   
  
var ciid = alert.cmdb\_ci.toString();   
if(JSUtil.notNil(ciid)){   
var ciGr = new GlideRecord('cmdb\_ci');   
if (ciGr.get(ciid)){   
var operation\_status = ci.operational\_status.toString();   
if (ignore\_statuses.indexOf(operation\_status) != -1)   
return false;   
}   
}   
  
// In this part of the function make any changes to alert using glide record interface. E.g:   
// alert.setValue('source', 'new source');   
  
// To abort alert creation return false;   
// returning a value other than boolean will result in an error   
return true;   
})(event, alert, origEventSysId); 

# Applicable Versions

* * *

Jakarta, Kingston, London
