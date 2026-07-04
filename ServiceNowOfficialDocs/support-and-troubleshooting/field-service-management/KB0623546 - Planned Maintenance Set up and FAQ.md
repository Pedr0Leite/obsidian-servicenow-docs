---
title: "Planned Maintenance Set up and FAQ"
aliases:
  - KB0623546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623546
kb_number: KB0623546
last_modified: 2024-04-07
---

## Issue

The Planned Maintenance application works with SM applications to help organizations manage regular, preventive maintenance of their assets.

Maintenance plans are used by applications to trigger the automatic creation of work orders or facilities requests. These work orders and facilities requests define how to perform maintenance on devices and vehicles, or just about any type of asset that requires maintenance. Work orders and requests can be based on a specific time interval, such as after a specified number of months since the previous maintenance was performed, or they can be based on meters or usage. 

  

## Resolution

To set up Planned Maintenance:

1.  Activate the plugin named SM Planned Maintenance.
2.  Navigate to Maintenance Plans.
3.  Create a maintenance plan.
4.  Define a maintenance schedule.
5.  Associate a maintenance plan to filtered records.
6.  Associate a schedule template to matching records.
7.  Run a scheduled job to execute a maintenance schedule.

For a detailed flowchart about setting up Planned Maintenance, see [Planned Maintenance Setup](https://servicenow.box.com/s/1hszxk06j1aoqxhhuhjxpv9hzhqjqyv1 "Planned Maintenance Setup").

  

For a detailed flowchart about Planned Maintenance work order created, see [Planned Maintenance Execution](https://servicenow.box.com/s/cbxzzzjj0r2u65jjzl5dminsv07cqzk8 "Planned Maintenance Execution").

  

The two flowcharts are also attached to this article. 

  

New properties for Planned Maintenance

* * *

We introduced 2 properties as part of this release:

-   **planned\_maintenance.fixed\_interval**

Use this property to setup duration Maintenance Schedules in fixed intervals.

False: Both the nightly schedule and the last work order completion will update Requested Due date and Next run time values for duration and duration or meter(just the duration part) schedules.

True: Only nightly schedule will update the next run values of Requested Due date and Next run time values for meter and duration or meter schedules.

-   **planned\_maintenance.fixed\_meter**

Use this property to have fixed count change for Meter Maintenance Schedules.

False: Both the nightly schedule and the last work order completion will update the next run values for "meter” and “duration or meter” (just the meter part) schedules.

True: Only nightly schedule will update the next run values the next run values for meter and duration or meter schedules.

 

FAQs

* * *

**Q: I have set up maintenance plan and maintenance schedule, however I do not see maintenance plan records created for assets?**

            Click on related link of Maintenance schedule - Associate schedule with filtered records.

**Q: Maintenance plan record has next run time in past. I still see no work orders or facilities request created.**

            Determine if the nightly scheduled job named 'Planned Maintenance Nightly Run' is active.

**Q: Maintenance plan records has next run time in past and also the nightly schedule job is active and running. However, I did not see work orders or facilities requests created?**

            Check if Schedule templates are set up for the maintenance schedule.

**Q: Can there be more than one schedule template associated with Maintenance Schedule?**

            Yes, each schedule can be associated with more than one schedule template.

**Q: What is the behavior if there is more than one schedule template associated?**

            When the nightly scheduled job picks up a maintenance plan record to create work orders, it creates one work order for each template associated with the Maintenance Schedule. 

**Q: When do I use model-based Maintenance Plan?**

            Select type of Maintenance Plan as 'Model Based' to base the maintenance plan on a specified model of a CI, such as a product model.

**Q: What task creation policies are available?**           

-   Leave alone: Do not allow the creation of new tasks or the deletion of existing ones.
-   Cancel existing: Allow tasks currently associated with the plan to be deleted.
-   Add to existing: Allow new tasks, along with existing active tasks, to be added to maintenance plans.

**Q: How do I determine work orders/ Facilities requests created by specific Maintenance Plan/ Maintenance Schedule?**

            Go to Work Orders or Facility request list view and filter records using Maintenance plan or Maintenance Schedule fields.

**Q: What is lead time?**

            It is the number of days prior to the Requested Due by date to determine the date on which work should begin. 

**Q: Is asset stored in work orders or facilities request when it is created?**

            Yes. If the base table of the table associated with Maintenance plan is asset (alm\_asset), then asset field of order is populated by the scheduler.
