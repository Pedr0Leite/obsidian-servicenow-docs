---
title: "Troubleshooting Service Level Agreements (SLA)"
aliases:
  - KB0523638
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523638
kb_number: KB0523638
last_modified: 2026-06-03
---

## Troubleshooting Service Level Agreements (SLA)

  

### Issue

Use the information in this article to take some initial troubleshooting steps and to understand several common SLA issues.

Here are some initial steps to follow when troubleshooting SLA issues.  
  

1.  Identify the SLA engine version that is running. There have been three major versions of the SLA engine:
    
    <table class="internalTable" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>SLA engine version</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">The version that hinged on the Escalation Engine. (pre-2010)</td><td style="vertical-align: middle; text-align: left;">Workflow-based, with much logic in a single large business rule, "Process SLAs"</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">The SLA Plugin (aka the 2010 engine)</td><td style="vertical-align: middle; text-align: left;">Run by Business Rules, Script Includes, and Scheduled Jobs; relegating the workflow to handle only notifications)</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">The 2011 engine (available in the&nbsp;<em>June 2011</em> version)</td><td style="vertical-align: middle; text-align: left;">A Major Revision of the "New" SLA engine (i.e. Iteration 2). which pulls much of the functionality that was previously spread out into a single extensible Script Include.</td></tr></tbody></table>
    
    See the ServiceNow product documentation for more information about the process of [moving from the 2010 Engine to the 2011 Engine.](https://docs.servicenow.com/csh?topicname=t_MoveFromThe2010ToThe2011Engine.html&version=latest "moving from the 2010 Engine to the 2011 Engine.") 
    
     **Note:** Fixing for the 2010 engine allows compatibility with the 2011 engine. (The 2011 engine has been designed to simply switch back/forth between 2010 and 2011 depending on a single sys\_properties boolean flag called com.snc.sla.engine.version.) There are multiple known errors on the 2010 SLA engine; we recommend migrating to the new engine.
    
2.  Identify the likely SLA component(s). After analyzing the unexpected behavior reported by the customer and confirming that you understand their expectations, determine the component that controls the reported SLA behavior - see [Installed with Service Level Management](https://docs.servicenow.com/csh?topicname=r_InstalledWithServiceLevelMgmt.html&version=latest "Installed with Service Level Management").
3.  Inspect examples.  
      
    -   Create a timeline using the SLA Desk check script
    -   Use the example that the customer has provided and confirm if the behavior they are seeing is unexpected or not
    -   If you need more information about SLAs, see [KB0529411: How the 2011 SLA Engine Really Works](/kb_view.do?sysparm_article=KB0529411 "KB0529411: How the 2011 SLA Engine Really Works")

### Resolution

Here are some common areas of confusion.

**No SLA is created if the technician closed the task in the same step in which it was created**

This is normal behavior, but there are some workarounds. If you use a Case process of Create > Resolve > Close _after a period of time,_ then the system creates the SLAs and they are marked **Achieved/Complete** with 0% elapsed percentage. This works because you pause the SLA immediately on **Resolve** and the **Close** is a separate update of the Case record.

You can also use existing tools and the **Simple** SLA condition type. This is because otherwise the SLA will not be attached in the first place.

-   Condition type: Simple
-   Start condition: (Whatever is required)
-   Stop Condition: (Whatever is required)

 **Note:** If you use "Simple," be careful that you do not attach another copy of the SLA on a subsequent case update when you meet its Stop condition a previous time around (easy to do if the Stop condition contains all the "terminal" states).

**Explanation of SLA calculations**

SLAs (task\_sla table) only calculate at certain times, not on the fly. For more information, see [SLA Calculation](https://docs.servicenow.com/csh?topicname=r_SLAAutomation.html&version=latest "SLA Calculation") in the product documentation.

SLAs are calculated and assessed by a business rule and a group of scheduled jobs (see below). The business rule is triggered when a task is updated, created, or deleted. The scheduled jobs run in the background at set intervals.

The asynchronous business rule named Process SLAs runs after every task is inserted or modified and evaluates the Start, Pause, and End conditions for the SLA.

SLA calculations are now updated based on when they are breached. These occur on the following Schedule Jobs (on the sys\_trigger table):

-   SLA update (already breached): repeats every day 
-   SLA update (breach after 30 days): repeats every 5 days 
-   SLA update (breach within 1 day): repeats every hour 
-   SLA update (breach within 1 hour): repeats every 10 minutes 
-   SLA update (breach within 10 min): repeats every 1 minute 
-   SLA update (breach within 30 days): repeats every day

 **Warning:** The mechanisms that control SLA workflow and SLA automation are completely independent of each other. Many customers have a requirement to send out email notification from the SLA worklfow showing the current elapsed percentage of the SLA. However, this does not work because using any field on the task\_sla table only displays the most recently updated value of that field. The result is that inaccurate values are sent out in the email. One solution is to hard code the desired elapsed percentage into SLA notifications by using notifications for each percentage level. For example, if you want an email to fire when the SLA has reached 75% elapsed, then you create an email notification for "75 percent SLA Warning" and use a special event to trigger that notification. The event can be called "sla.warning.75". You can specify the name of the event you want to trigger by using a Create Event workflow activity. A second solution is to call the code directly that would update the SLA before sending the notification. Use code similar to the "Run SLA Calculation" UI action.

  

 **Warning:** If you turn on the calculate SLA's on display property (glide.sla.calculate\_on\_display) then SLAs are also calculated when a user views the case form. SLAs are NOT updated when a user runs a report, looks at the case in a list, or when a notification accesses a task\_sla record through script. If Calculate On Display is turned on, the SLA updates when a user looks at the task (case, change\_request, sc\_request...) form. There is no way to have SLAs always calculate whenever they are needed - for performance reasons it is not feasible. The Calculate On Display property is turned off for your instance by default. This means that the business elapsed time and all other calculated fields only represent the values from the last time the SLA was calculated.

### Explanation of SLA definition duration field

When defining an SLA, the **Duration** field, in coordination with the **Schedule** field, is critical. The number of days specified in this field are converted into 24 hours. For example, if a schedule is used that has eight hour days, the duration 1 Day sets the SLA to breach three business days later.

Or say, for example, you select a five day two hour duration and a 9-5 schedule. The five days and two hours are considered 122 hours (5x24 + 2). The 122 hours are distributed across the 9-5 schedule at eight hours per day resulting in 15.25 schedule days (122/8 = 15.25). For more information, see [SLA Definition](https://docs.servicenow.com/csh?topicname=c_SLADefinitions.html&version=latest "SLA Definition").   
  

**Explanation of SLA actual percentage and business percentage**

The Actual Percentage and Business Percentage are not necessarily the same at any given point in time. However, when Business Duration reaches 100%, then Actual Percentage should also be 100%. The reason is because the only difference between the two is that one considers the schedule and one does not. For example, consider the following situation. You have a schedule with only one hour of scheduled time every day from 8AM to 9AM.The SLA has a total duration of two hours. Suppose that the SLA begins at 8:15 AM during the scheduled time. By 8:45 AM, 30 minutes have elapsed. 30 minutes would account for 25% of the total business duration (for example, 2 hours / 30 minutes). However Actual duration in this case would come out to be 48 hours since the planned end time will be at 8:15 AM, 2 days after the start time. 30 minutes of 48 hours is only 1% of Actual Percentage elapsed.  
  

**Explanation of SLA Time Left field and pause time**

The **Task SLA.Time Left** field keeps counting down while an SLA is paused. The **Task SLA.Actual Percentage** field, however, should still take pause time \[Task SLA.Pause Duration\] into consideration. You could write out the formula like this:   
  
\[Derived End Date\] = \[Pause Duration\] + \[SLA Definition.Duration\]  
\[Time Left\] = \[Derived End Date\] - \[Now\]

You can see the code that handles this in the script include named SLACalculatorNG:

var dc = this.\_newDurationCalculator(sla, newTaskSLA.sla\_duration + newTaskSLA.business\_pause\_duration);  
...  
var timeLeftMS = currentSLA.derived\_end\_time - nowMS;

The confusion occurs because Pause Duration is not calculated until a task SLA comes out of the Paused state, for example:

-   SLA Duration: 8 hours 
-   At 10:00 AM - Case & SLA are created 
-   At 11:00 AM - SLA is paused (1 hour elapsed, Pause Duration = 0)  
    -   0 + 8 - 1 = 7 hours Time Left
-   At 12:00 AM - SLA is calculated (2 hours elapsed, Pause Duration is STILL 0)  
    -   0 + 8 - 2 = 6 hours Time Left  
        
-   At 1:00 PM - SLA moves out of Pause to something else (3 hours elapsed, Pause Duration gets calculated. Now it's 2 hours)  
    -   2 + 8 - 3 = 7 hours Time Left  
        

### Related Links

-   [Understanding SLA Conditions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547356 "Understanding SLA Conditions")
-   [SLA elapsed time measures](https://docs.servicenow.com/csh?topicname=r_ElapsedTimeCounting.html&version=latest "SLA elapsed time measures")
