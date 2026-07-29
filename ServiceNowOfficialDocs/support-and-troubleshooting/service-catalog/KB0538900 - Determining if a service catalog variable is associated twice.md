---
title: "Determining if a service catalog variable is associated twice"
aliases:
  - KB0538900
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538900
kb_number: KB0538900
last_modified: 2024-05-01
---

## Determining if a service catalog variable is associated twice

  

### Issue

Determining if a variable is associated twice

Symptoms

* * *

-   Duplicate variables
-   Mandatory value not mandatory
-   Not mandatory is actually mandatory
-   Variable is read-only
-   Variable is not read-only

Resolution

* * *

A variable is double associated if it is attached to the catalog task as a variable and is also part of a variable set. If variables are associated twice with the same item, the following could occur:

-   variables may lose value when they leave the catalog item page and move to the target requested\_item record (or any other target record, such as an incident)
-   data may not pass to the request item
-   client scripts and UI policies may not work properly

To see if a variable exists on a form and in a set:

1.  Find the catalog item.
2.  Scroll to the **Variables** related list.  
      
    
3.  Use the gear to personalize the layout and add the column named **Variable set**.  
      
    In the example, the variable **Notes/Comments** appears twice on the form.  
      
    ![](/sys_attachment.do?sys_id=e5ce3ca2db0ab450e515c223059619b2)  
      
    
4.  If the item is double associated, do one of the following:  
      
    -   remove it from the **Variables** related list
    -   remove the variable set from the **Variable Sets** related list
    -   remove it from inside the variable set (if the variable set is used by more than one item, then this can break the other items, so this fix option carries the most risk)
