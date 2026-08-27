---
title: "How to quickly setup new data stream action with pagination"
aliases:
  - KB0756552
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756552
kb_number: KB0756552
last_modified: 2025-01-03
---

## How to quickly setup new data stream action with pagination

  

### Summary

The propose of this tutorial is to have you quickly set up and get familiar with the new data stream action & pagination

We'll be pulling data from an another instance, from \[cmdb\] table, using REST table APIs

### Release

data stream action & pagination were introduced in New York

### Instructions

In our example, we'll be getting data from another instance's \[cmdb\] table and logging each record being returned. The data stream action, when used in a flow, will always contain the flow logic "for each item in" (see below screenshot).

![](sys_attachment.do?sys_id=532643f01b0cb014f34d33bc1d4bcb0a)

Our data stream action will return the name, the created by user, and the sys id of each of the \[cmdb\] records. For each of the records from the remote \[cmdb\] table, we will be logging them.

1.  To add the new "data stream" action, click on the plus sign next to the tabs in the flow designer. You'll see the options of selecting flow, subflow, action, & data stream. Give your action a name and save.  
      
    
2.  In our example, we will not be passing in any variables to the action, and no action preprocessing will be done.   
      
    
3.  When editing the action, under "action outline" click on the "request" step, and for the field "how will you get data" select "REST Step" and check enable pagination.![data stream action](sys_attachment.do?sys_id=5f2643f01b0cb014f34d33bc1d4bcb06)  
      
    
4.  Once REST and pagination are selected, new steps are added to the action. Click on "pagination setup" step. From here we'll add the "limit" and "offset" variable, the "offset" variable will be used in the REST step of our action. The "limit" variable will contain a value of 100, and "next value from" script, offset will have an initial value of 0 and "next value from" script. (see screenshot below)The following script is from the documentation:  
      
    
    (function paginate(variables, pageResponse) {
    
    // Use this script to set pagination variables or
    
    // manipulate variables extracted by XPath or JSON Path
    
    var limit = parseInt(variables.limit);
    
    var totalCount = parseInt(pageResponse.response\_headers\['X-Total-Count'\]);
    
    var currentOffset = parseInt(variables.offset);
    
    var nextOffset = currentOffset + limit;
    
    if(nextOffset < totalCount){
    
    variables.getNextPage = true;
    
    variables.offset = nextOffset.toString();
    
    } else {
    
    variables.getNextPage = false;
    
    }
    
    })(variables, pageResponse);
    
      
    Essentially what the script is doing is making sure that all records from the table have been requested. The header of the response contains "X-Total-Count" which contains the total amount of records on the table. The offset variable is incremented and the variable is used on the next request to the remote instance, as we'll see in the REST step setup.  
    ![](sys_attachment.do?sys_id=572643f01b0cb014f34d33bc1d4bcb42)  
      
    
5.  Click on REST Step, from the connection field, select "use connection alias" and select your connection alias, this will contain the username and password and the base URL. Use module "Connection & Credential Aliases" to set one up. For Request Details setup as follows (see screenshot)  
    ![](sys_attachment.do?sys_id=d72643f01b0cb014f34d33bc1d4bcb3d)  
    \- Build Request "Manually"  
    \- Resource Path: /api/now/table/cmdb  
    \- HTTP Method: GET  
    \- Add two query parameters  
    \- sysparm\_limit, with a value of 100  
    \- sysparm\_offset, the value of this is the offset variable from the pagination set (drag the variable to form the data pill).  
      
    
6.  Next from the "Parsing" step, set the following:  
    \- How will you identify each record "JSON/XML Splitter"  
    \- How will you parse each item into an object "Script Parser"  
    Once you select the above options, additional sub-steps will be added  
    \-From the "Splitterstep" select "SourceFormat" as "JSON" & itemPath "$.result"  
    \-"result" is the array from the JSON object being returned when using the table API  
    \-From the "Script Parser Step" this step will map the incoming record's values to the output.targetObject, which will then be used as the output variable of the data stream action. Paste the following code, this will get use the name of the \[cmdb\] records, and created by, and sys id mapped to the targetObject  
    
    var record = JSON.parse(inputs.sourceItem);
    
    gs.info("each JSON sourceItem " + JSON.stringify(inputs.sourceItem));
    
    outputs.targetObject.name=record.name;
    
    outputs.targetObject.sys\_created\_by=record.sys\_created\_by;
    
    outputs.targetObject.sys\_id=record.sys\_id;
    
7.  The final configuration in our data stream action is to configure the output variables, to be used in our flow  
    \- from the "Outputs" step we will create a variable called, CMDB CIs, of type "object"  
    \- this contains the targetObject from step 6, from here we will need to create three sub-variables, where the names will have to match the variables created for the targetObject in step 6 (see screenshot below)  
    ![data stream output variables](sys_attachment.do?sys_id=db2643f01b0cb014f34d33bc1d4bcb40)
8.  Now publish the action, and now you can use it in any flow, the new action will contain the output variables where you can use in other actions within the main flow.

### Related Links

Further information can be found in the New York product documentation.
