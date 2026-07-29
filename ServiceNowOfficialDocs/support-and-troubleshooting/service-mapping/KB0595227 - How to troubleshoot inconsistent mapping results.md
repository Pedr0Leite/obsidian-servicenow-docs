---
title: "How to troubleshoot inconsistent mapping results"
aliases:
  - KB0595227
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0595227
kb_number: KB0595227
last_modified: 2024-04-07
---

## How to troubleshoot inconsistent mapping results

  

### Issue

Problem

* * *

Inconsistent results are displayed when running mapping to discover the same business service.   
  
  
Symptoms

* * *

You may receive a business service map consisting of different CIs every time you run the mapping process on the same entry points to discover the same business service.     
  
  
Cause

* * *

The parameters that influence the way Service Mapping renders mapping results are changed.  
  
  
Resolution

* * *

Follow the procedures below to ensure that the instance-related parameters causing the mapping results to change are set correctly.  
  

Change the MID Server configuration parameter:

1.  In the navigation pane, click **MID Servers** > **Properties**.
2.  Click **New**.
3.  In the **Name** field, enter **mid.servicewatch.solaris.dtrace**.
4.  In the **Value** field, enter **false**. 
5.  In the **MID Server** list, select the MID Server used to discover the business service in question.
6.  Click **Submit**.  
      
    

Fix the CI identifier for Oracle WebLogic Module:

1.  In the navigation pane, click **CI Identifiers**.
2.  From the list of CIs, select **WeblogicModule** (cmdb\_ci\_appl\_weblogicmodule).
3.  Click the entry under **Identifier Entries**.
4.  Clear the **Allow fallback to parent's rules** option to disable this feature. 
5.  Click **Submit****.  
      
    **
