---
title: "Project Scheduling Engine"
aliases:
  - KB0552065
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552065
kb_number: KB0552065
last_modified: 2025-10-06
---

## Project Scheduling Engine

  

### Issue

**Overview:**

This article describes the behavior of the Project Scheduling Engine in the Fuji and Eureka releases. This article covers the following topics: 

-   Project Schedule
-   Time Constraints
-   Dates and Duration
-   Relations

All examples in this article assume that you are using the base Project Management Schedule.

  
  

### Resolution

**Project schedule**

In ServiceNow, schedules are rules that include or exclude time for various actions or tasks. The Project Management application ships with a schedule **Project Management Schedule**, that specifies a 40-hour workweek.

The durations specified in projects and project tasks take the schedule into consideration. So, for instance, a task planned duration of 1-day means 8 hours of work. Conversely, if you create a task with 8 hours of duration, it would be saved as a 1-day task.

To understand this behavior, consider the following examples:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Input duration</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Eventual duration (after recalculations for the schedule)</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">8 hours</td><td style="vertical-align: middle; text-align: left;">1 day</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">12 hours</td><td style="vertical-align: middle; text-align: left;">1 day and 4 hours</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">1 day and 8 hours</td><td style="vertical-align: middle; text-align: left;">2 days</td></tr></tbody></table>

The project schedule engine always computes a duration based on the schedule specified in the Project record rather than the value in the **Planned duration** field.  

Also, consider the schedule entries associated with the schedule. For example, the Project Management schedule that we ship has two schedule entries:

-   Monday-Friday 8AM-12PM
-   Monday-Friday 1PM-5PM

This has an impact on the end date calculation of a task given its start date and duration. Consider the following examples: 

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>#</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Duration</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned End</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">1</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-08 08:00:00</span></td><td style="vertical-align: middle; text-align: left;">1 day</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-08 17:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">2</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-08 08:00:0</span></td><td style="vertical-align: middle; text-align: left;">5 hours&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-08 14:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">3</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-11 08:00:00</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;">2 days&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: -webkit-left;">2015-09-14 17:00:00</span>&nbsp;</td></tr></tbody></table>

For #1, we have a task with a duration of one day. It starts at 8AM on a workday and ends at 5PM on the same day.

For #2, we have a task with a duration of five hours. It starts at 8AM, but the end is set to 2pm instead of 1pm, because the schedule specifies a break from 12PM to 1PM. 

For #3, we have a task with a duration of 2 days. It starts on a Friday, so the end date is set for the _Monday_ of the following week. The schedule specifies Saturday and Sunday as holidays, so these days are not included in the workweek.

**Time constraints**

A time constraint is a restriction on a project task that determines when the project should start. The following two types of time constraints are supported: 

-   Start ASAP: the task is set to start ASAP
-   Start on a specific date: the task is set to start on a specific date

The following examples explain how time constraints affect the start dates of tasks. 

Consider the following project structure:  

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>#</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Parent</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">1</td><td style="vertical-align: middle; text-align: left;">Project</td><td style="vertical-align: middle; text-align: left;"><br></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span></td><td style="vertical-align: middle; text-align: left;"><br></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">1.1</td><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;">Project&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">1.2</td><td style="vertical-align: middle; text-align: left;">Task 2</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start on</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 08:00:00</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;">Project&nbsp;</td></tr></tbody></table>

 Then, the following scenarios demonstrate how time constraints affect the derivations of the planned start dates:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Parent</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 3</td><td style="vertical-align: middle; text-align: left;">Project</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 4</td><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 5</td><td style="vertical-align: middle; text-align: left;">Task 2</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 08:00:00</span>&nbsp;</td></tr></tbody></table>

When Task 3 is added under Project with the time constraint Start ASAP, the planned start date of Project is set as the planned start date of Task 3.

When Task 4 is added under Task 1 with the time constraint Start ASAP, the planned start date of Task 1 is set as the planned start date of Task 4..

When Task 5 is added under Task 2 with the time constraint Start ASAP, the planned start date of Task 2 is set as the planned start date of Task 5, because that is the earliest that Task 5 can start. 

If a task is created at any level with the time constraint Start on, the planned start date of the task can be set to anything on or after the Project start date. For example, in the project structure above, you cannot add a task with the time constraint Start on and the planned start earlier than 2015-09-08 08:00:00.

  

**Automatic change of time constraint on a task**

When child tasks are added to a task in a project, the time constraint of the task becoming parent is automatically set to Start on a specific date. In the above example, when Task 4 is added to Task 1, time constraint of Task 1 is changed from ASAP to specific and then the Task 1 Start date cannot be changed. To understand the behavior, consider the following example.

Consider a Task with the time constraint Start ASAP:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task</td><td style="vertical-align: middle; text-align: left;">Start ASAP</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span></td></tr></tbody></table>

Consider adding the following task Task 1 as a child task to Task:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Parent</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;">Task</td><td style="vertical-align: middle; text-align: left;">Start ASAP</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span></td></tr></tbody></table>

Then, Task is modified as follows (the time constraint is changed): 

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Contraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task</td><td style="vertical-align: middle; text-align: left;">Start on</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-08 08:00:00</span>&nbsp;</td></tr></tbody></table>

Consider adding the following task Task 2 with the time constraint Start on as a child task to Task:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Parent</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Task 2</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Task</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start on</span></td><td style="vertical-align: middle; text-align: left;">&nbsp;<span style="text-align: start;">2015-09-06 08:00:00</span></td></tr></tbody></table>

Then, Task is modified as follows (planned start date is changed):

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task</td><td style="vertical-align: middle; text-align: left;">Start on</td><td style="vertical-align: middle; text-align: left;">2015-09-06 08:00:00</td></tr></tbody></table>

  

**Dates and duration**

We have two sets of dates in Project and Project Tasks. First is the planned start date and planned end date Second is the actual start date and actual end date. Depending on the state of the project and task, the planned or actual values are populated.

  

Planned start date The following table includes different scenarios for the setting of default start dates for a project and its tasks:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Scenario</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start Date</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Project is created</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">The default start date of the project is 08:00: &nbsp;00AM on the next working day</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Task is created with with the time constraint Start ASAP</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">The default start date of the task is the same &nbsp;as the start date of the project</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Sub-task is created with the time constraint Start ASAP</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">The default start date of the sub-task is the same as the start date of the parent task</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start date of sub-task is changed</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">The start date of the parent task is changed to the start date of the sub-task</span></td></tr></tbody></table>

  

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;<span style="text-align: start;">If a task has multiple sub-tasks, the start date of the task is the same as the earliest start date of the child tasks.</span></td></tr></tbody></table>

  

Planned start date of a project or a task can be modified if the project or the task does not have any children. If a project or a task has children, the earliest planned start date of the children is set as the planned start date of the project or the task.

  

Planned end date For a project or for a task in the project, the planned end date is calculated using the following formula:

Planned End Date = Planned Start Date + Planned Duration

This formula is applicable only when the task or the project is in the pending or the open state. When the task moves to the work in progress state, the actual start date is populated. For a task that is in the work in progress or the closed state, the planned end date is calculated using the following formula:

Planned End Date = Actual Start Date + Planned Duration

The planned end date of a project or a task can be modified if the project or the task does not have any children. If a project or a task has children, the latest planned end date of the children is set as the planned end date of the project or the task.

  

**Actual start date**

When the state of a project or a task changes to the work in progress state, the current time is set as the actual start date of the project or the task. The actual start date can be edited and set to a new value until the task remains in the work in progress state.

The actual start date of a project or a task can be modified if the project or the task does not have any children. If a project or a task has children, the earliest actual start date of the children is set as the actual start date of the project or the task.

  

Actual end date When the state of a project or a task changes to the closed state, the current time is set as the actual end date of the project or the task. The actual end date can be edited and set to a new value until the task remains in a closed state. The actual end date is calculated using the following formula:

Actual End Date = Actual Start Date + Actual Duration The actual end date of a project or a task can be modified if the project or the task does not have any children. If a project or a task has children, the latest actual end date of the children is set as the actual end date of the project or the task.

  

**Planned duration**

Planned duration is calculated using the following formula:

Planned Duration = Planned End Date – Planned Start Date 

Any change in the planned duration of a task affects the planned end date of the task. The planned duration of a project or a task can be modified if the project or the task does not have any children.

Here is the impact of editing each of those dates and duration fields for various task states:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task State</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Edit Field</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Field Recalculated</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Pending/Open</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned Start Date</span></td><td style="vertical-align: middle; text-align: left;">Planned End Date<p style="text-align: start;">(Planned Start Date + Planned Duration)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Pending/Open</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned End Date</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned Duration</p><p style="text-align: start;">(Planned End Date - Planned Start Date)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Pending/Open</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned Duration</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned End Date</p><p style="text-align: start;">(Planned Start Date + Planned Duration)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Work in progress/Closed</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned Start Date</span></td><td style="vertical-align: middle; text-align: left;">No impact&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Work in progress/Closed</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned End Date</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned Duration</p><p style="text-align: start;">(Planned End Date - Actual Start Date)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Work in progress/Closed</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Planned Duration</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned End Date</p><p style="text-align: start;">(Actual Start Date + Planned Duration)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Work in progress</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Actual Start Date</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned End Date</p><p style="text-align: start;">(Actual Start Date + Planned Duration)</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Closed</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Actual Start Date</span></td><td style="vertical-align: middle; text-align: left;"><p style="text-align: start;">Planned End Date</p><p style="text-align: start;">(Actual Start Date + Planned Duration)</p></td></tr></tbody></table>

**Task relationships**

Project Management supports one type of relationship between tasks: **Finish-to-Start**.

Consider these tasks:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start Date</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned End Date</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Task 1</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 08:00:00</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 17:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Task 2</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">Start ASAP</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-01 08:00:00</span>&nbsp;</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-01 17:00:00</span>&nbsp;</td></tr></tbody></table>

 Adding a relation from Task 1 to Task 2, which makes Task 2 the successor in the relationship, recalculates Task 2’s planned dates as follows:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Dependency</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Contraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start Date</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned End Date</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;"><br></td><td style="vertical-align: middle; text-align: left;">Start ASAP</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 08:00:00</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 17:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 2</td><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;">Start ASAP</td><td style="vertical-align: middle; text-align: left;">2015-09-11 08:00:00&nbsp;</td><td style="vertical-align: middle; text-align: left;">2015-09-11 17:00:00&nbsp;</td></tr></tbody></table>

  
If Task 2 has a **Start on** time constraint instead of a **Start ASAP** time constraint, Task 2’s planned dates do not change:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Task</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Time Constraint</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned Start Date</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Planned End Date</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 1</td><td style="vertical-align: middle; text-align: left;">Start ASAP</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 08:00:00</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-10 17:00:00</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Task 2</td><td style="vertical-align: middle; text-align: left;">Start on</td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-01 08:00:00</span></td><td style="vertical-align: middle; text-align: left;"><span style="text-align: start;">2015-09-01 17:00:00</span>&nbsp;</td></tr></tbody></table>
