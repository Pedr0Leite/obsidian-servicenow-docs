---
title: "Why is my SLA not attaching?"
aliases:
  - KB0596013
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596013
kb_number: KB0596013
last_modified: 2025-07-28
---

## Issue

To investigate the reason for the SLA not attaching to a task, you must check the following:

-   Condition count widget
-   Configuration of condition types in Service Level Management  
    -   Default condition type (SLAConditionBase)
    -   Simple condition type (SLAConditionSimple)

### Condition count widget

If your system is running on the Fuji release or later, you can add an attribute to the condition fields on the SLA Definition table to enable the Condition Count Widget. Enabling this feature makes troubleshooting easier.  

### Configuration of condition types in Service Level Management

Condition types are script includes that the SLA engine uses to determine whether to start, stop, pause, cancel, or reset a Task SLA.

To determine how condition types have been configured within Service level management: 

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> These instructions only consider the two condition types provided by default. They do not consider customized or new condition types.</td></tr></tbody></table>

1.  Navigate to the list of SLA Definitions.
2.  Personalize the list and add the **Condition type** field.
3.  Go to Default (SLAConditionBase) or Simple (SLAConditionSimple) depending on the value in the field.  
    For example, either SLAConditionBase or SLAConditionSimple.  
    If the field is empty, continue to step 4 below.
4.  Navigate to the following URL, adding your instance’s name in the URL:  
    http://your-instance-name.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=956cb8b40a0a2c8941be2324e33ae3a9
5.  Go to Default (SLAConditionBase) or Simple (SLAConditionSimple) depending on the property value.  
    For example, either SLAConditionBase or SLAConditionSimple.

#### Default condition type (SLAConditionBase)

When using the Default condition type, Task SLA records only attach when the Start conditions match and the Stop conditions do not match.

The following flow diagram demonstrates the process.

![](/sys_attachment.do?sys_id=e5dceceedb42b450e515c22305961988)

#### Check the start conditions

1.  If you have enabled the Condition Count widget attribute, click on the link for start conditions. If not, then open a list of incident records and replicate your start conditions.
2.  Add another condition to your filter that includes a task record (blue #3 in screenshot below) with a Task SLA attached. This confirms that your Start condition matches the correct task. The list should look similar to the screenshot below.
    
    ![](/sys_attachment.do?sys_id=65dceceedb42b450e515c22305961994)
    
3.  If your filter does not bring up any records, your Start condition is the likely reason SLAs are not attaching. To determine the conditions that are causing the problem:  
    1.  In your current list, remove all the conditions except for the one specifying your Task record. Remove conditions for blue #1 and blue #2. Retain blue #3.  
        -   Add one of your filter conditions.
        -   Click **Run**.
        -   If your record is no longer in the list, take note of that condition and remove it.
        -   Repeat steps 1 to 3 until there are no conditions left to add. From the notes you have made of the conditions you removed, these are the ones that do not match your task.
        -   You must now change your Start conditions in order for it to match correctly.
    2.  If your filter brings up a record, your Stop condition must be checked.
4.  Check the stop conditions.  
    1.  Repeat steps 1.1 and 1.2, this time using the Stop conditions.
    2.  If your filter brings up the same record as in step 1, the problem is that your Start and your Stop conditions match at the same time and this is the reason the SLAs do not attach.

#### Simple condition type (SLAConditionSimple)

When using the Simple condition type, Task SLA records will only attach when the Start conditions match. If the Stop Conditions match when a Task SLA is being attached, the Task SLA is still processed but it completes immediately. The following flow diagram demonstrates the process.

![](/sys_attachment.do?sys_id=a9dceceedb42b450e515c223059619a2)

#### Check the start conditions.  

1.  If you have enabled the Condition Count widget attribute, click on the link for start conditions. If not, then open a list of incident records and replicate your start conditions.
2.  Add another condition to your filter that includes a task record (blue #3) with a Task SLA attached. This confirms that your Start condition matches the correct task. The list should look similar to the screenshot below.
    
    ![](/sys_attachment.do?sys_id=65dceceedb42b450e515c223059619ae)
    
3.  If your filter does not bring up any records, your Start condition is the likely reason SLAs are not attaching. To determine the conditions that are causing the problem:  
    1.  In your current list, remove all the conditions except for the one specifying your Task record. Remove conditions for blue #1 and blue #2. Retain blue #3.  
        -   Add one of your filter conditions.
        -   Click **Run**.
        -   If your record is no longer in the list, take note of that condition and remove it.
        -   Repeat steps 1 to 3 until there are no conditions left to add. From the notes you have made of the conditions you removed, these are the ones that do not match your task.
        -   You must now change your Start conditions in order for it to match correctly.
