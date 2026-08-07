---
title: "Performance Issue - Workbench not loading"
aliases:
  - KB0656983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656983
kb_number: KB0656983
last_modified: 2023-09-14
---

## Performance Issue - Workbench not loading

  

### Issue

Performance issue – Workbench not loading

  
  

# Overview

* * *

This article presents a workaround for the workbench failing to load the expected data.

# Issue

* * *

Navigate to Cost Transparency > Workbench.

Note the following screenshot for reference.

![](sys_attachment.do?sys_id=769a24a6db42b450e515c223059619f7)

You don't see any transaction on the application node running for too long.

The browser console displays the following error (highlighted):

js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:99 Couldn't load data from Data Definition Controller
  
(anonymous) @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:99  
(anonymous) @ dataDefinitionController.jsx?v=10-10-2017\_1630:420  
w @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:107  
(anonymous) @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:108  
$eval @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:118  
$digest @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:115  
$apply @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:119  
h @ js\_includes\_itfm\_dashboard.jsx?v=10-10-2017\_1630&lp=Mon\_Oct\_23\_09\_33\_12\_PDT\_2017&c=14\_208:79

# Workaround

* * *

1.  Under **Cost Transparency**, check **General Ledger > Staged Expenses** and click it.
    
2.  A list of staged expenses displays.
    
3.  Load the column **Posting date** if not available.
    
4.  Apply the filter \[Posting date\] \[is empty\].
    
    A list is displayed of Staged expenses that don't have posting date.
    
5.  Open one of the records.
    
    You will see something like the following example screenshot.
    
    ![](sys_attachment.do?sys_id=f69a24a6db42b450e515c223059619fc)
    
    The workbench performs calculations in reference to the posting date field as per the logic. Because these fields are empty, the calculation never completes and the workbench never loads.
    
    You can ask customer to fill in the posting dates or remove those records that are problematic.
    
    Once the posting date is updated or records removed,c the workbench would load normally without any issues.
