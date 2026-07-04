---
title: "Creating a new project from project template functionality not working"
aliases:
  - KB0656469
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656469
kb_number: KB0656469
last_modified: 2024-04-07
---

## Creating a new project from project template functionality not working

  

### Issue

Creating a new project from project template functionality not working 

Issue Summary  

* * *

From the project form **Project > Projects> Create New**, you can create a project using the **To create project from a template click here** link at the top of the form or from the project\_template form **Project> Projects> Template** using the **Create Project** Related link. 

On the **Create Project from template** page, provide information for the mandatory fields: **Project name**, **Start date**, and **Project template**. After filling out the fields, the Project record should be created with the associated template values.

After filling out the fields, the project is not created and the UI Macro Dialog window is loaded full screen.

\*When tailing the logs you might see an error pointing to the **create\_project** UI Page: 

`Caused by error in sys_ui_page.07009e91c3222100b0449f2974d3aeb6.processing_script at line 7`" and the UI Page will not be modified.

Most Probable Cause  

* * *

Custom Attributes in the pm\_project state Dictionary Override.  

Solution Proposed  

* * *

1.  Navigate to the sys\_dictionary record of the **State** field on the Task table:  
    /nav\_to.do?uri=sys\_dictionary.do?sys\_id=f4ab6f13b032200038b1cc9c77e3c5b4
    
2.  In the **Dictionary Overrides** section/tab, search for **planned\_task** and open that record:  
    <instance>/nav\_to.do?uri=sys\_dictionary\_override.do?sys\_id=4edc269adbe547401cfbd79b5e96190d
    
3.  Verify the attributes. Out of box, the attributes are: close\_states=3;4;7,default\_close\_state=3,default\_work\_state=2,default\_open\_state=1,default\_skipped\_state=7,default\_pending\_state=-5,pending\_states=-5,open\_states=1,work\_in\_progress\_states=2
    
4.  Revise the attributes and correct the customization to be compliant with the description in the documentation topic: [Customize a state for project or project task](https://docs.servicenow.com/csh?topicname=customize-project-task-states.html&version=latest) or revert to the base system (OOB) attributes.
    
5.  Save record and clear the cache.
