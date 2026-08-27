---
title: "Determining if a variable is defined on the workflow or execution plan"
aliases:
  - KB0538899
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538899
kb_number: KB0538899
last_modified: 2024-05-01
---

## Determining if a variable is defined on the workflow or execution plan

  

### Issue

Determining if a variable is defined on the workflow or execution plan

Symptoms

* * *

-   No variables on form
-   Variable not visible

  
Resolution

* * *

In some use cases, a catalog item runs a workflow or execution plan that creates a catalog task. Sometimes the catalog task may not show all or any of the variables that were in the original item.

To troubleshoot variables that are not visible on a catalog task created from a workflow:  

1.  The variable or variables may not be included in the workflow activity that defines the task. Check by finding the WF activity that is creating the task inside the Workflow editor window.  
      
    

![](/sys_attachment.do?sys_id=0dfc6822db82b450e515c223059619a8)  
  
-   Open the task.  
      
    The **Variables on Task Form** slush bucket appears on the form, with **Available** and **Selected** variables listed. The variables that you need to see must be in the **Selected** list.  
      
    
![](/sys_attachment.do?sys_id=8dfc6822db82b450e515c223059619cd)  
  
Note the following:

-   -   Changing the slush bucket does not change already created tasks's variables.
    -   The change is applied to new tasks created after the change.
    -   If you have multiple tasks in a workflow, you will need to do the same for all of them.
    -   Incorrect formatting on the catalog task variables will be caused by missing out the containers in the selected slush bucket.  
          
        

To troubleshoot variables that are not visible on a catalog task created from an execution plan:  

1.  The variable(s) may not be included in the execution plan that is creating the task. Check by finding the execution plan that is creating the task.  
      
    The related list contains the **Execution Plan Task** related list.  
      
    

![](/sys_attachment.do?sys_id=1dfca822db82b450e515c22305961952)  
  
Note the following:

-   -   Changing the **Available Variables** list does not change the variables on previously created tasks.
    -   The change is applied to new tasks created after the change.
    -   A related list on this task is called **Available Variables**.
    -   The variables that you need to see must be on the **Available Variables** list.
    -   If you have multiple tasks in an Execution Plan Task list, you will need to do the same for all of them.
    -   Incorrect formatting on the catalog task variables are caused by missing out the containers in the list.
