---
title: "Duplicate CIs get created as Discovery fails to identify serial numbers brought by SCCM"
aliases:
  - KB0718627
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718627
kb_number: KB0718627
last_modified: 2024-04-07
---

## Issue

Symptoms of this issue are duplicate CIs getting created, as Discovery fails to identify the serial numbers brought by SCCM.

## Resolution

Navigate to the Windows OS Desktop patterns and modify step 5 by adding target field name (Serial\_number) to refer the values 2 and 3 as shown below:  

/$sn\_pattern\_designer.do?sys\_id=bfaf65f7db75a200868a7c841f96199d&authoring\_mode=modify&editor\_mode=advanced&section\_item\_type=identification&section\_item\_name=discovery  
  
  
![](sys_attachment.do?sys_id=d48b63ac1b047cd0f34d33bc1d4bcbf4)  

  
  
Now it will be identifying at Rule 2 serial number, updating the CI instead of creating a new one.
