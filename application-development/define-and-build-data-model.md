---
title: Define and build the data model
description: After planning is complete, define and build the data model. Create one or more tables with fields, load the table with demo data, and verify access controls to the data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/define-and-build-data-model.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Build your application, Exploring professional development, Building pro-code applications, Developing your application, Building applications]
---

# Define and build the data model

After planning is complete, define and build the data model. Create one or more tables with fields, load the table with demo data, and verify access controls to the data.

## Agentic AI

Create applications with help from agentic AI. For more information, see [[use-ai-capabilities-in-custom-apps|Agentic development on the ServiceNow AI Platform]].

## Create an application

Create or open an application record.

-   Create: If creating an application directly, use [ServiceNow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/servicenow-studio-landing.md) to create the application.
-   Open: If developers do not have the admin role, the ServiceNow System Administrator needs to create the application and grant developers a [[delegated-development-landing|delegated development]] role. Developers then use [[servicenow-studio-landing|ServiceNow Studio]] to open the application for editing.

**Note:** The [[c_ApplicationScope|application scope]] and table name are sometimes referred to as the internal names for these objects and cannot be changed once they are created. However, the application name and table label can be changed. Application users see the internal names in the URL only. If possible, internal names should always be consistent with what the user sees.

-   **[[build-data-model|Build the data model]]**  
Create tables and fields on the tables to support the application’s data model.
-   **[[secure-data|Secure data]]**  
Data security is one of the most important and overlooked aspects of creating an application. ServiceNow automatically configures access control for a new or selected role during the table creation process. Only users with the role can access the table to read, create, write, and delete.
-   **[[manage-data|Manage data]]**  
With the data model \(tables and fields\) created and security set up, add data into the application’s table\(s\).

**Parent Topic:**[[build-your-application|Build your application]]

## Related

- [[use-ai-capabilities-in-custom-apps|Agentic development on the ServiceNow AI Platform]]
- [[build-data-model|Build the data model]]
- [[secure-data|Secure data]]
- [[manage-data|Manage data]]
- [[build-your-application|Build your application]]
- [[delegated-development-landing|Delegated Development]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[c_ApplicationScope|Application scope]]
