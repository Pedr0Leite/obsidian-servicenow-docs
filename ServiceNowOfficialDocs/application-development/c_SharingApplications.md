---
title: Application sharing
description: Administrators can share applications that are complete and are ready for use on other instances.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/c\_SharingApplications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Administer your apps, Deploying applications, Building applications]
---

# Application sharing

Administrators can share applications that are complete and are ready for use on other instances.

Application developers can share applications using one of the following methods.

|Sharing method|Makes available to|Typical use case|
|--------------|------------------|----------------|
|Publish to the application repository|All instances assigned to the same company|Transfer an application to a test or production environment.|
|Publish to the ServiceNow Store|All ServiceNow customers|Share or sell applications to other companies.|
|Publish to an Update Set|Any instance with access to the Update Set file|Save a version of an application for compliance or backup reasons.|
|Push to [[team-development-landing|team development]] instances|Other instances in the team development environment|Push developer changes to the parent instance.|

**Note:**

“Tracking schema”: Deleting a table or a column in a scoped application is enabled by default for freshly zBooted instances. This is done by having the system property `com.glide.apps.include_my_schema` set to “true”.

For upgraded instances, if you have no custom applications installed or in development, “tracking schema deletes” is enabled by default. Otherwise the property is set to “false” so that customers get the same experience for schema deletes in their applications as in previous releases before Paris. To learn more see the [New York and Scoped Applications New Features](https://community.servicenow.com/community?id=community_blog&sys_id=ef21c1d21bf04c507a5933f2cd4bcb34) article on the ServiceNow Community site.

## Custom licensing for ISV applications

For applications that you are sharing, you can create a definition to track usage metrics on your application. For more information, see [[custom-licensing-isv-apps|Custom licensing for ISV applications]].

-   **[ServiceNow application repository](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/application-repository-self-hosted/app-repo.md)**  
After you develop and test a custom application, you can make the application available to company instances by publishing it to the [[app-repo|ServiceNow application repository]].
-   **[[t_PublishAppsToTheServiceNowStore|Publish an application to the ServiceNow Store]]**  
Publishing an application to the ServiceNow Store makes it available to everyone.
-   **[[t_IncludeApplicationData|Create application files to include sample data]]**  
Include sample records from an application data table when sharing a custom application.
-   **[[t_PublishApplicationsToAnUpdateSet|Publish an application to an Update Set]]**  
Publishing an application creates an update set containing the current version of all application configuration records.
-   **[[queued-app-operations|Queued Application Operations]]**  
CICD APIs that must obtain the update **instance wide lock / mutex** to perform the requested operations are queued instead of being rejected when the update **instance wide lock / mutex** is occupied by the other operations.
-   **[Custom licensing for ISV applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/custom-licensing-isv-apps.md)**  
Monitor the usage of ISV applications with Subscription Management. [[create-definition-store-apps|Create a definition for your store application]] with the metadata you want collected. After publishing the application with the definition to the store, Usage Analytics runs and aggregates your defined metrics.

**Parent Topic:**[[r_ManagingApplications|Administer your apps]]

## Related

- [[custom-licensing-isv-apps|Custom licensing for ISV applications]]
- [[t_PublishAppsToTheServiceNowStore|Publish an application to the ServiceNow Store]]
- [[t_IncludeApplicationData|Create application files to include sample data]]
- [[t_PublishApplicationsToAnUpdateSet|Publish an application to an Update Set]]
- [[queued-app-operations|Queued Application Operations]]
- [[r_ManagingApplications|Administer your apps]]
- [[team-development-landing|Team Development]]
- [[app-repo|ServiceNow application repository]]
- [[create-definition-store-apps|Create a definition for your store application]]
