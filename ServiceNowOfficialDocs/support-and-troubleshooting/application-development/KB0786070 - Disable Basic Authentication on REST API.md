---
title: "Disable Basic Authentication on REST API"
aliases:
  - KB0786070
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786070
kb_number: KB0786070
last_modified: 2023-12-14
---

## Issue

-   Considering this scenario:  
    1.  An incoming **REST request authenticates** into the instance only with **OAuth2**. However, this can be **bypassed** with **Basic Authentication**.
    2.  Is it possible for Out Of T the Box (OOTB) to disable the **Basic Authentication** for **REST Request**?

## Resolution

-   There is **no way** to accomplish this scenario **Out Of the Box (OOB)**. However, below you can find **two possible approaches** to achieve the desired behavior.

1.  **Follow the community article [https://community.servicenow.com/community?id=community\_article&sys\_id=08d9af77db2ae3007d3e02d5ca961911](https://community.servicenow.com/community?id=community_article&sys_id=08d9af77db2ae3007d3e02d5ca961911)**  
      
    If you are concerned about modifying an OOB component, you can always make sure to duplicate the OOB Script include before changing it.  
      
    
2.  Using a Scripted Web Service to replace the OOB Table API. The advantage, in this case, would be to preserve the OOB script include. **Please review the community article for your further reference [https://community.servicenow.com/community?id=community\_question&sys\_id=cfcd27ebdb82e384107d5583ca96193a](https://community.servicenow.com/community?id=community_question&sys_id=cfcd27ebdb82e384107d5583ca96193a)**.

**NOTE**: The above-customized approaches are **not tested**, **nor supported by ServiceNow**. If you wish to implement them please make sure to thoroughly test your implementation in a sub-production instance before promoting it to production. 

## Additional Information

-   In addition to this, we suggest you post your requirement in our new Idea Portal. You can refer to **[Idea Management for Customer Enhancement Request (](https://support.servicenow.com/kb_view.do?sysparm_article=KB0755878)[KB0755878](https://support.servicenow.com/kb_view.do?sysparm_article=KB0755878)[)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0755878)**  for further information
