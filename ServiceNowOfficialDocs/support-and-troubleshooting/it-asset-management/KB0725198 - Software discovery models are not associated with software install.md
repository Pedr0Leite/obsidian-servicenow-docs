---
title: "Software discovery models are not associated with software install"
aliases:
  - KB0725198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725198
kb_number: KB0725198
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

When discovery or SCCM runs and brings in the newer software install records, the business rule "Create a Software Normalization" creates a software discovery model and links this software install record to it. On the subsequent discovery or SCCM run if there are data that is no longer installed or SCCM brings in the removed software installed, the install records will no longer be present and hence the discovery model will not have a link to it.   
  
SCCM 2012 v2 Removed Softwares :   
[https://####.service-now.com/nav\_to.do?uri=%2Fimp\_sccm2012v2\_removed\_sw\_list.do%3Fsysparm\_userpref\_module%3Dcb3c097337842200e3499b7a93990e78%26sysparm\_clear\_stack%3Dtrue](https://####.service-now.com/nav_to.do?uri=%2Fimp_sccm2012v2_removed_sw_list.do%3Fsysparm_userpref_module%3Dcb3c097337842200e3499b7a93990e78%26sysparm_clear_stack%3Dtrue "https://####.service-now.com/nav_to.do?uri=%2Fimp_sccm2012v2_removed_sw_list.do%3Fsysparm_userpref_module%3Dcb3c097337842200e3499b7a93990e78%26sysparm_clear_stack%3Dtrue")  
  
The cascade delete rule on the field discovery model that is present in the form for software install records is in restrict mode and hence although the software install records are deleted the discovery model stays. This is because the discovery model record is being referenced by either other records in software install table or other tables that are part of SAMP.   
  
Dictionary entry that shows cascade delete rule as restrict:   
[https://#######.service-now.com/nav\_to.do?uri=sys\_dictionary.do?sys\_id=47f2a2ab37042200fde08ff1b3990ec2%26sysparm\_view=advanced](https://#######.service-now.com/nav_to.do?uri=sys_dictionary.do?sys_id=47f2a2ab37042200fde08ff1b3990ec2%26sysparm_view=advanced "https://#######.service-now.com/nav_to.do?uri=sys_dictionary.do?sys_id=47f2a2ab37042200fde08ff1b3990ec2%26sysparm_view=advanced")
