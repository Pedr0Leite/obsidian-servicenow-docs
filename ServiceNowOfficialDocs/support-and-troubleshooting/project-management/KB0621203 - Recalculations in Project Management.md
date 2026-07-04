---
title: "Recalculations in Project Management"
aliases:
  - KB0621203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621203
kb_number: KB0621203
last_modified: 2024-01-28
---

## Recalculations in Project Management

  

### Issue

Recalculations in Project Management 

  
  

# What is recalculation?

* * *

Recalculation, where project dates are computed based on the parent-child hierarchy and the relationships set up across various project tasks, is the core of project planning.

Key recalculation points:

-   Dates are rolled up from child nodes to parent
-   After a node has children, its date cannot be modified through the user interface (except the top project where the Planned Start Date can be modified)
-   The logic of deriving dates is:
    -   For a node in Pending/Open states, Planned End Date = Planned Start Date + Planned Duration
    -   For a node in WIP state, Planned End Date = Actual Start Date + Planned Duration
    -   For a node in Closed state, Actual Duration = Actual End Date - Actual Start Date

# How do I know if recalculation is working correctly?

* * *

Navigate to planned\_task.list and query top\_task as described in [Troubleshooting Project Structure](https://hi.service-now.com/kb_view.do?sysparm_article=KB0621206 "this article"). Personalize (not configure) the list to add the following columns:

-   Planned Start Date
-   Planned End Date
-   Actual Start Date
-   Actual End Date

Sort the list by **Planned Start Date** in **Ascending (A-Z)** order. You should see the top project at the top of the list. The top project should share the **Planned Start Date** with at least one node appearing at the top of the list.

Sort the list by **Planned End Date** in **Descending (Z-A)** order. You should see the top project at the top of the list. The top project should share the **Planned End Date** with at least one node appearing at the top of the list.

# How do I trigger recalculation myself and check?

* * *

There are two options:

-   Use the [Diagnostics Update Set](https://hi.service-now.com/kb_view.do?sysparm_article=KB0621205 "Diagnostics Update Set")
-   Run an API call in **Scripts > Background**  
      
    For Geneva:  
      
    (new SNC.ProjectManagementAPI()).recalculate('<sys\_id\_of\_top\_project>')  
      
    For Helsinki:  
      
    (new SNC.PlannedTaskAPI()).recalculate('<sys\_id\_of\_top\_project>')

# How do I check that recalculation is completing properly?

* * *

1.  If the property does not already exist, [create](https://docs.servicenow.com/ "create") the **com.snc.pm.debug.enable** property.  
    Ensure that the type is **true|false** and the value is set to **true**.
2.  From **Scripts > Background**, trigger recalculation.  
    The platform prints out a significant number of messages in the system logs.
3.  Look for the highlighted messages in the screenshot below.  
    This output is from a Geneva instance and may differ slightly in subsequent releases.   
    Note that this modifies the project and task records, so be aware when running on a production instance.  
      
    ![](sys_attachment.do?sys_id=20aeb0a2db0ab450e515c22305961963)

If you see the last message Into saveRelations(), the recalculation has completed successfully and the project has been saved.

# How do I debug recalculation from forms/lists?

* * *

Trigger the recalculation by changing the **Start Date** or **Duration** of a project task.

Navigate to **System > Logs** and look for the following:

<table style="width: 520px;" border="1" cellspacing="0" cellpadding="0"><tbody><tr><td><strong>Message</strong></td><td><strong>Source</strong></td></tr><tr><td>&nbsp;Start of Load</td><td>&nbsp;com.snc.planned_task.core.loader.Planned</td></tr><tr><td>&nbsp;End of Load : - 00:00:00 : 37 :: 37</td><td>&nbsp;com.snc.planned_task.core.loader.Planned</td></tr><tr><td>&nbsp;Start of recalculation</td><td>&nbsp;com.snc.planned_task.core.engine.Automat</td></tr><tr><td>&nbsp;End of recalculation :&nbsp; - 00:00:00 : 45 :: 45&nbsp;</td><td>&nbsp;com.snc.planned_task.core.engine.Automat</td></tr><tr><td>&nbsp;Start of Save</td><td>&nbsp;com.snc.planned_task.core.datastore.Data</td></tr><tr><td>&nbsp;End of Save :&nbsp; - 00:00:00 : 11 :: 11&nbsp;</td><td>&nbsp;com.snc.planned_task.core.datastore.Data</td></tr></tbody></table>

These are the key logs that indicate the recalculation process is working properly. The process involves the following three steps:

1.  Load the Project into memory.
2.  Perform recalculation.
3.  Save the dirty records to the database.

# I still can't figure why recalculation is not happening

* * *

Check the **calculation\_type** field in Project and all sub-Projects/Project Tasks. They should be set to **Automatic** or **Manual**. Automatic projects are what we have used in this document. Manual projects do not honor relationships between nodes.

Check the project schedule in project record. Check if the schedule is valid. It should be valid for the dates of the project (for example, Schedule defined for year 2025 may not work properly today). It is acceptable to leave the schedule blank.
