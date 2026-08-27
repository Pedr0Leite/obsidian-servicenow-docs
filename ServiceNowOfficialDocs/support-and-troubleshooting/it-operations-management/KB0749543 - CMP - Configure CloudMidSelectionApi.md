---
title: "CMP -   Configure CloudMidSelectionApi "
aliases:
  - KB0749543
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749543
kb_number: KB0749543
last_modified: 2024-04-07
---

## CMP - Configure CloudMidSelectionApi

  

### Issue

# Overview

This Article will Demonstrate to use CloudMidSelectionApi to have the Cloud Operations go through specific MID server

# Configure CloudMidSelectionApi

-   Login to the Instance 
-   Impersonate with the user have Admin Privileges 
-   Make sure the Application is Cloud API 
-   Navigator >> Discovery >> MID server >> Choose the MID server to configure with "CloudMidSelectionApi"
-   Navigator >> System Definition >> Script Includes 

https://<Instancename>.service-now.com/sys\_script\_include\_list.do

-   From the name field choose "CloudMidSelectionApi" 

https://<Instancename>.service-now.com/sys\_script\_include.do?sys\_id=019292f7132893009f325db12244b04b&sysparm\_view=&sysparm\_record\_target=&sysparm\_record\_row=1&sysparm\_record\_list=nameCONTAINScloudmid%5EORDERBYname&sysparm\_record\_rows=1

-   Modify from Line 59  as per your requirement 

![](sys_attachment.do?sys_id=127e3462db0ab450e515c22305961983)

# Example Script 

-   Edit script include CloudMidSelectionApi, Line No 59

change from  
  
**return midSelector.selectMid(app, null, capabilities, context);**   
  
to: 

if (JSON.parse(context).service\_account\_id == 'xxxxxx-xxxx-xxxx-xxxx-xxxxxx') {      >>>>> Cloud Service Account ID   
return 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';   
}   
else {   
// Now we have everything set up - call the mid selector API to select one mid   
var selectedmid = midSelector.selectMid(app, null, capabilities, context);   
  
return midSysId;   
}
