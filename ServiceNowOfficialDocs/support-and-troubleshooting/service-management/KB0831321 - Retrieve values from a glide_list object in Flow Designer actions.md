---
title: "Retrieve values from a glide_list object in Flow Designer actions"
aliases:
  - KB0831321
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831321
kb_number: KB0831321
last_modified: 2025-08-27
---

## Retrieve values from a glide\_list object in Flow Designer actions

  

### Issue

When working with glide\_list objects in Flow Designer, values can be passed to actions and Script steps. The flow run details show this process working correctly, but retrieving multiple values from the object in code fails. Only single values are accessible; with multiple values, fields are visible but their values cannot be retrieved. 

### Release

All supported releases

### Resolution

To access all records in a GlideRecord object, iterate through them using the gr.next() method. The following code example demonstrates how to retrieve values from a List.User object in a Script step:

(function execute(inputs, outputs) {  
  
var gr = inputs.param1;  
while(gr.next()) {  
gs.log("sys\_id: " + gr.getValue('sys\_id'));  
for (var prop in gr){  
gs.log(prop + ":" + gr.getValue(prop))  
}  
}  
  
})(inputs, outputs);
