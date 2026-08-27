---
title: "Service Level Agreements (SLA) Troubleshooting Guide"
aliases:
  - KB0598456
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598456
kb_number: KB0598456
last_modified: 2026-06-03
---

## Service Level Agreements (SLA) Troubleshooting Guide

  

### Issue

Table of Contents  

* * *

<table class="tocTable" style="height: 223px;" width="756"><tbody><tr><td><a style="text-decoration: none;" href="#1"><span style="color: #646464;"><span style="color: #d1232b;">1.</span>&nbsp;Why is my SLA not getting attached to the task record?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#2"><span style="color: #646464;"><span style="color: #d1232b;">2.</span>&nbsp;Why do I have to refresh the form to see the attached task SLAs?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#3"><span style="color: #646464;"><span style="color: #d1232b;">3.</span>&nbsp;Why are task SLA records getting canceled?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#4"><span style="color: #646464;"><span style="color: #d1232b;">4.</span>&nbsp;What is the difference between <strong>Actual elapsed time</strong> and <strong>Business elapsed time</strong>?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#5"><span style="color: #646464;"><span style="color: #d1232b;">5.</span>&nbsp;Why are the <strong>Actual elapsed time</strong> and <strong>Business elapsed time</strong> not correct on the task SLA record?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#6"><span style="color: #646464;"><span style="color: #d1232b;">6.</span>&nbsp;Why do task SLAs not get updated on refresh in Dashboards / Homepages / Reports?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#7"><span style="color: #646464;"><span style="color: #d1232b;">7.</span>&nbsp;Why do my users receive&nbsp;a notification that an SLA has reached a certain percentage when the task SLA record does not reflect this?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#8"><span style="color: #646464;"><span style="color: #d1232b;">8.</span>&nbsp;What is the purpose of the <strong>SLA Due</strong>, <strong>Made SLA</strong>&nbsp;and <strong>Escalation</strong>&nbsp;fields on the Task record?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#9"><span style="color: #646464;"><span style="color: #d1232b;">9.</span>&nbsp;What is the difference between the <strong>Default</strong> and <strong>Simple</strong>&nbsp;SLA condition rules?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#10"><span style="color: #646464;"><span style="color: #d1232b;">10.</span>&nbsp;How can I define an SLA that has a <strong>Breach time</strong> (Planned end time) that is for a user defined time?</span></a></td></tr><tr><td><p><a style="text-decoration: none;" title="11. Why do task SLAs not get updated when modifying records referenced via dot-walking in a condition of the SLA Definition?" href="#11"><span style="color: #646464;"><span style="color: #d1232b;">11.</span>&nbsp;Why do task SLAs not get updated when modifying records referenced via dot-walking in a condition of the SLA Definition</span></a></p></td></tr></tbody></table>

style="text-decoration: none;" name="1">

  

1\. Why is my SLA not getting attached to the task record?

* * *

**Check for Active flag on SLA Definition**

Only active SLA definitions are evaluated.

  

![](https://support.servicenow.com/sys_attachment.do?sys_id=81aef0a2db0ab450e515c22305961974)

  

**![](https://support.servicenow.com/sys_attachment.do?sys_id=19aef0a2db0ab450e515c22305961990)**

  

**Note:** In Geneva and earlier releases, the Active option is not displayed on the default form layout or the default list layout. To verify if your SLA definitions are set to Active, configure the form and list layouts to show the Active option.

  

**Check the Start condition on the SLA Definition**

  

An SLA is attached to a task record only when values on the task record match the start condition specified in the SLA definition.

![](https://support.servicenow.com/sys_attachment.do?sys_id=51aef0a2db0ab450e515c223059619a4)

**Check the Stop condition and Cancel condition on the SLA definition** 

If the values on the task record match either the Stop or Cancel conditions, the SLA is not attached to the task record, even if the Start conditions match.

**Note:** The Cancel condition option is available in Helsinki and later releases.

  

**Check for customized business rules that might be setting the workflow to false**

Check for any customized "before" business rules on the task table that might be setting the workflow to false. The code is: current.setWorkflow(false);.

Comment out current.setWorkflow(false); statements and then test if SLAs are being attached. Setting a workflow to false stops further business rules from being executed. The SLA Engine depends on the base system business rules Run SLAs and Process SLAs to evaluate SLA conditions.

  

**Check if the base system business rules are active**

Check if the base system business rules Run SLAs and Process SLAs on the Task table are active.

  

**Check if any custom query business rules are defined**

Check if any custom query business rules are defined on the Task or SLA Definitions table that could be filtering out the records.

A query business rule provides the ability to add additional conditions whenever a table is queried. This might stop the SLA engine from being able to query the Task or SLA Definition records and could lead to improper evaluation of the SLA definitions.

Refer to the below screen shot to see how to query for any active Before Query business rules.

![](https://support.servicenow.com/sys_attachment.do?sys_id=99aef0a2db0ab450e515c223059619b2)

**Note:** This issue has been fixed in Helsinki and later releases. Refer to [KB0553527](https://support.servicenow.com/kb_view.do?sysparm_article=KB0553527 "KB0553527") for complete details. This article also provides a workaround for Geneva and prior releases.

style="text-decoration: none;" name="2">

  

  

2\. Why do I have to refresh the form to see the attached task SLAs?

* * *

**Check if SLA Engine is set to run asynchronously**

Fuji and earlier releases:

1.  Navigate to **Service Level Management > Administration > SLA Properties**.
2.  Check if the property **Run the 2011 SLA engine asynchronously after task insert or update operations** is on.  
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=61aef0a2db0ab450e515c223059619dc)

Geneva:

1.  Navigate to **Service Level Management > Properties > SLA Engine**.
2.  Check if the property **Run the 2011 SLA engine asynchronously after task insert or update operations** is on.  
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=21aef0a2db0ab450e515c223059619e5)

Helsinki and later releases:

1.  Navigate to **Service Level Management > Properties > SLA Engine**.
2.  Check if the property **Execute the 2011 SLA engine asynchronously** is on or off.   
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=65aef0a2db0ab450e515c223059619ed)  
      
    If this property is turned on, the SLA engine is executed in asynchronous mode. This creates a delay between the task record update and SLA engine execution. This improves the performance of inserts and updates to the task records, but requires the user to either refresh the task form or the Task SLAs related list to see the attached SLAs.

style="text-decoration: none;" name="3">

  

3\. Why are task SLA records getting canceled?

* * *

Check the start condition on the SLA definition. An SLA attached to a task is canceled if the start condition on the SLA definition no longer matches. It is important to understand this behavior inorder to define SLA conditions correctly. The start condition should be thought of as a condition that must be true for the whole period that you want the SLA to be active. It is not just a condition that has to match at the start.

In Helsinki and later releases, two new fields have been introduced: **When to Cancel** and **Cancel Condition**. The feature was designed to provide better control when an SLA is canceled. For more information, see [SLA Conditions](https://docs.servicenow.com/csh?topicname=c_SLAConditions.html&version=latest "“When to Cancel” and “Cancel Condition”") in the product documentation.

![](https://support.servicenow.com/sys_attachment.do?sys_id=b5ae34a2db0ab450e515c22305961908) 

style="text-decoration: none;" name="4">

  

4\. What is the difference between actual elapsed time and business elapsed time?

* * *

The SLA Engine maintains two sets of elapsed timings on each Task SLA record. The **Actual** fields contain times that are always calculated on a 24/7 basis. These fields indicate the physical time that has elapsed since the Task SLA record was created. The **Business** fields contain the timings based on the schedule that is associated with the Task SLA record. Schedules define a set of working or business hours.

Elapsed time example:

![](https://support.servicenow.com/sys_attachment.do?sys_id=7dae34a2db0ab450e515c2230596192c)

On the Task SLA record above:

-   The SLA Definition named **Priority 1 resolution (8 hour)** is attached to the **Task INC0010001**.
-   A schedule named **8-5 weekdays** is associated with this Task SLA. Start time for this Task SLA is 7:30 AM. That is the time when the **Start Condition** defined on the SLA Definition matched with the field values on the Task record.
-   Actual elapsed time shows that 1 hour 5 minutes 5 seconds have elapsed. This is the physical time that has elapsed since the Task SLA record was attached to the task record.
-   Business elapsed time shows 35 minutes 5 seconds have elapsed. That is because the attached Schedule has business hours specified as 8AM to 5PM, so the system calculates **Business elapsed tim**e starting from 8AM onwards. 

**Note:** When there is no schedule associated with the Task SLA record:

-   For Fuji and earlier releases, the Business values are empty
-   For Geneva and later releases, a system property allows you to choose if you want to set the **Business** values to be the same as the **Actual**  
      
    ![](sys_attachment.do?sys_id=0eae34a2db0ab450e515c22305961971)

**Note:** If your Task SLA has the wrong schedule:

-   In Helsinki and later releases, check the setting of the **Schedule Source** field on the SLA Definition record.  This controls which schedule is attached to the Task SLA record.

  ![](sys_attachment.do?sys_id=42ae34a2db0ab450e515c22305961984)

-   In Fuji and earlier releases, go to the SLA Properties module and check the setting:

    **![](sys_attachment.do?sys_id=02ae34a2db0ab450e515c22305961992)** 

style="text-decoration: none;" name="5">

  

  

5. Why are the Actual elapsed time and Business elapsed time not correct on the task SLA record?

* * *

The timings and percentages on the Task SLA records are not calculated and updated on a continuous basis because it can impact performance. The SLA Engine takes a “just-in-time” approach to calculate and update these values, as needed.

These values are updated in the following scenarios:

-   When an update to the Task record results in a change of stage on the Task SLA record, for example, from **Paused** to **In Progress** or from **In Progress** to **Completed**.
-   When one of the base system SLA Update scheduled jobs run.  
    **Note:** Paused task SLAs are excluded as there is no time elapsing for these records.  
    These jobs run more frequently when the Task SLA gets closer to its breach time. For more information, see [Scheduled jobs for SLA](https://docs.servicenow.com/csh?topicname=c_ScheduledJobsForSLA.html&version=latest "Scheduled jobs for SLA") in the product documentation
-   If the system property glide.sla.calculate\_on\_display is set to true and the Task SLA record is viewed.

Fuji and earlier releases:

1.  In the Application Navigator, type **sys\_properties.list** in the **Filter navigator** text box and press enter or return on your keyboard.
2.  Search for the property glide.sla.calculate\_on\_display.   
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=92ae34a2db0ab450e515c223059619b0)

Geneva:

1.  Navigate to **Service Level Management > Properties > SLA Engine**.
2.  Check for the property **Recalculate Task SLA records when a task's form is displayed (ensures current Task SLA calculations when viewing a task, may increase form load time)**.   
      
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=9eae34a2db0ab450e515c223059619c9)

Helsinki and later releases:

1.  Navigate to **Service Level Management > Properties > SLA Engine**.
2.  Check for the property **Refresh Task SLAs when a Task form is displayed**.   
      
    ****![](https://support.servicenow.com/sys_attachment.do?sys_id=5aae34a2db0ab450e515c223059619d1)****

******Note******: When this property is enabled, the Task SLA calculations are refreshed as the form is loading.

-   When a user manually initiates the Refresh action on the Task SLA record.  
    ****  
    ![](https://support.servicenow.com/sys_attachment.do?sys_id=16ae34a2db0ab450e515c223059619d9)****

******Note******: In Fuji and earlier releases, this UI action was named Run SLA Calculation.

style="text-decoration: none;" name="6">

  

  

6. Why do task SLAs not get updated on refresh in Dashboards / Homepages / Reports?

* * *

The timings and percentages on the Task SLA records are not calculated nor updated on a continuous basis as it can create performance overhead in system. The SLA Engine takes a “just-in-time” approach to calculate and update these values, as needed. Therefore task SLAs data is not supposed to be updated when loaded in any kind of report that may be rendered in Homepages or Dashboards.

A common example that causes confusion is the Homepage refresh timing that can be set to an interval of 5, 15, 30, or 60 minutes (ref [here](https://docs.servicenow.com/csh?topicname=r_RefreshTheHomepage.html&version=latest "here")): the refresh timing of the Homepage is not going to calculate/update the task SLAs data in the database. That refresh action is just going to load again the data from the database in order to show a possible new update that has been submitted.

style="text-decoration: none;" name="7">

  

  

7\. Why do my users receive a notification that an SLA has reached a certain percentage when the task SLA record does not reflect this?

* * *

The workflow for each Task SLA record maintains its own set of values for determining how much time has elapsed. Workflow uses these values to trigger the notifications to users when an SLA has been in progress for the percentages specified in the [SLA Percentage Timer](https://docs.servicenow.com/csh?topicname=r_SLAPercentageTimer.html&version=latest "SLA Percentage Timer") workflow activities.

Workflow maintains its own calculation deliberately so it is not dependent on the values stored in the Task SLA record as these may not be up to date.

There is a known error for this issue which includes a workaround that can be viewed at [KB0563889](https://support.servicenow.com/kb_view.do?sysparm_article=KB0563889 "KB0563889").

**Note:** This issue has been fixed in Helsinki and later releases. The system now updates the Task SLA record whenever an SLA Percentage Timer activity in the workflow expires.

style="text-decoration: none;" name="8">

  

8\. What is the purpose of the “SLA Due”, “Made SLA” and "Escalation" fields on the Task record?

* * *

Prior to the introduction of the SLA Engine (in the "Fall 2010" release), SLAs were processed by the “Escalation” engine that allowed each Task record to be associated with a single SLA. The fields “SLA Due,” “Made SLA,” and "Escalation" were maintained by the Escalation engine. This legacy SLA engine is still the only one used in Express instances.

The modern SLA engine improves on the original by allowing multiple SLAs to be tracked against each Task record. Users can understand if a particular Task SLA record has breached by viewing the individual Task SLA records - for the 2010 engine the Stage field will show Breached and in the 2011 engine a new "Has breached" field is used.

The Escalation engine is still present and running in the system as it also supports Inactivity Monitors (click [here](http://docs.servicenow.com/csh?topicname=t_SetAnInactivityMonitor.html&version=latest "here") for more information on Inactivity Monitors), even if you are using the SLA plugins, and this server-side code might change the value of the made\_sla field when the task is closed.

If there are existing task records in the system that have the legacy SLA fields populated, they could be old records created in earlier releases. However, this does not impact the modern SLA engine in any way. The legacy fields can be ignored. Further, because the values may change unexpectedly, they are not intended for customer use.

If you still see new task records being created with values populated for these legacy fields, then you can check if they are intended to be used by verifying the System Property "com.snc.sla.run\_old\_sla\_engine" to check if your instance is still configured to use the legacy Escalation engine for Service Level Agreements. If the property is false, you know the fields are reserved (because they are manipulated by the system) but the contents are not relevant. You can also check the contents of the legacy Service Level Agreements definition table ("sysrule\_escalate"). Be aware that depending on how you access this table you might see both legacy SLA definitions and Inactivity Monitor definitions.

style="text-decoration: none;" name="9">

  

9\. What is the difference between the “Default” and “Simple” SLA condition rules?

* * *

SLA condition rules control how the conditions you define in an SLA definition are combined to determine if an SLA should attach, pause, complete, reattach, or cancel.  
For example, the Default SLA Condition rule will only attach a new SLA if the "Start condition" matches and the "Stop condition" does not match.

You can specify the condition rule to use on a per SLA Definition basis but you will need to add the "Condition type" field (which is a reference to the "SLA Condition rules" table) to the form:

![](sys_attachment.do?sys_id=22ae74a2db0ab450e515c22305961919)

If the “Condition type” is blank on an SLA Definition, the SLA Engine will look up the default SLA Condition Rule to use from system property “com.snc.sla.default\_conditionclass”.

There are two SLA Condition Rules available out-of-the-box - **Default** and **Simple**. The table below shows which conditions are checked when determining which actions to process for an SLA. The order the actions are listed in below is also the order the SLA engine evaluates them.

This is important to remember in the situation where the conditions for multiple actions have matched.  
For example the conditions for completing and cancelling an SLA have matched - in this case the SLA would be marked as completed as this is evaluated first.

<table style="height: 98px; padding-left: 30px; border-color: #000000;" border="1" width="973" cellpadding="10"><tbody><tr><td style="border-color: #000000;" rowspan="2"><br></td><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;" colspan="2"><span style="color: #909090;"><strong>Condition Rule</strong></span></td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;">&nbsp;<span style="color: #505050;"><strong>Default</strong></span></td><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><span style="color: #505050;"><strong>Simple</strong></span></td></tr><tr style="border-color: #000000;"><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;">&nbsp;<span style="color: #505050;"><strong>A new SLA will attach when...</strong></span></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Start condition matches<br>&nbsp;<em>and</em></li><li>Stop condition does not match</li></ul><p>For Helsinki or later instances, if:</p><p><img id="pasted_img_e9b5100e9b46e0e9b9850e9b45e0e9b1" src="sys_attachment.do?sys_id=a2ae74a2db0ab450e515c22305961941" alt="" width="332" height="56"></p><p>has been selected on the SLA Definition then in the addition to the above:</p><ul style="list-style-type: disc;"><li>Cancel condition does not match</li></ul></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Start condition matches</li></ul><p><strong><em>Note:</em></strong> for Helsinki or later instances, the new Cancel condition&nbsp;<em>cannot&nbsp;</em>be used with the <strong>Simple</strong> SLA Condition Rule</p></td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><strong style="color: #505050;">A new SLA will stop (complete)&nbsp;when...</strong></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Stop&nbsp;condition matches</li></ul></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Stop&nbsp;condition matches</li></ul></td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><strong style="color: #505050;">An SLA will reattach (reset) when...</strong></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Reset&nbsp;condition&nbsp;matches<br><em>and</em></li><li>Start condition matches</li></ul></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Reset&nbsp;condition&nbsp;matches</li></ul></td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><strong style="color: #505050;">An SLA will cancel when...</strong></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Stop condition&nbsp;does not match<br>&nbsp;<em>and</em></li><li>Start condition does not match</li></ul><p>For Helsinki or later instances, the option selected in "When to cancel" determines what conditions will result in the SLA being cancelled:</p><table style="border-color: #000000;" border="1"><tbody><tr><td style="border-color: #000000;"><strong>Start conditions are not met</strong>&nbsp;</td><td style="border-color: #000000; vertical-align: middle;"><ul style="list-style-type: disc;"><li>Stop condition&nbsp;does not match<br>&nbsp;<em>and</em></li><li>Start condition does not match</li></ul></td></tr><tr><td style="border-color: #000000;"><strong>Never</strong>&nbsp;</td><td style="border-color: #000000;"><em>No conditions checked as SLA cannot cancel</em></td></tr><tr><td style="border-color: #000000;"><strong>Cancel conditions are met</strong></td><td style="border-color: #000000;">&nbsp;<ul style="list-style-type: disc;"><li>Cancel condition matches</li></ul></td></tr></tbody></table></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Stop condition&nbsp;does not match<br>&nbsp;<em>and</em></li><li>Start condition does not match<br><em>and</em></li><li>Pause condition does not match</li></ul><p><strong><em>Note:</em></strong>&nbsp;for Helsinki or later instances, the new options of never cancelling or matching with a defined Cancel condition cannot be used with the <strong>Simple</strong> SLA Condition Rule</p>&nbsp;<img id="pasted_img_47bc5fc047bcd09047bc47c047bc9ea0" src="sys_attachment.do?sys_id=eeae74a2db0ab450e515c22305961946" alt="" width="346" height="80"></td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><strong style="color: #505050;">An SLA will pause when...</strong></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Pause&nbsp;condition&nbsp;matches</li></ul><p>For Helsinki or later instances, if:</p><p><img id="pasted_img_b147a0b1bd30b1b780b18d50b17500b1" src="sys_attachment.do?sys_id=aaae74a2db0ab450e515c2230596194e" alt="" width="335" height="52"></p><p>has been selected on the SLA Definition then in addition to the above:</p><ul style="list-style-type: disc;"><li>Resume&nbsp;condition does not match</li></ul><p><br></p></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Pause&nbsp;condition&nbsp;matches</li></ul><p><em><strong>Note:</strong></em> for Helsinki or later instances, the new Resume condition cannot be used with the <strong>Simple</strong> SLA Condition Rule</p>&nbsp;</td></tr><tr><td style="background-color: #f2f2f2; border-color: #000000; text-align: center;"><strong style="color: #505050;">An SLA will resume when...</strong></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Pause&nbsp;condition&nbsp;does not match</li></ul><p>For Helsinki or later instances, if:</p><p><img id="pasted_img_b147a0b1bd30b1b780b18d50b17500b1" src="sys_attachment.do?sys_id=e6ae74a2db0ab450e515c22305961954" alt="" width="335" height="52"></p><p>has been selected on the SLA Definition then in addition to the above:</p><ul style="list-style-type: disc;"><li>Resume&nbsp;condition matches</li></ul></td><td style="border-color: #000000;"><ul style="list-style-type: disc;"><li>Pause&nbsp;condition does not match</li></ul><p><em><strong>Note:</strong></em> for Helsinki or later instances, the new Resume condition cannot be used with the <strong>Simple</strong> SLA Condition Rule</p>&nbsp;</td></tr></tbody></table>

If the out-of-the-box condition rules do not provide the SLA processing required for your instance, it is possible to create your own condition class (script include) and SLA condition rule record.

For more information on this see the online help topic [Extend SLA condition rules](https://docs.servicenow.com/bundle/helsinki-it-service-management/page/product/service-level-management/concept/c_ExtendSLAConditionRules.html "Extend SLA condition rules").

style="text-decoration: none;" name="10">

  

10\. How can I define an SLA that has a Breach time (Planned end time) that is for a user defined time?

* * *

It is possible to have an SLA Definition that creates Task SLA’s with a Breach time based on a date/time taken from the Task – for example the Due Date field which is available on all Task types.

This can be achieved by creating a Relative Duration which allows you to run a script to determine the SLA’s Breach time. You can then select this Relative Duration when defining your SLA Definition to replace the default User defined duration. The Duration always needs to return a static value, it cannot use gs.now or similar functions for calculations.

**NOTE:** Pause conditions are not supported for relative durations as these are viewed as providing a fixed date/time when the SLA should be met and as such the Breach time should not change.

You can create a new Relative Duration record by going to the Relative Durations module. An example of a script that would set the Breach time on the SLA to the date/time in the Due date field from the Task is:

/\* This relative duration script will set the Breach Time of the Task SLA to the value in the "Due date" of the Task. 
 
 
   If the "Due date" field is available on the Task form and editable then this effectively allows the user to specify the 
   Breach Time of the SLA. 
    
   If the Due Date field is empty or in the past, the script will instead set the Breach Time of the SLA to 1 second 
   after the Start time 
\*/  
  
(function() {  
  var startDateMs = calculator.startDateTime.getNumericValue();  
  var dueDate;  
  
  // Work out if "current" is a Task record or Task SLA and then get the "due\_date" element from the Task  
  var tableName = current.getTableName();  
  if (tableName) {  
       var baseTableName = GlideDBObjectManager.getAbsoluteBase(tableName);  
       if (baseTableName == "task")  
            dueDate = current.getElement("due\_date");  
       else if (baseTableName == "task\_sla")  
            dueDate = current.getElement("task.due\_date");  
  }  
  
  // if we've got a "due\_date" and it's after our SLA's Start time then use it  
  // otherwise we'll have to default to the same as Start Time plus 1 second (i.e. instant breach of SLA)  
  if (dueDate && !dueDate.nil() && dueDate.dateNumericValue() > startDateMs)  
       dueDate = dueDate.getGlideObject();  
  else {  
       dueDate = new GlideDateTime(calculator.startDateTime);  
       dueDate.addSeconds(1);  
  }  
  
  // if we have a schedule then check if the Due Date is in it and if it isn't  
  // find the next time we are in the schedule  
  if (calculator.schedule && !calculator.schedule.isInSchedule(dueDate))  
       dueDate.add(calculator.schedule.whenNext(dueDate, calculator.timezone));  
  
  // set the endDateTime property of the calculator object to dueDate  
  calculator.endDateTime = dueDate;  
  calculator.calcScheduleDuration();  
})();
    

The example above includes defaulting Breach Time on the SLA to 1 second after the Start Time if the Due Date is empty or in the past.  
If you created the example above with a name of **Breach on Due Date** then you would select this in an SLA Definition as shown below:

![](sys_attachment.do?sys_id=a2ae74a2db0ab450e515c2230596195a)

style="text-decoration: none;" name="11">

  

11\. Why do task SLAs not get updated when modifying records referenced via dot-walking in a condition of the SLA Definition?

* * *

Dot-walking allows to navigate to fields of another table via reference field; dot-walking is available in all the conditions of the SLA Definition.

A reason of confusion is often given by the expectation of getting the Task SLAs fields refreshed when a referenced record is modified.

The SLA Engine is triggered via the Business Rule named “Run SLAs” which runs for the Task table (and so, for any extending tables such as Incident, Problem etc.) on Insert and Update. Moreover, the execution of the SLA Engine against a specific record will check only SLA Definitions configured to run against the table of that record.

This means that modifications (or submission) of the Incident record will trigger the execution of the SLA Engine which will only check SLA Definitions against the Incident table. In the same way, modification of the User (or Group) record will just trigger the SLA Engine for that User (or Group) table and not for any other table.

Example: Let us assume to have the SLA Definition (named "Fred Luddy's group resolution") configured to run against the Incident table. Start condition is shown below:

![](/sys_attachment.do?sys_id=faae74a2db0ab450e515c22305961977)

  

As noticeable, the last portion of the query in the condition uses dot-walking (Assignment Group.Manager).

Now, take the case represented by the below two steps:

1.  The Incident INC0000001 is submitted and all the fields match the above conditions except Assignment Group.Manager which is Beth Anglin at this time. 
2.  The admin navigates to the Database group record and modifies the Manager field to be Fred Luddy.

When the step 2. is performed, the SLA engine does not run against the Incident table, resulting in not attaching the Task SLA "Fred Luddy's group resolution" to INC0000001.

That modification on the Database group will not trigger the execution of the SLA Engine against INC0000001 because Database is a record in the Group table while INC0000001 is in a different table (Incident).

**Possible workaround**:

As workaround for this behavior, you can try to manually trigger the SLA Engine to run against the records where current is set as referenced field.

To apply the workaround in the above example, write a Business Rule on the Group table, tick the flags Update and Advanced, and add the below script:

(function executeRule(current, previous /\*null when async\*/) {
	var grInc = new GlideRecord("incident");
	grInc.addQuery("assignment\_group", current.getUniqueValue());
	grInc.query();

	while (grInc.next())
		new TaskSLAController.run(grInc);
})(current, previous);

**Workaround implication**:

This workaround might cause low performances when modifying records of the table that the Business Rule runs against (Group table in the above example), since it may run on a huge amount of records. E.g. if Database is set as the Assignment Group of 1000 Incidents then the SLA Engine will run against all of them.

ServiceNow recommends to apply that workaround carefully and only if it is really needed.

A potential improvement of the above script, according to the provided example, is applying to the GlideRecord object all the query conditions configured in the SLA Definition:

(function executeRule(current, previous /\*null when async\*/) {
	var serviceNowCompanySysId = "012345678910111213141516171819202122";
	var newStateValue = 1;
	var grInc = new GlideRecord("incident");
	grInc.addActiveQuery();
	grInc.addQuery("priority", 1);
	grInc.addQuery("company", serviceNowCompanySysId);
	grInc.addQuery("state", newStateValue);
	grInc.addQuery("assignment\_group", current.getUniqueValue());
	grInc.query();

	while (grInc.next())
		new TaskSLAController.run(grInc);
})(current, previous);

**Note**: The above code tries to reduce the amount of incidents to run the SLA Engine against, however the data being processed might still be excessive.

  

### Related Links

[Service Level Management (SLA) Resources](https://support.servicenow.com/kb_view.do?sysparm_article=KB0623502 "Service Level Management (SLA) Resources")

[Service Level Agreements (SLA) FAQs](https://community.servicenow.com/docs/DOC-5853 "Service Level Agreements (SLA) FAQs")
