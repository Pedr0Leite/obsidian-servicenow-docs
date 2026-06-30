---
title: Basic system configuration
description: Basic system configuration encompasses changes made to the platform as well as supporting applications. These changes can affect global settings as well as settings for particular applications.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/p\_CoreConfigurationOverview.html
release: australia
topic_type: topic
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Get started, Administer the ServiceNow AI Platform]
---

# Basic system configuration

Basic system configuration encompasses changes made to the platform as well as supporting applications. These changes can affect global settings as well as settings for particular applications.

Learn about these ServiceNow AI Platform basic system components and settings:

-   [[c_ServiceNowPlugins|ServiceNow plugins]]
-   [[find-components|Find components installed with an application]]
-   [[r_AvailableSystemProperties|Available system properties]]
-   [[c_QueryJoinAndComplexitySizeLimits|Query join and complexity size limits]]
-   [[c_WebProxy|Web proxy]]

-   **[Experimentation framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown)**  
The [[experimentation-framework|experimentation framework]] enables ServiceNow to test and release new features using A/B testing in order to collect feedback to improve product experiences.
-   **[[feature-preview-program|Feature Preview Program]]**  
The Feature Preview Program provides access to pre-release capabilities on your instance. You can activate, test, and provide feedback on individual features before they are generally available.
-   **[ServiceNow plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ServiceNowPlugins.md)**  
Plugins are software components that provide features and functionalities within a ServiceNow instance.
-   **[Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md)**  
Activating a plugin installs an application on your instance. Each application consists of components such as tables, user roles, and [[c_ScheduledJobs|scheduled jobs]]. To view all components that are installed with an application, see the Application Files table.
-   **[Available system properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_AvailableSystemProperties.md)**  
Some properties are available on a [[r_SetArchiveRuleProcessingBehavior|system properties]] form, but some lesser-used properties are available only from the System Property \[sys\_properties\] table. Sometimes, the property does not exist in a base instance, but can be added if you change the value.
-   **[[t_AddAPropertyUsingSysPropsList|Add a system property]]**  
Add or create a property to control system behavior.
-   **[[t_CreatingAPropertiesModule|Create a system properties module]]**  
You can add a module in the application navigator to access the list of system properties. This module makes it easy to add properties to the System Properties table.
-   **[Query join and complexity size limits](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_QueryJoinAndComplexitySizeLimits.md)**  
The platform uses a relational database to store data. Retrieving data can involve multiple joins to create a single result set. While these joins are usually simple, in certain cases the system may issue very large joins to bring together large numbers \(&gt;20\) of tables.
-   **[Web proxy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_WebProxy.md)**  
Several properties support Web proxy configuration.

**Parent Topic:**[[get-started-now-platform|Getting started on the ServiceNow AI Platform]]

## Related

- [[c_ServiceNowPlugins|ServiceNow plugins]]
- [[find-components|Find components installed with an application]]
- [[r_AvailableSystemProperties|Available system properties]]
- [[c_QueryJoinAndComplexitySizeLimits|Query join and complexity size limits]]
- [[c_WebProxy|Web proxy]]
- [[feature-preview-program|Feature Preview Program]]
- [[t_AddAPropertyUsingSysPropsList|Add a system property]]
- [[t_CreatingAPropertiesModule|Create a system properties module]]
- [[get-started-now-platform|Getting started on the ServiceNow AI Platform]]
- [[experimentation-framework|Experimentation framework]]
- [[c_ScheduledJobs|Scheduled jobs]]
- [[r_SetArchiveRuleProcessingBehavior|System properties]]
