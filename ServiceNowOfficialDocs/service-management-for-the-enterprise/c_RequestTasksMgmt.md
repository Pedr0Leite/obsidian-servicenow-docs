---
title: Request task management
description: A request contains one or more tasks. These tasks allow qualifiers to define activities that must be done to complete a request.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-management-for-the-enterprise/c\_RequestTasksMgmt.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Request Management in a Service Management application, Service Management]
tags:
  - service-management-for-the-enterprise
  - type-concept
---

# Request task management

A request contains one or more tasks. These tasks allow qualifiers to define activities that must be done to complete a request.

Administrators can create multiple tasks under a single request.

Splitting a request into separate tasks, when necessary, enables qualifiers to do the following:

-   Assign different aspects of a request to different staff members.
-   Assign tasks to staff members who have different set of skills, or are in different locations.
-   Schedule tasks so they are either done one after another, or at the same time by different staff members.
-   Schedule additional tasks, if necessary, to complete the request.

**Note:** If you have the Request life cycle is request driven configuration option activated, you can manually add tasks as needed. If you have Request life cycle is task driven activated, an initial task is automatically created when the request record is created.

## Configuration Overview

Optionally, set up one or more additional request task management configurations:

-   [[r_TaskWindows|Task windows]]

    Set a task window to define the time period for performing the task by specifying the start and end dates.

-   [[t_UseTaskTempForMultReqTemp|Create a task template for common task requests]]

    Create task templates to efficiently manage frequently repeated tasks across multiple jobs. By reusing these templates in various request templates, you save time and ensure consistency. Task templates can also be used in Work Order requests to automatically include common information, streamlining the process and minimizing errors.

-   [[t_CloneARequestTask|Clone a request task]]

    Clone an existing task to save time and ensures consistency by allowing administrators to quickly replicate tasks while reducing errors and enabling easy customization.


-   **[[t_CreateRequestTasks|Create request tasks]]**  
Tasks are created in support of requests.
-   **[[r_SMRequestTaskStates|Request task states]]**  
Like requests, the associated request tasks follow a specific life cycle and move through a series of states, which are displayed in the **State** field on the task record.
-   **[Task windows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TaskWindows.md)**  
A task window is the time period, bordered by start and end times, in which a task is performed.
-   **[Create a task template for common task requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_UseTaskTempForMultReqTemp.md)**  
If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.
-   **[Clone a request task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CloneARequestTask.md)**  
Existing tasks can be cloned to create tasks with the same populated fields.

**Parent Topic:**[[rm-sm-application|Request Management in a Service Management application]]

**Related topics**  


[[t_ChangeTheLocationOfARequest|Change the location of a request]]

[[c_RequestApprovals|Request approvals]]

[[t_CollaborateOnARequest|Collaborate on a request]]

[[t_CloseARequest|Close a request]]

## Related

- [[r_TaskWindows|Task windows]]
- [[t_UseTaskTempForMultReqTemp|Create a task template for common task requests]]
- [[t_CloneARequestTask|Clone a request task]]
- [[t_CreateRequestTasks|Create request tasks]]
- [[r_SMRequestTaskStates|Request task states]]
- [[rm-sm-application|Request Management in a Service Management application]]
- [[t_ChangeTheLocationOfARequest|Change the location of a request]]
- [[c_RequestApprovals|Request approvals]]
- [[t_CollaborateOnARequest|Collaborate on a request]]
- [[t_CloseARequest|Close a request]]
