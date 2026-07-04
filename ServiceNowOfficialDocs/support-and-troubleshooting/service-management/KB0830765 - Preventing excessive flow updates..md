---
title: "Preventing excessive flow updates."
aliases:
  - KB0830765
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830765
kb_number: KB0830765
last_modified: 2025-10-29
---

## Preventing excessive flow updates.

  

### Issue

When utilizing the flow designer it is possible to create flows whose triggers are not properly limited. If a developer is not careful it is possible that a recursive flow can cause instance performance issues. This is also true of flows that run excessively. Developers need to be aware of how and why their flows could be triggered. 

  

  

### Cause

Typically, issues like this are related to the "Updated" or "Created or Updated" triggers. [List of flow triggers](https://docs.servicenow.com/csh?topicname=flow-triggers.html&version=latest "List of flow triggers")

Developers may miss a logic chain that leads to a flow being called over and over again either recursively or just letting platform updates trigger further flows. 

### Resolution

Let's start with the built in platform protections for awareness. Below is an excerpt from the documentation on flow designer.

  

## Direct recursion prevention and indirect recursion limit

To prevent instance outages and consumption of system resources, Flow Designer ignores any request to start a flow that is the result of direct recursion. Direct recursion occurs under these conditions.

-   An action calls the same flow that it is part of. For example, a script step makes an API call to a flow.
-   An action or subflow produces a result matching the flow trigger. For example, a flow that runs when an incident record is updated contains an update record action that updates an incident record.

Flow Designer also limits the number of times a flow can be started from indirect recursion. Indirect recursion occurs under these conditions.

-   The same flow is called multiple times in a chain of subflow calls. For example, if subflow A calls subflow B, and subflow B calls subflow A, then calling either subflow produces indirect recursion.
-   The same flow is triggered multiple times in a chain of subflows. For example, suppose that there are two flows triggered by record creation. Suppose that creating record A triggers flow A and also creates record B. Furthermore, creating record B triggers flow B and creates record A. Creating either record type produces indirect recursion.

By default, the system stops triggering flow runs after the run count reaches the indirect recursion limit of three runs. Administrators can change the limit by setting the system property com.glide.hub.flow\_engine.indirect\_recursion\_limit to an integer value equal to or greater than one. The system ignores any property value less than one and instead uses a limit of one. Consider the performance impact that increasing the indirect recursion limit may have on your instance.

Note: By default, a transaction quota rule prevents flows from running longer than an hour.

  

##   

**Being aware of interactive vs non interactive sessions. [Interactive vs Non-interactive sessions](https://docs.servicenow.com/csh?topicname=c_NonInteractiveSessions.html&version=latest "Interactive vs Non-interactive sessions")**

  

  

Developers should understand how an interactive session vs a non-interactive session functions. I am going to over simplify it, think of it like Interactive sessions are people taking actions and non-interactive sessions are the platform or automation taking action. When creating a flow if you are going to trigger on every update to a record, do you only care if a user is updating that record or both a human and job? 

  

If you only care about what the people are doing. Consider going under the advanced options and the "When to run the flow" section. You can then change who triggers this flow. This will help prevent flows triggered by background updates from updating too many times. We have seen where background jobs updating large numbers of records cause performance issues as they trigger very large numbers of flow updates. 

  

From the flow trigger documentation.

  

Note: Flows that have a record trigger that runs **For each unique change** can produce recursions when run in a non-interactive session. When such flows make a change to the trigger record, the change meets the flow trigger conditions and causes a recursion.

  

  

**Create appropriate filter conditions when creating flows.**

  

When designing flows, consider the exact conditions when your flows execution is important. For example, let's say you have a flow that checks a field on the incident form for every update. That field must be filled out or we need to notify the working engineer. This can get pretty excessive over the life span of an incident.  So we review the use case and find out that field has to be set while the incident is "Work in progress". That second part is key, I should make sure that my flow checks if the incident is in a "Work in Progress" state otherwise I can just ignore running my flow.  

  

This also goes with one time updates. Make sure that we are using the tools provided in the platform. The Run Trigger option has several choices. If we only need to run a flow one time on a record, we should set the filter appropriately and then set the trigger to only run once. 

  

**Consider running flows on the user session during development.**

  

It may be worthwhile to change the default flow behavior under the advanced options from 'Run flow in background' to 'Run flow in foreground' while testing. This can help a developer "feel" the processing of their flow. What this will do is cause the users session to pause until the flow it triggered is finished. Developers can use this to understand how a popular or commonly running flow affects the system. This will only run for 5 minutes on a user transaction however, it maybe worth while to make sure the flows are performant. You may never know that a flow is running too many times or for too long if you don't see the execution. 

  

  

**Utilize the flow contexts or 'Operations Dashboard' to monitor for excessive flows.  
**

You can review the flow executions either by looking at the Flow Designer -> Operations Dashboard or the Flow Designer -> Today's Executions to get an understanding of what your flows are doing. It is a good practice to review this to understand what flows are running long or a large number of times. You can then review the logs or engage support as needed to review with you the flow.
