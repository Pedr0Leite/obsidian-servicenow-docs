---
title: "How to add additional values to recurring price frequency in service catalog items"
aliases:
  - KB0596974
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596974
kb_number: KB0596974
last_modified: 2025-01-03
---

## How to add additional values to recurring price frequency in service catalog items

  

### Issue

How to add additional values to recurring price frequency in service catalog items 

Overview

* * *

Service catalog item records give you some options for the **Recurring price frequency** field, including **Daily**, **Weekly**, and **Monthly**. For some items, you may want or need to add additional choices to the **Recurring price frequency** field's drop-down menu.

Procedure

* * *

1.  In the Application Navigator, type **sys\_frequency.list** into the **Filter navigator** text box and press enter or return on your keyboard. 
2.  Click **New**. 
3.  Right-click on **Value** field label and select **Configure Dictionary**.  
      
    ![](/sys_attachment.do?sys_id=713b606adb42b450e515c223059619ca)  
      
    
4.  In the **Choices** section or tab, click **New** and add additional choices.  
    In the example below, the choice **Hourly** was added.  
      
    ![](/sys_attachment.do?sys_id=bd3b606adb42b450e515c223059619ed)  
      
    The new choice, **Hourly**, is displayed in the **Recurring price frequency** field drop-down menu.  
      
    ![](/sys_attachment.do?sys_id=8e3ba06adb42b450e515c22305961938)
