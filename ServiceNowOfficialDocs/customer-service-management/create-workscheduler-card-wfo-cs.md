---
title: Create a Work scheduler card using the Next Experience UI Builder
description: Create a work scheduler card and add the components that you want to display based on your needs in the Work Scheduler application in manager workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/create-workscheduler-card-wfo-cs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Setting up Work scheduler, Optimize workforce operations, Extend capabilities, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a Work scheduler card using the Next Experience UI Builder

Create a work scheduler card and add the components that you want to display based on your needs in the Work Scheduler application in manager workspace.

## Before you begin

Role required: admin, workspace\_admin, or ui\_builder\_admin​

## Procedure

1.  Navigate to **All** &gt; **Now Experience Framework** &gt; **UI Builder**.

2.  In the **My experiences** list, select **Manager Workspace**.

3.  Select the Pages icon.

4.  In the **Page** menu, select **Work scheduler**.

5.  In the left pane, go to the **Content** section and navigate to **Body \(Flex\)** &gt; **Work queue \(Flex\)** &gt; **Sidebar**.

6.  In the right pane, select the icon \(\[Omitted image "edit-card-icon.png"\] Alt text: Edit card icon\) in the **Work item cards default** sub-page.

7.  In the left pane, select **Body \(Flex\)** &gt; **Viewport1**.

8.  In the right pane, select **+Add** and enter a name for the card.

    The **Path** field is automatically populated.

9.  Select **Create**.

    A new card is created.

    **Important:** After you create the work scheduler card, you must select the name of this card in the **UX app route** field in the work configuration you have created. For information on setting up a work configuration, see [Set up a work configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/setup-work-scheduler.md).

10. Select **Done**.

    Follow the steps listed in each of the topics below in the given sequence to customize Work scheduler.


-   **[[work-sched-create-client-state-params-wfo-cs|Create a client state parameter for Work scheduler]]**  
Add custom client state parameter values to add properties to the card components.
-   **[[work-sched-create-page-scripts-wfo-cs|Create page scripts for Work scheduler]]**  
Add custom page scripts for the Work scheduler so that you can update the client state through events or update transform workItem object to properties.
-   **[[work-sched-create-page-properties-wfo-cs|Define the workItem property in the Work scheduler page configuration]]**  
Add the **workItem** property to the Work scheduler page configuration to receive the **workItem** object provided by the work queue.
-   **[[work-sched-event-mapping-wfo-cs|Define event mappings for Work scheduler]]**  
Add event mappings required for card interactions and for the card properties transformation to the page configurations in Work scheduler.
-   **[[work-sched-card-based-container-wfo-cs|Configure container components for Work scheduler]]**  
Present information in an intuitive format using the Card Base Container component.
-   **[[work-sched-card-based-header-wfo-cs|Configure a Work scheduler card heading component]]**  
Customize the Work scheduler heading component to display the title based on your needs.
-   **[[work-sched-stacked-component-wfo-cs|Configure a display type component for a Work scheduler card]]**  
Add the **Label value stacked** display work item fields within the card.
-   **[[work-sched-avatar-component-wfo-cs|Configure an avatar component for Work scheduler]]**  
Use the **Container** component to add an avatar and the user name of the work item assignee.
-   **[[associate-card-config-wfo-cs|Associate a work scheduler card to the work configuration]]**  
Associate the work scheduler card that you've created to the work configuration to display the card in the Work scheduler sidebar.

**Parent Topic:**[[setting-up-work-scheduler-wfo-cs|Setting up Work scheduler in Workforce Optimization for Customer Service]]

**Related topics**  


[Create a page in UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/create-page.md)

## Related

- [[work-sched-create-client-state-params-wfo-cs|Create a client state parameter for Work scheduler]]
- [[work-sched-create-page-scripts-wfo-cs|Create page scripts for Work scheduler]]
- [[work-sched-create-page-properties-wfo-cs|Define the workItem property in the Work scheduler page configuration]]
- [[work-sched-event-mapping-wfo-cs|Define event mappings for Work scheduler]]
- [[work-sched-card-based-container-wfo-cs|Configure container components for Work scheduler]]
- [[work-sched-card-based-header-wfo-cs|Configure a Work scheduler card heading component]]
- [[work-sched-stacked-component-wfo-cs|Configure a display type component for a Work scheduler card]]
- [[work-sched-avatar-component-wfo-cs|Configure an avatar component for Work scheduler]]
- [[associate-card-config-wfo-cs|Associate a work scheduler card to the work configuration]]
- [[setting-up-work-scheduler-wfo-cs|Setting up Work scheduler in Workforce Optimization for Customer Service]]
