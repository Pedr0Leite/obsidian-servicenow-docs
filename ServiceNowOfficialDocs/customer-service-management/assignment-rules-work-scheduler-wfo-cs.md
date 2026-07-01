---
title: Create a criteria for a matching rule in Work scheduler
description: Add a criteria for a matching rule to enable assignment of work items to team members based on the rule.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/assignment-rules-work-scheduler-wfo-cs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Assigning work using Work Scheduler, Workforce Optimization for Customer Service, Agent management, Use, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a criteria for a matching rule in Work scheduler

Add a criteria for a matching rule to enable assignment of work items to team members based on the rule.

## Before you begin

Role required: admin

## About this task

The following matching [[gamification-components-rules|rules]], which are available by default, are based on the selection criteria matching type:

|Rule name|Work configuration name|Table|UX app route|
|---------|-----------------------|-----|------------|
|Incident Matching rule|Incidents|Incident \[incident\]|Incident|
|Problem Matching rule|Problems|Problem \[problem\]|Problem|
|Requested item Matching rule|Requested items|Requested Item \[sc\_req\_item\]|Requested item|
|Request Matching rule|Requests|Request \[sc\_request\]|Request|
|Catalog Task Matching rule|Catalog Task|Catalog Task \[sc\_task\]|Catalog task|
|Change Request Matching rule|Change Request|Change Request \[change\_request\]|Change requests|
|Change Task Matching rule|Change Task|Change Task \[change\_task\]|Change task|

For information on how matching criteria works, see [[work-items-assignment-matching-criteria-wfo-cs|Matching criteria for work items in Work scheduler]].

The following four criteria are available by default:

-   WFO-[[mandatory-skills|Mandatory skills]]
-   WFO-Availability
-   WFO-Optional skills
-   WFO-Timezone overlap

## Procedure

1.  Navigate to **All** &gt; **Work scheduler** &gt; **Matching Rules**.

2.  In the Matching Rules list, select a matching rule; for example, the **Incident matching rule**.

3.  In the Select Criteria related list, select **New.**

4.  Fill in the fields on the form.

    For information on creating a new matching criteria, see [[create-assignment-wkbench-criteria|Create assignment workbench matching criteria]].

5.  Select **Submit**.


-   **[Matching criteria for work items in Work scheduler](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/work-items-assignment-matching-criteria-wfo-cs.md)**  
The assignment workbench uses configurable matching criteria, such as skills and availability, to evaluate the agents in a selected group and provide an overall ranking.

**Parent Topic:**[[work-scheduler-wfo-cs|Assigning work using Work Scheduler in Workforce Optimization for Customer Service]]

## Related

- [[work-items-assignment-matching-criteria-wfo-cs|Matching criteria for work items in Work scheduler]]
- [[create-assignment-wkbench-criteria|Create assignment workbench matching criteria]]
- [[work-scheduler-wfo-cs|Assigning work using Work Scheduler in Workforce Optimization for Customer Service]]
- [[gamification-components-rules|Rules]]
- [[mandatory-skills|Mandatory skills]]
