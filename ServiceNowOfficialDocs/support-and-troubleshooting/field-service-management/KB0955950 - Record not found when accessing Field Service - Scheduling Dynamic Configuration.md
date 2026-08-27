---
title: "\"Record not found\" when accessing Field Service -> Scheduling Dynamic Configuration"
aliases:
  - KB0955950
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955950
kb_number: KB0955950
last_modified: 2024-02-10
---

## "Record not found" when accessing Field Service -> Scheduling Dynamic Configuration

  

### Issue

When navigating to Field Service -> Scheduling Dynamic Configuration you are redirected to a blank page with info ¨Record not found¨

### Cause

The out of the box Module Dynamic Schedule Configuration has this filter condition:

sys\_ID is javascript:new DynamicSchedulingConfigID().getID()

And it is evaluated by the script include DynamicSchedulingConfigID:  
https://<yourinstancename>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=e3a366a73bc1320014544d72f3efc42d

```
var DynamicSchedulingConfigID = Class.create();
DynamicSchedulingConfigID.prototype = Object.extendsObject(AbstractAjaxProcessor, {
getID : function(){
var smConfig = new sn_sm.SMConfiguration();
var configGR = smConfig.getConfigurationByTableName("wm_order");
var request_driven = configGR.getElement("request_driven");
if(JSUtil.notNil(request_driven) && request_driven == true)
return "6691f2bb3b81320014544d72f3efc4a0";
return "3c10d525c32322001c845cb981d3ae72";
},
type: 'DynamicSchedulingConfigID'
});
```

it can be either:  
6691f2bb3b81320014544d72f3efc4a0 Work Order Dynamic Scheduling Config  
3c10d525c32322001c845cb981d3ae72 Work OrderTask Dynamic Scheduling Config

This is the table that the script include checks  
https://<yourinstancename>.service-now.com/sm\_config\_list.do?sysparm\_nostack=true  
  
The script will first check if there is an entry for wm\_order in that table and if it exists, then it will check the value of the field: Request Process process(request\_driven).

If it's true , then 6691f2bb3b81320014544d72f3efc4a0 sys id will be taken. Otherwise 3c10d525c32322001c845cb981d3ae72 will be selected.  

If the record has being deleted from table dynamic\_scheduling\_config, a blank page with the info message "Record not found" will show.

### Resolution

Navigate to dynamic\_scheduling\_config.list and check if one of this two records has been deleted:  

sys\_ID 6691f2bb3b81320014544d72f3efc4a0 Work Order Dynamic Scheduling Config  
sys\_ID 3c10d525c32322001c845cb981d3ae72 Work OrderTask Dynamic Scheduling Config  
  

If so, import the record back from an available instance or an OOB instance.
