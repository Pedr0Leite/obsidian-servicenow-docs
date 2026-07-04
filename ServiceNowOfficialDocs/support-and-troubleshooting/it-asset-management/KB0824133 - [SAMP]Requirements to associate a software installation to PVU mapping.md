---
title: "[SAMP]Requirements to associate a software installation to PVU mapping"
aliases:
  - KB0824133
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824133
kb_number: KB0824133
last_modified: 2024-11-24
---

## \[SAMP\]Requirements to associate a software installation to PVU mapping

  

Licence calculation happens automatically after the recommended requirements are met.  
  
Here are some references from the docs which can help you understand "IBM PVU Process Pack"

1.  Documentation about the "[IBM PVU Process Pack](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/asset-management/concept/c_IBMPVUProcessPack.html "IBM PVU Process Pack")"
2.  Requirements to associate a software installation to PVU mapping "[Requirements to associate a software installation to PVU mapping](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/asset-management/task/t_ReqAssocSWInstToPVUMapping.html "Requirements to associate a software installation to PVU mapping")"  
      
    -   "Meeting recommended requirements ensures that you receive the highest quality results with PVU mapping"  
          
        -   Use a discovery tool, such as ServiceNow Discovery, to identify hardware and populate the configuration management database (CMDB) with the configuration items you want to manage with IBM PVU licensing.
        -   Use a discovery tool, such as ServiceNow Discovery, to identify software installations. Check that the added CPU information is correct.
        -   Activate the Software Asset Management plugin - IBM PVU Process Pack plugin. This also activates the Software Asset Management plugin if it is not already active.
        -   Refresh processor definitions "[Refresh processor definitions for Software Asset Management plugin](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/asset-management/task/t_RefreshProcessorDefinitions.html "Refresh processor definitions for Software Asset Management plugin")"
        -   Ensure that the software models you want to manage with IBM PVU licensing have the correct license type: Per installation - IBM PVU.
        -   Create software counters to calculate IBM PVU licenses.
        -   Count licenses to determine compliance with IBM PVU guidelines.  
              
            
3.  IBM PVU mapping preparation "[IBM PVU mapping preparation](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/asset-management/concept/c_PreparingForIBMPVUMapping.html "IBM PVU mapping preparation")"
4.  Most IBM PVU mapping and license checking in the ServiceNow platform is managed automatically.
5.  For the automatic calculations to be as accurate as possible, it is important that configuration item and software model information be accurate.
6.  This can be populated by some automated discovery tools.
7.  The CPU data is often added accurately when the CMDB is populated with information. If the fields contain incorrect information, manually edit the fields on the configuration item form.

  
After activating the Software Asset Management plugin IBM PVU Process Pack, use the Refresh Processor Definitions module in the Software Asset Management plugin feature to create process definitions for existing computers in the Computer \[cmdb\_ci\_computer\] table.

1.  This step makes sure some business rules in SAM update the Processor Definition \[CMDB\_processor\_definition\] table automatically when changes are made to computers or when new computers are added.
2.  You should not need to use the Refresh Processor Definitions module a second time, but it is always available if you make significant changes to the Computer \[cmdb\_ci\_computer\] table.  
      
    -   Processor definitions "[Processor definitions](https://docs.servicenow.com/bundle/orlando-it-service-management/page/product/asset-management/reference/r_ViewingProcessorDefinitions.html "Processor definitions")"  
          
        
3.  Processor definitions are automatically derived from the information in the configuration item form for an item such as a computer or server.  
      
    -   Use software counters to calculate IBM PVU licenses "[Use software counters to calculate IBM PVU licenses](https://docs.servicenow.com/bundle/kingston-it-service-management/page/product/asset-management/task/t_UseSWCountersCalcIBMPVULice.html "Use software counters to calculate IBM PVU licenses")"  
          
        

To calculate IBM PVU licenses, you can create a software counter with the IBM PVU license type. For a given PVU software package, you only need to create the counter once and then it can be reused.
