---
title: "Lifecycle Event Best Practices and Performance Expectations"
aliases:
  - KB1307612
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1307612
kb_number: KB1307612
last_modified: 2025-09-03
---

## Lifecycle Event Best Practices and Performance Expectations

  

This document shares best practices to optimize performance and avoid runtime issues when creating a lifecycle event, based on our own testing and experience working with customers. It’s not meant to cover every consideration and should not be treated as a sole source of implementation guidance.

# General Best Practices for Lifecycle Events

1.  **Do NOT modify a lifecycle event in production if there are ongoing cases without thorough testing.** The changes to the configuration could cause unexpected consequences to the ongoing cases depending on where they are in their workflow. If the changes are needed in production and there are ongoing cases, we recommend:
    1.  Cloning prod and test the existing LE cases to see if they have any issues.
    2.  Cloning the lifecycle event and creating new cases with the new lifecycle event.  **Note**: this approach will have more overhead/maintenance (e.g., customers might need to update or create a new HR service to point to the new LE type). Also, this will not satisfy the customer use case if the customer wants the new config changes to be applied to the existing/ongoing cases.

1.  **Do not modify the subject person on a lifecycle event case once it is already triggered** or create a lifecycle event case without a subject person. This is likely to cause issues in the workflow.

2.  **Use caution if trying to modify the evaluation interval to trigger activity sets more immediately** – we recommend using a [Conditional Business Rule](https://www.servicenow.com/docs/bundle/xanadu-employee-service-management/page/product/human-resources/task/le-eval-interval-business-rule.html) to more immediately trigger an activity set. If this should happen the Resume Case button can help to re-execute the processing so the cancelled activities can be reprocessed.  Here is a table of calculations based on the Max Activity Count that gives an idea of when a customer can expect the parallel processing threads to be consumed.                                                                                                                                                     ![](/sys_attachment.do?sys_id=ad575fa187fdd29057288519dabb35d0)

3.  **When to use rescind vs. cancel**? Rescind should be used when you need to retract an already started process. For instance, if you have a new hire who has already begun their onboarding process but then decides not to join the organization, you can rescind their lifecycle event case. This will trigger the roll back process that you have configured for the lifecycle event to ensure the right activities are triggered (or not triggered) as a result. You can cancel a case when you do not need any counter processes to trigger.

4.  **When to use resume:**  ­There are 2 uses for ‘Resuming’ a case:
    1.  When an LE activity set is errored out or cancelled. You will need to fix the error and then you can resume the case.
        1.  **You should not manually error out an activity set to apply changes and resume the workflow**.  This will cause dangling workflow context where the old context is still in active state using computational resources. 
        2.  **Important: You can also reference the work notes in the case to see why a case may have errored.**
    2.  When you suspend a case and are ready to ‘resume’ it. For more information on when to use suspend/resume feature, please reference [this doc.](https://docs.servicenow.com/csh?topicname=t_SuspendAndResumeAnHRCase.html&version=latest)

5.  **Use caution when specifying the Lifecycle Event type on the HR Service being used to trigger the Lifecycle Event.** The type should not contain the same Lifecycle Event type being called by an activity in the same Lifecycle Event. This will cause an endless loop. The Lifecycle Event type is used to trigger the selected lifecycle event. If you are trying to create an HR case from a Lifecycle Event, you should use a normal HR service.

![](/sys_attachment.do?sys_id=a9575fa187fdd29057288519dabb35d7)

Best Practices for Performance in Lifecycle Events

**See** [**troubleshooting best practice FAQ here**](/kb?id=kb_article_view&sysparm_article=KB1117350)

**TLDR: The more complex the underlying workflow, the slower the load times of activities for employees and managers in the Lifecycle Event Request page (hrm\_ticket\_page).**  

-   Note: This document does not pertain to the new Journey Designer UI, only the Request page (hrm\_ticket\_page). The Journey page will have better performance. If you are interested in learning more about Journey designer
-   For more information on how you can migrate your Lifecycle Events employee experience to leverage the new Journey designer, reference this [Community post](https://www.servicenow.com/community/hrsd-blog/migrating-from-lifecycle-events-to-journey-designer/ba-p/2354912) and referenced migration guide.

**What is the max number of activities that should be included in an activity set?**

There is no one answer as performance will be a function of number of activities and complexity of activities. We would recommend 10 activities or less triggering at one time, whether part of an activity set or an activity container. The more you have triggering at one time, the worse the performance. If the activities are not complex, you can exceed this. The following factors can have further performance implications:

-   An employee is completing a task that will trigger an HR service (catalog request, etc.), the more complex the request, the slower the performance.
-   Triggering multiple activity sets at one time (the more background calls, the slower the performance)

**Customer Example:**

**Customer 1:** Customer has 42 activities across 5 activity sets

-   **Case creation:** 90-120 seconds
-   **Activity load time for employee:** 7-10 seconds from completing one activity to reloading the next

# Performance Metrics

#### This document covers the following UI:

-   **Request page** (specifically for lifecycle events)
-   Note: The Requests UI has slower performance than the new Journey page available with Journey designer (Tokyo+).

## Performance Metrics for a Lifecycle case on Requests Page:

Below are performance expectations related to Lifecycle events. We have made improvements in and delivered the updates in the following releases:

-   Employee Center Core 27.1.1 store release
-   Utah family: performance improvements from reducing complexity of record watchers on the Request page in desktop and mobile
-   Vancouver family: We will continue to make performance improvements based on further investigation.

Note: These updates will improve the performance on the Request page.

## Performance Metrics for a Lifecycle case on Requests Page:

We ran performance metrics to understand the time it takes when one activity is completed to load the next activity.

### Observations:

-   Activities of type ‘e-signature’, ‘mark as complete’, and learning will take 4-10 seconds to load the next activities.
-   Activities that are submitting subsequent cases or requests will take longer, 10-15 seconds.
    -   Examples: Submitting IT requests, order guides, submitting record producers (complete profile information will submit a record producer, create a case and close it out)
-   When the last activity in an activity set is complete, it will start to load the next activity and thus have slower load times (see data below)

Performance Data – Demo Data

These results are using are New Hire Onboarding Demo Data.

Note: Time to complete is in seconds.

![](/sys_attachment.do?sys_id=f5579fa187fdd29057288519dabb3573)

Performance Data – 50 activities in an activity set

These results are using ‘mark as complete’ and ‘watch video’ type activities [\[NH1\]](#_msocom_1) [\[NH2\]](#_msocom_2) [\[LC3\]](#_msocom_3) to show that less complex task types (even when in larger volume) will have lower load times.

![](/sys_attachment.do?sys_id=a5575fa187fdd29057288519dabb35d4)
