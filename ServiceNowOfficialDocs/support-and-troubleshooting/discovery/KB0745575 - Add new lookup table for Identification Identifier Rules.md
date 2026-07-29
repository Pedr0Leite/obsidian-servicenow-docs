---
title: "Add new lookup table for Identification Identifier Rules"
aliases:
  - KB0745575
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745575
kb_number: KB0745575
last_modified: 2024-04-07
---

## Add new lookup table for Identification Identifier Rules

  

### Issue

# Description

OOTB we have some lookup tables that can be used for identification.

For example, in the Hardware Rule, we use the cmdb\_serial\_number to identify a CI based serial numbers it finds for that device and subsequently inserts that rule into that serial number table, all while creating a reference to that CI to that serial number. 

![](/sys_attachment.do?sys_id=57b96862db42b450e515c223059619ce)

In some cases you may want to create your own custom lookup table. In this case there are additional steps that need to be taken. 

# Procedure

1)You will need to make your custom table that will be used for lookup. Unless you want to use some OOTB table for look up.

2)Then you will need to add that table and the field to match on to an identification rule, like you see above. 

3)Lastly you will need to create a custom lookup function like the ones we have OOTB for your custom lookup table.

-   This will need to be done on the script include "DiscoveryCDMBUtil"
-   See the functions there below:

![](/sys_attachment.do?sys_id=57b9a862db42b450e515c22305961943)

-   Notice that it calls "processSerialNiumbers()" function. So a function of the same will need to be written in that script include as well as called in the above function "lookupValuesToJson()".

4)

# Applicable Versions

All

# Additional Information

How this is being called in the first place:

Identiy Probe sensor (or if you are using patterns the Horizontial probe sensor) calls the DiscoveryIDSensor Script Include (SI).  
https://<instance-name>.service-now.com/nav\_to.do?uri=discovery\_sensor.do?sys\_id=2f32f7899f230200fe2ab0aec32e706a  
  
Then from there in the DiscoveryIDSensor SI, we call "CMDBIdentify" function which calls "checkInsertOrUpdate" function from "DiscoveryCMDBUtil".   
Eventually it will work its way down to the lines shared above section.   
  
Here, the function "lookupValuesToJson" will check to the see if the class that we just discovered has a lookup rule in the CI Identifier, where the class is cmdb\_serial\_number (or cmdb\_ci\_network\_adapter) in OOTB configuration.   
If they exist then the lookup payload part is built with the appropriate function called (lookups.concat(processSerialNumbers(ciData)); OR lookups.concat(processNetworkAdapters(ciData));) .  
You can see here that such a function nor condition exists to evaluate another table for lookup. If want to use another table(Class) you will need to add some condition on "lookupValuesToJson()" for that table, as we as create a function for that table similar to "processSerialNumbers()" and "processNetworkAdapters()".
