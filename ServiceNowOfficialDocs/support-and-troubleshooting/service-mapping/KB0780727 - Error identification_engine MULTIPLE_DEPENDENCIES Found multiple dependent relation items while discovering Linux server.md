---
title: "Error : identification_engine : MULTIPLE_DEPENDENCIES Found multiple dependent relation items while discovering Linux server"
aliases:
  - KB0780727
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780727
kb_number: KB0780727
last_modified: 2026-06-19
---

## Error : identification\_engine : MULTIPLE\_DEPENDENCIES Found multiple dependent relation items while discovering Linux server

  

### Issue

Discovery of a Linux server fails with the error "Failed Exploring CI Pattern, Pattern name: Linux Server" in the discovery logs.

When you review the identification logs, you would observe the below Identification engine errors

1 : 10-May-2019 01:05:04:AM : Error : identification\_engine : MULTIPLE\_DEPENDENCIES Found multiple dependent relation items \[{"parent":2,"child":0,"type":"Contains::Contained by"}\] and \[{"parent":1,"child":0,"type":"Contains::Contained by"}\] in payload  
2 : 10-May-2019 01:05:04:AM : Error : identification\_engine : Detected error while processing payload from ServiceWatch  
3 : 10-May-2019 01:05:04:AM : Error : identification\_engine : Input = {"items":\[{"className":"cmdb\_ci\_memory\_module","values":{"total\_width":"64","device\_locator":"RAM slot #XX1XX9XX","serial\_number":"X41XXX9XX","data\_width":"64","type":"DRAM","type\_detail":"Synchronous","sys\_class\_name":"cmdb\_ci\_memory\_module","capacity":"4096","bank\_label":"RAM slot #XX1XX9XX","discovery\_source":"ServiceNow","name":"RAM slot #XX1XX9XX","part\_number":"XXX-760XXX150MB","form\_factor":"DIMM"},"lookup":\[\],"related":\[\]},{"className":"cmdb\_ci\_linux\_server","values":{"default\_gateway":"10.11.102.1","short\_description":"Linux hostname 3.10.0-957.1.3.el7.x86\_64 #1 SMP Thu Nov 15 17:36:42 UTC 2018 x86\_64 x86\_64 x86\_64 GNU/Linux","cpu\_core\_thread":"1","cpu\_manufacturer":"27a389a1db176bc02ae5839648961944","sys\_class\_name":"cmdb\_ci\_linux\_server","manufacturer":"e49c85c56f995100985a93d31c3ee424","cpu\_count":"4","discovery\_source":"ServiceNow"

### Release

London Patch 7

### Cause

-   The Linux server input payload contains 4 RAM's of different memory capacity but with same serial number and name configured.
-   We have an OOB memory module identifier rule which checks for the serial number and name attributes before a record is inserted into the memory module table.
-   As the payload, contains 4 RAM's with the same name and serial number, the CI is not created in the cmdb\_ci\_memory\_module table.  
      
    

{&#13;  
"className" : "cmdb\_ci\_memory\_module",&#13;  
"values" : {&#13;  
"bank\_label" : "RAM slot #XX1XX9XX",&#13;  
"total\_width" : "64",&#13;  
"device\_locator" : "RAM slot #XX1XX9XX",&#13;  
"name" : "RAM slot #XX1XX9XX",&#13;  
"part\_number" : "XXW-1234XX7890X",&#13;  
"serial\_number" : "XX1XX9XX",&#13;  
"data\_width" : "64",&#13;  
"type" : "DRAM",&#13;  
"type\_detail" : "Synchronous",&#13;  
"form\_factor" : "DIMM",&#13;  
"sys\_class\_name" : "cmdb\_ci\_memory\_module",&#13;  
"capacity" : "16384"&#13;  
}&#13;  
},  
  
{&#13;  
"className" : "cmdb\_ci\_memory\_module",&#13;  
"values" : {&#13;  
"bank\_label" : "RAM slot #XX1XX9XX",&#13;  
"total\_width" : "64",&#13;  
"device\_locator" : "RAM slot #XX1XX9XX",&#13;  
"name" : "RAM slot #XX1XX9XX",&#13;  
"part\_number" : "XXW-1234XX7890X",&#13;  
"serial\_number" : "XX1XX9XX",&#13;  
"data\_width" : "64",&#13;  
"type" : "DRAM",&#13;  
"type\_detail" : "Synchronous",&#13;  
"form\_factor" : "DIMM",&#13;  
"sys\_class\_name" : "cmdb\_ci\_memory\_module",&#13;  
"capacity" : "4096"&#13;  
}&#13;  
},  
  
{&#13;  
"className" : "cmdb\_ci\_memory\_module",&#13;  
"values" : {&#13;  
"bank\_label" : "RAM slot #XX1XX9XX",&#13;  
"total\_width" : "64",&#13;  
"device\_locator" : "RAM slot #XX1XX9XX",&#13;  
"name" : "RAM slot #XX1XX9XX",&#13;  
"part\_number" : "XXW-1234XX7890X",&#13;  
"serial\_number" : "XX1XX9XX",&#13;  
"data\_width" : "64",&#13;  
"type" : "DRAM",&#13;  
"type\_detail" : "Synchronous",&#13;  
"form\_factor" : "DIMM",&#13;  
"sys\_class\_name" : "cmdb\_ci\_memory\_module",&#13;  
"capacity" : "2048"&#13;  
}&#13;  
},  
  
{&#13;  
"className" : "cmdb\_ci\_memory\_module",&#13;  
"values" : {&#13;  
"bank\_label" : "RAM slot #XX1XX9XX",&#13;  
"total\_width" : "64",&#13;  
"device\_locator" : "RAM slot #XX1XX9XX",&#13;  
"name" : "RAM slot #XX1XX9XX",&#13;  
"part\_number" : "XXW-1234XX7890X",&#13;  
"serial\_number" : "XX1XX9XX",&#13;  
"data\_width" : "64",&#13;  
"type" : "DRAM",&#13;  
"type\_detail" : "Synchronous",&#13;  
"form\_factor" : "DIMM",&#13;  
"sys\_class\_name" : "cmdb\_ci\_memory\_module",&#13;  
"capacity" : "1024"&#13;  
}&#13;  
} \],&#13;

### Resolution

-   In order to fix this issue, below 2 approaches can be considered.  
      
    
-   Approach 1 - You can either define unique serial numbers for the RAM's on the Linux server and rediscover the Linux server.
-   Approach 2 - Add a new attribute to the memory module identifier rule which is unique say "memory capacity" to the memory module identifier rule.

-   The recommended approach would be to define unique serial numbers for the RAM at the Linux server level rather than changing the OOB identifier rule.
-   Rediscover the Linux server after making the required changes, the Linux server would be successfully discovered.
