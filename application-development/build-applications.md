---
title: Building applications
description: Learn how to become an application developer using ServiceNow AI Platform low-code tools. Start with what you know and use a library of reusable components and published applications to modernize your legacy processes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/build-applications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
---

# Building applications

Learn how to become an application developer using ServiceNow AI Platform low-code tools. Start with what you know and use a library of reusable components and published applications to modernize your legacy processes.

## Get started

<table id="table_dzv_wmz_bvb" class="nav-card"><tbody><tr><td>

[Learning about creating applications \[Omitted image "bus-learn.svg"\] Alt text: Learn basic information about application development.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/getting-started-with-building-applications.md)

</td><td>

[Phase 1: Planning your application \[Omitted image "bus-task-list.svg"\] Alt text: Plan how your application will work.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/planning-applications.md)

</td><td>

[Phase 2: Developing your application \[Omitted image "bus-application-development.svg"\] Alt text: Add components and content to your application.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/developing-applications.md)

</td></tr><tr><td>

[Phase 3: Testing and debugging your application \[Omitted image "bus-automated-testing-framework.svg"\] Alt text: Verify that the application meets your business requirements.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/testing-and-debugging-applications.md)

</td><td>

[Phase 4: Deploying your application \[Omitted image "bus-rocketship.svg"\] Alt text: Deploy your application to your production environment.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/deploying-applications.md)

</td><td>

[Phase 5: Maintaining your application \[Omitted image "bus-optimize-manage.svg"\] Alt text: Review the status of your application and make changes as needed.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/maintaining-applications.md)

</td></tr></tbody>
</table>## What's new

Build apps smarter and deliver them faster with the new [[servicenow-studio-landing|ServiceNow Studio]]. ServiceNow Studio empowers platform developers with a modern, unified environment for building on the ServiceNow AI Platform. ServiceNow Studio features streamlined navigation to applications and metadata, integrated low-code tools, efficient tracking and packaging of development work that accelerates development processes and enhances productivity.

## App development phases

-   **\[Omitted image "bus-learn.svg"\] Alt text: [[getting-started-with-building-applications|Learning about creating applications]]**

    Decide whether you want to build a new application or extend an existing application. Check the ServiceNow Store and the ServiceNow Community for existing solutions.

    Before building your first application, you may want to learn some basic information about application development. This phase is optional, and you can complete it at any time while you work on other phases.

    -   How [ServiceNow AI Platform](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-platform/now-platform-landing.md) is made up of tables and records. Learn how to convert a spreadsheet into record data.
    -   How to [[get-dev-instance|Get a development instance]] to practice creating applications.
    -   How to find out [[licensing|Licensing]] for which application features require a subscription.
    -   How to contact [[r_support-servicenow-developers|Support for developers]] to ask questions about application development.
-   **\[Omitted image "bus-task-list.svg"\] Alt text: [[planning-applications|Phase 1: Planning your application]]**

    The application development process starts with planning. Consider how the application will work, who will use it, and how it will improve your users' experience. Your application plan should answer the following questions:

    -   What are the goals, objectives, and outputs of your application?
    -   Who uses your application?
    -   Who has access to parts of the application?
    -   What tasks do people complete with your application?
    -   Where does the data come from?
    -   How do people interact with your application?
    -   What processes must the application support?
    -   What UI experience does the application use?
    -   Is there an existing application available on the ServiceNow Store or the ServiceNow Community that you can use or extend?
    -   What subscriptions does your application require?
-   **\[Omitted image "bus-application-development.svg"\] Alt text: [[developing-applications|Phase 2: Developing your application]]**

    During the development phase, you add the components and content of your application. Most applications consist of the following:

    -   **Data**

        Information is stored in your application via tables that you configure. For example, employee phone numbers or office locations.

    -   **Experience**

        Experiences are graphical interfaces that your users interact with. For example, you can create a portal where users find information, submit requests, or complete business tasks.

    -   **Logic and automation**

        Automate all the work in your application by [[app-tutorial-logic-automation-layer|adding logic and automation]]. For example, you can build a flow that sends a notification to the admin when someone makes a request.

    -   **Security**

        Configure roles and access controls to limit who can use your application. For example, you can restrict access to application data to users who have a specific role.

    Choose a builder that matches the type of user experience that your application provides.

    -   See [Build apps using App Engine Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/app-engine-studio/aes-overview.md) to learn about low-code development.
    -   See [Build workflows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/build-workflows.md) to learn about creating automation with Workflow Studio or Playbooks.
    -   See [[builder-library-table|Builder library]] to learn about specialized application resources.
-   **\[Omitted image "bus-automated-testing-framework.svg"\] Alt text: [[testing-and-debugging-applications|Phase 3: Testing and debugging your application]]**

    Verify that the application meets your business requirements. Your testing should cover the following elements:

    -   Record operations, such as create, read, update, and delete.
    -   User interface elements, such as views and UI policies.
    -   Runtime operations, such as business rules and event script actions.
-   **\[Omitted image "bus-rocketship.svg"\] Alt text: [[deploying-applications|Phase 4: Deploying your application]]**

    After successfully testing an application, deploy it to your production environment with your builder tool.

    -   See [Managing app development using the App Engine Management Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/app-engine-management-center/managing-app-development-using-aemc.md) to learn about the [[app-engine-management-center|App Engine Management Center]]
    -   See [ServiceNow application repository](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/application-repository-self-hosted/app-repo.md) to learn about the Application Repository.
    -   See [System update sets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/system-update-sets/system-update-sets.md) to learn about classic [[get-started-deployment|deployment]] using update sets.
-   **\[Omitted image "bus-optimize-manage.svg"\] Alt text: [[maintaining-applications|Phase 5: Maintaining your application]]**

    Use your Phase 2 builder tool to update and modify your application. Use your Phase 3 testing tool to verify that your application still functions properly.


## Applications and features

-   [Learning about developing on the ServiceNow AI Platform](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/getting-started-with-building-applications.md)
-   [Planning your application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/planning-applications.md)
-   [Developing your application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/developing-applications.md)
-   [Testing and debugging applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/testing-and-debugging-applications.md)
-   [Deploying applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/deploying-applications.md)
-   [Maintaining your application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/maintaining-applications.md)

## Related

- [[getting-started-with-building-applications|Learning about developing on the ServiceNow AI Platform]]
- [[get-dev-instance|Get a development instance]]
- [[licensing|Licensing]]
- [[r_support-servicenow-developers|Support for developers]]
- [[planning-applications|Planning your application]]
- [[developing-applications|Developing your application]]
- [[builder-library-table|Builder library]]
- [[testing-and-debugging-applications|Testing and debugging applications]]
- [[deploying-applications|Deploying applications]]
- [[maintaining-applications|Maintaining your application]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[app-tutorial-logic-automation-layer|Adding logic and automation]]
- [[app-engine-management-center|App Engine Management Center]]
- [[get-started-deployment|Deployment]]
